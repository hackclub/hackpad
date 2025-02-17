# SPDX-FileCopyrightText: 2024
# SPDX-License-Identifier: MIT

import time
import board
from adafruit_display_text.bitmap_label import Label
from displayio import Group
from terminalio import FONT

import adafruit_sht4x

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector
sht = adafruit_sht4x.SHT4x(i2c)

print("Found SHT4x with serial number", hex(sht.serial_number))

sht.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION
# Can also set the mode to enable heater
# sht.mode = adafruit_sht4x.Mode.LOWHEAT_100MS
# print("Current mode is: ", adafruit_sht4x.Mode.string[sht.mode])


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
    temperature, relative_humidity = sht.measurements
    # Update the label.text property to change the text on the display
    display_output_label.text = (
        f"Temperature: {temperature:.1f} C \nHumidity: {relative_humidity:.1f} %"
    )
    # Wait for a bit
    time.sleep(1)
