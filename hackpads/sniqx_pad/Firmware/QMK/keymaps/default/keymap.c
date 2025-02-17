// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     *         ┌───┬───┐
     *         │ V │ P │
     * ┌───┬───┼───┼───┤
     * │esc│ d │ i │Etr│
     * ├───┼───┼───┼───┤
     * │ h │ j │ k │ l │
     * └───┴───┴───┴───┘
     */
    [0] = LAYOUT_ortho_3x4(
        KC_V, KC_P, KC_NO, KC_NO,
        KC_ESC, KC_D, KC_I, KC_ENT,
        KC_H, KC_J, KC_K, KC_L
    )
};

const uint16_t PROGMEM encoder_map[][1][2] = {
    [0] = { ENCODER_CCW_CW(MS_WHLU, MS_WHLD),  ENCODER_CCW_CW(KC_VOLD, KC_VOLU)  },
};

#ifdef OLED_ENABLE
void oled_render_boot(bool bootloader) {
    oled_clear();
    for (int i = 0; i < 16; i++) {
        oled_set_cursor(0, i);
        if (bootloader) {
            oled_write_P(PSTR("Awaiting New Firmware "), false);
        } else {
            oled_write_P(PSTR("Rebooting "), false);
        }
    }

    oled_render_dirty(true);
}
#endif