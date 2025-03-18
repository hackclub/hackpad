// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┬───┐
     * │CMD│OPT│ Z │ A │
     * ├───┼───┼───┼───┤
     * │CTR│SHF│ C │ V │
     * └───┴───┴───┴───┘
     */
    [0] = LAYOUT(
        KC_RIGHT_GUI,   KC_LALT,   KC_Z,   KC_A,
        KC_LCTL,   KC_LSFT,   KC_C,   KC_V
    )
};
