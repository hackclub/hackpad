#pragma once


// Basic keyboard information
#define VENDOR_ID       0xFEED       // Customize with your own vendor ID
#define PRODUCT_ID      0x1234       // Customize with your own product ID
#define DEVICE_VER      0x0001       // Hardware version number
#define MANUFACTURER    VijetaGarg    // Your name or brand
#define PRODUCT         MusicBox     // The name of your keyboard


#define AUDIO_ENABLE // For audio features, if applicable
#define MEDIA_KEY_ENABLE // Enable media keys if they are part of your implementation

// Matrix size (rows and columns)
#define MATRIX_ROWS 2                // Update according to your matrix
#define MATRIX_COLS 3               // Update according to your matrix

// Matrix pin configuration
#define MATRIX_ROW_PINS { D3, D0, D2} // Set pins for your rows
#define MATRIX_COL_PINS { D1, D10 } // Set pins for your columns

#define I2C1_SDA_PIN D4
#define I2C1_SCL_PIN D5

#define UNUSED_PINS                    // If any pins are unused, you can leave this empty

// Diode direction
#define DIODE_DIRECTION COL2ROW        // Set diode direction to COL2ROW or ROW2COL

// Debounce time for switches
#define DEBOUNCING_DELAY 5             // Set debounce time (5ms is a good default)

// Set up features you want to enable (if needed)
#define BOOTMAGIC_ENABLE               // Enable Bootmagic
#define EXTRAKEY_ENABLE                // Enable Extra keys (like media keys)

// For OLED display support
#define OLED_DRIVER_ENABLE
