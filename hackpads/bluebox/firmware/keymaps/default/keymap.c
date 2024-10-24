// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H



const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┐
     * │esc│hme│end│
     * ├───┼───┼───┤
     * │del│up │ctl│
     * ├───┼───┼───┤
     * │lft│dwn│rgt│
     * └───┴───┴───┘
     */
    [0] = LAYOUT_ortho_3x3(
        KC_ESCAPE,    KC_HOME,    KC_END,
        KC_DELETE,    KC_UP,    KC_LEFT_CTRL,
        KC_LEFT,    KC_DOWN,    KC_RIGHT
    )
};

#ifdef OLED_ENABLE

//rotate oled
oled_rotation_t oled_init_user(oled_rotation_t rotation) {

      return OLED_ROTATION_90;

}


//oled code

bool oled_task_user(){


   return 0;

}

#endif
