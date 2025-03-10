// config.h
#pragma once

#define MATRIX_ROWS 8  // 4 per side
#define MATRIX_COLS 8  // 4 per side
#define DIODE_DIRECTION COL2ROW

#define SPLIT_KEYBOARD
#define USE_I2C
#define OLED_ENABLE
#define SPLIT_TRANSPORT_MIRROR

#define SOFT_SERIAL_PIN GP0  // TRRS Serial communication

#define OLED_DISPLAY_128X64
#define OLED_TIMEOUT 30000  // 30 sec timeout

// rules.mk
OLED_ENABLE = yes
SPLIT_KEYBOARD = yes
LTO_ENABLE = yes
EXTRAKEY_ENABLE = yes

// keymap.c
#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT(
        KC_Q,    KC_W,    KC_E,    KC_R,   KC_T,    KC_Y,    KC_U,    KC_I,
        KC_A,    KC_S,    KC_D,    KC_F,   KC_G,    KC_H,    KC_J,    KC_K,
        KC_Z,    KC_X,    KC_C,    KC_V,   KC_B,    KC_N,    KC_M,    KC_ENT,
        KC_LCTL, KC_LALT, KC_LGUI, KC_SPC, KC_SPC,  KC_RGUI, KC_RALT, KC_RCTL
    )
};

#ifdef OLED_ENABLE
bool oled_task_user(void) {
    oled_write_ln("HI", false);
    return false;
}
#endif
