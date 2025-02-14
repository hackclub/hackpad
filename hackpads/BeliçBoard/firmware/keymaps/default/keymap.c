#include QMK_KEYBOARD_H

enum custom_keycodes {
    EMAIL = SAFE_RANGE
};

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT(
        KC_AUDIO_MUTE, MO(1), LSG(KC_A),
        DF(2), _______, _______
    ),
    [1] = LAYOUT(
        KC_COPY, KC_NO, KC_PASTE,
        KC_WWW_SEARCH, _______, EMAIL
    ),
    [2] = LAYOUT(
        _______, KC_Z, DF(0),
        KC_Q, KC_S, KC_D
    )
};

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    switch (keycode) {
        case EMAIL:
            if (record->event.pressed) {
                SEND_STRING("email@example.com");
            }
            break;
    }
    return true;
};


#ifdef OLED_ENABLE
bool oled_task_user(void) {
    oled_write_P(PSTR("Layer: "), false);

    switch (get_highest_layer(layer_state)) {
        case 0:
            oled_write_P(PSTR("Default\n"), false);
            break;
        case 1:
            oled_write_P(PSTR("Copy Paste\n"), false);
            break;
        case 2:
            oled_write_P(PSTR("ZQSD\n"), false);
            break;
        default:
            oled_write_P(PSTR("Unknown"), false);
    }

    return false;
}
#endif

#if defined(ENCODER_MAP_ENABLE)
const uint16_t PROGMEM encoder_map[][NUM_ENCODERS][NUM_DIRECTIONS] = {
    [0] = { ENCODER_CCW_CW(KC_VOLD, KC_VOLU),  ENCODER_CCW_CW(QK_MOUSE_WHEEL_DOWN, QK_MOUSE_WHEEL_UP) },
    [1] = { ENCODER_CCW_CW(QK_MOUSE_WHEEL_DOWN, QK_MOUSE_WHEEL_UP),  ENCODER_CCW_CW(QK_MOUSE_WHEEL_LEFT, QK_MOUSE_WHEEL_RIGHT) },
};
#endif
