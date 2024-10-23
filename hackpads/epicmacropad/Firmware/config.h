#pragma once

// For OLED
#define OLED_BRIGHTNESS 128
#define OLED_DISPLAY_ADDRESS 0x3C



// For Matrix
#define MATRIX_ROWS 4
#define MATRIX_COLS 5
#define COL_EXPANDED { false, false, false, false, true }
#define MATRIX_ONBOARD_ROW_PINS { GP26, GP27, GP28, GP29}
//#define MATRIX_ONBOARD_COL_PINS { 0, 0, 0, 0, 0, 0, B1, B2, B3, D2, D3, C6 }
#define MATRIX_ONBOARD_COL_PINS { GP3, GP4, GP2, GP1 }
#define EXPANDER_COL_REGISTER GPIOA
#define EXPANDER_ROW_REGISTER GPIOB
#define MATRIX_EXPANDER_COL_PINS { GP4 }
#define MATRIX_EXPANDER_ROW_PINS { }



// For encoders
#define ENCODER_MAP_KEY_DELAY 10
#define NUM_ENCODERS 2   // Number of encoders on your keyboard
#define NUM_DIRECTIONS 2 // Usually, this is 2 (CW and CCW)