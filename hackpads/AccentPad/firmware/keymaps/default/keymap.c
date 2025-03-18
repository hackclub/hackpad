// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H
#include "keymap_us_international.h"
#include "sendstring_us_international.h"

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┬───┐
     * │ á │ à │ â │ ä │
     * ├───┼───┼───┼───┤
     * │ ã │ ç │ ā │ ø │
     * ├───┼───┼───┼───┤
     * │ å │ ą │ ă │ ǎ │
     * ├───┼───┼───┼───┤
     * │ æ │ œ │ ð │ þ │
     * └───┴───┴───┴───┘
     */
    [0] = LAYOUT(
        US_ACUT,       US_DGRV,       US_DCIR,         US_DIAE,
        US_DTIL,       US_CCED,       S(ALGR(US_3)),   US_OSTR,
        S(ALGR(US_0)), S(ALGR(US_8)), S(ALGR(US_9)),   S(ALGR(US_DOT)),
        ALGR(US_Z),    ALGR(US_K),    US_ETH,          US_THRN
    )
};
