#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT(
        KC_MPLY, KC_MPRV, KC_MNXT,  // Top Row: Play/Pause, Previous Track, Next Track
        KC_MUTE, KC_VOLD, KC_VOLU   // Bottom Row: Mute, Volume Down, Volume Up
    )
};

// Rotary encoder functionality
bool encoder_update_user(uint8_t index, bool clockwise) {
    if (clockwise) {
        tap_code(KC_VOLU);  // Increase Volume
    } else {
        tap_code(KC_VOLD);  // Decrease Volume
    }
    return true;  // Changed from false to true to allow other encoder processing
}

// Encoder switch functionality (Mute/Unmute on GP3)
void matrix_scan_user(void) {
    if (!gpio_read_pin(GP3)) { // Fixed GPIO handling for RP2040
        tap_code(KC_MUTE);  // Toggle mute
    }
}