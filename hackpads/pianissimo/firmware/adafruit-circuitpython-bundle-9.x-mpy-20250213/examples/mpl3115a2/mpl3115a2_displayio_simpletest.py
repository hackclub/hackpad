# SPDX-FileCopyrightText: 2024 Tim Cocks for Adafruit Industries
# SPDX-FileCopyrightText: 2025 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from adafruit_display_text.bitmap_label import Label
from terminalio import FONT
from displayio import Group
import adafruit_mpl3115a2

# Simple demo of using the built-in display.
# create a main_group to hold anything we want to show on the display.
main_group = Group()
# Initialize I2C bus and sensor.
i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_mpl3115a2.MPL3115A2(i2c)


# Create Label(s) to show the readings. If you have a very small
# display you may need to change to scale=1.
display_output_pressure = Label(FONT, text="", scale=2)
display_output_altitude = Label(FONT, text="", scale=2)
display_output_temperature = Label(FONT, text="", scale=2)

# place the label(s) in the middle of the screen with anchored positioning
display_output_pressure.anchor_point = (0, 0)
display_output_pressure.anchored_position = (
    4,
    board.DISPLAY.height // 2 - 60,
)
display_output_altitude.anchor_point = (0, 0)
display_output_altitude.anchored_position = (
    4,
    board.DISPLAY.height // 2 - 40,
)
display_output_temperature.anchor_point = (0, 0)
display_output_temperature.anchored_position = (
    4,
    board.DISPLAY.height // 2 - 20,
)


# add the label(s) to the main_group
main_group.append(display_output_pressure)
main_group.append(display_output_altitude)
main_group.append(display_output_temperature)

# set the main_group as the root_group of the built-in DISPLAY
board.DISPLAY.root_group = main_group

# begin main loop
while True:
    # update the text of the label(s) to show the sensor readings
    pressure = sensor.pressure
    display_output_pressure.text = f"Pressure: {pressure:.2f} hPa"
    altitude = sensor.altitude
    display_output_altitude.text = f"Altitude: {altitude:.2f} m"
    temperature = sensor.temperature
    display_output_temperature.text = f"Temperature: {temperature:.2f} C"
    # wait for a bit
    time.sleep(2)
