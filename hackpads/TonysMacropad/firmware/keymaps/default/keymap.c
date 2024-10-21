// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H
#include "rgblight.h"

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┐
     * │ 7 │ 8 │ 9 │ 
     * ├───┼───┼───┤
     * │ 4 │ 5 │ 6 │
     * ├───┼───┼───┤
     * │ 1 │ 2 │ 3 │
     * └───────┴───┘
     */
    [0] = LAYOUT(
        KC_P7,   KC_P8,   KC_P9,
        KC_P4,   KC_P5,   KC_P6,
        KC_P1,   KC_P2,   KC_P3,
        KC_P0
    )
};

const uint16_t PROGMEM encoder_map[][1][2] = {
    [0] = { ENCODER_CCW_CW(KC_VOLU, KC_VOLD) },
};

void set_led_color(uint8_t r, uint8_t g, uint8_t b) {
    // set leds in decreasing brightness
    rgblight_setrgb_at(r, g, b, 0); 
    rgblight_setrgb_at(r / 2, g / 2, b / 2, 1); 
    rgblight_setrgb_at(r / 3, g / 3, b / 3, 2); 
    rgblight_setrgb_at(r / 4, g / 4, b / 4, 3); 
}

bool process_record_user(uint16_t keycode, keyrecord_t* record) {
    if(record->event.pressed) {
        switch(keycode) {
            case KC_P9:
                set_led_color(255, 0, 0);
                break;
            case KC_P8:
                set_led_color(0, 255, 0);
                break;
            case KC_P7:
                set_led_color(255, 255, 0);
                break;
            case KC_P6:
                set_led_color(255, 0, 255);
                break;
            case KC_P5:
                set_led_color(0, 0, 255);
                break;
            case KC_P4:
                set_led_color(0, 255, 255);
                break;
            case KC_P3:
                set_led_color(100, 255, 100);
                break;
            case KC_P2:
                set_led_color(255, 100, 100);
                break;
            case KC_P1:
                set_led_color(100, 100, 255);
                break;
        }
    }
    return true;  // Process other keycodes
}