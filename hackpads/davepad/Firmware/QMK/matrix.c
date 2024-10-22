#include <stdint.h>
#include <stdbool.h>
#if defined(__AVR__)
#include <avr/io.h>
#endif
#include "i2c_master.h"
#include "mcp23017.h"
#include "config.h"
#include "matrix.h"
#include "debounce.h"
#include "print.h"
#include "wait.h"

#define TIMEOUT 20

#define print_matrix_header()  print("\nr/c 01234567\n")
#define print_matrix_row(row)  print_bin_reverse8(matrix_get_row(row))
#define ROW_SHIFTER ((uint8_t)1)

i2c_status_t expander_write(uint8_t pin, uint8_t state) {
    return i2c_write_register16(MCP23017_ADD, pin, &state, 1, TIMEOUT);
}

i2c_status_t expander_read(uint8_t pin, uint8_t *state) {
    return i2c_read_register16(MCP23017_ADD, pin, state, 1, TIMEOUT);
}

matrix_row_t matrix[MATRIX_ROWS];
matrix_row_t raw_matrix[MATRIX_ROWS];

matrix_row_t matrix_get_row(uint8_t row) {
    // TODO: return the requested row data
    return matrix[row];
}

inline
bool matrix_is_on(uint8_t row, uint8_t col)
{
    return (matrix[row] & ((matrix_row_t)1<<col));
}

void matrix_print(void) {
    // TODO: use print() to dump the current matrix state to console
    print_matrix_header();

    for (uint8_t row = 0; row < MATRIX_ROWS; row++) {
        print_hex8(row); print(": ");
        print_matrix_row(row);
        print("\n");
    }
}

__attribute__((weak)) void matrix_init_kb(void) { matrix_init_user(); }

__attribute__((weak)) void matrix_scan_kb(void) { matrix_scan_user(); }

__attribute__((weak)) void matrix_init_user(void) {}

__attribute__((weak)) void matrix_scan_user(void) {}

// uses standard row code
static void select_row(uint8_t row)
{
    expander_write(MATRIX_ROW_PINS[row], 255);
}

inline static void unselect_row(uint8_t row)
{
    expander_write(MATRIX_ROW_PINS[row], 0);
}

static void unselect_rows(void)
{
    for(uint8_t x = 0; x < MATRIX_ROWS; x++) {
        unselect_row(x);
    }
}

static void init_pins(void) {
    unselect_rows();
    for (uint8_t x = 0; x < MATRIX_COLS; x++) {
        expander_write(MATRIX_COL_PINS[x], 0);
    }
}

static bool read_cols_on_row(matrix_row_t current_matrix[], uint8_t current_row)
{
    // Store last value of row prior to reading
    matrix_row_t last_row_value = current_matrix[current_row];

    // Clear data in matrix row
    current_matrix[current_row] = 0;

    // Select row and wait for row selecton to stabilize
    select_row(current_row);
    wait_us(30);

    // For each col...
    for(uint8_t col_index = 0; col_index < MATRIX_COLS; col_index++) {
        uint8_t pin_state;
        expander_read(MATRIX_COL_PINS[col_index], &pin_state);

        current_matrix[current_row] |=  pin_state ? 0 : (ROW_SHIFTER << col_index);
    }

    // // Unselect row
    unselect_row(current_row);

    return (last_row_value != current_matrix[current_row]);
}

void matrix_init(void) {

    i2c_init();
    init_pins();
    // initialize matrix state: all keys off
    for (uint8_t i=0; i < MATRIX_ROWS; i++) {
        raw_matrix[i] = 0;
        matrix[i] = 0;
    }

    debounce_init(MATRIX_ROWS);

    matrix_init_kb();
}

uint8_t matrix_scan(void)
{
    bool changed = false;

    for (uint8_t current_row = 0; current_row < MATRIX_ROWS; current_row++) {
        changed |= read_cols_on_row(raw_matrix, current_row);
    }

    debounce(raw_matrix, matrix, MATRIX_ROWS, changed);

    matrix_scan_kb();
    return (uint8_t)changed;
}
