// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later
 // Include for standard integer types

#include <stdint.h> 
#include QMK_KEYBOARD_H


#define MATRIX_ROWS 2
#define MATRIX_COLS 3

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT_ortho_1x3(
        KC_VOLU,      KC_VOLD,       KC_MPLY,     
                         
        KC_MUTE         
    )
};

#ifdef OLED_ENABLE
bool oled_task_user(void) {
    // Check if the keyboard is powered on
    if (matrix_is_on()) {
        oled_write_P(PSTR("musicBox\n"), false);  // Display "musicBox" when the keyboard is on
    } else {
        oled_clear();  // Clear the OLED when the keyboard is off
    }
   
    return false; // No further processing needed
}
#endif


void matrix_init_user(void) {
    #ifdef OLED_ENABLE
        oled_init();  // Initialize the OLED display
    #endif
}
