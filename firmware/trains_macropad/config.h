#pragma once

#include "config_common.h"

// Define matrix size
#define MATRIX_ROWS 2
#define MATRIX_COLS 4

// Define the pins for I2C (for PFC8574A and OLED)
#define I2C_SCL_PIN D0
#define I2C_SDA_PIN D1

// Define rotary encoder pins
#define ENCODERS_PAD_A { D2, D4 }
#define ENCODERS_PAD_B { D3, D5 }
#define ENCODER_RESOLUTION 4

// RGB LED settings
#define RGB_DI_PIN D6
#define RGBLED_NUM 8

// OLED settings
#define OLED_DISPLAY_128X32
