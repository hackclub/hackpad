# SPDX-FileCopyrightText: Copyright (c) 2022 Pete Lewis for SparkFun Electronics
# SPDX-FileCopyrightText: Copyright (c) 2024 Cooper Dalrymple
#
# SPDX-License-Identifier: MIT

"""
Demonstrates analog audio input (on INPUT2s), sets volume control, and headphone output on the
WM8960 Codec.

Audio should be connected to both the left and right "INPUT2" inputs, they are labeled "RIN2" and
"LIN2" on the board.

This example will pass your audio source through the mixers and gain stages of the codec using all
of the analog bypass paths.

It will output the sound on the headphone outputs.
It is setup to do a capless headphone setup, so connect your headphones ground to "OUT3" and this
provides a buffered VMID.

You can now control the volume of the codecs built in headphone buffers using this function:
codec.setHeadphoneVolumeDB(6.00); Valid inputs are -74.00 (MUTE) up to +6.00, (1.00dB steps).

HARDWARE CONNECTIONS

**********************
MCU --------- CODEC
**********************
QWIIC ------- QWIIC       *Note this connects GND/3.3V/SDA/SCL
GND --------- GND         *optional, but not a bad idea
5V ---------- VIN         *needed to power codec's onboard AVDD (3.3V vreg)

**********************
CODEC ------- AUDIO IN
**********************
GND --------- TRS INPUT SLEEVE        *ground for line level input
LINPUT2 ----- TRS INPUT TIP           *left audio
RINPUT2 ----- TRS INPUT RING1         *right audio

**********************
CODEC -------- AUDIO OUT
**********************
OUT3 --------- TRS OUTPUT SLEEVE          *buffered "vmid" (aka "HP GND")
HPL ---------- TRS OUTPUT TIP             *left HP output
HPR ---------- TRS OUTPUT RING1           *right HP output

Originally authored by Pete Lewis @ SparkFun Electronics, October 14th, 2022
https://github.com/sparkfun/SparkFun_WM8960_Arduino_Library

For information on the data sent to and received from the CODEC, refer to the WM8960 datasheet at:
https://github.com/sparkfun/SparkFun_Audio_Codec_Breakout_WM8960/blob/main/Documents/WM8960_datasheet_v4.2.pdf
"""

import board
from adafruit_wm8960 import Input, WM8960

codec = WM8960(board.I2C())

# Select the desired input. Available options are MIC1 (single-ended), MIC2 (differential),
# MIC3 (differential), LINE2, or LINE3.
codec.input = Input.MIC1

# Configure the microphone boost gain
codec.gain = 0.5

# Bypass analog signal to analog output
codec.monitor = 1.0

# Enable the amplifier and set the output volume
codec.headphone = 0.5
