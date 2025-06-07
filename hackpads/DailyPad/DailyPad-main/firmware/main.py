# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D3, board.D4, board.D2, board.D1]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Define macros to type (and “Enter”) each URL
# KC.MACRO sends a sequence of characters, including newline (\n) for “Enter” :contentReference[oaicite:0]{index=0}
ONSHAPE = KC.MACRO("https://www.onshape.com\n")
RUSSIAN_MATH = KC.MACRO("https://student.russianmath.com\n")
DISCORD = KC.MACRO("https://discord.com\n")
GOOGLE_CLASSROOM = KC.MACRO("https://classroom.google.com\n")

# Here you define the buttons corresponding to the pins
keyboard.keymap = [
    [ONSHAPE, RUSSIAN_MATH, DISCORD, GOOGLE_CLASSROOM]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
