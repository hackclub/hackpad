#define tim12

#ifndef CONFIG_H
#define CONFIG_H

// Matrix size
#define MATRIX_ROWS 5
#define MATRIX_COLS 3

// Matrix pin configuration
#define MATRIX_ROW_PINS { GP0, GP1, GP2, GP3, GP6 }
#define MATRIX_COL_PINS { GP8, GP9, GP10 }

// Include QMK RGB lighting configurations
#define WS2812_DI_PIN GP7
#define RGBLED_NUM 12
#define RGBLIGHT_LED_COUNT RGBLED_NUM
#define RGBLIGHT_SLEEP
#define RGBLIGHT_LIMIT_VAL 120
#define RGBLIGHT_HUE_STEP 10
#define RGBLIGHT_SAT_STEP 17
#define RGBLIGHT_VAL_STEP 17

// OLED display configuration
#define OLED_DRIVER_ENABLE
#define OLED_I2C_ADDRESS 0x3C
#define OLED_BRIGHTNESS 128

#endif // CONFIG_H