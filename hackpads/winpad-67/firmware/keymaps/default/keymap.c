// Copyright 2024 Siddhant K (grimsteel)
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H
#include "raw_hid.h"

// 12 for "Brightness: ", 3 chars for brightness, 1 '%', null term
#define MONITOR_BRIGHTNESS_MAX 17
// 8 for "Source: ", 8 for input name, 1 null term
#define MONITOR_SOURCE_MAX 17
#define MONITOR_NAME_MAX 17
#ifndef RAW_EPSIZE
#    define RAW_EPSIZE 32
#endif

enum layer_names {
    SWAY,
    MONITOR,
    CONTROL
};

enum my_keycodes {
    MODE = SAFE_RANGE,
    BRIGHT_UP,
    BRIGHT_DOWN,
    BRIGHT_DEFAULT,
    CYCLE_MONITORS,
    DP_1,
    DP_2,
    HDMI_1,
    HDMI_2,
    VGA,
    DVI
};

enum hid_rx_types { SWAY_TITLE, MONITOR_STATUS };

struct {
    uint8_t brightness;
    uint8_t input_source;
} monitor_state = {.brightness = 0, .input_source = 0};

#define NUM_INPUT_NAMES 0x13

// taken from the MCCS spec
const char input_names[NUM_INPUT_NAMES][8] = {
    "",
    "VGA 1",
    "VGA 2",
    "DVI 1",
    "DVI 2",
    "Cmps 1",
    "Cmps 2",
    "S-vid 1",
    "S-vid 2",
    "Tuner 1",
    "Tuner 2",
    "Tuner 3",
    "Cmpt 1",
    "Cmpt 2",
    "Cmpt 3",
    "DP 1",
    "DP 2",
    "HDMI 1",
    "HDMI 2",
};

char sway_title[RAW_EPSIZE - 1];
char monitor_source_title[MONITOR_SOURCE_MAX] = "Source: ?";
char monitor_brightness_title[MONITOR_BRIGHTNESS_MAX] = "Brightness: ?%";
char monitor_name_title[MONITOR_NAME_MAX] = "?";
// "Color: xxx*\0"
char hue_str[12];

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┐
     * │Mod│Vol│Up │
     * ├───┼───┼───┤
     * │Tog│Ver│Hor│
     * ├───┼───┼───┤
     * │Sta│Tab│Ful│
     * └───┴───┴───┘
     */
    [SWAY] = LAYOUT(
                    //stacked           tabbed   fullscreen
                    G(KC_S),            G(KC_W), G(KC_F),
        //tabbed            vertical horizontal
                    G(KC_E),            G(KC_V), G(KC_B),
                    // mode             mute     select up
                    MODE, KC_MUTE, LSG(KC_UP)
                    ),
    [MONITOR] = LAYOUT(
                       HDMI_2, DP_2,           DVI,
                       HDMI_1, DP_1,           VGA,
                       MODE,   BRIGHT_DEFAULT, CYCLE_MONITORS
                       ),
    [CONTROL] = LAYOUT(
                       QK_BOOTLOADER, QK_REBOOT, KC_NO,
                       QK_UNDERGLOW_MODE_NEXT, QK_UNDERGLOW_MODE_PREVIOUS, KC_NO,
                       MODE, QK_UNDERGLOW_TOGGLE, KC_NO
                       )
};

const uint16_t PROGMEM encoder_map[][1][2] = {
    [SWAY] = { ENCODER_CCW_CW(KC_VOLU, KC_VOLD) },
    [MONITOR] = { ENCODER_CCW_CW(BRIGHT_UP, BRIGHT_DOWN) },
    [CONTROL] = { ENCODER_CCW_CW(QK_UNDERGLOW_HUE_UP, QK_UNDERGLOW_HUE_DOWN) }
};

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    if (keycode == MODE) {
        // cycle layers
        
        // only on press
        if (!record->event.pressed) return false;
        uint8_t cur = get_highest_layer(layer_state);
        uint8_t new = cur == SWAY ? MONITOR : cur == MONITOR ? CONTROL : SWAY;
        layer_move(new);
        
        return false;
    } else if (keycode >= BRIGHT_UP && keycode <= DVI) {
        // only on press
        if (!record->event.pressed) return false;
        
        // send as HID command
        uint8_t buf[RAW_EPSIZE];
        memset(buf, 0, RAW_EPSIZE);
        buf[0] = keycode - BRIGHT_UP;
        raw_hid_send(buf, RAW_EPSIZE);
        if (keycode == BRIGHT_UP) monitor_state.brightness++;
        else if (keycode == BRIGHT_DOWN) monitor_state.brightness--;
        return false;
    }
    return true;
}

