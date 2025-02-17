# SPDX-FileCopyrightText: Copyright (c) 2023 Scott Shawcroft for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
# pylint: disable=unused-import

import board
import busio
import usb.core
import adafruit_midi
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
from adafruit_midi.control_change import ControlChange
from adafruit_midi.pitch_bend import PitchBend
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

# This setup is to use TX pin on Feather RP2040 with USB Type A Host as MIDI out
# You must wire up the needed resistors and jack yourself
# This will forward all MIDI messages from the device to hardware uart MIDI
uart = busio.UART(rx=board.RX, tx=board.TX, baudrate=31250, timeout=0.001)

midi_device = adafruit_midi.MIDI(midi_in=raw_midi, in_channel=0)
midi_uart = adafruit_midi.MIDI(midi_out=uart, midi_in=uart)


while True:
    msg = midi_device.receive()
    if msg:
        print("midi msg:", msg)
        midi_uart.send(msg)
