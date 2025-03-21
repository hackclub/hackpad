from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.handlers.stock import simple_key_sequence
from kmk.modules.encoder import EncoderHandler
from kmk.modules.rgb import RGB
import board
import digitalio
import neopixel
import busio
import adafruit_ssd1306
from kmk.keys import KC

keyboard = KMKKeyboard()

keyboard.matrix = MatrixScanner(
    columns=(board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, 
             board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19),
    rows=(board.GP0, board.GP1, board.GP2, board.GP3, board.GP4),
)

i2c = busio.I2C(board.GP20, board.GP21)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
display.fill(0)
display.text("Hello", 40, 10, 1)
display.show()

num_pixels = 83
pixels = neopixel.NeoPixel(board.GP22, num_pixels, brightness=0.3, auto_write=False)

def rainbow_cycle(wait):
    for j in range(256):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()

def wheel(pos):
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

rainbow_cycle(0.01)

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

def mute_toggle():
    keyboard.send_key_sequence(simple_key_sequence("MUTE"))

encoder_handler.pins = ((board.GP26, board.GP27, board.GP28),)
encoder_handler.tap_time = 150
encoder_handler.set_encoder_switch_handler(0, mute_toggle)

keyboard.keymap = [
    [KC.ESC, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSPC],
    [KC.TAB, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.ENTER],
    [KC.LSHIFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.RSHIFT],
    [KC.LCTRL, KC.LALT, KC.SPACE, KC.RALT, KC.RCTRL]
]

if __name__ == "__main__":
    keyboard.go()
