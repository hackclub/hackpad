#pragma once

#include "config_common.h"

#define OLED_DISPLAY_128X64
#define OLED_IC OLED_IC_SSD1306
#define OLED_TIMEOUT 60000
#define OLED_BRIGHTNESS 255
#define OLED_UPDATE_INTERVAL 100

#define I2C1_SDA_PIN GP6
#define I2C1_SCL_PIN GP7
#define I2C1_CLOCK_SPEED 400000

#define ENCODERS_PAD_A { GP26, GP28 }
#define ENCODERS_PAD_B { GP27, GP29 }
#define ENCODER_RESOLUTION 4

#define DIODE_DIRECTION COL2ROW
