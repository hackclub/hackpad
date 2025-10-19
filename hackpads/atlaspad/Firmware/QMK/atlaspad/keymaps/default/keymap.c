// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

//box drawing characters
// ┌ ┬ ┐
// ├ ┼ ┤
// └ ┴ ┘
// ─ │

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───────┬───┐
     * │/\ │       │Hom│
     * ├───┤       ├───┤
     * │\/ │       │End│
     * ├───┼───┬───┼───┤
     * │F1 │F2 │F3 │F4 │
     * ├───┼───┼───┼───┤
     * │F5 │F6 │F7 │F8 │
     * └───────┴───┴───┘
     */
    [0] = LAYOUT_pad_4x4_2Enc(
        KC_PGUP,               KC_HOME,
        KC_PGDN,               KC_END,
        KC_F1, KC_F2,  KC_F3,  KC_F4,
        KC_F5, KC_F6,  KC_F7,  KC_F8
    )
};

#ifdef DIP_SWITCH_ENABLE
//Encoders as DIP switches in Matrix Grid
uint32_t stateBefore = 1UL << 4;

bool dip_switch_update_mask_user(uint32_t state) { 
    if (state == stateBefore) return false;
    uint32_t rising = state & ~stateBefore;
    if (stateBefore != 1UL << 4) {
        uint32_t enc1 = rising & (1UL << 0 | 1UL << 1); 
        uint32_t enc2 = (rising & (1UL << 2 | 1UL << 3))>>2;

        if (enc1 == 2){
            tap_code(KC_RIGHT);
        } else if (enc1 == 1){
            tap_code(KC_LEFT);
        }
        if (enc2 == 2){
            tap_code_delay(KC_KB_VOLUME_UP,10);
        } else if (enc2 == 1){
            tap_code_delay(KC_KB_VOLUME_DOWN,10);
        }
    }
    stateBefore = state;
    return true;
}
#endif  

#ifdef OLED_ENABLE
oled_rotation_t oled_init_user(oled_rotation_t rotation) {
        return OLED_ROTATION_180; 
}
bool oled_task_user(void) {
    //test line
    oled_write_P(PSTR("Atlaspad by Volkov"), false);
    // Host Keyboard LED Status
    led_t led_state = host_keyboard_led_state();
    oled_write_P(led_state.num_lock ? PSTR("NUM ") : PSTR("    "), false);
    oled_write_P(led_state.caps_lock ? PSTR("CAP ") : PSTR("    "), false);
    oled_write_P(led_state.scroll_lock ? PSTR("SCR ") : PSTR("    "), false);
    
    return false;
}
#endif