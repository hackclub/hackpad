#include QMK_KEYBOARD_H

#define gui_one 0xF0
#define gui_two 0xF1
#define gui_three 0xF2
#define gui_four 0xF3
#define gui_five 0xF4

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT(
        gui_one, gui_two, gui_three, gui_four, gui_five
    )
};

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    switch (keycode) {
        case gui_one:
            if (record->event.pressed) {
                register_code(KC_LGUI); 
                tap_code(KC_1);        
                unregister_code(KC_LGUI); 
            }
            return false; 
        case gui_two:
            if (record->event.pressed) {
                register_code(KC_LGUI); 
                tap_code(KC_2);        
                unregister_code(KC_LGUI); 
            }
            return false; 
        case gui_three:
            if (record->event.pressed) {
                register_code(KC_LGUI); 
                tap_code(KC_3);        
                unregister_code(KC_LGUI); 
            }
            return false; 
        case gui_four:
            if (record->event.pressed) {
                register_code(KC_LGUI); 
                tap_code(KC_4);        
                unregister_code(KC_LGUI); 
            }
            return false; 
        case gui_five:
            if (record->event.pressed) {
                register_code(KC_LGUI); 
                tap_code(KC_5);        
                unregister_code(KC_LGUI); 
            }
            return false; 
    }
    return true; 
}