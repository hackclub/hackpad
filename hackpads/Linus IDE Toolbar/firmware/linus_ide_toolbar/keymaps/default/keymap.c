// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┬───┬───┐
     * │ D │ S │ R │ SO│ SI│
     * └───┴───┴───┴───┴───┘
     */

    [0] = LAYOUT(
        KC_F20, KC_F21, KC_F22, KC_F23, KC_F24
    )
};

#ifdef OLED_ENABLE
#ifdef RAW_ENABLE

oled_rotation_t oled_init_user(oled_rotation_t rotation) {
    return OLED_ROTATION_180;  // flips the display 180 degrees if offhand
}

// HID input handler
void raw_hid_receive(uint8_t *data, uint8_t length) {
    char *input = (char *)data;
    oled_clear()
    oled_write_P(PSTR(input), false);
}

#endif
#endif