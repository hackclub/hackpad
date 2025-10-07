// Copyright 2024 Siddhant K (grimsteel)
// SPDX-License-Identifier: GPL-2.0-or-later

#define ENCODER_A_PINS { GP2 }
#define ENCODER_B_PINS { GP4 }

#define WS2812_DI_PIN GP1
#define RGBLIGHT_LED_COUNT 3
#define RGBLIGHT_EFFECT_RAINBOW_MOOD
//#define RGBLIGHT_MODE_RAINBOW_MOOD 0
//#define RGBLIGHT_DEFAULT_MODE RGBLIGHT_MODE_RAINBOW_MOOD
#define RGBLIGHT_LIMIT_VAL 64

#define I2C_DRIVER I2CD1
#define I2C1_SDA_PIN GP6
#define I2C1_SCL_PIN GP7

#define OLED_FONT_H "font.c"
