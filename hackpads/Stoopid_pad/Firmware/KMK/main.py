from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.mcp23017 import MCP23017
from kmk.extensions.ssd1306_oled import SSD1306_OLED
import board

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D3, board.D4, board.D2, board.D1, board.D5, board.D6]

io_expander = MCP23017()
io_expander.pins = (0, 1)  
keyboard.extensions.append(io_expander)

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Rotary encoder setup
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

def encoder_clockwise():
    return KC.VOLU  

def encoder_counterclockwise():
    return KC.VOLD  

encoder_handler.pins = ((board.D7, board.D8),)  
encoder_handler.map = [(encoder_clockwise, encoder_counterclockwise)]

oled = SSD1306_OLED(i2c_bus=board.I2C(), width=128, height=32, rotation=0)
keyboard.extensions.append(oled)

def update_oled():
    oled.clear()
    oled.text("Stupid Stuff", 0, 0)
    oled.text("Goes Here :3", 0, 10)

    oled.show()

keyboard.before_matrix_scan = update_oled

keyboard.keymap = [
    [
        KC.A, KC.B,  
        KC.E, KC.SEMICOLON, KC.MINUS
        KC.G, KC.EQUAL, KC.P
    ]
]

# Start KMK!
if __name__ == '__main__':
    keyboard.go()
