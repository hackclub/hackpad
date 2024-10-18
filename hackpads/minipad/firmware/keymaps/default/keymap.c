#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───────┬───────┐
     * │M_CTRL │PG_UP  │
     * ├───────┼───────┤
     * │ MUTE  │PG_DWN │
     * └───────┴───────┘
     */
    [0] = LAYOUT(
        KC_MISSION_CONTROL, KC_PAGE_UP,
        KC_KB_MUTE, KC_PAGE_DOWN
    )
};

#ifdef ENCODER_ENABLE
bool encoder_update_user(uint8_t index, bool clockwise) {
    if (index == 0) { // First encoder
        if (clockwise) {
            tap_code(KC_VOLU); // Volume up
        } else {
            tap_code(KC_VOLD); // Volume down
        }
    }
    return true; // Return true to indicate the event was handled
}
#endif