# SPDX-FileCopyrightText: Copyright (c) 2024 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import board
import digitalio
from adafruit_hx711.hx711 import HX711
from adafruit_hx711.analog_in import AnalogIn

data = digitalio.DigitalInOut(board.D5)
data.direction = digitalio.Direction.INPUT
clock = digitalio.DigitalInOut(board.D6)
clock.direction = digitalio.Direction.OUTPUT

hx711 = HX711(data, clock)
channel_a = AnalogIn(hx711, HX711.CHAN_A_GAIN_128)
# channel_b = AnalogIn(hx711, HX711.CHAN_B_GAIN_32)

while True:
    print(f"Reading: {channel_a.value}")
    time.sleep(1)
