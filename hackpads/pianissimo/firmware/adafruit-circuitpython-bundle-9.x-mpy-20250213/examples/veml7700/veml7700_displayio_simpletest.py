# SPDX-FileCopyrightText: 2024 Tim Cocks for Adafruit Industries
# SPDX-FileCopyrightText: 2024 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from adafruit_display_text.bitmap_label import Label
from terminalio import FONT
from displayio import Group
import adafruit_veml7700

# Simple demo of the VEML7700 light sensor.
# create a main_group to hold anything we want to show on the display.
main_group = Group()
# Initialize I2C bus and sensor.
i2c = board.I2C()  # uses board.SCL and board.SDA
veml7700 = adafruit_veml7700.VEML7700(i2c)

# Create two Labels to show the readings. If you have a very small
# display you may need to change to scale=1.
light_lux_output_label = Label(FONT, text="", scale=2)

# place the label in the middle of the screen with anchored positioning
light_lux_output_label.anchor_point = (0, 0)
light_lux_output_label.anchored_position = (
    4,
    board.DISPLAY.height // 2,
)

# add the label to the main_group
main_group.append(light_lux_output_label)

# set the main_group as the root_group of the built-in DISPLAY
board.DISPLAY.root_group = main_group

# begin main loop
while True:
    # Update the label.text property to change the text on the display
    light_lux_output_label.text = f"Ambient light:{veml7700.light}"
    # wait for a bit
    time.sleep(0.5)
