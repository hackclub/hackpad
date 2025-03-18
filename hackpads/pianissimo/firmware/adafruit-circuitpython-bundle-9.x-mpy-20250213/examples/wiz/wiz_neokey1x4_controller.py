# SPDX-FileCopyrightText: Copyright (c) 2024 Tim Cocks for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
Demonstration of Wiz light control using a Neokey 1x4 QT I2C
https://www.adafruit.com/product/4980
"""

import json
import time

import board
import wifi
from adafruit_neokey.neokey1x4 import NeoKey1x4

from adafruit_wiz import SCENE_IDS, WizConnectedLight

udp_host = "192.168.1.143"  # IP of UDP Wiz connected light
udp_port = 38899  # Default port is 38899, change if your light is configured differently

my_lamp = WizConnectedLight(udp_host, udp_port, wifi.radio, debug=True)

# use default I2C bus
i2c_bus = board.STEMMA_I2C()

# Create a NeoKey object
neokey = NeoKey1x4(i2c_bus, addr=0x30)

# list of colors to cycle through
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
# current index in the color cycle
cur_rgb_index = 0

# list of temperatures to cycle through
temperatures = [2200, 2800, 3600, 4800, 6200]
# current index in the temperature cycle
cur_temp_index = 0

while True:
    # if btn A pressed
    if neokey[0]:
        print("Button A")
        # toggle the on/off state
        my_lamp.state = not my_lamp.state
        time.sleep(0.5)

    # if btn B pressed
    if neokey[1]:
        print("Button B")
        # set the current RGB color
        my_lamp.rgb_color = colors[cur_rgb_index]
        # increment the index for next time and wrap around to zero as needed
        cur_rgb_index = (cur_rgb_index + 1) % len(colors)
        time.sleep(0.5)

    # if btn C pressed
    if neokey[2]:
        print("Button C")
        # set the current light color temperature
        my_lamp.temperature = temperatures[cur_temp_index]
        # increment the index for next time and wrap around to zero as needed
        cur_temp_index = (cur_temp_index + 1) % len(temperatures)
        time.sleep(0.5)
    # if btn D pressed
    if neokey[3]:
        print("Button D")
        # uncomment to see the available scenes
        # print(SCENE_IDS.keys())

        # set the scene
        my_lamp.scene = "Party"
