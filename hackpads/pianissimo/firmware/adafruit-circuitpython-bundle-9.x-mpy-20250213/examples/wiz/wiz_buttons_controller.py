# SPDX-FileCopyrightText: Copyright (c) 2024 Tim Cocks for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
Basic demonstration of Wiz light control using 4 push buttons each
wired to their own pin.
"""

import board
import keypad
import wifi

from adafruit_wiz import SCENE_IDS, WizConnectedLight

udp_host = "192.168.1.143"  # IP of UDP Wiz connected light
udp_port = 38899  # Default port is 38899, change if your light is configured differently

my_lamp = WizConnectedLight(udp_host, udp_port, wifi.radio, debug=True)

# Basic push buttons initialization with keypad
buttons = keypad.Keys(
    (board.D11, board.D12, board.A1, board.A0), value_when_pressed=False, pull=True
)

# list of colors to cycle through
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
# current index in the color cycle
cur_rgb_index = 0

# list of temperatures to cycle through
temperatures = [2200, 2800, 3600, 4800, 6200]
# current index in the temperature cycle
cur_temp_index = 0

while True:
    # check for button press events
    event = buttons.events.get()
    if event and event.pressed:
        if event.key_number == 0:
            print("Button 0")
            # toggle the on/off state
            my_lamp.state = not my_lamp.state

        elif event.key_number == 1:
            print("Button 1")
            # set the current RGB color
            my_lamp.rgb_color = colors[cur_rgb_index]
            # increment the index for next time and wrap around to zero as needed
            cur_rgb_index = (cur_rgb_index + 1) % len(colors)

        elif event.key_number == 2:
            print("Button 2")
            # set the current light color temperature
            my_lamp.temperature = temperatures[cur_temp_index]
            # increment the index for next time and wrap around to zero as needed
            cur_temp_index = (cur_temp_index + 1) % len(temperatures)

        elif event.key_number == 3:
            print("Button 3")
            # uncomment to see the available scenes
            # print(SCENE_IDS.keys())

            # set the scene
            my_lamp.scene = "Party"
