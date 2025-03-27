// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#ifndef CONFIG_H
#define CONFIG_H

// Matrix size
#define MATRIX_ROWS 3
#define MATRIX_COLS 4

// Matrix pin configuration
#define MATRIX_ROW_PINS { GP4, GP0, GP26 }
#define MATRIX_COL_PINS { GP27, GP28, GP29, GP3 }

// OLED display configuration
#define OLED_DRIVER_ENABLE
#define OLED_I2C_ADDRESS 0x3C
#define OLED_BRIGHTNESS 128

// Rotary encoder configuration
#define ENCODER_RESOLUTION 4

#endif // CONFIG_H