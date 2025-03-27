// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

enum layers {
   _DVORAK,
   _LOWER,
   _RAISE,
};

#define LOWER MO(_LOWER)
#define RAISE MO(_RAISE)

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

/* DVORAK

* ┌───┬───┬───┬───┬───┬───┬────────┬───┬───┬───┬───┬───┬───┐
* │ESC│ 1 │ 2 │ 3 │ 4 │ 5 │        │ 6 │ 7 │ 8 │ 9 │ 0 │ = │
* ├───┼───┼───┼───┼───┼───┤        ├───┤───┤───┤───┤───┤───┤
* │Tab│ ' │ , │ . │ P │ Y │        │ F │ G │ C │ R │ L │ / │
* ├───┼───┼───┼───┼───┼───┤        ├───┤───┤───┤───┤───┤───┤
* │N/A│ A │ O │ E │ U │ I │        │ D │ H │ T │ N │ S │ENT│
* ├───┼───┼───┼───┼───┼───┤        ├───┤───┤───┤───┤───┤───┤
* │SFT│ ; │ Q │ J │ K │ X │        │ B │ M │ W │ V │ Z │ - │
* ├───┼───┼───┼───┼───┴───┤        ├───┴───┤───┤───┤───┤───┤
* │CTL│GUI│ALT│LYR│ SPACE │        │ BACK  │LYR│N/A│N/A│N/A│
* └───┴───┴───┴───┴───────┴────────┴───────┴───┴───┴───┴───┘
*/

[_DVORAK] = LAYOUT_2x2u(
    KC_ESC,   KC_1,    KC_2,    KC_3,    KC_4,    KC_5,    KC_6,    KC_7,    KC_8,    KC_9,    KC_0,    KC_EQL,
    KC_TAB,   KC_QUOT, KC_COMM, KC_DOT,  KC_P,    KC_Y,    KC_F,    KC_G,    KC_C,    KC_R,    KC_L,    KC_SLSH,
    KC_NO,    KC_A,    KC_O,    KC_E,    KC_U,    KC_I,    KC_D,    KC_H,    KC_T,    KC_N,    KC_S,    KC_ENT,
    KC_LSFT,  KC_SCLN, KC_Q,    KC_J,    KC_K,    KC_X,    KC_B,    KC_M,    KC_W,    KC_V,    KC_Z,    KC_MINS,
              KC_LCTL, KC_LGUI, KC_LALT, LOWER,   KC_SPC,  KC_BSPC, RAISE,   KC_NO,    KC_NO,    KC_NO
),

/* LOWER

* ┌───┬───┬───┬───┬───┬───┬────────┬───┬───┬───┬───┬───┬───┐
* │   │   │   │   │   │   │        │   │   │   │   │   │   │
* ├───┼───┼───┼───┼───┼───┤        ├───┤───┤───┤───┤───┤───┤
* │   │   │   │   │   │   │        │   │   │   │   │   │   │
* ├───┼───┼───┼───┼───┼───┤        ├───┤───┤───┤───┤───┤───┤
* │   │   │   │   │   │   │        │   │   │   │   │   │   │
* ├───┼───┼───┼───┼───┼───┤        ├───┤───┤───┤───┤───┤───┤
* │   │   │UND│CUT│CPY│PST│        │   │   │   │   │   │   │
* ├───┼───┼───┼───┼───┴───┤        ├───┴───┤───┤───┤───┤───┤
* │   │   │   │   │       │        │       │   │   │   │   │
* └───┴───┴───┴───┴───────┴────────┴───────┴───┴───┴───┴───┘
*/

[_LOWER] = LAYOUT_2x2u(
   KC_NO,   KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,
   KC_NO,   KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,
   KC_NO,   KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,
   KC_NO,   KC_NO,    KC_NO,    KC_UNDO,    KC_CUT,    KC_COPY,    	KC_PSTE,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,
                  KC_NO, KC_NO, KC_NO, KC_NO,   KC_NO,  KC_NO, KC_NO,   KC_NO,    KC_NO,    KC_NO
),

/* RAISE

* ┌───┬───┬───┬───┬───┬───┬────────┬───┬───┬───┬───┬───┬───┐
* │F1 │F2 │F3 │F4 │F5 │F6 │        │F7 │F8 │F9 │F10│F11│F12│
* ├───┼───┼───┼───┼───┼───┤        ├───┤───┤───┤───┤───┤───┤
* │   │   │   │   │   │   │        │   │   │   │   │   │   │
* ├───┼───┼───┼───┼───┼───┤        ├───┤───┤───┤───┤───┤───┤
* │   │   │   │   │   │   │        │   │   │   │   │   │   │
* ├───┼───┼───┼───┼───┼───┤        ├───┤───┤───┤───┤───┤───┤
* │   │   │   │   │   │   │        │   │   │   │   │   │   │
* ├───┼───┼───┼───┼───┴───┤        ├───┴───┤───┤───┤───┤───┤
* │   │   │   │   │       │        │       │   │   │   │   │
* └───┴───┴───┴───┴───────┴────────┴───────┴───┴───┴───┴───┘
*/

[_RAISE] = LAYOUT_2x2u(
   KC_F1,   KC_F2,    KC_F3,    KC_F4,    KC_F5,    KC_F6,    KC_F7,    KC_F8,    KC_F9,    KC_F10,    KC_F11,    KC_F12,
   KC_NO,   KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,
   KC_NO,   KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,
   KC_NO,   KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,    KC_NO,
                  KC_NO, KC_NO, KC_NO, KC_NO,   KC_NO,  KC_NO, KC_NO,   KC_NO,    KC_NO,    KC_NO
),

};
