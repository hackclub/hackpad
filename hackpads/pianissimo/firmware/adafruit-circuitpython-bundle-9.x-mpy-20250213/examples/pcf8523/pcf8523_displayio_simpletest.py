# SPDX-FileCopyrightText: 2024 Tim Cocks for Adafruit Industries
# SPDX-FileCopyrightText: 2024 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

# Simple demo of the PCF8523 real-time clock using a built-in display.
import time
import board
from adafruit_display_text.bitmap_label import Label
from terminalio import FONT
from displayio import Group
from adafruit_pcf8523.pcf8523 import PCF8523


# create a main_group to hold anything we want to show on the display.
main_group = Group()
# Initialize I2C bus and sensor.
i2c = board.I2C()  # uses board.SCL and board.SDA
rtc = PCF8523(i2c)

# Lookup table for names of days (nicer printing).
days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)

# Set the time
t = time.struct_time((2024, 12, 12, 10, 31, 0, 0, -1, -1))
rtc.datetime = t
print("Setting time to:", t)

# Create two Labels to show the readings. If you have a very small
# display you may need to change to scale=1.
date_output_label = Label(FONT, text="", scale=2)
time_output_label = Label(FONT, text="", scale=2)

# place the label in the middle of the screen with anchored positioning
date_output_label.anchor_point = (0, 0)
date_output_label.anchored_position = (4, board.DISPLAY.height // 2)
time_output_label.anchor_point = (0, 0)
time_output_label.anchored_position = (4, 20 + board.DISPLAY.height // 2)

# add the label to the main_group
main_group.append(date_output_label)
main_group.append(time_output_label)

# set the main_group as the root_group of the built-in DISPLAY
board.DISPLAY.root_group = main_group

# begin main loop
while True:
    # Update the label.text property to change the text on the display
    t = rtc.datetime
    date_output_label.text = (
        f"The date is {days[int(t.tm_wday)]} {t.tm_mday}/{t.tm_mon}/{t.tm_year}"
    )
    time_output_label.text = f"The time is {t.tm_hour}:{t.tm_min:02}:{t.tm_sec:02}"
    # wait for a bit
    time.sleep(1)
