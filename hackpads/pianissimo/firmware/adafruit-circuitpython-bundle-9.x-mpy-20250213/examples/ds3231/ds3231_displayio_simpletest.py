# SPDX-FileCopyrightText: 2024
# SPDX-License-Identifier: MIT

import board
from adafruit_display_text.label import Label
from displayio import Group
from terminalio import FONT

import adafruit_ds3231

# Create the RTC object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector
ds3231 = adafruit_ds3231.DS3231(i2c)


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


# Lookup tables for names of days and months - pretty printing
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
months = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)

# Begin main loop
while True:
    t = ds3231.datetime
    # Update the label.text property to change the text on the display
    display_output_label.text = f"{days[t.tm_wday]}\
        \n{t.tm_mday} {months[t.tm_mon-1]} {t.tm_year}\
        \n{t.tm_hour}:{t.tm_min:02}:{t.tm_sec:02}"
