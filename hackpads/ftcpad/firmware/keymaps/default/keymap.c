// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┐
     * │STB│U P│TAB│
     * ├───┼───┼───┤
     * │LFT│DWN│RGT│
     * └───┴───┴───┘
     */
    [0] = LAYOUT_ortho_2x3(
        LSFT(KC_TAB),    KC_UP,    KC_TAB,
        KC_LEFT,    KC_DOWN,    KC_RIGHT
    )
};

#ifdef OLED_ENABLE
bool oled_task_user(void) {

    led_t led_state = host_keyboard_led_state();
    oled_write_P(led_state.num_lock ? PSTR("NUM ") : PSTR("    "), false);
    oled_write_P(led_state.caps_lock ? PSTR("CAP ") : PSTR("    "), false);
    oled_write_P(led_state.scroll_lock ? PSTR("SCR ") : PSTR("    "), false);
    
    return false;
}
#endif
#if defined(ENCODER_MAP_ENABLE)
const uint16_t PROGMEM encoder_map[][NUM_ENCODERS][NUM_DIRECTIONS] = {
    [0] = { ENCODER_CCW_CW(KC_PAGE_UP, KC_PAGE_DOWN)},
};
#endif