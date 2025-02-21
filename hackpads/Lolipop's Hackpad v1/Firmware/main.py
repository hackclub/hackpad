#Lolipop's Hackpad firmware
# Note that i will certainly update this code once i get the hardware, as rn i can't test it and 
# its hard to project myself on the features and the code that will be in this without the actual hackpad in front of me


# You import all the IOs of your board
import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.rgb import RGB
import adafruit_ssd1306
from adafruit_display_text import label
import terminalio

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Add a changing hue RGB light to pin D4
rgb = RGB(pixel_pin=board.D4, num_pixels=1, val_limit=255, hue_default=0)
keyboard.modules.append(rgb)

# Define your pins here!
PINS = [board.D0, board.D1, board.D2, board.D3, board.D7, board.D8, board.D9, board.D10]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [
        KC.LCTRL(KC.C),  # Copy
        KC.LCTRL(KC.V),  # Paste
        KC.LCTRL(KC.X),  # Cut
        KC.LCTRL(KC.Z),  # Undo
        KC.LCTRL(KC.Y),  # Redo
        KC.LALT(KC.F4),  # Alt + F4 (Close window)
        KC.LWIN(KC.D),  # Win + D (Show desktop)
        KC.LWIN(KC.L),  # Win + L (Lock screen)
    ]
]

# Initialize I2C interface for OLED display
i2c = busio.I2C(board.D5, board.D6)

# Initialize the OLED display
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear the display
oled.fill(0)
oled.show()

# Display "Hello, World!" on the OLED
oled.text("Hello, World!", 0, 15, 1)
oled.show()

# Start kmk!
if __name__ == '__main__':
    keyboard.go()