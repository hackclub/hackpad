// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

#include "version.h"

#include "quantum.h"
#define MATRIX_ROW_PINS { GP21, GP20, GP8 }
#define MATRIX_COL_PINS { GP4, GP5, GP6, GP7 }


const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┬───┐
     * │ Q │ W │ E │ C │
     * ├───┼───┼───┼───┤
     * │ A │ S │ D │ X │
     * ├───┼───┼───┼───┤
     * │Prev│Play│Next│Mute│
     * └───┴───┴───┴───┘
     */
    [0] = LAYOUT(
      KC_Q, KC_W, KC_E, KC_C,
      KC_A, KC_S, KC_D, KC_X,
      KC_MRWD, KC_MPLY, KC_MFFD, KC_MUTE
    )
};
