// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌─────┬─────┬─────┬─────┬─────┐
     * │ ESC │  N  │  I  │  T  │  M  │
     * ├─────┼─────┼─────┼─────┼─────┤
     * │ TAB │  A  │  Z  │  E  │  R  │
     * ├─────┼─────┼─────┼─────┼─────┤
     * │SHIFT│  Q  │  S  │  D  │  F  │
     * ├─────┼─────┼─────┼─────┼─────┤
     * │CTRL │  W  │  X  │  C  │SPACE│
     * └─────┴─────┴─────┴─────┴─────┘
     */
    [0] = LAYOUT(
        KC_ESCAPE,     KC_N, KC_I, KC_T, KC_M,
        KC_TAB,        KC_A, KC_Z, KC_E, KC_R,
        KC_LEFT_SHIFT, KC_Q, KC_S, KC_D, KC_F,
        KC_LEFT_CTRL,  KC_W, KC_X, KC_C, KC_SPACE
    )
};
