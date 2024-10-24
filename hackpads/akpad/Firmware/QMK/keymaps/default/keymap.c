// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ├───┼───┼───┼───┤
     * │ M │ M │ M │ A │
     * ├───┼───┼───┼───┤
     * │ M │ M │ M │ A │
     * ├───┼───┼───┼───┤
     * │ F │ U │ C │ P │
     * ├───┼───┼───┼───┤
     * │ B │ R │ W │ S │
     * └───┴───┴───┴───┘
     * M refers to mouse key/control
     * A refers to an application
     * F is find, U is undo, C is copy and P is paste
     * B is browser search, R is refresh, W is wake, S is sleep
     */

    [0] = LAYOUT(
        MS_BTN1, MS_UP,   MS_BTN2,  KC_CALC,
        MS_LEFT, MS_DOWN, MS_RIGHT, KC_MAIL,
        KC_FIND, KC_UNDO, KC_COPY,  KC_PASTE,
        KC_WSCH, KC_WREF, KC_WAKE,  KC_SLEP
    )
};

#if defined(ENCODER_MAP_ENABLE)
const uint16_t PROGMEM encoder_map[][1][2] = {
    [0] = { ENCODER_CCW_CW(KC_KB_VOLUME_DOWN, KC_KB_VOLUME_UP)
};
#endif
