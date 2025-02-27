# SPDX-FileCopyrightText: 2024 Tim Cocks for Adafruit Industries
# SPDX-License-Identifier: MIT
"""
Illustrates how to dynamically update arcs over time.
"""
import time
import board

import displayio
from adafruit_display_shapes.arc import Arc
from adafruit_display_shapes.circle import Circle

# use built in display (PyPortal, PyGamer, PyBadge, CLUE, etc.)
# see guide for setting up external displays (TFT / OLED breakouts, RGB matrices, etc.)
# https://learn.adafruit.com/circuitpython-display-support-using-displayio/display-and-display-bus
display = board.DISPLAY

w2 = int(display.width / 2)
h2 = int(display.height / 2)

WHITE = 0xFFFFFF
RED = 0xFF0000
GREEN = 0x00FF00
BLUE = 0x0000FF

# Make the display context
group = displayio.Group()
display.root_group = group

# little circle in the center of all arcs
circle = Circle(w2, h2, 5, fill=0x00FF00)
group.append(circle)

# red arc , 10 pixels wide
arc1 = Arc(
    x=w2,
    y=h2,
    radius=min(display.width, display.height) / 4,
    angle=90,
    direction=90,
    segments=20,
    arc_width=10,
    fill=RED,
)
group.append(arc1)

# blue arc (or pie)
arc2 = Arc(
    x=w2,
    y=h2,
    radius=min(display.width, display.height) / 6,
    angle=90,
    direction=0,
    segments=10,
    arc_width=min(display.width, display.height) / 6 - 5,
    outline=BLUE,
)
group.append(arc2)

while True:
    for i in range(360 // 40 + 1):
        arc1.angle = i * 40
        arc2.direction = i * 40
        time.sleep(0.05)
        print(len(arc2))
