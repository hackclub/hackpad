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

enum ergo_kola_layers {
    _QWERTY,
    _LOWER,
    _RAISE,
    _ADJUST
  };
  
  enum ergo_kola_keycodes {
    QWERTY = SAFE_RANGE
  };
  
  #define LOWER MO(_LOWER)
  #define RAISE MO(_RAISE)
  

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [_QWERTY] = LAYOUT(
        KC_TAB, KC_Q, KC_W, KC_E, KC_R, KC_T,                        KC_Y, KC_U, KC_I, KC_O, KC_P, KC_BSPC,\
        KC_ESC, KC_A, KC_S, KC_D, KC_F, KC_G,                        KC_H, KC_J, KC_K, KC_L, KC_SCLN, KC_QUOT, \
        KC_LSFT, KC_Z, KC_X, KC_C, KC_V, KC_B,                       KC_N, KC_M, KC_COMM, KC_DOT, KC_SLASH, KC_RETN, \
        KC_MUTE, KC_LCTL, KC_LOPT, KC_LGUI, TL_LOWR, KC_SPC,         KC_SPC, TL_UPPR, KC_RIGHT, KC_DOWN, KC_UP, KC_LEFT,           \
                                LM_TOGG, LM_NEXT,                          LM_BRIU, LM_BRID,
    ),
    [_LOWER] = LAYOUT(
        KC_TILDE, KC_EXCLAIM, KC_AT, KC_HASH, KC_DOLLAR, KC_PERCENT,         KC_CIRCUMFLEX, KC_AMPERSAND, KC_ASTERISK, KC_LEFT_PAREN, KC_RIGHT_PAREN, ______,\
        KC_DELETE, KC_F1, KC_F2, KC_F3, KC_F4, KC_F5,                        KC_F6, KC_MINUS, KC_EQUAL, KC_LBRC, KC_RBRC, KC_PIPE, \
        _______, KC_F7, KC_F8, KC_F9, KC_F10, KC_F11,                        KC_F12, _______, _______, KC_HOME, KC_END, _______, \
        _______, _______, _______, _______, _______, _______,         _______, _______, _______, _______, _______, _______,           \
                                            _______, _______,         _______, _______
    ),
    [_RAISE] = LAYOUT(
        KC_GRV, KC_1, KC_2, KC_3, KC_4, KC_5,               KC_6, KC_7, KC_8, KC_9, KC_0, ______,\
        _______, KC_F1, KC_F2, KC_F3, KC_4, KC_F5,          KC_F6, KC_UNDS, KC_PLUS, KC_LCBR, KC_RCBR, KC_BSLS, \
        _______, KC_F7, KC_F8, KC_F9, KC_F10, KC_F11,         KC_F12, _______, _______, KC_PGUP, KC_PGDN, _______, \
        _______, _______, _______, _______, _______, _______,         _______, _______, _______, _______, _______, _______,           \
                                            _______, _______,         _______, _______
    ),
    [_ADJUST] = LAYOUT(
        _______, _______, _______, LM_TOGG, LM_NEXT, LM_PREV,         LM_BRIU, LM_BRID, LM_SPDU, LM_SPDD, KC_DEL , \
        _______, _______, _______, _______, _______, _______,         _______, _______, _______, _______, _______, _______, \
        _______, _______, _______, _______, _______, _______,         _______, _______, _______, _______, _______, _______, \
        _______, _______, _______, _______, _______, _______,         _______, _______, _______, _______, _______, _______,           \
                                            _______, _______,         _______, _______
    )
};

layer_state_t layer_state_set_user(layer_state_t state) {
    return update_tri_layer_state(state, _LOWER, _RAISE, _ADJUST);
  }