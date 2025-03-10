import board
import digitalio
import rotaryio
import displayio
import terminalio
import busio
import adafruit_display_text.label
import adafruit_displayio_ssd1306
import neopixel
import time
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.scanners.keypad import MatrixScanner
from kmk.extensions.peg_oled_display import Oled,OledDisplayMode,OledData

keyboard = KMKKeyboard()

i2c = busio.I2C(board.SCL, board.SDA)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

oled_label = adafruit_display_text.label.Label(terminalio.FONT, text='Krishveer OSU_Pad', x=10, y=10)
splash = displayio.Group()
splash.append(oled_label)
display.show(splash)

keyboard.modules.append(EncoderHandler())

keyboard.matrix = MatrixScanner(
    column_pins=[board.D6, board.D7, board.D0],
    row_pins=[board.D1, board.D2],
    columns_to_anodes=True,
)

encoder = rotaryio.IncrementalEncoder(board.D8, board.D9)
encoder_switch = digitalio.DigitalInOut(board.D3)
encoder_switch.direction = digitalio.Direction.INPUT
encoder_switch.pull = digitalio.Pull.UP

num_pixels = 16
pixels = neopixel.NeoPixel(board.D10, num_pixels, brightness=0.3, auto_write=False)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def wheel(pos):
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

def update_encoder():
    last_position = encoder.position
    while True:
        current_position = encoder.position
        if current_position > last_position:
            keyboard.tap_key(KC.VOLU)
        elif current_position < last_position:
            keyboard.tap_key(KC.VOLD)
        if not encoder_switch.value:
            keyboard.tap_key(KC.MUTE)
        last_position = current_position

keyboard.keymap = [
    [KC.COPY, KC.PASTE, KC.ENTER],
    [KC.ESC, KC.TAB, KC.SPACE],
]

keyboard.before_matrix_scan = update_encoder

while True:
    rainbow_cycle(0.05)

keyboard.go()
