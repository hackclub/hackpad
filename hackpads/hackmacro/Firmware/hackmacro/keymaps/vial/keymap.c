// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H
#include "ws2812.h"

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
    [0] = LAYOUT_ortho_4x4(
        KC_P7,   KC_P8,   KC_P9,   KC_PSLS,
        KC_P4,   KC_P5,   KC_P6,   KC_PAST,
        KC_P1,   KC_P2,   KC_P3,   KC_PMNS,
        KC_P0,   KC_PDOT, KC_PENT, KC_PPLS
    )
};

led_config_t g_led_config = { {
  // Key Matrix to LED Index
  {   1,      NO_LED, NO_LED,   8      },
  {   2,      NO_LED, NO_LED,   7      },
  {   3,      4,      5,        6,     }
}, {
  // LED Index to Physical Position
  { 0,  0 }, { 0,  32 }, { 45,  64 }, { 90,  64 }, { 134,  64 }, { 179,  64 }, { 224,  32 }, { 224,  0 }
}, {
  // LED Index to Flag
  1, 1, 1, 1, 1, 1, 1, 1
} };