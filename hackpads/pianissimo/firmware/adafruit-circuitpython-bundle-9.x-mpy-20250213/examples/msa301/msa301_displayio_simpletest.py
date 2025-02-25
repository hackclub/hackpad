# SPDX-FileCopyrightText: 2024 Tim Cocks for Adafruit Industries
# SPDX-FileCopyrightText: 2024 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from adafruit_display_text.bitmap_label import Label
from terminalio import FONT
from displayio import Group
from adafruit_msa3xx import MSA301

# Simple demo of using the built-in display.
# create a main_group to hold anything we want to show on the display.
main_group = Group()
# Initialize I2C bus and sensor.
i2c = board.I2C()  # uses board.SCL and board.SDA
msa = MSA301(i2c)

# Create Label(s) to show the readings. If you have a very small
# display you may need to change to scale=1.
display_output_label = Label(FONT, text="", scale=2)

# place the label(s) in the middle of the screen with anchored positioning
display_output_label.anchor_point = (0, 0)
display_output_label.anchored_position = (
    4,
    board.DISPLAY.height // 2 - 60,
)

# add the label(s) to the main_group
main_group.append(display_output_label)

# set the main_group as the root_group of the built-in DISPLAY
board.DISPLAY.root_group = main_group

# begin main loop
while True:
    # update the text of the label(s) to show the sensor readings
    x, y, z = msa.acceleration
    display_output_label.text = f"X:{x:.2f} m/s^2\nY:{y:.2f} m/s^2\nZ:{z:.2f} m/s^2"
    # wait for a bit
    time.sleep(0.5)
