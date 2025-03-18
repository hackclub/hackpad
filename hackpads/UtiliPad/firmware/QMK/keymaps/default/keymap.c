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
     * │ F13 │ F14 │ ENC │
     * ├─────┼─────┼─────┤
     * │ F16 │ F17 │ F18 │
     * └─────┴─────┴─────┘
     */
    [_BL] = LAYOUT(
        KC_F13,    KC_F14,    KC_MUTE,  // Encoder press acts as mute
        KC_F16,    KC_F17,    KC_F18
    ),
    [_SL] = LAYOUT(
        KC_F1,     KC_F2,     KC_TRNS,  // Transparent, meaning no action on encoder press in this layer
        KC_F3,     KC_F4,     KC_F5
    ),
};

// Encoder Function
bool encoder_update_user(uint8_t index, bool clockwise) {
    if (IS_LAYER_ON(_BL)) {
        if (clockwise) {
            tap_code(KC_VOLU);  // Volume Up on base layer
        } else {
            tap_code(KC_VOLD);  // Volume Down on base layer
        }
    } else if (IS_LAYER_ON(_SL)) {
        if (clockwise) {
            tap_code(KC_BRIU);  // Brightness Up on second layer
        } else {
            tap_code(KC_BRID);  // Brightness Down on second layer
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
