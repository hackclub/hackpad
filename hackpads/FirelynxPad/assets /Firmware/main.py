import board
import busio
import digitalio
import rotaryio
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_displayio_ssd1306 import SSD1306
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.matrix import MatrixScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.handlers.sequences import send_string

# Initialize keyboard
keyboard = KMKKeyboard()

# Define key matrix
keyboard.matrix = MatrixScanner(
    rows=[board.D0, board.D6, board.D7],
    columns=[board.D1, board.D2, board.D3],
    diode_orientation=MatrixScanner.DIODE_COL2ROW
)

# Rotary Encoder Setup
encoder = rotaryio.IncrementalEncoder(board.D8, board.D9)
encoder_button = digitalio.DigitalInOut(board.D10)
encoder_button.direction = digitalio.Direction.INPUT
encoder_button.pull = digitalio.Pull.UP

# OLED Display Setup
displayio.release_displays()
i2c = busio.I2C(board.SCL, board.SDA)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = SSD1306(display_bus, width=128, height=32)
splash = displayio.Group()
display.show(splash)

# Text label for OLED
oled_text = label.Label(terminalio.FONT, text="", color=0xFFFF, x=5, y=15)
splash.append(oled_text)

def update_oled(text):
    oled_text.text = text
    display.show(splash)

# Define keymap
keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D, KC.E, KC.F, KC.G, KC.H, KC.I]
]

# Add Macros module
macros = Macros()
keyboard.modules.append(macros)

# Rotary Encoder Handling
last_position = encoder.position
def encoder_task():
    global last_position
    position = encoder.position
    if position > last_position:
        keyboard.tap_key(KC.VOLU)  # Volume Up
    elif position < last_position:
        keyboard.tap_key(KC.VOLD)  # Volume Down
    last_position = position

    # Handle encoder button
    if not encoder_button.value:
        keyboard.tap_key(KC.MUTE)

# Keyboard loop
if __name__ == '__main__':
    while True:
        encoder_task()
        update_oled("Macropad Active")
        keyboard.go()