layer_state_t layer_state_set_user(layer_state_t state) {
    oled_clear();
    
    return state;
}

// OLED display data
void raw_hid_receive(uint8_t *data, uint8_t length) {
    switch (data[0]) {
    case SWAY_TITLE:
        for (int i = 1; i < length - 1; i++) {
            sway_title[i - 1] = (char) data[i];
        }
        // force a null terminator at the end
        sway_title[length - 1] = 0;
        break;
    case MONITOR_STATUS:
        // first byte is brightness, second byte is input source, rest is monitor name
        monitor_state.brightness = data[1];
        // make sure it's within range
        if (data[2] >= NUM_INPUT_NAMES) {
            monitor_state.input_source = 0;
        } else {
            monitor_state.input_source = data[2];
        }
        snprintf(
                 monitor_brightness_title,
                 MONITOR_BRIGHTNESS_MAX,
                 "Brightness: %3d%%",
                 monitor_state.brightness
        );
        snprintf(
                 monitor_source_title,
                 MONITOR_SOURCE_MAX,
                 "Source: %-8s",
                 input_names[monitor_state.input_source]
        );
        snprintf(
                 monitor_name_title,
                 MONITOR_NAME_MAX,
                 "%-17s",
                 &data[3]
        );
        break;
    }
}

/*bool oled_task_user(void) {
    oled_clear();
    switch (get_highest_layer(layer_state)) {
    case SWAY:
        oled_write(sway_title, false);
        break;
    case MONITOR:
        oled_write(monitor_status_title, false);
        oled_set_brightness(monitor_state.brightness);
        break;
        }
    //oled_write("hello there", false);
    oled_set_brightness(monitor_state.brightness);
    return false;
}*/


static const char PROGMEM SWAY_LOGO[] = {
    0x80, 0x81, 0x82, 0x83, 0x00,
    0xA0, 0xA1, 0xA2, 0xA3, 0x00,
    0xC0, 0xC1, 0xC2, 0xC3, 0x00
};

static const char PROGMEM DDC_LOGO[] = {
    0x84, 0x85, 0x86, 0x87, 0x00,
    0xA4, 0xA5, 0xA6, 0xA7, 0x00,
    0xC4, 0xC5, 0xC6, 0xC7, 0x00
};
static const char PROGMEM GEAR_LOGO[] = {
    0x88, 0x89, 0x8A, 0x8B, 0x00,
    0xA8, 0xA9, 0xAA, 0xAB, 0x00,
    0xC8, 0xC9, 0xCA, 0xCB, 0x00
};

bool oled_task_user(void) {
    switch (get_highest_layer(layer_state)) {
    case SWAY:
        // all three rows
        oled_write_P(SWAY_LOGO, false);
        oled_set_cursor(0, 1);
        oled_write_P(SWAY_LOGO + 5, false);
        oled_set_cursor(0, 2);
        oled_write_P(SWAY_LOGO + 10, false);

        oled_set_cursor(5, 1);
        oled_write_P("Sway WM", false);
        break;
    case MONITOR:
        // all three rows
        oled_write_P(DDC_LOGO, false);
        oled_set_cursor(0, 1);
        oled_write_P(DDC_LOGO + 5, false);
        oled_set_cursor(0, 2);
        oled_write_P(DDC_LOGO + 10, false);

        oled_set_cursor(5, 0);
        oled_write_P("Monitor:", false);

        oled_set_cursor(5, 1);
        oled_write(monitor_name_title, false);
        oled_set_cursor(5, 2);
        oled_write(monitor_brightness_title, false);
        oled_set_cursor(5, 3);
        oled_write(monitor_source_title, false);
        break;
    case CONTROL:
        oled_write_P(GEAR_LOGO, false);
        oled_set_cursor(0, 1);
        oled_write_P(GEAR_LOGO + 5, false);
        oled_set_cursor(0, 2);
        oled_write_P(GEAR_LOGO + 10, false);

        oled_set_cursor(5, 0);
        oled_write_P("Settings:", false);
        
        // RGB light color
        oled_set_cursor(5, 2);
        snprintf(
                 hue_str,
                 12,
                 "Color: %3d\x7F",
                 rgblight_get_hue()
        );
        oled_write(hue_str, false);
        break;
    }
    return false;
}
