// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

enum layer_names {
    _BASE,
};

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     *     ┬───┐
     *     │VOL│
     * ├───┼───┼───┤
     * │FF │RW │P/P│
     * ├───┼───┼───┘
     * │MUT│WAK│   
     * └───┴───┘
     */

    [_BASE] = LAYOUT(
        KC_NO,               // Volume key (top single key)
        KC_MFFD, KC_MRWD, KC_MPLY, // Fast forward, rewind, play/pause (first row)
        KC_MUTE, KC_WAKE        // Mute and Wake (second row)
    )
};

const uint16_t PROGMEM encoder_map[][1][2] = {
    [0] = { ENCODER_CCW_CW(KC_VOLU, KC_VOLD) },
};

