// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later
#include QMK_KEYBOARD_H

extern MidiDevice midi_device;

// MIDI CC codes for generic on/off switches (80, 81, 82, 83)
// Off: 0-63
// On:  64-127

#define MIDI_CC_OFF 0
#define MIDI_CC_ON  127

enum custom_keycodes {
    MIDI_CC80 = SAFE_RANGE,
};

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    switch (keycode) {
        case MIDI_CC80:
            if (record->event.pressed) {
                midi_send_cc(&midi_device, midi_config.channel, 80, MIDI_CC_ON);
            } else {
                midi_send_cc(&midi_device, midi_config.channel, 80, MIDI_CC_OFF);
            }
            return true;
    }
    return true;
};

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    LAYOUT(
         QK_MIDI_TOGGLE, QK_MIDI_OCTAVE_UP, QK_MIDI_OCTAVE_DOWN, QK_MIDI_NOTE_C_0, QK_MIDI_MIDI_NOTE_C_1, QK_MIDI_NOTE_C_2, QK_MIDI_NOTE_C_3, QK_MIDI_NOTE_C_4, QK_MIDI_NOTE_D_0, QK_MIDI_NOTE_E_0, QK_MIDI_NOTE_F_0, QK_MIDI_NOTE_G_0, QK_MIDI_NOTE_A_0, QK_MIDI_NOTE_B_0
#if defined(ENCODER_MAP_ENABLE)
const uint16_t PROGMEM encoder_map[][NUM_ENCODERS][NUM_DIRECTIONS] = {
    [0] = { ENCODER_CCW_CW(QK_MIDI_VELOCITY_UP, QK_MIDI_VELOCITY_DOWN),  ENCODER_CCW_CW(QK_MIDI_CHANNEL_UP, QK_MIDI_CHANNEL_DOWN), ENCODER_CCW_CW(QK_MIDI_PITCH_BEND_UP, QK_MIDI_PITCH_BEND_DOWN),  ENCODER_CCW_CW(QK_MIDI_TRANSPOSE_UP, QK_MIDI_TRANSPOSE_DOWN)  },
};
#endif
    )
};