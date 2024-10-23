// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┬───┐
     * │ 7 │ 8 │ 9 │   │
     * ├───┼───┼───┼───┤
     * │ 4 │ 5 │ 6 │ TAB │
     * ├───┼───┼───┼───┤
     * │ 1 │ 2 │ 3 │ 0 │
     * └───┴───┴───┴───┘
     */
    [0] = LAYOUT(
        KC_P7,   KC_P8,   KC_P9,   KC_NO,
        KC_P4,   KC_P5,   KC_P6,   KC_TAB,
        KC_P1,   KC_P2,   KC_P3,   KC_P0,
    )
};

const uint16_t PROGMEM encoder_map[][1][2] = {
    [0] = { ENCODER_CCW_CW(KC_VOLU, KC_VOLD) },
};
