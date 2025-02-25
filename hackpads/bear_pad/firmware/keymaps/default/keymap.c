#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT(
        KC_A,   KC_B,   KC_D,   KC_E,
        KC_F,   KC_G,   KC_H,   KC_I,
        KC_J,   KC_K,   KC_L,   KC_M
    )
};
