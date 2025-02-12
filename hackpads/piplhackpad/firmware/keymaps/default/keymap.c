#include QMK_KEYBOARD_H

#if defined(ENCODER_MAP_ENABLE)
const uint16_t PROGMEM encoder_map[][1][2] = {
    [0] =  { ENCODER_CCW_CW(KC_VOLD, KC_VOLU)}
};
#endif

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0]= LAYOUT(
        KC_1,   KC_2,   KC_3,   KC_AUDIO_MUTE,
        KC_4,   KC_4,   KC_6,   KC_MINUS,
        KC_7,   KC_8,   KC_9,   KC_PLUS,
        KC_BSPC,   KC_0,   KC_DEL,   KC_ENTER
    )
};
