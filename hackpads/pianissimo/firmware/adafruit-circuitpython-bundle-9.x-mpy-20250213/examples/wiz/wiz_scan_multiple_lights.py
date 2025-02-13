# SPDX-FileCopyrightText: Copyright (c) 2024 Tim Cocks for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
Scan the network for Wiz lights. Print out the MAC addresses of any lights found.
Set each light to a different random RGB color.
"""

import random

import wifi

from adafruit_wiz import WizConnectedLight, scan

udp_port = 38899  # Default port is 38899
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
mac_to_light_map = {}

found_lights = scan(wifi.radio, timeout=1)
for light_info in found_lights:
    mac_to_light_map[light_info["result"]["mac"]] = WizConnectedLight(
        light_info["ip"], udp_port, wifi.radio
    )
    print(f"Found Light with MAC: {light_info['result']['mac']}")

for mac, light in mac_to_light_map.items():
    chosen_color = random.choice(colors)
    print(f"Setting light with MAC: {mac} to {chosen_color}")
    light.rgb_color = chosen_color
