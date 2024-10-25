#pragma once

#include "quantum.h"

#define MATRIX_ROWS 3
#define MATRIX_COLS 7

#define MATRIX_ROW_PINS { D0, D1, D2 }  // Replace with actual row pins
#define MATRIX_COL_PINS { C0, C1, C2, C3, C4, C5, C6 }  // Replace with actual column pins

#define DIODE_DIRECTION COL2ROW

#define DEBOUNCE 5
#define USB_MAX_POWER_CONSUMPTION 100
#define USB_POLLING_INTERVAL 10

// Uncomment the features you want to enable
// #define MOUSEKEY_ENABLE
// #define EXTRAKEY_ENABLE
// #define RGBLIGHT_ENABLE
