// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later


// POTENTIALLY HELPFUL: https://github.com/qmk/qmk_firmware/blob/master/keyboards/handwired/dactyl/keymaps/default/keymap.c


#include "keycodes.h"
#include QMK_KEYBOARD_H


#define BASE 0 // default layer



const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┬───┐
     * │ 7 │ 8 │ 9 │ / │
     * ├───┼───┼───┼───┤
     * │ 4 │ 5 │ 6 │ * │
     * ├───┼───┼───┼───┤
     * │ 1 │ 2 │ 3 │ - │
     * ├───┼───┼───┼───┤
     * │ 0 │ . │Ent│ + │
     * └───┴───┴───┴───┘
     */
    [BASE] = LAYOUT(
        KC_F13,   KC_F14,   KC_F15,   KC_F16, KC_F17,
        KC_F18,   KC_F19,   KC_F20,   KC_F21, KC_F22,
        KC_F23,   KC_F24,   KC_BRIGHTNESS_UP,   KC_BRIGHTNESS_DOWN, KC_AUDIO_VOL_UP,
        KC_AUDIO_VOL_DOWN,   KC_AUDIO_MUTE, KC_SYSTEM_SLEEP, KC_SYSTEM_POWER, KC_MEDIA_NEXT_TRACK
    ),
};


#if defined(ENCODER_MAP_ENABLE)
const uint16_t PROGMEM encoder_map[][NUM_ENCODERS][NUM_DIRECTIONS] = {
    [0] = { ENCODER_CCW_CW(MS_WHLU, MS_WHLD), ENCODER_CCW_CW(KC_VOLD, KC_VOLU) },
};


bool encoder_update_user(uint8_t index, bool clockwise) {
    if (index == 0) { /* First encoder */
        if (clockwise) {
            tap_code(KC_PGDN);
        } else {
            tap_code(KC_PGUP);
        }
    } else if (index == 1) { /* Second encoder */
        if (clockwise) {
            tap_code(KC_PGDN);
        } else {
            tap_code(KC_PGUP);
        }
    }
    return false;
}
#endif

#ifdef OLED_ENABLE
bool oled_task_user(void) {
    oled_write_P(PSTR("Test"), false);
    return false;
}
#endif