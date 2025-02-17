# SPDX-FileCopyrightText: Copyright (c) 2024 Jeff Epler for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

import board
import rainbowio
import supervisor

from adafruit_tm1814 import TM1814PixelBackground

# The pin where the LED strip data line is connected
TM1814 = board.A0
# The number of TM1814 controllers. Note that sometimes one "pixel" controls
# more than one LED package.
#
# One common configuration is 3 LED packages & 1
# controller per 50mm, giving 100 TM1814 controllers (300 LED packages) in 5
# meters of LED strip.
NUM_PIXELS = 100
pixels = TM1814PixelBackground(TM1814, NUM_PIXELS, brightness=0.1)

# Cycle the rainbow at about 1 cycle every 4 seconds
while True:
    pixels.fill(rainbowio.colorwheel(supervisor.ticks_ms() // 16))
