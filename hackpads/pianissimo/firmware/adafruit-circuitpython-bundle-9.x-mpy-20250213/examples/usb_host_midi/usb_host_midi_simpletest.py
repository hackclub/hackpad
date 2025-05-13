# SPDX-FileCopyrightText: Copyright (c) 2023 Scott Shawcroft for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

import audiobusio
import board
import synthio
import usb.core
import wm8960
import adafruit_midi
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
import adafruit_usb_host_midi

print("Looking for midi device")
raw_midi = None
while raw_midi is None:
    for device in usb.core.find(find_all=True):
        try:
            raw_midi = adafruit_usb_host_midi.MIDI(device)
            print("Found", hex(device.idVendor), hex(device.idProduct))
        except ValueError:
            continue


# This setup is for the headphone output on the iMX RT 1060 EVK.
dac = wm8960.WM8960(board.I2C())
dac.start_i2s_out()
audio = audiobusio.I2SOut(
    board.AUDIO_BCLK, board.AUDIO_SYNC, board.AUDIO_TXD, main_clock=board.AUDIO_MCLK
)
synth = synthio.Synthesizer(sample_rate=44100)
audio.play(synth)

midi = adafruit_midi.MIDI(midi_in=raw_midi, in_channel=0)

pressed = {}

while True:
    msg = midi.receive()
    if isinstance(msg, NoteOn) and msg.velocity != 0:
        note = synthio.Note(synthio.midi_to_hz(msg.note))
        print("noteOn: ", msg.note, "vel:", msg.velocity)
        synth.press(note)
        pressed[msg.note] = note
    elif (
        isinstance(msg, NoteOff) or (isinstance(msg, NoteOn) and msg.velocity == 0)
    ) and msg.note in pressed:
        print("noteOff:", msg.note, "vel:", msg.velocity)
        note = pressed[msg.note]
        synth.release(note)
        del pressed[msg.note]
