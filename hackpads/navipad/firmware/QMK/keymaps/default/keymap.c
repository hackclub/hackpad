// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

bool is_alt_tab_active = false; // ADD this near the beginning of keymap.c
uint16_t alt_tab_timer = 0;     // we will be using them soon.

enum custom_keycodes {
    WIN_VIEW,
    WIN_FOR,
    WIN_BACK,
    NEW_DESK,
    CLOSE_DESK,
    DESK_FOR,
    DESK_BACK
};

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

    [0] = LAYOUT(
        RCS(KC_N), RALT(KC_F4), NEW_DESK, CLOSE_DESK, MO(1),
        RGUI(KC_1), RGUI(KC_2), RGUI(KC_3), RGUI(KC_4), RGUI(KC_5),
        RGUI(KC_6), RGUI(KC_7), RGUI(KC_8), RGUI(KC_9), RGUI(KC_0),
        KC_UNDO, KC_AGIN, KC_CUT, KC_COPY, KC_PSTE
    ),

    [1] = LAYOUT(
        KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,
        KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,
        KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,
        KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS
    ),
};

const uint16_t PROGMEM encoder_map[][1][2] = {
    [0] = { ENCODER_CCW_CW(WIN_BACK, WIN_FOR) },
    [1] = { ENCODER_CCW_CW(DESK_BACK, DESK_FOR) }
};

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    if (record->event.pressed) {
        switch(keycode) {
            case WIN_VIEW:
                register_code(KC_RGUI);
                tap_code(KC_TAB);
                unregister_code(KC_RGUI);
                return false;
            case WIN_FOR:
                if (!is_alt_tab_active) {
                    is_alt_tab_active = true;
                    register_code(KC_LALT);
                }
                alt_tab_timer = timer_read();
                tap_code(KC_TAB);
                return false;
            case WIN_BACK:
                if (!is_alt_tab_active) {
                    is_alt_tab_active = true;
                    register_code(KC_LALT);
                }
                alt_tab_timer = timer_read();
                register_code(KC_RSFT);
                tap_code(KC_TAB);
                unregister_code(KC_RSFT);
                return false;
            case NEW_DESK:
                register_code(KC_RCTL);
                register_code(KC_RGUI);
                tap_code(KC_D);
                unregister_code(KC_RGUI);
                unregister_code(KC_RCTL);
                return false;
            case CLOSE_DESK:
                register_code(KC_RCTL);
                register_code(KC_RGUI);
                tap_code(KC_F4);
                register_code(KC_RCTL);
                register_code(KC_RGUI);
                return false;
            case DESK_FOR:
                register_code(KC_RCTL);
                register_code(KC_RGUI);
                tap_code(KC_RGHT);
                register_code(KC_RCTL);
                register_code(KC_RGUI);
                return false;
            case DESK_BACK:
                register_code(KC_RCTL);
                register_code(KC_RGUI);
                tap_code(KC_LEFT);
                register_code(KC_RCTL);
                register_code(KC_RGUI);
                return false;
        }
    }
    return true;
}

void matrix_scan_user(void) { // The very important timer.
  if (is_alt_tab_active) {
    if (timer_elapsed(alt_tab_timer) > 750) {
      unregister_code(KC_LALT);
      is_alt_tab_active = false;
    }
  }
}