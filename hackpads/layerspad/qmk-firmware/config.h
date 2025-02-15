#pragma once

// OLED Configuration
#define OLED_DISPLAY_128X64
#define OLED_TIMEOUT 60000  // 1 minute timeout
#define OLED_BRIGHTNESS 128 // Medium brightness

// Matrix Configuration
#define MATRIX_ROWS 3
#define MATRIX_COLS 3
#define MATRIX_ROW_PINS { GP26, GP27, GP28 }  // Row pins
#define MATRIX_COL_PINS { GP29, GP6, GP7 }    // Column pins
#define DIODE_DIRECTION COL2ROW
#define DEBOUNCE 5

// Tap Dance Configuration
#define TAPPING_TERM 300
#define TAPPING_TERM_PER_KEY

// RGB Matrix Configuration
#ifdef RGB_MATRIX_ENABLE
    #define RGB_MATRIX_LED_COUNT 12            // Number of LEDs
    #define RGB_MATRIX_MAXIMUM_BRIGHTNESS 150  // Maximum brightness level (0-255)
    #define RGB_MATRIX_STARTUP_VAL RGB_MATRIX_MAXIMUM_BRIGHTNESS
    #define RGB_MATRIX_STARTUP_MODE RGB_MATRIX_SOLID_COLOR
    #define RGB_MATRIX_TIMEOUT 0
    #define RGB_DISABLE_WHEN_USB_SUSPENDED
    
    // The pin connected to the data pin of the LEDs
    #define RGB_DI_PIN GP0                    // LED data pin
    
    // Enable additional RGB matrix effects
    #define RGB_MATRIX_FRAMEBUFFER_EFFECTS
    #define RGB_MATRIX_KEYPRESSES
    
    // Enable animations
    #define ENABLE_RGB_MATRIX_SOLID_COLOR
    #define ENABLE_RGB_MATRIX_ALPHAS_MODS
    #define ENABLE_RGB_MATRIX_GRADIENT_UP_DOWN
    #define ENABLE_RGB_MATRIX_BREATHING
    #define ENABLE_RGB_MATRIX_BAND_SAT
    #define ENABLE_RGB_MATRIX_BAND_PINWHEEL_SAT
    #define ENABLE_RGB_MATRIX_CYCLE_ALL
    #define ENABLE_RGB_MATRIX_CYCLE_LEFT_RIGHT
    #define ENABLE_RGB_MATRIX_CYCLE_UP_DOWN
    #define ENABLE_RGB_MATRIX_RAINBOW_MOVING_CHEVRON
    #define ENABLE_RGB_MATRIX_CYCLE_PINWHEEL
#endif

// Encoder Configuration
#define ENCODERS_PAD_A { GP26 }    // Encoder A pin
#define ENCODERS_PAD_B { GP27 }    // Encoder B pin
#define ENCODER_RESOLUTION 4        // Default resolution
#define ENCODER_DEFAULT_POS 0x3     // Default position

// General keyboard configuration
#define FORCE_NKRO                  // Enable NKRO
#define USB_POLLING_INTERVAL_MS 1   // 1000Hz polling rate