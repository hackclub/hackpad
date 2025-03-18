import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.layers import Layers
from kmk.extensions.display import Display, SSD1306, TextEntry, ImageEntry


i2c_bus = busio.I2C(board.GP21, board.GP20)
display_driver = SSD1306(
    i2c=i2c_bus,
    # Optional device_addres argument. Default is 0x3C.
    # device_address=0x3C,
)

display = Display(
    display=display_driver,
    entries=[
        TextEntry(text='Layer: ', x=0, y=32, y_anchor='B'),
        TextEntry(text='BASE', x=40, y=32, y_anchor='B', layer=0),
    ],
    height=64,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=1,
)

keyboard = KMKKeyboard()
layers = Layers()
encoder_handler = EncoderHandler()
keyboard.modules.append(layers)
keyboard.modules.append(encoder_handler)
keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(display)

# Define matrix pins based on the schematic, using GP pins
keyboard.col_pins = (board.GP0, board.GP1, board.GP2)  # COLUMN_1, COLUMN_2, COLUMN_3
keyboard.row_pins = (board.GP3, board.GP4, board.GP5)  # ROW_A, ROW_B, ROW_C
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Custom key sequences (as before)
OPEN_VSCODE = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("code"), KC.ENTER))
OPEN_CURRENT_FOLDER = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("code ."), KC.ENTER))
OPEN_GITHUB = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("https://github.com"), KC.ENTER))
OPEN_SLACK = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("slack"), KC.ENTER))
OPEN_DISCORD = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("discord"), KC.ENTER))
OPEN_BRAVE = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("brave"), KC.ENTER))
OPEN_CHROME = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("chrome"), KC.ENTER))
SHUTDOWN = simple_key_sequence((KC.LGUI(KC.X), KC.U, KC.U))  # Windows shutdown sequence

# Define keymap
keyboard.keymap = [
    [
        OPEN_VSCODE,        OPEN_CURRENT_FOLDER, OPEN_GITHUB,
        OPEN_SLACK,         OPEN_DISCORD,        KC.LOCK,
        OPEN_BRAVE,         OPEN_CHROME,         SHUTDOWN
    ]
]

# Configure encoder based on the schematic, using GP pins
encoder_handler.pins = ((board.GP6, board.GP7, board.GP8),)  # ENCA, ENCB, ENC_SWITCH
# Encoder map
encoder_handler.map = [(
    (KC.VOLU, KC.VOLD),
    KC.MUTE  # This will be triggered when the encoder is pressed
)]

if __name__ == '__main__':
    keyboard.go()