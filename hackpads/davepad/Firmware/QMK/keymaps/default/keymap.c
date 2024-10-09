// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H
#include "oled_driver.h"
// #include MCP_23017_H
#include "config.h"
#define BASE   0
#define FN     1
#define TMUX   2
#define NUMPAD 3
#define MATH_ENTRY 4
#define APP_0 15
#define APP_1 14
#define APP_2 13 // etc
#define APP_3 12
#define APP_4 11
#define APP_5 10
#define APP_6 9
#define APP_7 8
#define APP_8 7
#define APP_9 6
#define APP_10 5

#define WS2812_DI_PIN D7 // TD: redefine
const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [BASE] = LAYOUT(
        KC_SLEP  ,  KC_F13,   KC_F14,   QK_RBT,    KC_MUTE,
        MT(MATH_ENTRY, KC_F15)    ,  KC_F16,   KC_F17,   KC_F18,    KC_F19,
        MT(TMUX, KC_F20)   ,  KC_F21,   KC_F22,   KC_UP,    KC_F23,
        KC_LEFT_GUI,  MO(FN),   KC_LEFT, KC_DOWN, KC_RIGHT
    ),
    [FN] = LAYOUT(
        KC_WAKE,   KC_EJCT,   QK_REP,   QK_MAGIC_TOGGLE_NKRO,   KC_TRNS,
        PB_1,   PB_2,   PB_3,   PB_4,   PB_5,
        PB_6,   PB_7,   PB_8,   PB_9,   PB_10,
        PB_11,   KC_TRNS,   PB_12,   PB_13,   PB_14
    ),
    [NUMPAD] = LAYOUT( // For using as a laptop numpad
        KC_P7,   KC_P8,   KC_P9,   KC_TRNS,   KC_TRNS,
        KC_P4,   KC_P5,   KC_P6,   KC_PSLS,   KC_PAST,
        KC_P1,   KC_P2,   KC_P3,   KC_PEQL,   KC_PPLS,
        KC_P0,   KC_PDOT,   KC_PCMM,   KC_PMNS, KC_PENT
    ),
    [MATH_ENTRY] = LAYOUT( // Mainly greek alphabet
        UC(0x2126),   UC(0x222B),   UC(0x03BC),   UC(0x0394), UC(0x2234),
        KC_NO,  UC(0x2200),   UC(0x03BB),   UC(0x03C0), UC(0x03C6),
        UC(0x03B5),   UC(0x2211),   UC(0x0251),   UC(0x03B2), UC(0x03B3),
        UC(0x0398),   UC(0x03C4),   UC(0x03C1),   UC(0x2800), UC(0x221A)
    ),
    [TMUX] = LAYOUT(
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS
    ),
    [APP_0] = LAYOUT(
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS
    ),
    [APP_1] = LAYOUT(
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS
    ),
    [APP_2] = LAYOUT(
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS
    ),
    [APP_3] = LAYOUT(
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS
    ),
    [APP_4] = LAYOUT(
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS
    ),
    [APP_5] = LAYOUT(
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS
    ),
    [APP_6] = LAYOUT(
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS
    ),
    [APP_7] = LAYOUT(
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS
    ),
    [APP_8] = LAYOUT(
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS
    ),
    [APP_9] = LAYOUT(
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS
    ),
    [APP_10] = LAYOUT(
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,
        KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS,   KC_TRNS
    )
};

