// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┬
     * │ X │   │ T │
     * ├───┼───┼───┼
     * │ Q │ W │ E │
     * ├───┼───┼───┼
     * │ A │ S │ D │
     * ├───┼───┼───┼
     *
     */
    [0] = LAYOUT(
        KC_X,   KC_SPACE,   KC_T,
        KC_Q,   KC_W,   KC_E,
        KC_A,   KC_S,   KC_D
    )

};

#if defined(ENCODER_MAP_ENABLE)
const uint16_t PROGMEM encoder_map[][NUM_ENCODERS][NUM_DIRECTIONS] = {
    [0] = { ENCODER_CCW_CW(KC_LCTL, KC_LSFT) }
};
#endif

#ifdef OLED_DRIVER_ENABLE
bool oled_task_user(void) {
    oled_clear();
    oled_write_ln_P(PSTR("LerPad :D"), false);
    return false;
}
#endif
