#include QMK_KEYBOARD_H

// Layer declaration
enum layers {
    _BASE,
};

// Encoder functionality
void encoder_update_user(uint8_t index, bool clockwise) {
    if (index == 0) {
        if (clockwise) {
            tap_code(KC_VOLU);
        } else {
            tap_code(KC_VOLD);
        }
    } else if (index == 1) {
        if (clockwise) {
            tap_code(KC_PGUP);
        } else {
            tap_code(KC_PGDN);
        }
    }
}

// Keymap Layout
const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [_BASE] = LAYOUT(
        KC_ESC, KC_1, KC_2, KC_3, 
        KC_4, KC_5, KC_6, KC_7
    )
};
