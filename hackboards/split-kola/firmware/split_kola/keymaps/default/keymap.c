/*
Copyright 2025 Micah Edwards

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/
#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT(
        KC_1, KC_2, KC_3, KC_4, KC_5, KC_6, KC_7,                             KC_8, KC_9, KC_0, KC_MINUS, KC_EQUAL, KC_BACKSPACE,               \
        KC_DELETE, KC_GRAVE, KC_Q, KC_W, KC_E, KC_R, KC_T,                    KC_Y, KC_U, KC_I, KC_O, KC_P, KC_LEFT_BRACKET, KC_RIGHT_BRACKET, \
        LT(1, KC_ESCAPE), KC_TAB, KC_A, KC_S, KC_D, KC_F, KC_G,                      KC_H, KC_J, KC_K, KC_L, KC_SEMICOLON, KC_QUOTE, KC_NONUS_BACKSLASH, \
                KC_Z, KC_X, KC_C, KC_V, KC_B,                                   KC_N, KC_M, KC_COMMA, KC_DOT, KC_SLASH,            \
                KC_LEFT_SHIFT, KC_LEFT_CTRL, KC_LEFT_GUI, KC_SPACE,             KC_SPACE, KC_RIGHT_CTRL, KC_ENTER, KC_RIGHT_SHIFT
    ),
    [1] = LAYOUT(
        KC_F1, KC_F2, KC_F3, KC_F4, KC_F5, KC_F6, KC_F7,                            KC_F8, KC_F9, KC_F10, KC_F11, KC_F12, KC_DELETE        , \
        KC_INSERT, KC_PRINT_SCREEN, _______, _______, _______, _______, _______,    _______, _______, _______, _______, _______, _______, _______, \
        KC_NO, _______, _______, _______, _______, _______, _______,              KC_CAPS_LOCK, _______, _______, _______, _______, _______, _______, \
                _______, _______, _______, _______, _______,                            _______, _______, _______, _______, _______,           \
                KC_LEFT_SHIFT, KC_LEFT_CTRL, KC_LEFT_ALT, _______,                      _______, KC_RIGHT_CTRL, KC_RIGHT_ALT, KC_RIGHT_SHIFT
    ),
    [2] = LAYOUT(
        _______, _______, _______, _______, _______, _______, _______,          _______, _______, _______, _______, _______, _______        , \
        _______, _______, _______, _______, _______, _______, _______,          _______, _______, _______, _______, _______, _______, _______, \
        _______, _______, _______, _______, _______, _______, _______,          _______, _______, _______, _______, _______, _______, _______, \
                _______, _______, _______, _______, _______,                        _______, _______, _______, _______, _______,           \
                    _______, _______, _______, _______,                                 _______, _______, _______, _______
    ),
    [3] = LAYOUT(
        _______, _______, _______, _______, _______, _______, _______,          _______, _______, _______, _______, _______, _______        , \
        _______, _______, _______, _______, _______, _______, _______,          _______, _______, _______, _______, _______, _______, _______, \
        _______, _______, _______, _______, _______, _______, _______,          _______, _______, _______, _______, _______, _______, _______, \
                _______, _______, _______, _______, _______,                        _______, _______, _______, _______, _______,           \
                    _______, _______, _______, _______,                                 _______, _______, _______, _______
    )
};

#ifdef ENCODER_MAP_ENABLE
const uint16_t PROGMEM encoder_map[][NUM_ENCODERS][NUM_DIRECTIONS] = {
    [0] = { ENCODER_CCW_CW(KC_VOLD, KC_VOLU), ENCODER_CCW_CW(KC_MPRV, KC_MNXT) },
    [1] = { ENCODER_CCW_CW(KC_VOLD, KC_VOLU), ENCODER_CCW_CW(KC_MPRV, KC_MNXT) },
    [2] = { ENCODER_CCW_CW(KC_VOLD, KC_VOLU), ENCODER_CCW_CW(KC_MPRV, KC_MNXT) },
    [3] = { ENCODER_CCW_CW(KC_VOLD, KC_VOLU), ENCODER_CCW_CW(KC_MPRV, KC_MNXT) },
};
#endif