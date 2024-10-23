#include "matrix.h"
#include "mcp23017.h"

static const uint8_t row_pins[MATRIX_ROWS] = { MCP23017_GPA5, MCP23017_GPA6, MCP23017_GPA7 };
static const uint8_t col_pins[MATRIX_COLS] = { MCP23017_GPA0, MCP23017_GPA1, MCP23017_GPA2, MCP23017_GPA3, MCP23017_GPA4 };

void matrix_init_custom(void) {
    mcp23017_init();
    for (uint8_t col = 0; col < MATRIX_COLS; col++) {
        mcp23017_set_output(col_pins[col], true);
    }
    for (uint8_t row = 0; row < MATRIX_ROWS; row++) {
        mcp23017_set_input(row_pins[row], true);
    }
}

bool matrix_scan_custom(void) {
    for (uint8_t col = 0; col < MATRIX_COLS; col++) {
        mcp23017_set_output(col_pins[col], false);
        for (uint8_t row = 0; row < MATRIX_ROWS; row++) {
            bool key_pressed = mcp23017_read_pin(row_pins[row]);
            matrix_update(row, col, key_pressed);
        }
        mcp23017_set_output(col_pins[col], true);
    }
    return false;
}
