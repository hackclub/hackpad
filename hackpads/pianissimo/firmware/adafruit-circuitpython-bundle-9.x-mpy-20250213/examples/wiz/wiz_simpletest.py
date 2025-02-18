# SPDX-FileCopyrightText: Copyright (c) 2024 Tim Cocks for Adafruit Industries
#
# SPDX-License-Identifier: MIT
import time

import wifi

from adafruit_wiz import SCENE_IDS, WizConnectedLight

udp_host = "192.168.1.143"  # IP of UDP Wiz connected light
udp_port = 38899  # Default port is 38899, change if your light is configured differently

my_lamp = WizConnectedLight(udp_host, udp_port, wifi.radio)


print(f"Current Status: {my_lamp.status}")

print("Setting RGB Color")
my_lamp.rgb_color = (255, 0, 255)
time.sleep(2)

print("Turning off")
my_lamp.state = False
time.sleep(2)

print("Turning on")
my_lamp.state = True

print("Setting Light Color Temperature")
my_lamp.temperature = 2200
time.sleep(2)

print("Lowering the Brightness")
my_lamp.brightness = 10
time.sleep(2)

print("Raising the Brightness")
my_lamp.brightness = 100

print("Available Scenes:")
print(SCENE_IDS.keys())
print("Setting Scene")
my_lamp.scene = "Party"
