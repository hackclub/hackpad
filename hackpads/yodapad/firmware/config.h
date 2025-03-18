// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#define ENCODER_A_PINS {GP28}
#define ENCODER_B_PINS {GP27}

#define KEY_1 RGB_TOG
#define KEY_2 RGB_MODE_FORWARD
#define KEY_3 KC_MEDIA_PLAY_PAUSE
#define KEY_4 KC_PASTE
#define KEY_5 KC_COPY
#define KEY_6 KC_CUT
#define KEY_7 KC_TAB
#define KEY_8 KC_ENTER
#define KEY_9 KC_BACKSPACE

#define WS2812_DI_PIN GP1
#define RGBLIGHT_LED_COUNT 9
#define ENABLE_RGB_MATRIX_HUE_WAVE

#define MATRIX_ROWS 3
#define MATRIX_COLS 3

#define NUM_ENCODERS 1
#define NUM_DIRECTIONS 2