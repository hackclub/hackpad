#pragma once

#include "config_common.h"

/* USB Device descriptor parameter */
#define VENDOR_ID       0x03A8
#define PRODUCT_ID      0xA701
#define DEVICE_VER      0x0001
#define MANUFACTURER    YourName
#define PRODUCT         4x4 Macropad RP2040
#define DESCRIPTION     A simple 4x4 macropad using RP2040

/* Key matrix size */
#define MATRIX_ROWS 4
#define MATRIX_COLS 4

/* Pin definitions */
#define MATRIX_ROW_PINS { D3, D4, D5, D6 }  // Define your row pins (GPIO0 to GPIO3 for example)
#define MATRIX_COL_PINS { D0, D1, D2, D10 }  // Define your column pins (GPIO4 to GPIO7 for example)

#define UNUSED_PINS

/* Diode direction */
#define DIODE_DIRECTION COL2ROW

/* Debounce configuration */
#define DEBOUNCE 5

/* RGB LEDS */
#define WS2812_DI_PIN 10
#define RGBLIGHT_LED_COUNT 10

/* Encoder */
#define ENCODER_A_PINS { D8 }
#define ENCODER_B_PINS { D7 }
#define ENCODER_RESOLUTION 4

/* Mechanical locking support. Use KC_LCAP, KC_LNUM, or KC_LSCR instead in keymap */
#define LOCKING_SUPPORT_ENABLE
#define LOCKING_RESYNC_ENABLE

/* Encoder support (if needed, set in rules.mk) */
// #define ENCODERS_PAD_A { GP14 }
// #define ENCODERS_PAD_B { GP15 }
// #define ENCODER_RESOLUTION 4

/* Bootmagic Lite keycode (optional, allows resetting keymap) */
#define BOOTMAGIC_LITE_ROW 0
#define BOOTMAGIC_LITE_COLUMN 0
