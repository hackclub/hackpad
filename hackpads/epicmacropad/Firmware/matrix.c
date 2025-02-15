#include "quantum.h"
#include "i2c_master.h"
#include "timer.h"
#include "matrix.h"
#include "epicmacropad.h"
#include "wait.h"
#include "print.h"

#include "config.h"

// Configuration
#ifndef DEBOUNCE
#   define DEBOUNCE 5
#endif

#if (DEBOUNCE > 0)
    static uint16_t debouncing_time;
    static bool debouncing = false;
#endif

#ifdef MATRIX_MASKED
    extern const matrix_row_t matrix_mask[];
#endif

static const uint8_t onboard_row_pins[MATRIX_ROWS] = MATRIX_ONBOARD_ROW_PINS;
static const uint8_t onboard_col_pins[MATRIX_COLS] = MATRIX_ONBOARD_COL_PINS;
static const bool col_expanded[MATRIX_COLS] = COL_EXPANDED;

static matrix_row_t matrix[MATRIX_ROWS];
static matrix_row_t matrix_debouncing[MATRIX_ROWS];

// Since diode direction is col to row
static const uint8_t expander_col_pins[MATRIX_COLS] = MATRIX_EXPANDER_COL_PINS;
static void init_cols(void);
static bool read_cols_on_row(matrix_row_t current_matrix[], uint8_t current_row);
static void unselect_rows(void);
static void select_row(uint8_t row);
static void unselect_row(uint8_t row);

static uint8_t expander_reset_loop;
uint8_t expander_status;
uint8_t expander_input_pin_mask;
bool i2c_initialized = false;

#define ROW_SHIFTER ((matrix_row_t)1)

__attribute__ ((weak))
void matrix_init_user(void) {}

__attribute__ ((weak))
void matrix_scan_user(void) {}

__attribute__ ((weak))
void matrix_init_kb(void) {
    matrix_init_user();
}

__attribute__ ((weak))
void matrix_scan_kb(void) {
    matrix_scan_user();
}

inline
uint8_t matrix_rows(void)
{
    return MATRIX_ROWS;
}

inline
uint8_t matrix_cols(void)
{
    return MATRIX_COLS;
}

void init_expander(void) {
    if (!i2c_initialized) {
        // Initialize I2C
        i2c_init();
        i2c_initialized = true;
        wait_ms(1000);  // Replace with suitable delay
    }

    if (!expander_input_pin_mask) {
        // Initialize input pin mask based on the matrix configuration
        for (int col = 0; col < MATRIX_COLS; col++) {
            if (col_expanded[col]) {
                expander_input_pin_mask |= (1 << expander_col_pins[col]);
            }
        }
    }

    // Set GPIO direction and pull-up configuration
    uint8_t direction[2] = { expander_input_pin_mask, 0 };
    uint8_t pullup[2] = { expander_input_pin_mask, 0 };

    // Use I2C to write register values
    expander_status = i2c_write_register(I2C_ADDR, IODIRA, direction, 2, I2C_TIMEOUT);
    if (expander_status) return;

    expander_status = i2c_write_register(I2C_ADDR, GPPUA, pullup, 2, I2C_TIMEOUT);
}

void matrix_init(void)
{
    init_expander();

    // Initialize matrix state: all keys off
    unselect_rows();
    init_cols();

    for (uint8_t i = 0; i < MATRIX_ROWS; i++) {
        matrix[i] = 0;
        matrix_debouncing[i] = 0;
    }

    matrix_init_kb();
}

uint8_t matrix_scan(void)
{
    if (expander_status) { // If there was an error
        if (++expander_reset_loop == 0) {
            // Try to reset expander once every 255 matrix scans
            init_expander();
        }
    }

    for (uint8_t current_row = 0; current_row < MATRIX_ROWS; current_row++) {
#if (DEBOUNCE > 0)
        bool matrix_changed = read_cols_on_row(matrix_debouncing, current_row);
        if (matrix_changed) {
            debouncing = true;
            debouncing_time = timer_read();
        }
#else
        read_cols_on_row(matrix, current_row);
#endif
    }

#if (DEBOUNCE > 0)
    if (debouncing && (timer_elapsed(debouncing_time) > DEBOUNCE)) {
        for (uint8_t i = 0; i < MATRIX_ROWS; i++) {
            matrix[i] = matrix_debouncing[i];
        }
        debouncing = false;
    }
#endif

    matrix_scan_kb();
    return 1;
}

inline
bool matrix_is_on(uint8_t row, uint8_t col)
{
    return (matrix[row] & (ROW_SHIFTER << col));
}

inline
matrix_row_t matrix_get_row(uint8_t row)
{
#ifdef MATRIX_MASKED
    return matrix[row] & matrix_mask[row];
#else
    return matrix[row];
#endif
}

void matrix_print(void)
{
    print("\nr/c 0123456789ABCDEF\n");
    for (uint8_t row = 0; row < MATRIX_ROWS; row++) {
        print_hex8(row); print(": ");
        print_bin_reverse16(matrix_get_row(row));
        print("\n");
    }
}

// Initialize columns using QMK GPIO functions
static void init_cols(void) {
    for (uint8_t x = 0; x < MATRIX_COLS; x++) {
        if (!col_expanded[x]) {
            setPinInput(onboard_col_pins[x]);
            writePin(onboard_col_pins[x], true);  // Enable pull-up
        }
    }
}

// Read columns using QMK GPIO functions
static bool read_cols_on_row(matrix_row_t current_matrix[], uint8_t current_row) {
    matrix_row_t last_row_value = current_matrix[current_row];
    current_matrix[current_row] = 0;

    select_row(current_row);
    wait_us(30);  // Short wait for signal stabilization

    // Read columns from expander
    if (!expander_status) {
        uint8_t state = 0;
        expander_status = i2c_read_register(I2C_ADDR, EXPANDER_COL_REGISTER, &state, 1, I2C_TIMEOUT);
        if (!expander_status) {
            current_matrix[current_row] |= (~state) & expander_input_pin_mask;
        }
    }

    // Read columns from onboard GPIO pins
    for (uint8_t col_index = 0; col_index < MATRIX_COLS; col_index++) {
        if (!col_expanded[col_index]) {
            uint8_t pin_state = readPin(onboard_col_pins[col_index]);
            current_matrix[current_row] |= (pin_state == 0) ? (ROW_SHIFTER << col_index) : 0;
        }
    }

    unselect_row(current_row);
    return (last_row_value != current_matrix[current_row]);
}

static void select_row(uint8_t row) {
    setPinOutput(onboard_row_pins[row]);
    writePin(onboard_row_pins[row], 0);  // Set row low
}

static void unselect_row(uint8_t row) {
    writePin(onboard_row_pins[row], 1);  // Set row high
}

static void unselect_rows(void) {
    for (uint8_t x = 0; x < MATRIX_ROWS; x++) {
        unselect_row(x);
    }
}
