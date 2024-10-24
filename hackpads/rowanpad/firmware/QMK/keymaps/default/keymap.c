// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

enum layers  {
    _BASE = 0,
    _ARROWS,
    _MEDIA
};

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /** 
    *  -----------
    * |
*  -----------                          
    */
    [_BASE] = LAYOUT_ortho_4x4(                
        KC_P7,   KC_P8,   KC_P4,   KC_P5   
    ),

    [_ARROWS] = LAYOUT_ortho_4x4(
        KC_LEFT,  KC_UP, KC_DOWN, KC_RIGHT
    ),

    [_MEDIA] = LAYOUT_ortho_4x4(
        KC_VOLU,  KC_VOLD, KC_MPLY, KC_MSTP
    )
};

// Joystick input setup
joystick_config_t joystick_axes[JOYSTICK_AXIS_COUNT] = {
    JOYSTICK_AXIS_IN(GP1, 127, 0, -127),
    JOYSTICK_AXIS_IN(GP29 , 127, 0, -127),
};  

// OLED Driver
#ifdef OLED_ENABLE
bool oled_task_user(void) {
    // Host Keyboard Layer Status
    oled_write_P(PSTR("Layer: "), false);

    switch (get_highest_layer(layer_state)) {
        case _BASE:
            oled_write_P(PSTR("Default\n"), false);
            break;
        case _ARROWS:
            oled_write_P(PSTR("Arrow Keys\n"), false);
            break;
        case _MEDIA:
            oled_write_P(PSTR("Media\n"), false);
            break;
        default:
            // Or use the write_ln shortcut over adding '\n' to the end of your string
            oled_write_ln_P(PSTR("Undefined"), false);
    }
    
    return false;
}
#endif