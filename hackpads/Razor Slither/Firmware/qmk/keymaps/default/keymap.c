// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┐
     * │ A │ B │ C │
     * ├───┼───┼───┤
     * │ D │ E │ F │
     * ├───┼───┼───┤
     * │ G │ H │ I │
     * └───┴───┴───┘
     */
    [0] = LAYOUT_ortho_3x3(
        KC_LSFT,    KC_W,    KC_ENTER,
        KC_A,    KC_S,    KC_D,
        KC_X,    KC_SPACE,    KC_Z
    )
};

const uint16_t PROGMEM encoder_map[][1][2] ={
    [0] = { ENCODER_CCW_CW(MS_WHLU, MS_WHLD) },
};
