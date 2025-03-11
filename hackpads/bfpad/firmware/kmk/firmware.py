import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.RGB import RGB

keyboard = KMKKeyboard()

encoder = EncoderHandler()
encoder_handler.pins = ((board.SCK, board.RX, None,),)
encoder_handler.map = [((KC.VOLD, KC.VOLU, KC.NO,),)]
keyboard.modules.append(encoder)

i2c_bus = busio.I2C(board.SCL, board.SDA)
display_driver = SSD1306(i2c=i2c_bus)
display = Display(display=display_driver)
display.entries = [
	ImageEntry(image="pfptiny.bmp", x=0, y=0),
	TextEntry(text="bfpad", x=40, y=16, y_anchor="M")
]
keyboard.extensions.append(display)

rgb = RGB(pixel_pin = board.TX, num_pixels=11)
keyboard.extensions.append(rgb)

keyboard.col_pins = (board.MOSI, board.A0, board.MISO)
keyboard.row_pins = (board.A3, board.A2, board.A1)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.keymap = [
    [[KC.RABK, KC.DOT, KC.COMMA], [KC.LABK, KC.PLUS, KC.LBRACKET], [KC.MINUS, KC.MUTE, KC.RBRACKET]]
]

if __name__ == '__main__':
    keyboard.go()