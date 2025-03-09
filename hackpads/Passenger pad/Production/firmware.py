import board
import time
import busio
import displayio
from adafruit_displayio_ssd1306 import SSD1306
from adafruit_display_text import label
import terminalio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()


keys = [board.D0, board.D1, board.D2, board.D3, board.D4, board.D5, board.D6, board.D7]
enc_pins = (board.D8, board.D9)
enc_btn = board.D10

keyboard.matrix = KeysScanner(pins=keys, value_when_pressed=False)
keyboard.keymap = [[KC.A, KC.B, KC.C, KC.D, KC.E, KC.F, KC.G, KC.H]]

encoder = EncoderHandler()
encoder.pins = enc_pins
encoder.map = [KC.VOLD, KC.VOLU]
keyboard.modules.append(encoder)

keyboard.gpio_to_keycodes.update({enc_btn: KC.ENTER})


displayio.release_displays()
i2c = busio.I2C(board.SCL, board.SDA)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = SSD1306(display_bus, width=128, height=32)


splash = displayio.Group()
text_area = label.Label(terminalio.FONT, text="MacroPad Ready", x=10, y=15)
splash.append(text_area)
display.show(splash)


while True:
    keyboard.update()
    
    
    pressed_keys = [kc.name for row in keyboard.keymap for kc in row if kc.pressed]
    text_area.text = f"Keys: {' '.join(pressed_keys)}" if pressed_keys else "Waiting..."
    
    time.sleep(0.01)
