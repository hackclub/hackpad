// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┐
     * │ Q │ W │ E │
     * ├───┼───┼───┤
     * │ A │ S │ D │
     * ├───┼───┼───┤
     * │ 1 │ 2 │ 3 │
     * └───┴───┴───┘
     */
    [0] = LAYOUT_ortho_3x3(
        KC_Q,    KC_W,    KC_E,
        KC_A,    KC_S,    KC_D,
        KC_1,    KC_2,    KC_3
    )
};
