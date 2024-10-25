#pragma once

/* USB Device descriptor parameter */
#define VENDOR_ID    0xFEED
#define PRODUCT_ID   0x6060
#define DEVICE_VER   0x0001
#define MANUFACTURER "Silas Lovett"
#define PRODUCT      "LerPad"

/* key matrix size */
#define MATRIX_ROWS 3
#define MATRIX_COLS 3

/* key matrix pins */
#define DIODE_DIRECTION COL2ROW

/* Debounce reduces chatter (unintended double-presses) */
#define DEBOUNCE 5

#define ENCODER_A_PINS { GP27 }
#define ENCODER_B_PINS { GP26 }

#define ENCODER_RESOLUTION 1
#define NUM_ENCODERS 1
#define NUM_DIRECTIONS 2


/* OLED settings */
#define OLED_DRIVER_ENABLE
#define OLED_WIDTH 128
#define OLED_HEIGHT 32
#define OLED_I2C_ADDRESS 0x3C
#define OLED_ROTATION 0
