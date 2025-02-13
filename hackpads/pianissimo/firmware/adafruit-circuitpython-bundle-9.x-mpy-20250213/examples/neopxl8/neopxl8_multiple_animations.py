# SPDX-FileCopyrightText: 2024 Tim Cocks
#
# SPDX-License-Identifier: Unlicense

import board
import adafruit_ticks
from adafruit_led_animation.animation.sparklepulse import SparklePulse
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.group import AnimationGroup
from adafruit_led_animation.helper import PixelMap
from adafruit_led_animation.color import PURPLE, WHITE, AMBER, JADE
from adafruit_neopxl8 import NeoPxl8

# Customize for your strands here
num_strands = 8
strand_length = 30
first_led_pin = board.NEOPIXEL0

num_pixels = num_strands * strand_length

# Make the object to control the pixels
pixels = NeoPxl8(
    first_led_pin,
    num_pixels,
    num_strands=num_strands,
    auto_write=False,
    brightness=0.1,
)


def strand(n):
    return PixelMap(
        pixels,
        range(n * strand_length, (n + 1) * strand_length),
        individual_pixels=True,
    )


# Create the 8 virtual strands
strands = [strand(i) for i in range(num_strands)]

# For each strand, create a comet animation of a different color
animations = [
    Comet(strands[0], speed=0.01, color=PURPLE, tail_length=10, bounce=True),
    Chase(strands[1], speed=0.1, size=3, spacing=6, color=WHITE),
    Pulse(strands[2], speed=0.1, period=3, color=AMBER),
    Sparkle(strands[3], speed=0.1, color=PURPLE, num_sparkles=10),
    SparklePulse(strands[4], speed=0.1, period=3, color=JADE),
    RainbowComet(strands[5], speed=0.1, tail_length=7, bounce=True),
    RainbowChase(strands[6], speed=0.1, size=3, spacing=2, step=8),
    RainbowSparkle(strands[7], speed=0.1, num_sparkles=15),
]

# Group them so we can run them all at once
animations = AnimationGroup(*animations)

# Run the animations and report on the speed in frame per second
t0 = adafruit_ticks.ticks_ms()
frame_count = 0
while True:
    animations.animate()
    frame_count += 1
    t1 = adafruit_ticks.ticks_ms()
    dt = adafruit_ticks.ticks_diff(t1, t0)
    if dt > 1000:
        print(f"{frame_count * 1000/dt:.1f}fps")
        t0 = t1
        frame_count = 0
