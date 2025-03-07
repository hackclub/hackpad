# SPDX-FileCopyrightText: 2024
# SPDX-License-Identifier: MIT

import time
import board
from adafruit_display_text.bitmap_label import Label
from displayio import Group
from terminalio import FONT

import adafruit_vcnl4040

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector
vcnl4040 = adafruit_vcnl4040.VCNL4040(i2c)


# Example written for boards with built-in displays
display = board.DISPLAY

# Create a main_group to hold anything we want to show on the display.
main_group = Group()

# Create a Label to show the readings. If you have a very small
# display you may need to change to scale=1.
display_output_label = Label(FONT, text="", scale=2)

# Place the label near the top left corner with anchored positioning
display_output_label.anchor_point = (0, 0)
display_output_label.anchored_position = (4, 4)

# Add the label to the main_group
main_group.append(display_output_label)

# Set the main_group as the root_group of the display
display.root_group = main_group

# Begin main loop
while True:
    # Update the label.text property to change the text on the display
    display_output_label.text = f"Proximity: {vcnl4040.proximity} \
        \nLight: {vcnl4040.lux:.1f} lux \
        \nWhite: {vcnl4040.white:.1f}"
    # Wait a bit between reads
    time.sleep(0.5)
