// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include <stdint.h>
#include QMK_KEYBOARD_H

enum custom_keycodes {
    MODE_SWITCH = SAFE_RANGE,
    M1,
    M2,
    M3,
    M4,
    M5,
    M6,
    M7,
    M8,
    M9,
    M10,
    M11,
    M12,
    M13,
    M14,
    M15,
    M16,
    M17,
    M18
};

#define LAYER_CYCLE_START 0
#define LAYER_CYCLE_END 3

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┬───┐
     * │ A │ B │ C │ J │
     * ├───┼───┼───┼───┘
     * │ D │ E │ F │
     * ├───┼───┼───┤
     * │ G │ H │ I │
     * └───┴───┴───┘
     */
    [0] = LAYOUT(QK_BOOTLOADER, QK_DEBUG_TOGGLE, QK_CLEAR_EEPROM, MODE_SWITCH, KC_LCTL, QK_MAKE, KC_LGUI, KC_LALT, QK_REBOOT, KC_PWR),
    [1] = LAYOUT(KC_P1, KC_P2, KC_P3, MODE_SWITCH, KC_P4, KC_P5, KC_P6, KC_P7, KC_P8, KC_P9),
    [2] = LAYOUT(M1, M2, M3, MODE_SWITCH, M4, M5, M6, M7, M8, M9),
    [3] = LAYOUT(M10, M11, M12, MODE_SWITCH, M13, M14, M15, M16, M17, M18)
};

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    switch (keycode) {
        case MODE_SWITCH:
            if (!record->event.pressed) {
                return false;
            }
            uint8_t current_layer = get_highest_layer(layer_state);

            if (current_layer > LAYER_CYCLE_END || current_layer < LAYER_CYCLE_START) {
                return false;
            }

            uint8_t next_layer = current_layer + 1;
            if (next_layer > LAYER_CYCLE_END) {
                next_layer = LAYER_CYCLE_START;
            }

            layer_move(next_layer);
            return false;
        case M1:
            if (record->event.pressed) {
                // Macro 1 code here
            }
            return false;
        case M2:
            if (record->event.pressed) {
                // Macro 2 code here
            }
            return false;
        case M3:
            if (record->event.pressed) {
                // Macro 3 code here
            }
            return false;
        case M4:
            if (record->event.pressed) {
                // Macro 4 code here
            }
            return false;
        case M5:
            if (record->event.pressed) {
                // Macro 5 code here
            }
            return false;
        case M6:
            if (record->event.pressed) {
                // Macro 6 code here
            }
            return false;
        case M7:
            if (record->event.pressed) {
                // Macro 7 code here
            }
            return false;
        case M8:
            if (record->event.pressed) {
                // Macro 8 code here
            }
            return false;
        case M9:
            if (record->event.pressed) {
                // Macro 9 code here
            }
            return false;
        case M10:
            if (record->event.pressed) {
                // Macro 10 code here
            }
            return false;
        case M11:
            if (record->event.pressed) {
                // Macro 11 code here
            }
            return false;
        case M12:
            if (record->event.pressed) {
                // Macro 12 code here
            }
            return false;
        case M13:
            if (record->event.pressed) {
                // Macro 13 code here
            }
            return false;
        case M14:
            if (record->event.pressed) {
                // Macro 14 code here
            }
            return false;
        case M15:
            if (record->event.pressed) {
                // Macro 15 code here
            }
            return false;
        case M16:
            if (record->event.pressed) {
                // Macro 16 code here
            }
            return false;
        case M17:
            if (record->event.pressed) {
                // Macro 17 code here
            }
            return false;
        case M18:
            if (record->event.pressed) {
                // Macro 18 code here
            }
            return false;
        default:
            return true;
    }
}

#ifdef OLED_ENABLE
bool oled_task_user(void) {
    // Host Keyboard Layer Status
    oled_write_P(PSTR("Layer: "), false);

    switch (get_highest_layer(layer_state)) {
        case 0:
            oled_write_ln_P(PSTR("QMK"), false);
            break;
        case 1:
            oled_write_ln_P(PSTR("Numpad"), false);
            break;
        case 2:
            oled_write_ln_P(PSTR("Macros 1"), false);
            break;
        case 3:
            oled_write_ln_P(PSTR("Macros 2"), false);
            break;
        default:
            oled_write_ln_P(PSTR("Undefined"), false);
    }
    return false;
}
#endif
