import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.modtap import ModTap
from adafruit_display_text import label
import adafruit_ssd1306
import busio

keyboard = KMKKeyboard()

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

col_pins = [board.D0, board.D1]
row_pins = [board.D2, board.D3, board.D4]

keyboard.col_pins = col_pins
keyboard.row_pins = row_pins
keyboard.diode_orientation = DiodeOrientation.COL2ROW

i2c = busio.I2C(board.GPIO07, board.GPIO06)
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
current_volume = 50

encoder_handler.pins = ((board.A, board.B, None, False),
                       (board.C, board.D, None, False))

encoder_handler.map = [ 
    ((KC.VOLU, KC.VOLD), (KC.VOLU, KC.VOLD))
]

def update_oled():
    oled.fill(0)
    text = f"Volume: {current_volume}%"
    text_area = label.Label(terminalio.FONT, text=text, x=0, y=15)
    oled.show()

keyboard.keymap = [
    [
        KC.N0, KC.N1, 
        KC.N2, KC.N3,
        KC.N4, KC.N5,  
    ]
]

def on_encoder_update(keyboard, encoder_id, state):
    global current_volume
    if state:
        current_volume = min(100, current_volume + 5)
    else:
        current_volume = max(0, current_volume - 5)
    update_oled()

encoder_handler.on_move = on_encoder_update

if __name__ == '__main__':
    update_oled()
    keyboard.go()