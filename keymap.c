// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later
#include QMK_KEYBOARD_H
enum custom_keycodes {
    GC = SAFE_RANGE,
    NEWTAB = SAFE_RANGE+1,
    DISCORD = SAFE_RANGE+2,
    GMAIL = SAFE_RANGE+3,
};
bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    switch (keycode) {
    case GC:
        if (record->event.pressed) {
            // when keycode GC is pressed
            SEND_STRING("https://classroom.google.com/u/1/");
        } else {
            // when keycode GC is released
}
        break;
    case NEWTAB:
        if (record->event.pressed) {
            SEND_STRING(SS_TAP(XK_COMMAND), SS_DELAY(50), SS_TAP(XK_N));
        }
        break;
            
    case DISCORD:
        if (record->event.pressed) {
              SEND_STRING("https://discord.com/channels/1234637010753294388/1234637014603665456");
        }
        break;
    case GMAIL:
        if (record->event.pressed) {
            SEND_STRING("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox");
        }
        break;
    }
    return true;
};
        
const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    
    [0] = LAYOUT(
        KC_LAUNCHPAD,   KC_WWW_REFRESH, {KC_LCTL ,KC_LGUI ,KC_SPC},
        {NEWTAB, GC, KC_ENTER},   {NEWTAB, DISCORD, KC_ENTER},   {NEWTAB, GMAIL, KC_ENTER},
        
    )
