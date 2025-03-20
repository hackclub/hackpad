# Goofy mcp23017 reading
    # See https://github.com/KMKfw/kmk_firmware/blob/74fa1fb52e41b95c1df9047e1ffff39001bb67e6/user_keymaps/dzervas/lab68.py for 

    # Also https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/scanners.md/

import board

import busio
from digitalio import DigitalInOut, Direction, Pull

from adafruit_mcp230xx.mcp23017 import MCP23017

from kmk.hid import HIDModes
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation

from kmk.scanners.digitalio import MatrixScanner
from kmk.scanners.encoder import RotaryioEncoder

from kmk.modules.macros import Macros
from kmk.modules.macros import Press, Release, Tap

# https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/rgb.md

from kmk.extensions.RGB import RGB


import displayio
import adafruit_displayio_ssd1306
import terminalio
from adafruit_display_text import label

displayio.release_displays()

i2c = busio.I2C(scl = board.SCL, sda = board.SDA)

mcp = MCP23017(i2c, address=0x20)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)

#TODO: less boring OLED
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

root = displayio.Group()
display.root_group = root

text = "I'm Jankpad!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=20, y=10)
root.append(text_area)

class JankBoard(KMKKeyboard):
    def __init__(self, mcp):
        self.mcp = mcp

        for i in range(8):
            p = mcp.get_pin(i)
            if (i < 4):
                p.direction = Direction.INPUT
            else:
                p.direction = Direction.OUTPUT
            p.pull = Pull.UP


        self.matrix = [
            MatrixScanner(cols = [mcp.get_pin(i) for i in range(4, 8)],
                          rows = [mcp.get_pin(i) for i in range(4)],
                          diode_orientation = DiodeOrientation.COL2ROW,
                          pull = Pull.UP
            ),
            RotaryioEncoder(
                pin_a=board.A1,
                pin_b=board.A0
            ),
            RotaryioEncoder(
                pin_a=board.A3,
                pin_b=board.A4
            )
        ]

jank = JankBoard(mcp)

#TODO: more rgb set up

rgb = RGB(pixel_pin = board.D10, num_pixels=16)
jank.extensions.append(rgb)

def ctl(k):
    return KC.MACRO(Press(KC.LCTL), Tap(k), Release(KC.LCTL))

# tiling window manager shortcuts
def move(k):
    return KC.MACRO(Press(KC.LGUI), Tap(k), Release(KC.LGUI))

def shift(k):
    return KC.MACRO(Press(KC.LSHIFT), Press(KC.LGUI), Tap(k), Release(KC.LGUI), Release(KC.LSHIFT))


jank.keymap = [
    [KC.ESCAPE, ctl(KC.X), ctl(KC.C), ctl(KC.V),
     move(KC.H), move(KC.J), move(KC.K), move(KC.L),
     shift(KC.H), shift(KC.J), shift(KC.K), shift(KC.L),
     KC.H, KC.J, KC.K, KC.L,
     KC.UP, KC.DOWN,    #first encoder
     KC.LEFT, KC.RIGHT  #second encoder
     ]
]

if __name__ == '__main__':
    jank.go()
