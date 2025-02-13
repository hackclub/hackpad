# SPDX-FileCopyrightText: 2024  Channing Ramos
#
# SPDX-License-Identifier: MIT

"""
Basic JPG imageload example
"""

import board
import displayio

import adafruit_imageload

group = displayio.Group()
board.DISPLAY.root_group = group

image, color_converter = adafruit_imageload.load("images/jpg_test.jpg")

tile_grid = displayio.TileGrid(image, pixel_shader=color_converter)
group.append(tile_grid)

while True:
    pass
