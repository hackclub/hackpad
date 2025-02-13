// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H
#include <stdio.h>
#include <stdint.h>

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┬───┐
     * │ 7 │ 8 │ 9 │ / │
     * ├───┼───┼───┼───┤
     * │ 4 │ 5 │ 6 │ * │
     * ├───┼───┼───┼───┤
     * │ 0 │ . │Ent│ + │
     * └───┴───┴───┴───┘
     */
    [0] = LAYOUT(
        KC_SLEP,  KC_MPLY,  KC_MYCM,   MO(1),
        KC_Q,     KC_W,     KC_E,     KC_MAIL,
        KC_A,     KC_S,     KC_D,     KC_SPC
    ),

    [1] = LAYOUT(
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   QK_BOOT
    )
};

bool encoder_update_user (uint8_t index, bool clockwise)
{
    if (index == 0)
    {
        tap_code(KC_VOLU);
    }
    else
    {
        tap_code(KC_VOLD);
    }

    if (index == 1)
    {
        tap_code(KC_BRIU);
    }
    else
    {
        tap_code(KC_BRID);
    }

    return false;
}