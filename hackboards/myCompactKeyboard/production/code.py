from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.modules.split import Split, SplitType
from kmk.modules.encoder import EncoderHandler
from kmk.modules.rgb import RGB
from kmk.modules.display import OledDisplay
import board
import digitalio
import neopixel
import adafruit_ssd1306

keyboard = KMKKeyboard()

# Configurar la matriz de teclas
keyboard.matrix = MatrixScanner(
    rows=[board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9],
    columns=[board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP26, board.GP27],
    diode_orientation=MatrixScanner.DIODE_COL2ROW
)

# Configurar la pantalla OLED
WIDTH = 128
HEIGHT = 32
counter = 0

i2c = board.I2C()
display = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
display.fill(0)
display.show()

def update_oled():
    display.fill(0)
    display.text(f'Counter: {counter}', 0, 0, 1)
    display.show()

# Configurar los LEDs RGB
NUM_LEDS = 96
pixels = neopixel.NeoPixel(board.GP22, NUM_LEDS, auto_write=False)
pixels.fill((0, 0, 0))
pixels.show()

def blink_led():
    led_index = counter % NUM_LEDS
    pixels[led_index] = (255, 255, 255)
    pixels.show()
    time.sleep(0.1)
    pixels[led_index] = (0, 0, 0)
    pixels.show()

# Configurar encoders
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

def rotary_callback(position, direction):
    global counter
    if direction == 1:
        counter += 1
        update_oled()
        blink_led()
    elif direction == -1:
        counter = max(0, counter - 1)
        update_oled()
        blink_led()

encoder_handler.pins = [(board.GP0, board.GP28), (board.GP28, board.GP1)]
encoder_handler.callbacks = [rotary_callback, rotary_callback]

# Definir las capas del teclado
keyboard.keymap = [
    [KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12],
    [KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL],
    [KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC],
    [KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.BSLS],
    [KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.NO],
    [KC.GRV, KC.SPC, KC.RALT, KC.APP, KC.LCTL, KC.HOME, KC.END, KC.ESC, KC.NO, KC.NO, KC.NO, KC.NO],
    [KC.TAB, KC.SPC, KC.FN, KC.LALT, KC.NO, KC.UP, KC.NO, KC.LEFT, KC.PSCR, KC.PGUP, KC.NO, KC.NO],
    [KC.CAPS, KC.LSFT, KC.LCTL, KC.LGUI, KC.LEFT, KC.DOWN, KC.RIGHT, KC.ENTER, KC.DEL, KC.PGDN, KC.NO, KC.NO]
]

keyboard.go()
