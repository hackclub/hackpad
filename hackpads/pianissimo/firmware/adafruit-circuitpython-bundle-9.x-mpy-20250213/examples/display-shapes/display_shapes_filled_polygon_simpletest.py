# SPDX-FileCopyrightText: 2024 Tim Cocks for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import displayio
from adafruit_display_shapes.filled_polygon import FilledPolygon

# Make the display context
splash = displayio.Group()
board.DISPLAY.root_group = splash

# Make a background color fill
color_bitmap = displayio.Bitmap(320, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF
bg_sprite = displayio.TileGrid(color_bitmap, x=0, y=0, pixel_shader=color_palette)
splash.append(bg_sprite)
##########################################################################

# Draw a star with blue outline and pink fill
polygon = FilledPolygon(
    [
        (55, 40),
        (62, 62),
        (85, 62),
        (65, 76),
        (75, 100),
        (55, 84),
        (35, 100),
        (45, 76),
        (25, 62),
        (48, 62),
    ],
    outline=0x0000FF,
    stroke=4,
    fill=0xFF00FF,
)
splash.append(polygon)

while True:
    pass
