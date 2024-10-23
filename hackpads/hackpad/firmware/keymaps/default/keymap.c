// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

enum layer_names {
    _1
};

uint8_t current_layer = _1;

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

    [_1] = LAYOUT(
        KC_7,   KC_8,   KC_9,   KC_DOT,
        KC_4,   KC_5,   KC_6,   KC_0,
        KC_1,   KC_2,   KC_3,   KC_ENT
      
    )
};
