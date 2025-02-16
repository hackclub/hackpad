#include QMK_KEYBOARD_H

#define LAYOUT( \
    K00, K01, K02, \
    K10, K11, K12 \
) { \
    { K00, K01, K02 }, \
    { K10, K11, K12 } \
}

enum layer_names { 
    _BASE, 
    _INIT, 
};

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = { 
    [_BASE] = LAYOUT( 
        KC_BSPC, MO(_INIT), KC_PSTE, 
        KC_SPC, KC_COPY, KC_ENT 
    ), 
    [_INIT] = LAYOUT( 
        QK_BOOT, QK_REBOOT, KC_F22, 
        KC_BTN1, KC_BTN2, KC_ENT 
    ) 
};

#ifdef OLED_ENABLE
bool oled_task_user(void) { 
    // Host Keyboard Layer Status 
    oled_write_P(PSTR("Layer: "), false); 
    switch (get_highest_layer(layer_state)) { 
        case _BASE: 
            oled_write_P(PSTR("Default\n"), false); 
            break; 
        default: 
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
