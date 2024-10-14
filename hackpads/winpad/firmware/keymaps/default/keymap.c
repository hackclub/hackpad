// Copyright 2024 Siddhant K (grimsteel)
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H
#include "raw_hid.h"

// 3 chars for brightness, 12 for "% - Source: ", 6 for input name, 1 null term
#define MONITOR_STATE_MAX 22
#ifndef RAW_EPSIZE
#    define RAW_EPSIZE 32
#endif

enum layer_names {
    SWAY,
    MONITOR
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

#define NUM_INPUT_NAMES 6

const char input_names[NUM_INPUT_NAMES][7] = {
    "DP-1",
    "DP-2",
    "HDMI-1",
    "HDMI-2",
    "VGA",
    "DVI"
};

char sway_title[RAW_EPSIZE - 1];
char monitor_status_title[MONITOR_STATE_MAX];

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
        // mode             mute     select up
        MT(MOD_LSFT, MODE), KC_MUTE, LSG(KC_A),
        //tabbed            vertical horizontal
        G(KC_E),            G(KC_V), G(KC_B),
        //stacked           tabbed   fullscreen
        G(KC_S),            G(KC_W), G(KC_F)
    ),
    [MONITOR] = LAYOUT(
        MODE,   BRIGHT_DEFAULT, CYCLE_MONITORS,
        HDMI_1, DP_1,           VGA,
        HDMI_2, DP_2,           DVI
    )
};

const uint16_t PROGMEM encoder_map[][1][2] = {
    [SWAY] = { ENCODER_CCW_CW(KC_VOLD, KC_VOLU) },
    [MONITOR] = { ENCODER_CCW_CW(BRIGHT_DOWN, BRIGHT_UP) }
};

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    if (keycode == MODE) {
        // cycle layers
        
        // only on press
        if (!record->event.pressed) return false;
        uint8_t cur = get_highest_layer(layer_state);
        uint8_t new = cur == SWAY ? MONITOR : SWAY;
        layer_move(new);
        return false;
    } else if (keycode >= BRIGHT_UP && keycode <= DVI) {
        // send as HID command
        uint8_t buf[RAW_EPSIZE];
        buf[0] = keycode - BRIGHT_UP;
        raw_hid_send(buf, RAW_EPSIZE);
        return false;
    }
    return true;
}

layer_state_t layer_state_set_user(layer_state_t state) {
    switch (get_highest_layer(state)) {
    case MONITOR:
        // I'll make these fancier once I actually get the hackpad
        rgblight_setrgb(255, 0, 0);
        break;
    case SWAY:
        rgblight_setrgb(0, 255, 0);
        break;
    }
    return state;
}

// OLED display data
void raw_hid_receive(uint8_t *data, uint8_t length) {
    switch (data[0]) {
    case SWAY_TITLE:
        for (int i = 1; i < RAW_EPSIZE - 1; i++) {
            sway_title[i - 1] = (char) data[i];
        }
        // force a null terminator at the end
        sway_title[RAW_EPSIZE - 1] = 0;
        break;
    case MONITOR_STATUS:
        // first byte is brightness, second byte is input source
        monitor_state.brightness = data[1];
        // make sure it's within range
        if (data[2] >= NUM_INPUT_NAMES) {
            monitor_state.input_source = 0;
        } else {
            monitor_state.input_source = data[2];
        }
        snprintf(
                 monitor_status_title,
                 MONITOR_STATE_MAX,
                 "%d%% - Source: %s",
                 monitor_state.brightness,
                 input_names[monitor_state.input_source]
        );
        break;
    }
}

bool oled_task_user(void) {
    switch (get_highest_layer(layer_state)) {
    case SWAY:
        oled_write(sway_title, false);
        break;
    case MONITOR:
        oled_write(monitor_status_title, false);
        break;
    }
    return false;
}
