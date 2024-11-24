// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include <stdint.h>
#include <stdbool.h>
#include QMK_KEYBOARD_H


const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───────┬───────┬───────┐
     * │   1   │   2   │   3   │  _______
     * │       │       │       │ │       │
     * ├───────┼───────┼───────┤ │       │
     * │   4   │ BLTOG │   6   │ │ VKTOG │
     * │       │       │       │ │       │
     * ├───────┼───────┼───────┤ │       │
     * │   7   │   8   │   9   │ │_______│
     * │       │       │       │
     * └───────┴───────┴───────┘
     */
    [0] = LAYOUT(
        QK_PROGRAMMABLE_BUTTON_1, QK_PROGRAMMABLE_BUTTON_2,   QK_PROGRAMMABLE_BUTTON_3,
        QK_PROGRAMMABLE_BUTTON_4, UG_TOGG,                    QK_PROGRAMMABLE_BUTTON_6,
        QK_PROGRAMMABLE_BUTTON_7, QK_PROGRAMMABLE_BUTTON_8,   QK_PROGRAMMABLE_BUTTON_9,
                                  VK_TOGG
    )
};

bool encoder_update_user(uint8_t index, bool clockwise) {
    if (index == 0) {
        if (clockwise) {
            // switch LED mode to the next one
            rgblight_step();
        } else {
            // switch LED mode to the previous one
            rgblight_step_reverse();
        }
    }
    return false;
}
