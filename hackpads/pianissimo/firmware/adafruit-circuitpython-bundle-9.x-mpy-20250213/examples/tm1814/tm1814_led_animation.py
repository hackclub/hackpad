# SPDX-FileCopyrightText: Copyright (c) 2024 Jeff Epler for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

import board
import rainbowio
import supervisor
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.sequence import AnimationSequence

from adafruit_tm1814 import TM1814PixelBackground

# The pin where the LED strip data line is connected
TM1814 = board.A0
# The number of TM1814 controllers. Note that sometimes one "pixel" controls
# more than one LED package.
#
# One common configuration is 3 LED packages & 1 controller per 50mm, giving
# 100 TM1814 controllers (300 LED packages) in 5 meters of LED strip.
NUM_PIXELS = 100
pixels = TM1814PixelBackground(TM1814, NUM_PIXELS, brightness=0.1)

# Perform a rainbow animation sequence
rainbow = Rainbow(pixels, speed=0.1, period=2)
rainbow_chase = RainbowChase(pixels, speed=0.1, size=5, spacing=3)
rainbow_comet = RainbowComet(pixels, speed=0.1, tail_length=7, bounce=True)
rainbow_sparkle = RainbowSparkle(pixels, speed=0.1, num_sparkles=15)


animations = AnimationSequence(
    rainbow,
    rainbow_chase,
    rainbow_comet,
    rainbow_sparkle,
    advance_interval=5,
    auto_clear=True,
)

while True:
    animations.animate()
