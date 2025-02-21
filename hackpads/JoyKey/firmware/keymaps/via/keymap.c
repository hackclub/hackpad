// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

enum layer_names {
    _BASE,
    KICAD,
    ONSHAPE,
};

//custin codes
S_PARROT = KC.MACRO(":ultrafastparrot:");

driver = SSD1306(
    # Mandatory:
    i2c=i2c_bus,
    # Optional:
    device_address=0x3C,
)
display = Display(
    # Mandatory:
    display=driver,
    # Optional:
    width=128, # screen size
    height=32, # screen size
    flip = False, # flips your display content
    flip_left = False, # flips your display content on left side split
    flip_right = False, # flips your display content on right side split
    brightness=0.6, # initial screen brightness level
    brightness_step=0.1, # used for brightness increase/decrease keycodes
    dim_time=30, # time in seconds to reduce screen brightness
    dim_target=0.1, # set level for brightness decrease
    off_time=60, # time in seconds to turn off screen
    powersave_dim_time=10, # time in seconds to reduce screen brightness
    powersave_dim_target=0.1, # set level for brightness decrease
    powersave_off_time=30, # time in seconds to turn off screen
)

display.entries = [
    ImageEntry(image="layer-1.bmp", layer=0),
    ImageEntry(image="layer-2.bmp", layer=1),
    ImageEntry(image="layer-3.bmp", layer=2),
    ImageEntry(image="layer-4.bmp", layer=3),
]

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     *     ┬───┐
     *     │ 2 │
     * ├───┼───┼───┤
     * │ 3 │ 5 │ 6 │
     * └───┴───┴───┘
     */

    /*
    The wiring is a little convoluted - refer to the diagram below:
    
    */
    [_BASE] = LAYOUT(
        KC_P7, KC_P8, KC_P4,
        KC_P5, S_PARROT
    )
    [KICAD] = LAYOUT(
        KC_P7, KC_P8, KC_P4,
        KC_P5, KC_P6
    )
    [ONSHAPE] = LAYOUT(
        KC_P7, KC_P8, KC_P4,
        KC_P5, KC_P6
    )
};

const uint16_t PROGMEM encoder_map[][1][2] = {
    [0] = { ENCODER_CCW_CW(MS_WHLU, MS_WHLD) },
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
            // Or use the write_ln shortcut over adding '\n' to the end of your string
            oled_write_ln_P(PSTR("Undefined"), false);
    }

    // Host Keyboard LED Status
    led_t led_state = host_keyboard_led_state();
    oled_write_P(led_state.num_lock ? PSTR("NUM ") : PSTR("    "), false);
    oled_write_P(led_state.caps_lock ? PSTR("CAP ") : PSTR("    "), false);
    oled_write_P(led_state.scroll_lock ? PSTR("SCR ") : PSTR("    "), false);
    
    return false;
}

// Encoder Function
bool encoder_update_user(uint8_t index, bool clockwise) {
    if (IS_LAYER_ON(_BL)) {
        if (clockwise) {
            tap_code(KC_VOLU);  // Volume Up on base layer
        } else {
            tap_code(KC_VOLD);  // Volume Down on base layer
        }
    } else if (IS_LAYER_ON(_SL)) {
        if (clockwise) {
            tap_code(KC_BRIU);  // Brightness Up on second layer
        } else {
            tap_code(KC_BRID);  // Brightness Down on second layer
        }
    }

    return true; // Return true to indicate the encoder event was handled
}

// OLED Function
#ifdef OLED_ENABLE
bool oled_task_user(void) {
    // Display the active layer
    oled_write_ln_P(PSTR("Layer"), false);
    switch (get_highest_layer(layer_state)) {
        case _BL:
            oled_write_ln_P(PSTR("Layer: Ctrl"), false);
            break;
        case _SL:
            oled_write_ln_P(PSTR("Layer: Func"), false);
            break;
        default:
            oled_write_ln_P(PSTR("Undefined"), false);
    }

    // Display encoder functionality
    if (IS_LAYER_ON(_BL)) {
        oled_write_ln_P(PSTR("Vol Ctrl"), false);
    } else if (IS_LAYER_ON(_SL)) {
        oled_write_ln_P(PSTR("Bright Ctrl"), false);
    }

    return false;
}

#endif
