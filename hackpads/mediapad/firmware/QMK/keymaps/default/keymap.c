// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┬───┬───┐
     * │|<|│ <<│|> │>> │|>|│
     * └───┴───┴───┴───┴───┘
     */
    [0] = LAYOUT(
        KC_MPRV,   KC_BRID,   KC_MPLY,   KC_BRIU,   KC_MNXT
    )
};

const uint16_t PROGMEM encoder_map[][1][2] = {
    [0] = {
        ENCODER_CCW_CW(KC_VOLU, KC_VOLD),
    },
};
