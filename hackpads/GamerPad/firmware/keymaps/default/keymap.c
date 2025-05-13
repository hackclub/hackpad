// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┬───┐
     * │ 7 │ 8 │ 9 │ / │
     * ├───┼───┼───┼───┤
     * │ 4 │ 5 │ 6 │ * │
     * ├───┼───┼───┼───┤
     * │ 1 │ 2 │ 3 │ - │
     * ├───┼───┼───┼───┤
     * │ 0 │ . │Ent│ + │
     * └───┴───┴───┴───┘
     */
    [0] = LAYOUT(
        KC_Q, KC_W, KC_E, MT(DM_REC1, DM_PLY1),
        KC_A, KC_S, KC_D, MT(DM_REC2, DM_PLY2),
        PDF(0), PDF(1), PDF(2),  DM_RSTP
    ),
    [1] = LAYOUT(
        MS_BTN1, MS_BTN2, MS_BTN3, MS_WHLU,
        MS_BTN4, MS_BTN5, MS_BTN6, MS_WHLD,
        PDF(0), PDF(1), PDF(2),  QK_UNDERGLOW_TOGGLE
    ),
    [2] = LAYOUT(
        KC_F13, KC_F14, KC_F15, KC_F16,
        KC_F17, KC_F18, KC_F19, KC_F20,
        PDF(0), PDF(1), PDF(2),  KC_LWIN
    )
};
