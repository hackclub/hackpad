// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * GoosePad aka "goose calculator"
     *
     * ┌───┬───┐┌──────┐
     * │ / │ * ││ OLED │
     * └───┴───┘└──────┘
     * ┌───┬───┬───┬───┐
     * │ 7 │ 8 │ 9 │ 0 │
     * ├───┼───┼───┼───┤
     * │ 4 │ 5 │ 6 │ - │
     * ├───┼───┼───┼───┤
     * │ 1 │ 2 │ 3 │ + │
     * └───┴───┴───┴───┘
     */

    [0] = LAYOUT(
        KC_KP_SLASH, KC_KP_ASTERISK,
        KC_7, KC_8, KC_9, KC_0,
        KC_4, KC_5, KC_6, KC_KP_MINUS,
        KC_1, KC_2, KC_3, KC_KP_PLUS
    ),
};

#ifdef OLED_ENABLE
oled_rotation_t oled_init_user(oled_rotation_t rotation) { return OLED_ROTATION_180; }

bool oled_task_user(void) {
    
    oled_set_cursor(0, 1);

    oled_write("Hi!", false);

    return false;
}
#endif
