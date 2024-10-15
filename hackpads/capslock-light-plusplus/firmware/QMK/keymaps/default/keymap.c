// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

enum layer_names {
    _BASE,
    _UNI,
};

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * 
     * The wiring is VERY convoluted!
     * 
     * [6][7][8]
     * [3][4][5]
     * [0][1][2]
     * 
     * Maps to a physical layout of:
     * 
     * [OLED]   [6]
     * [0][2][4][7]
     * [1][3][5][8]
     * 
     * 6 is a EC11 encoder
     */

    [_BASE] = LAYOUT(
        KC_AUDIO_MUTE, KC_F19, TO(_UNI),
        KC_F16, KC_F17, KC_F18, 
        KC_F13, KC_F14, KC_F15
    ),

    [_UNI] = LAYOUT(
        KC_TRNS, UC(0x2212), TO(_BASE),
        UC(0x00BD), UC(0x00BE), UC(0x00B7), 
        UC(0x00B1), UC(0x2260), UC(0x00BC)
    )
};

const uint16_t PROGMEM encoder_map[][1][2] = {
    [0] = { ENCODER_CCW_CW(KC_AUDIO_VOL_UP, KC_AUDIO_VOL_DOWN) },
    [1] = { ENCODER_CCW_CW(KC_AUDIO_VOL_UP, KC_AUDIO_VOL_DOWN) }
    
};
/*
const rgblight_segment_t PROGMEM my_capslock_layer[] = RGBLIGHT_LAYER_SEGMENTS(
    {1, 1, HSV_RED}
);

const rgblight_segment_t PROGMEM my_layer1_layer[] = RGBLIGHT_LAYER_SEGMENTS(
    {9, 2, HSV_CYAN}
);

const rgblight_segment_t* const PROGMEM my_rgb_layers[] = RGBLIGHT_LAYERS_LIST(
    my_capslock_layer,
    my_layer1_layer
);
*/
#ifdef OLED_ENABLE
bool oled_task_user(void) {

    // Acualy display capslock status, the whole point of this board
    led_t led_state = host_keyboard_led_state();
    oled_write_P(led_state.caps_lock ? PSTR("CAPS ") : PSTR("     "), false);
    oled_write_P(led_state.num_lock ? PSTR("NUM ") : PSTR("    "), false);
    oled_write_P(led_state.scroll_lock ? PSTR("SCR ") : PSTR("    "), false);
    oled_write_P(PSTR("\n"), false);

    // Host Keyboard Layer Status
    oled_write_P(PSTR("Layer: "), false);
    switch (get_highest_layer(layer_state)) {
        case _BASE:
            oled_write_P(PSTR("FN Keys"), false);
            break;
        case _UNI:
            oled_write_P(PSTR("Unicode Characters"), false);
            break;
        default:
            oled_write_P(PSTR("Undefined"), false);
    }
    
    return false;
}
#endif
/*
bool led_update_user(led_t led_state) {
    rgblight_set_layer_state(0, led_state.caps_lock);
    return true;
}
*/