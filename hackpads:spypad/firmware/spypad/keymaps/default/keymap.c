#include QMK_KEYBOARD_H

enum layers {
    NUMPAD_LAYER,
    COMMAND_LAYER
};

// Variable to track which profile is active
bool is_numpad_layer_active = true;

// Encoder behavior based on active layer
void encoder_update_user(uint8_t index, bool clockwise) {
    if (is_numpad_layer_active) {
        // Profile 1: Numpad Layer
        switch (index) {
            case 0: // Encoder 1: Ctrl + Left / Ctrl + Right
                if (clockwise) {
                    tap_code16(C(KC_RGHT));
                } else {
                    tap_code16(C(KC_LEFT));
                }
                break;
            case 1: // Encoder 2: F7 / F8
                if (clockwise) {
                    tap_code(KC_F8);
                } else {
                    tap_code(KC_F7);
                }
                break;
            case 2: // Encoder 3: Zoom In / Zoom Out
                if (clockwise) {
                    tap_code(KC_ZOOM_IN);
                } else {
                    tap_code(KC_ZOOM_OUT);
                }
                break;
        }
    } else {
        // Profile 2: Command Layer
        switch (index) {
            case 0: // Encoder 1: Ctrl + Left / Ctrl + Right
                if (clockwise) {
                    tap_code16(C(KC_RGHT));
                } else {
                    tap_code16(C(KC_LEFT));
                }
                break;
            case 1: // Encoder 2: F7 / F8
                if (clockwise) {
                    tap_code(KC_F8);
                } else {
                    tap_code(KC_F7);
                }
                break;
            case 2: // Encoder 3: Zoom In / Zoom Out
                if (clockwise) {
                    tap_code(KC_ZOOM_IN);
                } else {
                    tap_code(KC_ZOOM_OUT);
                }
                break;
        }
    }
}

// Function to switch between layers
void matrix_scan_user(void) {
    if (!is_numpad_layer_active) {
        layer_move(COMMAND_LAYER);
    } else {
        layer_move(NUMPAD_LAYER);
    }
}

// Function to toggle layers using the pushbutton of Encoder 3
bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    if (record->event.pressed) {
        switch (keycode) {
            case KC_BTN3:  // Assuming `KC_BTN3` is mapped to Encoder 3's pushbutton
                // Toggle layer state
                is_numpad_layer_active = !is_numpad_layer_active;
                return false;
        }
    }
    return true;
}

// Define the keymaps for both profiles (layers)
// Adjusting the layout to reflect vertical rows and horizontal columns
const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

    [NUMPAD_LAYER] = LAYOUT(
        KC_P7, KC_P4, KC_P1, KC_PAST, KC_NO,
        KC_P8, KC_P5, KC_P2, KC_PMNS, KC_NO,
        KC_P9, KC_P6, KC_P3, KC_PPLS, KC_NO
    ),

    [COMMAND_LAYER] = LAYOUT(
        LCTL(KC_C), LCTL(KC_V), LCTL(KC_X), KC_F12, KC_NO,            // Copy, Paste, Cut, F12
        LCTL(KC_LEFT), LCTL(KC_RGHT), LCTL(LSFT(KC_LEFT)), KC_F11, KC_NO, // Cmd + Left/Right, Cmd + Shift + Left/Right, F11
        LCTL(KC_TAB), LCTL(KC_Z), LCTL(LSFT(KC_Z)), KC_F10, KC_NO     // Cmd + Tab, Undo, Redo, F10
    )
};
