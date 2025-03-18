// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

enum layer_name {
    _BASE,
};

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┬
     * │ 8 │ 9 │10 │
     * ├───┼───┼───┼
     * │ 5 │ 6 │ 7 │
     * ├───┼───┼───┼
     * │ 2 │ 3 │ 4 │
     * ├───┼───┼───┼
     */

    /*
    The wiring is a little convoluted - refer to the diagram below:
    
    */
    [_BASE] = LAYOUT(
        //this is how they look irl not in schematic
        KC_P1, KC_P2, KC_P3,
        KC_P4, KC_P5, KC_P6,
        KC_P7, KC_P8, KC_P9
    )
};

const uint16_t PROGMEM encoder_map[][1][2] = {
    [0] = { ENCODER_CCW_CW(KC_VOLU, KC_VOLD)},
};

#ifdef OLED_ENABLE
bool oled_task_user(void) {
    // Host Keyboard Layer Status
    oled_write_P(PSTR("Layer: "), false);

    switch (get_highest_layer(layer_state)) {
        case _BASE:
            oled_write_P(PSTR("Default\n"), false);
            break;
        default:
            // Or use the write_ln shortcut over adding '\n' to the end of your string
            oled_write_ln_P(PSTR("Undefined"), false);
    }
    
    return false;
}
#endif