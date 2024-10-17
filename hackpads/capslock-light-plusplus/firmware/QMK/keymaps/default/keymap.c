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
    [0] = {ENCODER_CCW_CW(KC_AUDIO_VOL_UP, KC_AUDIO_VOL_DOWN)}, 
    [1] = {ENCODER_CCW_CW(KC_AUDIO_VOL_UP, KC_AUDIO_VOL_DOWN)}
};

/* Code for non-existant RGB lighting
const rgblight_segment_t PROGMEM my_capslock_layer[] = RGBLIGHT_LAYER_SEGMENTS(
    {1, 1, HSV_RED}
);

const rgblight_segment_t PROGMEM my_layer1_layer[] = RGBLIGHT_LAYER_SEGMENTS(
    {1, 1, HSV_CYAN}
);

const rgblight_segment_t* const PROGMEM my_rgb_layers[] = RGBLIGHT_LAYERS_LIST(
    my_capslock_layer,
    my_layer1_layer
);

bool led_update_user(led_t led_state) {
    rgblight_set_layer_state(0, led_state.caps_lock);
    return true;
}
*/

#ifdef OLED_ENABLE
bool oled_task_user(void) {
    led_t led_state = host_keyboard_led_state();

    // Host Keyboard Layer Status. Also swap for icon?
    oled_set_cursor(10, 0);
    oled_write_P(PSTR("Layer: "), false);
    oled_set_cursor(11, 1);
    switch (get_highest_layer(layer_state)) {
        case _BASE:
            oled_write_P(PSTR("FN Keys"), false);
/* Theory for base layer
 * ███ ███ ███ Layer: 
 * █A█ █1█ █S█  FN Keys
 * ███ ███ ███
 *          
 */
            oled_set_cursor(0, 0); // full size 3x3 boxes for the lock symbols
            if (led_state.caps_lock) {
                oled_write_P(PSTR("   "), true);
                oled_set_cursor(0, 1);
                oled_write_P(PSTR(" A "), true);
                oled_set_cursor(0, 2);
                oled_write_P(PSTR("   "), true);
            } else {
                oled_write_P(PSTR("   "), false);
                oled_set_cursor(0, 1);
                oled_write_P(PSTR(" A "), false);
                oled_set_cursor(0, 2);
                oled_write_P(PSTR("   "), false);
            }
            oled_set_cursor(4, 0);
            if (led_state.num_lock) {
                oled_write_P(PSTR("   "), true);
                oled_set_cursor(4, 1);
                oled_write_P(PSTR(" 1 "), true);
                oled_set_cursor(4, 2);
                oled_write_P(PSTR("   "), true);
            } else {
                oled_write_P(PSTR("   "), false);
                oled_set_cursor(4, 1);
                oled_write_P(PSTR(" 1 "), false);
                oled_set_cursor(4, 2);
                oled_write_P(PSTR("   "), false);
            }
            oled_set_cursor(7, 0);
            if (led_state.scroll_lock) {
                oled_write_P(PSTR("   "), true);
                oled_set_cursor(7, 1);
                oled_write_P(PSTR(" S "), true);
                oled_set_cursor(7, 2);
                oled_write_P(PSTR("   "), true);
            } else {
                oled_write_P(PSTR("   "), false);
                oled_set_cursor(7, 1);
                oled_write_P(PSTR(" S "), false);
                oled_set_cursor(7, 2);
                oled_write_P(PSTR("   "), false);
            }
            break;
        case _UNI:
            oled_write_P(PSTR("Unicode"), false);
/* Theory for unicode layer
 * █A█ █1█ █S█ Layer: 
 *              Unicode
 * +- |1/4|3/4|TM
 * =/=|1/2| * |Fn
 */
            oled_set_cursor(0, 0); // Slim lock symbols to leave space for the unicode characters
            if (led_state.caps_lock) {
                oled_write_P(PSTR(" A "), true);
            } else {
                oled_write_P(PSTR(" A "), false);
            }
            oled_set_cursor(4, 0);
            if (led_state.num_lock) {
                oled_write_P(PSTR(" 1 "), true);
            } else {
                oled_write_P(PSTR(" 1 "), false);
            }
            oled_set_cursor(7, 0);
            if (led_state.scroll_lock) {
                oled_write_P(PSTR(" S "), true);
            } else {
                oled_write_P(PSTR(" S "), false);
            }
            oled_set_cursor(0, 2);
            // TODO make this a bit more readable, currently displays my best approximation of the unicode characters
            oled_write_P(PSTR("+- |1/4|3/4|TM\n=/=|1/2| * |Fn"), false);
            break;
        default:
            oled_write_P(PSTR("Undefined"), false);
    }

    return false;
}
#endif