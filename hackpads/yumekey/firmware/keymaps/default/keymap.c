// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * [ Esc   ] [ W     ] [ Enter ] [ .     ] [ Z     ]
     * [ A     ] [ S     ] [ D     ] [ .     ] [ X     ]
     */
    [0] = LAYOUT(
        KC_ESC,  KC_W,     KC_ENT,   KC_NO,    KC_Z,
        KC_A,    KC_S,     KC_D,     KC_NO,    KC_X
    )
};

#ifdef ENCODER_MAP_ENABLE
const uint16_t PROGMEM encoder_map[][1][2] = {
    [0] = { ENCODER_CCW_CW(MS_WHLU, MS_WHLD) }    
};
#endif

#ifdef OLED_ENABLE
bool oled_task_user() {
    oled_set_cursor(0, 1);
    oled_write("Everything works??", false);
    return false;
}
#endif
