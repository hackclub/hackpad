// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

enum custom_keycodes
{
    SQRT,
    CBRT,
    POWSQ,
    POW,
    SUB, //Subscripts
    LANSWITCH, //Langauge switchers
};



bool process_record_user(unit16_t keycode, keyrocord_t *record){
    switch (keycode) {
        case SQRT:
            if (record->event.pressed) {
                SEND_STRING("sqrt")
            }
            else {
                // key released
            }
            break;
        case CBRT:
                if (record->event.pressed) {
                    SEND_STRING("cbrt")
                }
                else {
                    // key released
                }
                break;
        case POWSQ:
                if (record->event.pressed) {
                    SEND_STRING(SS_LSFT("6")"2"SS_TAP(X_RGHT))
                }
                else {
                    // key released
                }
                break;
        case POW:
                if (record->event.pressed) {
                    SEND_STRING(SS_LSFT("6"))
                }
                else {
                    // key released
                }
                break;
        case SUB:
                if (record->event.pressed) {
                    SEND_STRING(SS_LSFT("-"))
                }
                else {
                    // key released
                }
                break;
        case LANSWITCH:
                if (record->event.pressed) {
                    SEND_STRING(SS_DOWN(X_LWIN)SS_TAP(X_SPC)SS_UP(X_LWIN))
                }
                else {
                    // key released
                }
                break;
    }
    return true;
}


const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ├───┼───┼───┼
     * │SQR│^2 │ V+│
     * ├───┼───┼───┼
     * │CBR│ ^ │ V-│
     * ├───┼───┼───┼
     * │LAS│SUB│Ent│
     * └───┴───┴───┴
     */
    [0] = LAYOUT_mackerel3x3(
        SQRT,   POWSQ,   KC_VOLU,  
        CBRT,   POW,   KC_VOLD,   
        KC_MUTE,   SUB,   KC_PENT
    )
};
