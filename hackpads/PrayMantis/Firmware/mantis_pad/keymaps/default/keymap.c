// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

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
    [0] = LAYOUT(
        KC_BRIU,   KC_VOLU,   KC_MPRV,
        KC_BRID,   KC_VOLD,   KC_MNXT,
        KC_CALC,   KC_KB_MUTE,   KC_MPLY
    )
};

#ifdef OLED_ENABLE

bool oled_task_user() {

    oled_set_cursor(0,1);
    oled_write("Mantis Board..", false);

    return false;
}

#endif