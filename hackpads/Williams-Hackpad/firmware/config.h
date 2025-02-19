#pragma once
#define RGBLIGHT_LED_COUNT 2
#define WS2812_LED_COUNT 2
#define WS2812_DI_PIN 6



#define WS2812_DI_PIN GP6
#define RGBLED_NUM 2
#define WS2812_LED_COUNT RGBLIGHT_LED_COUNT

// Bootloader for bootmagic to occur
#define BOOTLOADER_DOUBLE_TAP_RESET
#define RP2040_BOOTLOADER_DOUBLE_TAP

// My layout dimensions
#define MATRIX_ROWS 2
#define MATRIX_COLS 3
#define MCU RP2040

// Pins for the rotary encoders and LEDs
#define ENCODER_DIRECTION_FLIP
#define ENCODER_RESOLUTION 4
#define ENCODER_A_PINS { GP28, GP27 }
#define ENCODER_B_PINS { GP29, GP26 }
#define LED2_PIN GP6

// Matrix settings (key debounce time, etc)
#define DEBOUNCE 5

// RGB config
#define RGBLED_NUM 2   // Number of LEDs
#define RGBLIGHT_LIMIT_VAL 120
#define RGBLIGHT_LIMIT_VAL 120  // Maximum brightness

#define MANUFACTURER "William"
#define DIRECT_PIN_INPUTS  // Disables matrix and uses direct pins

//sry towards the end I gave up on annotations

