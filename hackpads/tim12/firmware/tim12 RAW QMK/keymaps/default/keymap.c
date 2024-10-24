// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
    *     ┌───┬───┐
    *     │F23│F24│
    *     ├───┼───┤
    *     │F21│F22|
    *     ├───┼───┤
    *     │F19│F20│
    * ┌───┼───┼───┤
    * │ly1│F17│F18│
    * ├───┼───┼───┤
    * │ly2│F15│F16│
    * └───┴───┴───┘
    */
    [0] = LAYOUT_numpad_3x5(
        KC_NO, KC_F23, KC_F24, 
        KC_NO, KC_F21, KC_F22,
        KC_NO, KC_F19, KC_F20,
        MO(1), KC_F17, KC_F18,
        MO(2), KC_F15, KC_F16
    ),
    /*
    *     ┌───┬───┐
    *     │   │   │
    *     ├───┼───┤
    *     │   │   │
    *     ├───┼───┤
    *     │   │   │
    * ┌───┼───┼───┤
    * │ly1│   │   │
    * ├───┼───┼───┤
    * │ly2│   │   │
    * └───┴───┴───┘
    */
    [1] = LAYOUT_numpad_3x5(
        KC_NO, KC_NO, KC_NO,
        KC_NO, KC_NO, KC_NO,
        KC_NO, KC_NO, KC_NO,
        MO(1), KC_NO, KC_NO,
        MO(2), KC_NO, KC_NO
    ),
    /*
    *     ┌───┬───┐
    *     │   │   │
    *     ├───┼───┤
    *     │   │   │
    *     ├───┼───┤
    *     │   │   │
    * ┌───┼───┼───┤
    * │ly1│   │   │
    * ├───┼───┼───┤
    * │ly2│   │   │
    * └───┴───┴───┘
    */
    [2] = LAYOUT_numpad_3x5(
        KC_NO, KC_NO, KC_NO,
        KC_NO, RGB_TOG, RGB_MOD,   // Toggle RGB and cycle through modes
        KC_NO, RGB_HUI, RGB_HUD,   // Increase/decrease hue
        MO(1), RGB_SAI, RGB_SAD,   // Increase/decrease saturation
        MO(2), RGB_VAI, RGB_VAD    // Increase/decrease brightness
    )
}; // TODO: add more layers for more functionality
    // RGB control, media keys, etc.

#if defined(ENCODER_MAP_ENABLE)
const uint16_t PROGMEM encoder_map[] = {
    [0] = { ENCODER_CCW_CW(KC_VOLU, KC_VOLD), 0, 0},  // First encoder
    [1] = { ENCODER_CCW_CW(UG_PREV, UG_NEXT), 0, 0}   // Second encoder
};

#endif

#ifdef OLED_ENABLE
bool oled_task_user(void) {
    // Host Keyboard Layer Status
    oled_write_P(PSTR("Layer: "), false);

    switch (get_highest_layer(layer_state)) {
        case 0:
            oled_write_P(PSTR("Default\n"), false);
            break;
        case 1:
            oled_write_P(PSTR("FN\n"), false);
            break;
        case 2:
            oled_write_P(PSTR("ADJ\n"), false);
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