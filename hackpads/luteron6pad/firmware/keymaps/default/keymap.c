// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H
#ifdef OLED_ENABLE


//LAYERS
enum layer_names {
    BASE,//BASE LAYER
    FUNC,//FUNCTION LAYER
    CODE,//Coding Layer
};


//OLED SETTINGS
// Rotate OLED
//oled_rotation_t oled_init_user(oled_rotation_t rotation) {
//    return OLED_ROTATION_90;  
//}

// Draw to OLED
bool oled_task_user() {
    // Set cursor position
    oled_set_cursor(0, 1);
    
    // Write text to OLED
    oled_write("Welcome to luteron6's Hackpad!", false);
    
    return false;
}
#endif
//END OLED SETTINGS


//ENCODER SETTINGS
//Layers are _BL,_FL, and _CL
#if defined(ENCODER_MAP_ENABLE)
const uint16_t PROGMEM encoder_map[][NUM_ENCODERS][NUM_DIRECTIONS] = {
    [0] = { ENCODER_CCW_CW(DF(CODE), DF(FUNC))}, //Base Layer
    [1] = { ENCODER_CCW_CW(DF(BASE), DF(CODE))}, //Function Layer
    [2] = { ENCODER_CCW_CW(DF(FUNC), DF(BASE))}, //Code Layer
};
#endif
//END ENCODER SETTINGS


const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┐
     * │ 1 │ 2 │ROT│<---3
     * ├───┼───┼───┤
     * │ 4 │ 5 │ 6 │
     * └───┴───┴───┘
     */
    [BASE] = LAYOUT_3x2(
        KC_1,   KC_2,   KC_3,
        KC_4,   KC_5,   KC_6
    ),
    
    [FUNC] = LAYOUT_3x2(
        KC_1,   KC_2,   KC_3,
        KC_4,   KC_5,   KC_6
    ),

    [CODE] = LAYOUT_3x2(
        KC_1,   KC_2,   KC_3,
        KC_4,   KC_5,   KC_6
    ),
};