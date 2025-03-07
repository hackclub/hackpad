#include <stdint.h>     // For uint8_t and uint16_t
#include <stdbool.h>    // For bool
#include QMK_KEYBOARD_H // Use quotes for local headers

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT(
        KC_A, KC_B, KC_C,  // Row 1
        KC_D, KC_E, KC_F   // Row 2
    )
};

// Rotary Encoder Functionality
bool encoder_update_user(uint8_t index, bool clockwise) {
    if (index == 0) { // First encoder
        if (clockwise) {
            tap_code(KC_VOLU); // Volume Up
        } else {
            tap_code(KC_VOLD); // Volume Down
        }
    } else if (index == 1) { // Second encoder
        if (clockwise) {
            tap_code(KC_PGDN); // Page Down
        } else {
            tap_code(KC_PGUP); // Page Up
        }
    }
    return true;
}

// LED Control
void keyboard_post_init_user(void) {
    // Set initial LED state
    rgblight_enable();
    rgblight_sethsv(HSV_RED);
}
