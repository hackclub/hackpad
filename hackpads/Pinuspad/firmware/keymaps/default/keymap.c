// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

enum layer_names {
    _BASE,
    _MACRO,
    _ARROWS
};

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ─────────────
     * │ 7 │ 8 │ 9 │
     * ├───┼───┼───┤
     * │ 4 │ 5 │ 6 │
     * ├───┼───┼───┤
     * │ 1 │ 2 │ 3 │
     * └───┴───┴───┘
     */

    [_BASE] = LAYOUT_ortho_3x3(
        DF(_ARROWS), KC_PRINT_SCREEN, DF(_MACRO),
        KC_PAGE_UP, KC_PAGE_DOWN, KC_MEDIA_PLAY_PAUSE,
        KC_COPY, KC_COPY, KC_FIND
    ),

    [_MACRO] = LAYOUT_ortho_3x3(
        DF(_BASE), KC_F13, DF(_ARROWS),
        KC_F14, KC_F15, KC_F16,
        KC_F17, KC_F18, KC_F19
    ),

    [_ARROWS] = LAYOUT_ortho_3x3(
        DF(_MACRO), KC_UP, DF(_BASE),
        KC_LEFT, KC_NO, KC_RIGHT,
        KC_NO, KC_DOWN, KC_NO
    )
};

const uint16_t PROGMEM encoder_map[][2][2] = {
    [_BASE] = { ENCODER_CCW_CW(KC_VOLU, KC_VOLD), ENCODER_CCW_CW(KC_RIGHT, KC_LEFT) },
    [_MACRO] = { ENCODER_CCW_CW(KC_VOLU, KC_VOLD), ENCODER_CCW_CW(KC_RIGHT, KC_LEFT) },
    [_ARROWS] = { ENCODER_CCW_CW(KC_VOLU, KC_VOLD), ENCODER_CCW_CW(KC_RIGHT, KC_LEFT) },
};

#ifdef OLED_ENABLE
bool oled_task_user() {

    oled_write_P(PSTR("Layer: "), false);

    switch (get_highest_layer(layer_state)) {
        case _BASE:
            oled_write_ln_P(PSTR("Base"), false);
            break;
        case _MACRO:
            oled_write_ln_P(PSTR("Macro"), false);
            break;
        case _ARROWS:
            oled_write_ln_P(PSTR("Arrows"), false);
            break;
        default:
            oled_write_ln_P(PSTR("Undefined"), false);
    }

    led_t led_state = host_keyboard_led_state();
    oled_write_ln_P(led_state.num_lock ? PSTR("NUM: ON") : PSTR("NUM: OFF"), false);
    oled_write_ln_P(led_state.caps_lock ? PSTR("CAPS: ON") : PSTR("CAPS: OFF"), false);
    
    return false;
}
#endif