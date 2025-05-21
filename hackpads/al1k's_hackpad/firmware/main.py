import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here according to the schematic
PINS = [board.D0, board.D1, board.D2, board.D3, board.D4, board.D5]  # GPIO26, GPIO27, GPIO28, GPIO29, GPIO7, GPIO0

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,  # Buttons pull to GND when pressed (LOW)
)

# Define the buttons corresponding to the pins (SW1 to SW6) with media controls
keyboard.keymap = [
    [
        KC.VOLD,  # SW1: Volume Down
        KC.MUTE,  # SW2: Mute
        KC.VOLU,  # SW3: Volume Up
        KC.MRWD,  # SW4: Previous Song
        KC.MPLY,  # SW5: Play/Pause
        KC.MFFD,  # SW6: Next Song
    ]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
