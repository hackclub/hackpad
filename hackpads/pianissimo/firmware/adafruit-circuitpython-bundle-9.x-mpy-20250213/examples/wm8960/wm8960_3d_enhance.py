# SPDX-FileCopyrightText: Copyright (c) 2022 Pete Lewis for SparkFun Electronics
# SPDX-FileCopyrightText: Copyright (c) 2024 Cooper Dalrymple
#
# SPDX-License-Identifier: MIT

"""
Demonstrates analog audio input (on INPUT1s), ADC/DAC Loopback, sets volume control, and Headphone
output on the WM8960 Codec.

Audio should be connected to both the left and right "INPUT1" inputs, they are labeled "RIN1" and
"LIN1" on the board.

This example will pass your audio source through the mixers and gain stages of the codec into the
ADC. Turn on Loopback (so ADC is feed directly to DAC).
Then send the output of the DAC to the headphone outs.

You can now control the volume of the codecs built in headphone amp using this function:
codec.setHeadphoneVolumeDB(6.00)
Valid inputs are -74.00 (MUTE) up to +6.00, (1.00dB steps).

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
LINPUT1 ----- TRS INPUT TIP           *left audio
RINPUT1 ----- TRS INPUT RING1         *right audio

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

import time
import board
from adafruit_wm8960 import Input, WM8960

codec = WM8960(board.I2C())
codec.loopback = True
codec.input = Input.MIC1
codec.gain = 0.5
codec.volume = 1.0

codec.headphone = 0.5

# Toggle 3D enhance on and off
while True:
    codec.enhance = 0.0 if codec.enhance else 1.0
    time.sleep(2.0)
