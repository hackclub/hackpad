# SPDX-FileCopyrightText: 2024 Tim Cocks for Adafruit Industries
# SPDX-FileCopyrightText: 2024 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

# Simple demo of the SI1145 UV sensor using a built-in display.
import time
import board
from adafruit_display_text.bitmap_label import Label
from terminalio import FONT
from displayio import Group
import adafruit_si1145


# create a main_group to hold anything we want to show on the display.
main_group = Group()
# Initialize I2C bus and sensor.
i2c = board.I2C()  # uses board.SCL and board.SDA
si1145 = adafruit_si1145.SI1145(i2c)

# Create a Label to show the readings. If you have a very small
# display you may need to change to scale=1.
display_output_label = Label(FONT, text="", scale=2)

# place the label in the middle of the screen with anchored positioning
display_output_label.anchor_point = (0, 0)
display_output_label.anchored_position = (4, board.DISPLAY.height // 2)

# add the label to the main_group
main_group.append(display_output_label)

# set the main_group as the root_group of the built-in DISPLAY
board.DISPLAY.root_group = main_group

# begin main loop
while True:
    # Update the label.text property to change the text on the display
    vis, ir = si1145.als
    display_output_label.text = f"Visible = {vis}, Infrared = {ir}"
    # wait for a bit
    time.sleep(1.0)
