# SPDX-FileCopyrightText: Copyright (c) 2024 Tim C for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
Illustrate usage of the AnchoredTileGrid class.

A speech blurb image is positioned relative to the
point at the bottom of the blurb.
"""

import board
from displayio import Group, OnDiskBitmap, Palette
from vectorio import Circle

from adafruit_anchored_tilegrid import AnchoredTileGrid

# Reference to built-in display
display = board.DISPLAY

# palette to use for drawing a circle
circle_palette = Palette(1)
circle_palette[0] = 0xFF00FF

# circle object, we'll place our speech blurb near this
circle = Circle(pixel_shader=circle_palette, radius=20, x=40, y=70)

# initialize a Group and add the circle to it
main_group = Group()
main_group.append(circle)

# load the speech blurb bitmap
speech_blurb_bmp = OnDiskBitmap("example_image.bmp")

# make the background chroma key color transparent
speech_blurb_bmp.pixel_shader.make_transparent(0)

# initialize an AnchoredTileGrid for the blurb
speech_blurb = AnchoredTileGrid(bitmap=speech_blurb_bmp, pixel_shader=speech_blurb_bmp.pixel_shader)

# set the anchor point to the bottom point of the speech blurb
speech_blurb.anchor_point = (0.18, 1.0)

# position it near the circle
speech_blurb.anchored_position = (circle.x + 16, circle.y - 16)

# add it to the group
main_group.append(speech_blurb)

# set our group to root_group, so it gets shown on the display
display.root_group = main_group


while True:
    # wait forever so our group stays visible
    pass
