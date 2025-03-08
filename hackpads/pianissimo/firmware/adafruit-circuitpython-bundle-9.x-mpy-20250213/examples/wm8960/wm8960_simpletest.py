# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Scott Shawcroft for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2024 Cooper Dalrymple
#
# SPDX-License-Identifier: Unlicense

"""
Demonstrates I2C Output on WM8960 Codec by generating a simple tone using synthio. Sounds like an
alarm clock.

It will output the sound on the headphone outputs.
It is setup to do a capless headphone setup, so connect your headphones ground to "OUT3" and this
provides a buffered VMID.

HARDWARE CONNECTIONS

**********************
MCU --------- CODEC
**********************
QWIIC ------- QWIIC       *Note this connects GND/3.3V/SDA/SCL
GND --------- GND         *optional, but not a bad idea
5V ---------- VIN         *needed to power codec's onboard AVDD (3.3V vreg)
AUDIO_TXD --- DDT         *aka DAC_DATA/I2S_SDO/"serial data out", this carries the I2S audio data
                           from MCU to codec DAC
AUDIO_BCLK -- BCK         *aka BCLK/I2S_SCK/"bit clock", this is the clock for I2S audio, can be
                           controlled via controller or peripheral.
AUDIO_SYNC -- DLRC        *aka I2S_WS/LRC/"word select"/"left-right-channel", this toggles for left
                           or right channel data.

**********************
CODEC ------- AUDIO OUT
**********************
OUT3 -------- TRS OUTPUT SLEEVE          *buffered "vmid" (aka "HP GND")
HPL --------- TRS OUTPUT TIP             *left HP output
HPR --------- TRS OUTPUT RING1           *right HP output

You can now control the volume of the codecs built in headphone buffers using this function:
codec.setHeadphoneVolumeDB(6.00)
Valid inputs are -74.00 (MUTE) up to +6.00, (1.00dB steps).

For information on the data sent to and received from the CODEC, refer to the WM8960 datasheet at:
https://github.com/sparkfun/SparkFun_Audio_Codec_Breakout_WM8960/blob/main/Documents/WM8960_datasheet_v4.2.pdf
"""

import time
import board
import digitalio
import audiobusio
import synthio
from adafruit_wm8960 import WM8960

codec = WM8960(board.I2C(), 44100, 16)
codec.volume = 1.0
codec.headphone = 0.5
codec.speaker = 0.5

# Configure I2S Output
audio = audiobusio.I2SOut(board.AUDIO_BCLK, board.AUDIO_SYNC, board.AUDIO_TXD)

# Setup synthio
synth = synthio.Synthesizer(sample_rate=codec.sample_rate)
audio.play(synth)

led = digitalio.DigitalInOut(board.LED)
led.switch_to_output()

while True:
    print("note on")
    synth.press(65)  # midi note 65 = F4
    led.value = True
    time.sleep(0.5)
    synth.release(65)  # release the note we pressed
    led.value = False
    print("note off")
    time.sleep(0.5)
