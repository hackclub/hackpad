import board
import busio
import displayio
import terminalio
import neopixel
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from adafruit_display_text import label
from adafruit_displayio_ssd1306 import SSD1306

# D0: Switch@Rotary encoder
# D1: Rotary-Encoder output A
# D3: Rotary-Encoder output B
# D4: Display SDA
# D5: Display SCL
# D7: Switch 1
# D8: Switch 2
# D9: Switch 3
# D10: Switch 4

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D7, board.D8, board.D9, board.D10)  # SW1-SW4
keyboard.row_pins = ()

pixels = neopixel.NeoPixel(board.D6)
pixels.fill(255,255,255)
pixels.show()

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.D1, board.D2, board.D0),)  # A, B, Switch
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD), KC.MUTE)
]
keyboard.keymap = [
    [KC.N1, KC.N2, KC.N3, KC.N4]
]

displayio.release_displays()
i2c = busio.I2C(board.D5, board.D4)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = SSD1306(display_bus, width=128, height=64)

splash = displayio.Group()
text_area = label.Label(terminalio.FONT, text="Keyboard", color=0xFFFFFF, x=10, y=10)
splash.append(text_area)
display.show(splash)

def update_display(message):
    text_area.text = message
    display.show(splash)

def on_keypress(key):
    update_display(f"Pressed: {key.name}")

keyboard.pressed_callbacks.append(on_keypress)

if __name__ == '__main__':
    keyboard.go()
