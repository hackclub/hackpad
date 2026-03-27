// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

#define _MAC 0
#define _NUM 1
#define _ALT 2

#if defined(ENCODER_MAP_ENABLE)
// https://docs.qmk.fm/features/encoders
const uint16_t PROGMEM encoder_map[][NUM_ENCODERS][NUM_DIRECTIONS] = {
    [_MAC] = { ENCODER_CCW_CW(KC_VOLD, KC_VOLU) },
    [_NUM] = { ENCODER_CCW_CW(KC_VOLD, KC_VOLU) },
    [_ALT] = { ENCODER_CCW_CW(KC_BRID, KC_BRIU) },
};
#endif

#ifdef OLED_ENABLE
bool oled_task_user(void) {
    oled_write_P(PSTR("Layer: "), false);

    switch (get_highest_layer(layer_state)) {
        case _MAC:
            oled_write_ln_P(PSTR("Shortcuts"), false);
            break;
        case _NUM:
            oled_write_P(PSTR("Numpad | NUM LOCK: "), false);
            if (host_keyboard_led_state().num_lock) {
                oled_write_ln_P(PSTR("ON"), false);
            } else {
                oled_write_ln_P(PSTR("OFF"), false);
            }
            break;
        case _ALT:
            oled_write_ln_P(PSTR("Alt"), false);
            break;
        default:
            // Or use the write_ln shortcut over adding '\n' to the end of your string
            oled_write_ln_P(PSTR("Undefined"), false);
    }

    // Host Keyboard LED Status
    led_t led_state = host_keyboard_led_state();
    oled_write_P(led_state.num_lock ? PSTR("NUM ") : PSTR("    "), false);
    oled_write_P(led_state.caps_lock ? PSTR("CAP ") : PSTR("    "), false);
    oled_write_P(led_state.scroll_lock ? PSTR("SCR ") : PSTR("    "), false);
    
    return false;
}
#endif

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┐
     * │Cpy│Und│Slp│
     * ├───┼───┼───┤
     * │Pst│Red│Wak│
     * ├───┼───┼───┤
     * │Cal│Nxt│Prv│
     * ├───┼───┼───┤
     * │Psc│Alt│Med│
     * └───┴───┴───┘
     */
    [_MAC] = LAYOUT(
        KC_COPY, KC_UNDO, KC_SLEP,
        KC_PSTE, KC_AGIN, KC_WAKE,
        KC_CALC, KC_MNXT, KC_MPRV,
        KC_PSCR, MO(_ALT),KC_MPLY
    ),
    /*
     * ┌───┬───┬───┐
     * │ 7 │ 8 │ 9 │
     * ├───┼───┼───┤
     * │ 4 │ 5 │ 6 │
     * ├───┼───┼───┤
     * │ 1 │ 2 │ 3 │
     * ├───┼───┼───┤
     * │ 0 │   │   │
     * └───┴───┴───┘
     */
    [_NUM] = LAYOUT(
        KC_P7,   KC_P8,   KC_P9,
        KC_P4,   KC_P5,   KC_P6,
        KC_P1,   KC_P2,   KC_P3,
        KC_P0,   KC_TRNS, KC_TRNS
    ),
        /*
     * ┌───┬───┬───┐
     * │---│---│---│
     * ├───┼───┼───┤
     * │Num│ * │ / │
     * ├───┼───┼───┤
     * │MOD│ + │ - |
     * ├───┼───┼───┤
     * │Ent│   │Mut│
     * └───┴───┴───┘
     */
    [_ALT] = LAYOUT(
        KC_NO,   KC_NO,   KC_NO,
        KC_LNUM, KC_PAST, KC_PSLS,
        TG(_NUM),KC_PPLS, KC_PMNS,
        KC_PENT, KC_TRNS, KC_MUTE
    ),
};
