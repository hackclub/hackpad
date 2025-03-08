# SPDX-FileCopyrightText: Copyright (c) 2022 Pete Lewis for SparkFun Electronics
# SPDX-FileCopyrightText: Copyright (c) 2024 Cooper Dalrymple
#
# SPDX-License-Identifier: MIT

"""
Demonstrates how to use the automatic level control feature of the WM8960 Codec.

Attach a potentiomenter to GND/A0/3V3 to actively adjust the ALC target setting.

This example sets up the codec for analog audio input (on INPUT1s), ADC/DAC Loopback, sets headphone
volume, and Headphone output on the WM8960 Codec.

Audio should be connected to both the left and right "INPUT1" inputs, they are labeled "RIN1" and
"LIN1" on the board.

This example will pass your audio source through the mixers and gain stages of the codec into the
ADC. Turn on Loopback (so ADC is feed directly to DAC).
Then send the output of the DAC to the headphone outs.

We will use the user input via potentiometer on A0 to set the ALC target value. The ALC will adjust
the gain of the pga input buffer to try and keep the signal level at the target.

HARDWARE CONNECTIONS

**********************
MCU --------- CODEC
**********************
QWIIC ------- QWIIC       *Note this connects GND/3.3V/SDA/SCL
GND --------- GND         *optional, but not a bad idea
5V ---------- VIN         *needed to power codec's onboard AVDD (3.3V vreg)

**********************
MCU --------- POTENTIOMTER (aka blue little trimpot)
**********************
GND --------- "right-side pin"
A0 ---------- center pin            *aka center tap connection
3V3 --------- "left-side pin"

**********************
CODEC ------- AUDIO IN
**********************
GND --------- TRS INPUT SLEEVE        *ground for line level input
LINPUT1 ----- TRS INPUT TIP           *left audio
RINPUT1 ----- TRS INPUT RING1         *right audio

**********************
CODEC ------- AUDIO OUT
**********************
OUT3 -------- TRS OUTPUT SLEEVE          *buffered "vmid" (aka "HP GND")
HPL --------- TRS OUTPUT TIP             *left HP output
HPR --------- TRS OUTPUT RING1           *right HP output

Originally authored by Pete Lewis @ SparkFun Electronics, October 14th, 2022
https://github.com/sparkfun/SparkFun_WM8960_Arduino_Library

For information on the data sent to and received from the CODEC, refer to the WM8960 datasheet at:
https://github.com/sparkfun/SparkFun_Audio_Codec_Breakout_WM8960/blob/main/Documents/WM8960_datasheet_v4.2.pdf
"""

import time
import board
from analogio import AnalogIn
from adafruit_simplemath import map_range
from adafruit_wm8960 import Input, WM8960

analog_in = AnalogIn(board.A0)

codec = WM8960(board.I2C())
codec.input = Input.MIC1
codec.gain = 0.5
codec.volume = 1.0
codec.headphone = 0.5

codec.alc = True
codec.alc_gain = (
    0.75,  # target
    1.0,  # max gain
    0.0,  # min gain
    0.0,  # noise gate
)
codec.alc_time = (
    0.024,  # attack
    0.192,  # decay
    0.0,  # hold
)

codec.loopback = True

gain = list(codec.alc_gain)
while True:
    gain[0] = map_range(analog_in.value, 0, 65536, 0.0, 1.0)
    codec.alc_gain = gain
    time.sleep(1.0)
