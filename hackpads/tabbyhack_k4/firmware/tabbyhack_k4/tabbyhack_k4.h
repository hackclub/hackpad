// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H
#ifndef tabbyhack_k4.h
#define tabbyack_k4.h
const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    
    [0] = LAYOUT(
        KC_P7,   KC_P8,   
        KC_P4 ,  KC_P9
        KC_PSLS
    ),
 /*   [1] = LAYOUT(
        KC_P7,   KC_P8,   
        KC_P4 ,  KC_P9
        KC_PSLS
*/
 //   ),
};

bool encoder_update_user(uint8_t index, bool clockwise) {
    switch(get_highest_layer(layer_state|default_layer_state)) {
        case _LAYER0:
            if (clockwise) {
                    tap_code16(C(KC_VOLU));;
                } else {
                    tap_code16(C(KC_VOLD));;
                }

#endif
