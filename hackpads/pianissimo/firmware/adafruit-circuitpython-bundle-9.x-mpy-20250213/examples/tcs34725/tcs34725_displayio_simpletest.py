# SPDX-FileCopyrightText: 2024 Tim Cocks for Adafruit Industries
# SPDX-FileCopyrightText: 2024 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from adafruit_display_text.bitmap_label import Label
from terminalio import FONT
from displayio import Group
import adafruit_tcs34725

# Simple demo of using the built-in display.
# create a main_group to hold anything we want to show on the display.
main_group = Group()
# Initialize I2C bus and sensor.
i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_tcs34725.TCS34725(i2c)

# Create Label(s) to show the readings. If you have a very small
# display you may need to change to scale=1.
color_output_label = Label(FONT, text="", scale=2)
temperature_output_label = Label(FONT, text="", scale=2)
lux_output_label = Label(FONT, text="", scale=2)

# place the label(s) in the middle of the screen with anchored positioning
color_output_label.anchor_point = (0, 0)
color_output_label.anchored_position = (
    4,
    board.DISPLAY.height // 2 - 60,
)
temperature_output_label.anchor_point = (0, 0)
temperature_output_label.anchored_position = (
    4,
    board.DISPLAY.height // 2 - 0,
)
lux_output_label.anchor_point = (0, 0)
lux_output_label.anchored_position = (
    4,
    board.DISPLAY.height // 2 + 20,
)

# add the labels to the main_group
main_group.append(color_output_label)
main_group.append(temperature_output_label)
main_group.append(lux_output_label)

# set the main_group as the root_group of the built-in DISPLAY
board.DISPLAY.root_group = main_group

# begin main loop
while True:
    # Raw data from the sensor in a 4-tuple of red, green, blue, clear light component values
    color_output_label.text = f"RGB color 3-tuple:\n{sensor.color_rgb_bytes}"
    # Read the color temperature and lux of the sensor too.
    temperature_output_label.text = f"Temp: {sensor.color_temperature}K"
    lux_output_label.text = f"Lux: {sensor.lux}"
    # wait for a bit
    time.sleep(0.5)
