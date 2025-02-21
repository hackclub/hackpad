// SPDX-License-Identifier: GPL-2.0-or-later

#define DIP_SWITCH_MATRIX_GRID { {1,3}, {0,3}, {3,3},{2,3}} //Encoders 1 and 2, Inps A&B

#define WS2812_DI_PIN GP0
//#define RGBLIGHT_LED_COUNT 14

//#define RP_I2C_USE_I2C1


#define LAYOUT_pad_4x4_2Enc( \
    sw1,        sw2, \
    sw3,        sw4, \
    sw5,sw6,sw7,sw8, \
    sw9,sw10,sw11,sw12 \
){ \
    {sw1,sw5,sw9,KC_NO}, \
    {sw2,sw6,sw10,KC_NO}, \
    {sw3,sw7,sw11,KC_NO}, \
    {sw4,sw8,sw12,KC_NO} \
}
