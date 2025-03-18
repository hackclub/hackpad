// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

    [0] = LAYOUT(
        KC_P7,   KC_P8,
        KC_P4,   KC_P9,
        KC_PSLS
    ),
    /* [1] = LAYOUT(
        KC_P7,   KC_P8,
        KC_P4,   KC_P9,
        KC_PSLS
    ) */
};

bool encoder_update_user(uint8_t index, bool clockwise) {
    switch(get_highest_layer(layer_state|default_layer_state)) {
        case 0:  // Use 0 instead of _LAYER0
            if (clockwise) {
                tap_code16(C(KC_VOLU));
            } else {
                tap_code16(C(KC_VOLD));
            }
            break; // Always include a break statement to prevent fall-through
    }
    return false; // Return a value to indicate no further action
}

