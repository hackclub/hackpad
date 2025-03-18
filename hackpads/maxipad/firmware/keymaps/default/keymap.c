// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┐
     * │ <<│/\ │>> │
     * ├───┼───┼───┤
     * │ < │\/ │ > │
     * └───┴───┴───┘
     */
    [0] = LAYOUT(
        KC_MEDIA_PREV_TRACK, KC_UP, KC_MEDIA_NEXT_TRACK,
        KC_LEFT, KC_DOWN, KC_RIGHT
    )
};
