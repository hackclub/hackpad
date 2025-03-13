// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

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
    [0] = LAYOUT(
    KC_MEDIA_PLAY_PAUSE,  // First key (0,1)
    KC_MEDIA_PREV_TRACK,  // Second key (1,0)
    KC_NO,  // Third key (1,1)
    KC_MEDIA_NEXT_TRACK,        // Fourth key (1,2)
    KC_MEDIA_STOP                 // Fifth key (2,1) - Fill in if unused
)

};

const uint16_t PROGMEM encoder_map[][1][2] = {
    [0] = {
        ENCODER_CCW_CW(KC_VOLU, KC_VOLD)
    }
};