// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     *             ┌───┐
     *             │ o │
     * ┌───────────┼───┤
     * │ D │ F │ J │ K │
     * └───┴───┴───┴───┘
     */
    [0] = LAYOUT(
                              KC_KB_MUTE,  // encoder
        QK_MACRO_0, QK_MACRO_1, QK_MACRO_2,   QK_MACRO_3   // dfjk
    )
};

const uint16_t PROGMEM encoder_map[][1][2] = {
    [0] = { ENCODER_CCW_CW(KC_KB_VOLUME_DOWN, KC_KB_VOLUME_UP) },
};