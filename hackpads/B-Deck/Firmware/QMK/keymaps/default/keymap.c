// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

    [0] = LAYOUT(
        KC_1, KC_2, KC_3,KC_KB_MUTE,
        KC_LCTL, KC_Z, KC_X, KC_C, KC_V
    )
};

const uint16_t PROGMEM encoder_map[][1][2] = {
    [0] = { ENCODER_CCW_CW(KC_VOLU, KC_VOLD) },
};

#ifdef OLED_ENABLE
bool oled_task_user(void) {
    // Host Keyboard Layer Status
    oled_write_P(PSTR("Layer: "), false);
    switch (biton32(layer_state)) {
        case 0:
            oled_write_P(PSTR("Default\n"), false);
            break;
        // Add more cases for additional layers if needed
        default:
            oled_write_P(PSTR("Undefined\n"), false);
    }
    return false;
}
#endif