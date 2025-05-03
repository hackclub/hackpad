import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)


encoder_handler.pins = ((board.GPIO4_D9_MISO, board.GPIO3_D10_MOSI, board.GPIO2_D8_SCK, True),)  # True enables push switch


keyboard.col_pins = (board.GPIO26_A0_D0, board.GPIO27_A1_D1, board.GPIO28_A2_D2, board.GPIO29_A3_D3)
keyboard.row_pins = (board.GPIO4_D4_SDA, board.GPIO5_D5_SCL, board.GPIO6_D6_TX, board.GPIO7_D7_CS)
keyboard.diode_orientation = DiodeOrientation.ROW2COL


keyboard.keymap = [
    [
        
        KC.N1,    KC.N2,
        KC.N3,    KC.N4,    KC.N5,     KC.N6,
        KC.N7,    KC.N8,    KC.N9,     KC.N0,
        KC.A,     KC.B,
    ]
]

encoder_handler.map = [(
    ((KC.VOLU, KC.VOLD), KC.MUTE),  
)]

if __name__ == '__main__':
    keyboard.go()
