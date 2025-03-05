import board
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.col_pins = (board.D1, board.D2, board.D3)  
keyboard.row_pins = (board.D4, board.D5, board.D6)  

keyboard.keymap = [ [KC.Q, KC.W, KC.E, KC.A, KC.S, KC.D, KC.Z, KC.X, KC.C] ]

encoder_handler = EncoderHandler()
encoder_handler.pins = (board.D7, board.D8)
encoder_handler.map = [((KC.VOLU, KC.VOLD),)] 

keyboard.modules.append(encoder_handler)

if __name__ == '__main__':
    keyboard.go()