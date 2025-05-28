#include QMK_KEYBOARD_H
#include "oled_driver.h"
#include <stdio.h>
#include "uart.h"

char media_line[128] = "Waiting for media...";

// Called once after keyboard startup
void keyboard_post_init_user(void) {
    uart_init();  // Initializes UART
}

// Polls serial input and stores incoming string
void matrix_scan_user(void) {
    static char c;
    static int idx = 0;

    while (uart_available()) {
        c = uart_read();
        if (c == '\n' || idx >= sizeof(media_line) - 1) {
            media_line[idx] = '\0';
            idx = 0;
        } else {
            media_line[idx++] = c;
        }
    }
}

// Displays received media title/artist
bool oled_task_user(void) {
    oled_clear();
    oled_write_ln(media_line, false);
    return false;
}

// Encoder handling
bool encoder_update_user(uint8_t index, bool clockwise) {
    switch (index) {
        case 0:
            tap_code(clockwise ? KC_VOLU : KC_VOLD);
            break;
        case 1:
            tap_code(clockwise ? KC_RIGHT : KC_LEFT);
            break;
    }
    return true;
}

// Keymap layout
const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT(
        KC_NO,
        KC_MPRV,
        KC_MNXT,
        KC_MPLY
    )
};
