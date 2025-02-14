#include QMK_KEYBOARD_H

// Define the keymap layout
#define LAYOUT_ortho_2x4( \
    k00, k01, k02, k03, \
    k10, k11, k12, k13 \
) { \
    { k00, k01, k02, k03 }, \
    { k10, k11, k12, k13 } \
}

// Define keymaps
const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT_ortho_2x4(
        KC_ESC, KC_1,    KC_2,    KC_3, 
        KC_4,   KC_5,    KC_6,    KC_7
    ),
};

// Define encoder map
const uint16_t PROGMEM encoder_map[][NUM_ENCODERS][NUM_DIRECTIONS] = {
    [0] = { { KC_VOLD, KC_VOLU }, { KC_MUTE, KC_MUTE } },
};

// You can add other configurations or macros as needed
