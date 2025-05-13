# SPDX-FileCopyrightText: 2024 Tim C, written for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
Illustrates usage of LinearLayout to display a text label to the right of
an icon.
"""
import adafruit_imageload
import board
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_displayio_layout.layouts.linear_layout import LinearLayout

# use built in display (PyPortal, PyGamer, PyBadge, CLUE, etc.)
# see guide for setting up external displays (TFT / OLED breakouts, RGB matrices, etc.)
# https://learn.adafruit.com/circuitpython-display-support-using-displayio/display-and-display-bus
display = board.DISPLAY

# Make the display context
main_group = displayio.Group()
display.root_group = main_group

layout = LinearLayout(
    x=10, y=10, padding=4, orientation=LinearLayout.HORIZONTAL_ORIENTATION
)

lbl = label.Label(terminalio.FONT, scale=4, x=0, y=0, text="Hello")

icon, icon_palette = adafruit_imageload.load("icons/Play_48x48_small.bmp")
icon_tile_grid = displayio.TileGrid(icon, pixel_shader=icon_palette)
layout.add_content(icon_tile_grid)
layout.add_content(lbl)

main_group.append(layout)
while True:
    pass
