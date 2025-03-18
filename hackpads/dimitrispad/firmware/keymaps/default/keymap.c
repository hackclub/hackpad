// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

enum layer_names {
    _BASE,
    _JS,
    _HTML,
    _JAVA,
};

enum custom_keycodes { JS_ASYNCFUNCTION = SAFE_RANGE, JS_DOCQS, JS_ARRF, HTML_DIV, HTML_CLASS, HTML_P, JAVA_PUB_STATIC_VOID, JAVA_PUBCLASS, JAVA_PRINT };

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [_BASE] = LAYOUT(
        KC_NO,
        KC_TAB,   KC_C,   KC_D,   KC_E,
        KC_UNDO, KC_COPY,  KC_PASTE, KC_SEMICOLON
    ),
    [_JS] = LAYOUT(
        KC_TRNS,
        KC_TRNS, JS_ASYNCFUNCTION, JS_DOCQS, JS_ARRF,
        KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS
    ),
    [_HTML] = LAYOUT(
        KC_TRNS,
        KC_TRNS, HTML_DIV, HTML_CLASS, HTML_P,
        KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS
    ),
    [_JAVA] = LAYOUT(
        KC_TRNS,
        KC_TRNS, JAVA_PUB_STATIC_VOID, JAVA_PUBCLASS, JAVA_PRINT,
        KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS
    )
};

uint8_t selected_layer = 1;
bool encoder_update_user(uint8_t index, bool clockwise) {
    switch (index) {
        case 0:
            if (!clockwise && selected_layer < 3) {
                selected_layer++;
            } else if (clockwise && selected_layer > 1) {
                selected_layer--;
            }
            layer_clear();
            layer_on(_BASE);
            layer_on(selected_layer);
    }
    return false;
}

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    switch (keycode) {
        case JS_ASYNCFUNCTION:
            if (record->event.pressed) SEND_STRING("async function ");
            break;
        case JS_DOCQS:
            if (record->event.pressed) SEND_STRING("document.querySelector(\"\")" SS_TAP(X_LEFT) SS_TAP(X_LEFT));
            break;
        case JS_ARRF:
            if (record->event.pressed) SEND_STRING("()=>");
            break;

        case HTML_DIV:
            if (record->event.pressed) SEND_STRING("<div>\n</div>" SS_TAP(X_LEFT) SS_TAP(X_LEFT) SS_TAP(X_LEFT) SS_TAP(X_LEFT) SS_TAP(X_LEFT) SS_TAP(X_LEFT));
            break;
        case HTML_CLASS:
            if (record->event.pressed) SEND_STRING("class=\"\"" SS_TAP(X_LEFT));
            break;
        case HTML_P:
            if (record->event.pressed) SEND_STRING("<p>\n</p>" SS_TAP(X_LEFT) SS_TAP(X_LEFT) SS_TAP(X_LEFT) SS_TAP(X_LEFT));
            break;

        case JAVA_PUB_STATIC_VOID:
            if (record->event.pressed) SEND_STRING("public static void ");
            break;
        case JAVA_PUBCLASS:
            if (record->event.pressed) SEND_STRING("public class ");
            break;
        case JAVA_PRINT:
            if (record->event.pressed) SEND_STRING("System.out.printf(\"\")" SS_TAP(X_LEFT) SS_TAP(X_LEFT));
            break;
    }
    return true;
};

bool oled_task_user(void) {

    oled_write_P(PSTR("Language: "), false);

    switch (get_highest_layer(layer_state)) {
        case _BASE:
            oled_write_P(PSTR("Default\n"), false);
            break;
        case _JS:
            oled_write_P(PSTR("Javascript\n"), false);
            break;
        case _HTML:
            oled_write_P(PSTR("HTML\n"), false);
            break;
        case _JAVA:
            oled_write_P(PSTR("Java\n"), false);
            break;
        default:
            oled_write_P(PSTR("Undefined\n"), false);
    }

    return false;
}
