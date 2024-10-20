// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * physical layout
// ┌───┬───┬───┬───┬───────────┐
// │ 7 │ 8 │ 9 │ / │ Encoder 1 │
// ├───┼───┼───┼───┼───────────┼
// │ 4 │ 5 │ 6 │ * │ Encoder 2 │ 
// ├───┼───┼───┼───┼───────────┼
// │ 1 │ 2 │ 3 │ - │           │           
// ├───┼───┼───┼───┼───────────┼
// │ 0 │ . │Ent│ + │           │
// └───┴───┴───┴───┴───────────┘
     */
    [0] = LAYOUT_4x4_2encoders(
        KC_1,   KC_2,   KC_3,   KC_SLSH,
        KC_4,   KC_5,   KC_6,   KC_KP_ASTERISK,
        KC_7,   KC_8,   KC_9,   KC_MINUS,
        KC_0,   KC_PDOT, KC_PENT, KC_PPLS,
        KC_MPRV, KC_MNXT
    )
};
