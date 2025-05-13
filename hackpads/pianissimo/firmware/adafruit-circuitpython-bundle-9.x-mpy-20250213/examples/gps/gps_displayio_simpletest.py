# SPDX-FileCopyrightText: 2024
# SPDX-License-Identifier: MIT

import time
import board
from adafruit_display_text.label import Label
from displayio import Group
from terminalio import FONT

import adafruit_gps

# import busio
# uart = busio.UART(board.TX, board.RX, baudrate=9600, timeout=10)
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector

# Create a GPS module instance.
# gps = adafruit_gps.GPS(uart, debug=False)  # Use UART
gps = adafruit_gps.GPS_GtopI2C(i2c, debug=False)  # Use I2C interface

# Turn on the basic GGA and RMC info (what you typically want)
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")

# Set update rate to once a second 1hz (what you typically want)
gps.send_command(b"PMTK220,1000")


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


last_print = time.monotonic()

# Begin main loop
while True:
    gps.update()

    current = time.monotonic()
    # Update display data every second
    if current - last_print >= 1.0:
        last_print = current
        if not gps.has_fix:
            # Try again if we don't have a fix yet.
            display_output_label.text = "Waiting for fix..."
            continue
        # We have a fix! (gps.has_fix is true)
        t = gps.timestamp_utc

        # Update the label.text property to change the text on the display
        display_output_label.text = f"Timestamp (UTC): \
            \n{t.tm_mday}/{t.tm_mon}/{t.tm_year} {t.tm_hour}:{t.tm_min:02}:{t.tm_sec:02}\
            \nLat: {gps.latitude:.6f}\
            \nLong: {gps.longitude:.6f}"
