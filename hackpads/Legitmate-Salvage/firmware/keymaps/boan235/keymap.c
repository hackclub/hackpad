// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

enum layer_names {
    _BASE,
    _AUDIO,
    _CODE
};

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /* Base Layer
     * ┌───┬───┬───┐
     * │ 7 │ 8 │ 9 │
     * ├───┼───┼───┤
     * │ 4 │ 5 │ 6 │
     * ├───┼───┼───┤
     * │ 1 │ 2 │ 3 │
     * └───┴───┴───┘
     *       ┌───┐
     *       │ 0 │
     *       └───┘
     */
    [_BASE] = LAYOUT(
        KC_7, KC_8, KC_9,
        KC_4, KC_5, KC_6,
        KC_1, KC_2, KC_3,
        MO(_AUDIO) // Extra key to switch to AUDIO layer
    ),
    /* Audio Layer
     * ┌─────┬─────┬─────┐
     * │ MUTE│ VOL+│ VOL-│
     * ├─────┼─────┼─────┤
     * │ PREV│ PLAY│ NEXT│
     * ├─────┼─────┼─────┤
     * │ STOP│     │     │
     * └─────┴─────┴─────┘
     *       ┌─────┐
     *       │     │
     *       └─────┘
     */
    [_AUDIO] = LAYOUT(
        KC_MUTE, KC_VOLU, KC_VOLD,
        KC_MPRV, KC_MPLY, KC_MNXT,
        KC_MSTP, _______, _______, MO(_CODE) // Extra key to switch to CODE layer
    ),
    /* Code Layer
     * ┌─────┬─────┬─────┐
     * │ COPY│ PASTE│ CUT│
     * ├─────┼─────┼─────┤
     * │ UNDO│ REDO│ FIND│
     * ├─────┼─────┼─────┤
     * │ HOME│     │     │
     * └─────┴─────┴─────┘
     *       ┌─────┐
     *       │     │
     *       └─────┘
     */
    [_CODE] = LAYOUT(
        KC_COPY, KC_PASTE, KC_CUT,
        KC_UNDO, C(KC_Y), KC_FIND, // Replaced KC_REDO with C(KC_Y) for redo
        KC_HOME, _______, _______, MO(_BASE) // Extra key to switch back to BASE layer
    )
};

const uint16_t PROGMEM encoder_map[][NUM_ENCODERS][NUM_DIRECTIONS] = {
    [_BASE] = { { KC_VOLU, KC_VOLD } },
    [_AUDIO] = { { KC_VOLU, KC_VOLD } },
    [_CODE] = { { KC_VOLU, KC_VOLD } }
};

#ifdef OLED_ENABLE
bool oled_task_user() {
    oled_set_cursor(0, 1);

    switch (get_highest_layer(layer_state)) {
        case _BASE:
            oled_write_P(PSTR("BASE"), false);
            break;
        case _AUDIO:
            oled_write_P(PSTR("AUDIO"), false);
            break;
        case _CODE:
            oled_write_P(PSTR("CODE"), false);
            break;
    }

    return false;
}
#endif