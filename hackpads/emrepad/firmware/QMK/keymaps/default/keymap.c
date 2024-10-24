// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H



// enum custom_keycoades
// {
//     CALC
// };

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┬───┐
     * │ 7 │ 8 │ 9 │ + │
     * ├───┼───┼───┼───┤
     * │ 4 │ 5 │ 6 │ + │
     * ├───┼───┼───┼───┤
     * │ 1 │ 2 │ 3 │ - │
     * ├───┼───┼───┼───┤
     * │ 0 │ 0 │ D │ - │
     * └───┴───┴───┴───┘
     */
    [0] = LAYOUT_emre_4x4(
        KC_7,    KC_8,    KC_9,    KC_PLUS,
        KC_4,    KC_5,    KC_6,    KC_PLUS,
        KC_1,    KC_2,    KC_3,    KC_ENTER,
        KC_0,    KC_0,    KC_DELETE,    KC_ENTER
    )
};

// bool process_record_user(uint16_t keycode, keyrecord_t *record)
// {
//     switch (keycode)
//     {
//         case CALC:
//             if(record->event.pressed)
//             {
//                 SEND_STRING(SS_DOWN(X_LGUI) SS_TAP(X_R) SS_UP(X_LGUI) SS_DELAY(50) "calc" SS_TAP(X_ENTER))
//             }
//             else
//             {
                
//             }
//         break;
//     }
//     return true;
// };
