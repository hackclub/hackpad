#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

    [0] = LAYOUT(
        KC_PSCR,   KC_SCRL,   KC_MEDIA_EJECT,
        KC_INS,   KC_HOME,   KC_PGUP,
        KC_DELETE,   KC_END,   KC_PGDN
      
    )
};
