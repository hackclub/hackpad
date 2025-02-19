import board
import neopixel
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

# Define the pins for your buttons
PINS = [board.GPIO1, board.GPIO2, board.GPIO4]  # SW1, SW2, SW3

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Define the keymap with Copy, Paste, and Save
keyboard.keymap = [
    [
        KC.MACRO(Press(KC.LCMD), Tap(KC.C), Release(KC.LCMD)),  # Copy (SW1)
        KC.MACRO(Press(KC.LCMD), Tap(KC.V), Release(KC.LCMD)),  # Paste (SW2)
        KC.MACRO(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)),  # Save (SW3)
    ]
]

# LED control
led_pin = board.GPIO6  # Data line for the LEDs
num_leds = 7  # Number of LEDs
pixels = neopixel.NeoPixel(led_pin, num_leds, brightness=0.5)

# Set LEDs to white
pixels.fill((255, 255, 255))
pixels.show()

if __name__ == '__main__':
    keyboard.go()