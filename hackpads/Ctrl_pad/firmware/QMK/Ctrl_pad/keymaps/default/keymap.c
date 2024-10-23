// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

// Define the layers
enum layer_names {
    _BL,
    _SL,
};

// Keymaps
const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌─────┬─────┬─────┐
     * │ F13 │ F14 │ F15 │
     * ├─────┼─────┼─────┤
     * │ F16 │ F17 │ F18 │
     * ├─────┼─────┼─────┤
     * │ F19 │ F20 │ F21 │
     * └─────┴─────┴─────┘
     */
    [_BL] = LAYOUT(
        KC_SLEP,    KC_WAKE,    TG(_SL),
        KC_MPRV,    KC_MPLY,    KC_MNXT,
        KC_F16,     KC_F17,     KC_F18
    ),
    [_SL] = LAYOUT(
        KC_F1,    KC_F2,    KC_TRNS,
        KC_F3,    KC_F4,    KC_F5,
        KC_F6,    KC_F7,    KC_F8
    ),
};

// Encoder Function
bool encoder_update_user(uint8_t index, bool clockwise) {
    if (IS_LAYER_ON(_BL)) {
        if (clockwise) {
            tap_code(KC_VOLU);
        } else {
            tap_code(KC_VOLD);
        }
    } else if (IS_LAYER_ON(_SL)) {
        if (clockwise) {
            tap_code(KC_BRIU);
        } else {
            tap_code(KC_BRID);
        }
    }
    
    return true; // Return true to indicate the encoder event was handled
}

// OLED Function
#ifdef OLED_ENABLE
bool oled_task_user(void) {
    // Display the active layer
    oled_write_ln_P(PSTR("Layer"), false);
    switch (get_highest_layer(layer_state)) {
        case _BL:
            oled_write_ln_P(PSTR("Layer: Ctrl"), false);
            break;
        case _SL:
            oled_write_ln_P(PSTR("Layer: Func"), false);
            break;
        default:
            oled_write_ln_P(PSTR("Undefined"), false);
    }

    // Display encoder functionality
    if (IS_LAYER_ON(_BL)) {
        oled_write_ln_P(PSTR("Vol Ctrl"), false);
    } else if (IS_LAYER_ON(_SL)) {
        oled_write_ln_P(PSTR("Bright Ctrl"), false);
    }
    
    return false;
}
#endif // OLED_ENABLE
