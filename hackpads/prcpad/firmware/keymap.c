#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT_ortho_3x3(
        KC_A, KC_B, KC_C,
        KC_D, KC_E, KC_F,
        KC_G, KC_H, KC_NO
    )
};
#ifdef OLED_ENABLE

bool oled_task_user() {
    oled_clear();
    oled_write_P(PSTR("Testing OLED!"), false); // Replace THIS line with whatever you'd like the OLED to display.
    // There are more details in the OLED page!
    return false;
}

#endif



bool encoder_update_user(uint8_t index, bool clockwise) {
    if (index == 0) { /* Encoder code */
        if (clockwise) {
            tap_code(KC_PGDN);
        } else {
            tap_code(KC_PGUP); // The QMK keycode value of choice. List at https://docs.qmk.fm/keycodes
        } // More info at the Rotary Encoder page
    }
    return false;
}
