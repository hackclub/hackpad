// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌─────┬─────┬─────┬─────┐
     * │ F9  │ F10 │ F11 │ F12 │
     * ├─────┼─────┼─────┼─────┤
     * │ F13 │ F14 │ F15 │ F16 │
     * ├─────┼─────┼─────┼─────┤
     * │ F17 │ F18 │ F19 │ F20 │
     * ├─────┼─────┼─────┼─────┤
     * │ F21 │ F22 │ F23 │ F24 │
     * └─────┴─────┴─────┴─────┘
     */
    [0] = LAYOUT(
        KC_F9,   KC_F10,   KC_F11,   KC_F12,
        KC_F13,   KC_F14,   KC_F15,   KC_F16,
        KC_F17,   KC_F18,   KC_F19,   KC_F20,
        KC_F21,   KC_F22, KC_F23, KC_F24
    )
};
