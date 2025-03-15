// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include "action.h"
#include "deferred_exec.h"
#include "oled_driver.h"
#include "quantum.h"
#include "wpm.h"
#include "color.h"

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┬───┐
     * │ z │ x │ c │ v │
     * └───┴───┴───┴───┘
     */
    [0] = LAYOUT(
        KC_Z,   KC_X,   KC_C,   KC_V
    )
};

bool pressed[4];
uint16_t key_time[4] = {0, 0, 0, 0};
uint8_t key_hue[4] = {0, 0, 0, 0};

#ifdef RGBLIGHT_ENABLE
deferred_token rgb_timer_token;
static const uint16_t rgb_fadeout_time = 1000; // How fast does RGb fade out
static const uint8_t max_total_kps = 16; // When does RGB effect max out
static const uint16_t update_time = 100; // How often do RGB values update 
static const uint8_t hue_step = 4; // How much to shift hue by on keypress

void update_rgb(void) {
    float saturation_factor = (float) get_current_wpm() / max_total_kps;
    if (saturation_factor > max_total_kps) saturation_factor = 1.0f;
    uint8_t saturation = saturation_factor * 255;
    
    for (int i = 0; i < 4; i++) {
        uint16_t time_elapsed = timer_elapsed(key_time[i]);
        uint8_t brightness = (time_elapsed <= rgb_fadeout_time) ? (time_elapsed / rgb_fadeout_time * 255) : 255;

        rgb_t rgb = hsv_to_rgb((hsv_t) {key_hue[i], saturation, brightness});
        rgblight_driver.set_color(0, rgb.r, rgb.g, rgb.b);
    }
}

uint32_t update_rgb_callback(uint32_t _trigger_time, void *cb_arg) {
    update_rgb();
    return 100; // 100ms repeat
}

void keyboard_post_init_user() {
    deferred_token rgb_timer = defer_exec(0, update_rgb_callback, NULL);
    rgb_timer_token = rgb_timer;
}
#endif

bool process_record_user(uint16_t _keycode, keyrecord_t *record) {
    uint8_t col = record->event.key.col;
    
    #ifdef RGBLIGHT_ENABLE
    if (record->event.pressed) {
        key_time[col] = timer_read();
        key_hue[col] = (key_hue[col] + hue_step) % 256;
        update_rgb();
        extend_deferred_exec(rgb_timer_token, update_time); // Delay redundant update
    }
    #endif
    
    pressed[col] = record->event.pressed;
    
    return true;
}

#ifdef OLED_ENABLE
static const char raw_key_up[] = {
    3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3
};

static const char raw_key_down[] = {
    192,192,192,192,192,192,192,192,192,192,192,192,192,192,192,192,192,192,192,192,192,192,192,192
};

bool oled_task_user(void) {
    oled_write_ln_P(PSTR("MayoDevice"), false);

    uint8_t kps = get_current_wpm();
    oled_write_P(PSTR("KPS | "), false);
    oled_write_ln_P(get_u8_str(kps, ' '), false);

    // Visualize keypresses
    oled_set_cursor(4, 28);
    for (int i = 0; i < 4; i++) {
        if (pressed[i]) {
            oled_write_raw_P(raw_key_down, 24);
        } else {
            oled_write_raw(raw_key_up, 24);
        } 

        oled_advance_char();
        oled_advance_char();
        oled_advance_char(); // bruh
    }

    return false;
}
#endif