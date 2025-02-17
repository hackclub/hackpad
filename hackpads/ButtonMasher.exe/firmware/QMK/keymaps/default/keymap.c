// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     *     ┬───┬
     *     │ 1 │
     * ┼───┼───┼───┤
     * │ 5 │ 2 │ 3 │
     * ├───┼───┼───┼
     *     │ 4 │
     *     ┼───┼

     */
    [0] = LAYOUT(
        UG_NEXT, KC_MPLY, KC_MFFD, KC_MUTE, KC_MRWD
    )
    
};

const uint16_t PROGMEM encoder_map[][1][2] = {
    [0] = { ENCODER_CCW_CW(KC_BRIU, KC_BRID) },
};
