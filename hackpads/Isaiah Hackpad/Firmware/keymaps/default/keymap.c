// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

enum layer_names {
    _BASE,
};


const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌─────┬─────┬─────┐
     * │Ctrl │ UP  │SHIFT│
     * ├─────┼─────┼─────┤
     * │LEFT │DOWN │RIGHT│
     * ├─────┼─────┼─────┤
     * │VOLUP│ MUTE│VOLDO│
     * └─────┴─────┴─────┘
     * 
     */
    [_BASE] = LAYOUT(
        KC_LCTL, KC_UP, KC_LSFT,
        KC_LEFT, KC_DOWN, KC_RIGHT,
        KC_AUDIO_VOL_UP, KC_AUDIO_MUTE, KC_AUDIO_VOL_DOWN
    )
};