#if defined(ENCODER_MAP_ENABLE)
const uint16_t PROGMEM encoder_map[][NUM_ENCODERS][NUM_DIRECTIONS] = {
    [1] =  { ENCODER_CCW_CW(KC_NO, KC_NO),  ENCODER_CCW_CW(KC_TRNS, KC_TRNS)  },
    [0] =  { ENCODER_CCW_CW(TO(15), TO(2)),  ENCODER_CCW_CW(KC_VOLD, KC_VOLU)  },
    [2] =  { ENCODER_CCW_CW(TO(0), TO(3)),  ENCODER_CCW_CW(KC_TRNS, KC_TRNS) },
    [3] =  { ENCODER_CCW_CW(TO(2), TO(4)),  ENCODER_CCW_CW(KC_TRNS, KC_TRNS) },
    [4] =  { ENCODER_CCW_CW(TO(3), TO(5)),  ENCODER_CCW_CW(KC_TRNS, KC_TRNS) },
    [5] =  { ENCODER_CCW_CW(TO(4), TO(6)),  ENCODER_CCW_CW(KC_TRNS, KC_TRNS) },
    [6] =  { ENCODER_CCW_CW(TO(5), TO(7)),  ENCODER_CCW_CW(KC_TRNS, KC_TRNS) },
    [7] =  { ENCODER_CCW_CW(TO(6), TO(8)),  ENCODER_CCW_CW(KC_TRNS, KC_TRNS) },
    [8] =  { ENCODER_CCW_CW(TO(7), TO(9)),  ENCODER_CCW_CW(KC_TRNS, KC_TRNS) },
    [9] =  { ENCODER_CCW_CW(TO(8), TO(10)),  ENCODER_CCW_CW(KC_TRNS, KC_TRNS) },
    [10] = { ENCODER_CCW_CW(TO(9), TO(11)),  ENCODER_CCW_CW(KC_TRNS, KC_TRNS) },
    [11] = { ENCODER_CCW_CW(TO(10), TO(12)),  ENCODER_CCW_CW(KC_TRNS, KC_TRNS) },
    [12] = { ENCODER_CCW_CW(TO(11), TO(13)),  ENCODER_CCW_CW(KC_TRNS, KC_TRNS) },
    [13] = { ENCODER_CCW_CW(TO(12), TO(14)),  ENCODER_CCW_CW(KC_TRNS, KC_TRNS) },
    [14] = { ENCODER_CCW_CW(TO(13), TO(15)),  ENCODER_CCW_CW(KC_TRNS, KC_TRNS) },
    [15] = { ENCODER_CCW_CW(TO(14), TO(0)),  ENCODER_CCW_CW(KC_TRNS, KC_TRNS) },
};
#endif

#ifdef OLED_ENABLE
bool oled_task_user(void) {
    // Host Keyboard Layer Status
    oled_write_P(PSTR("Layer: "), false);

    switch (get_highest_layer(layer_state)) {
        case BASE:
            oled_write_P(PSTR("Default\n"), false);
            break;
        case FN:
            oled_write_P(PSTR("FN\n"), false);
            break;
        case TMUX:
            oled_write_P(PSTR("TMUX\n"), false);
            break;
        case NUMPAD:
            oled_write_P(PSTR("NUMPAD\n"), false);
            break;
        case MATH_ENTRY:
            oled_write_P(PSTR("MATH_ENTRY\n"), false);
            break;
        default:
            // Or use the write_ln shortcut over adding '\n' to the end of your string
            oled_write_ln_P(PSTR("Undefined"), false);
    }

    // Host Keyboard LED Status
    led_t led_state = host_keyboard_led_state();
    oled_write_P(led_state.num_lock ? PSTR("NUM ") : PSTR("    "), false);
    oled_write_P(led_state.caps_lock ? PSTR("CAP ") : PSTR("    "), false);
    oled_write_P(led_state.scroll_lock ? PSTR("SCR ") : PSTR("    "), false);

    return false;
}
static void render_logo(void) {
    static const char PROGMEM qmk_logo[] = {
        0x80, 0x81, 0x82, 0x83, 0x84, 0x85, 0x86, 0x87, 0x88, 0x89, 0x8A, 0x8B, 0x8C, 0x8D, 0x8E, 0x8F, 0x90, 0x91, 0x92, 0x93, 0x94,
        0xA0, 0xA1, 0xA2, 0xA3, 0xA4, 0xA5, 0xA6, 0xA7, 0xA8, 0xA9, 0xAA, 0xAB, 0xAC, 0xAD, 0xAE, 0xAF, 0xB0, 0xB1, 0xB2, 0xB3, 0xB4,
        0xC0, 0xC1, 0xC2, 0xC3, 0xC4, 0xC5, 0xC6, 0xC7, 0xC8, 0xC9, 0xCA, 0xCB, 0xCC, 0xCD, 0xCE, 0xCF, 0xD0, 0xD1, 0xD2, 0xD3, 0xD4, 0x00
    };

    oled_write_P(qmk_logo, false);
}

void oled_render_boot(bool bootloader) {
    oled_clear();
    render_logo();
    for (int i = 0; i < 16; i++) {
        oled_set_cursor(0, i);
        if (bootloader) {
            oled_write_P(PSTR("Awaiting New Firmware "), false);
        } else {
            oled_write_P(PSTR("Rebooting "), false);
        }
    }

    oled_render_dirty(true);
}

bool shutdown_user(bool jump_to_bootloader) {
    oled_render_boot(jump_to_bootloader);
    return false;
}
#endif
