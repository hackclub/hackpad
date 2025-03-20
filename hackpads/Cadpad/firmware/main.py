import board
import neopixel
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.extensions.hid import HID

kb = KMKKeyboard()
kb.modules.append(Macros())
kb.extensions.append(HID())
leds = neopixel.NeoPixel(board.GP3, 3, brightness=0.3)

pins = [board.GP26, board.GP27, board.GP28, board.GP29, board.GP6, board.GP7]
kb.matrix = KeysScanner(pins=pins, value_when_pressed=False)

def set_led(i, color):
    leds[i] = color

def on_press(key):
    colors = {KC.Q: (255, 0, 0), KC.W: (0, 255, 0), KC.E: (0, 0, 255)}
    if key in colors:
        set_led(list(colors.keys()).index(key), colors[key])

def on_release(_):
    for i in range(3):
        set_led(i, (0, 0, 0))

kb.keymap = [[KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y]]

if __name__ == '__main__':
    kb.go()
