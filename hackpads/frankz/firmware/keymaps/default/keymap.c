// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

enum layer_names {
    _1,
    _2,
    _3,
    _4
};

enum custom_keycodes {
    RESET_LAYER = SAFE_RANGE
};

uint8_t current_layer = _1;

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

    [_1] = LAYOUT(
        KC_A, KC_MUTE, RESET_LAYER, 
	KC_1, KC_2, KC_3, 
	KC_4, KC_5, KC_6, 
        KC_7, KC_8, KC_9
    ),
    [_2] = LAYOUT(
        KC_B, KC_MUTE, RESET_LAYER, 
	KC_1, KC_2, KC_3, 
	KC_4, KC_5, KC_6, 
        KC_7, KC_8, KC_9
    ),
    [_3] = LAYOUT(
        KC_C, KC_MUTE, RESET_LAYER, 
	KC_1, KC_2, KC_3, 
	KC_4, KC_5, KC_6, 
        KC_7, KC_8, KC_9
    ),
    [_4] = LAYOUT(
        KC_D, KC_MUTE, RESET_LAYER, 
	KC_1, KC_2, KC_3, 
	KC_4, KC_5, KC_6, 
        KC_7, KC_8, KC_9
    )
};

bool encoder_update_user(uint8_t index, bool clockwise) {
    if (index == 0) {
        if (clockwise) {
            tap_code(KC_VOLU);
        } else {
            tap_code(KC_VOLD);
        }
    } else if (index == 1) {
        if (clockwise) {
            current_layer++; 
            if (current_layer > _4) {
                current_layer = _1;
            }
        } else {
            if (current_layer == _1) {
                current_layer = _4;
            } else {
                current_layer--; 
            }
        }
        layer_move(current_layer);
    }
    return false;
};

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    switch (keycode) {
        case RESET_LAYER:
            if (record->event.pressed) {
                layer_move(_1);
            }
            return false;
    }
    return true;
};
