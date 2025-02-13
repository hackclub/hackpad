# SPDX-FileCopyrightText: 2024 Tim Cocks for Adafruit Industries
# contributions by J Fletcher, adapting code by Prof Gallaugher:
#           https://www.youtube.com/watch?v=cdx1A1xoEWc&t=5s
# tested on ESP32-S3 Reverse TFT Feather:
#           https://www.adafruit.com/product/5691
# SPDX-License-Identifier: MIT

import time
import board
from adafruit_display_text.bitmap_label import Label
from terminalio import FONT
from displayio import Group
import adafruit_vl53l1x

# create a main_group to hold anything we want to show on the display.
main_group = Group()

# Create sensor object, communicating over the board's default I2C bus
# i2c = board.I2C()  # uses board.SCL and board.SDA
i2c = board.STEMMA_I2C()
# For using the built-in STEMMA QT connector on a microcontroller
vl53 = adafruit_vl53l1x.VL53L1X(i2c)

# Create a Label to show the readings. If you have a very small
# display you may need to change to scale=1.
display_output_label = Label(FONT, text="", scale=1)

# place the label near the top left corner with anchored positioning
display_output_label.anchor_point = (0, 0)
display_output_label.anchored_position = (4, 4)

# add the label to the main_group
main_group.append(display_output_label)

# set the main_group as the root_group of the built-in DISPLAY
board.DISPLAY.root_group = main_group
# create a display object placeholder to be updated by the loop
screen = f"Distance: {''}cm, {''}in, {''}ft"
# initiate repeated sensor readings
vl53.start_ranging()


# begin main loop
while True:
    # There will be no values to populate at first, just the bare 'Distance: cm, in, ft' text
    # Assuming the first 'try' succeeds, this will be updated once the loop starts over
    display_output_label.text = screen

    # This 'try' sequence will either update the displayed items with fresh data or repeat the
    # last available data. VL53L1X sensors output `None` when no object reflects the laser,
    # e.g., there is nothing within 4 meters, or when objects pass too quickly in and out of
    # view (usually perpendicular to the field of vision).
    try:
        if vl53.distance:
            # simple test to see there is a value to read; no value = exception
            distance = vl53.distance
            # sets the variable (used by the display) to the sensor data
            inches = distance * 0.394
            # VL53L1X outputs distance in metric, so we convert to imperial
            screen = f"Distance: {distance: .1f}cm, {inches: .1f}in, {inches/12: .1f}ft"
            # if we made it this far, we have new data to display!
    except TypeError:
        repeat_screen = screen
        screen = repeat_screen
        # if things went sideways, we repeat the previous loop's data so we can try again

    time.sleep(0.25)
