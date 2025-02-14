#include QMK_KEYBOARD_H
#include "oled_driver.h"

static uint8_t volume = 50;

void oled_task_user(void) {

    oled_clear();
    
    oled_set_cursor(0, 0); 

    oled_write_P(PSTR("Volume: "), false);

    oled_write(get_volume_string(), false);
}

const char *get_volume_string(void) {
    static char volume_str[4]; 
    snprintf(volume_str, sizeof(volume_str), "%d", volume);  
    return volume_str;
}


enum custom_keycodes {
    ENC_ROTATE_LEFT = SAFE_RANGE,
    ENC_ROTATE_RIGHT
};


bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    switch (keycode) {
        case ENC_ROTATE_LEFT:
            if (record->event.pressed) {
                
                if (volume > 0) {
                    volume--;  
                }
                oled_task_user(); 
                register_code(KC_VOLD); 
                unregister_code(KC_VOLD);
            }
            break;
        case ENC_ROTATE_RIGHT:
            if (record->event.pressed) {
               
                if (volume < 100) {
                    volume++;  
                }
                oled_task_user();  
                register_code(KC_VOLU);  
                unregister_code(KC_VOLU);
            }
            break;
    }
    return true;
}

const uint16_t keymaps[][MATRIX_ROWS][MATRIX_COLS] = {{
    {KC_1, KC_2, KC_3},
    {KC_4, KC_5, KC_6},
    {KC_7, KC_8, KC_9},
}};
