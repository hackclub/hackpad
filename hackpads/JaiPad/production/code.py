from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

layers_ext = Layers()
keyboard.modules.append(layers_ext)

keyboard.row_pins = (board.D4, board.D5, board.D6)  
keyboard.col_pins = (board.D8, board.D1, board.D2, board.D3)  

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [  
        KC.A, KC.B, KC.C, KC.D,
        KC.E, KC.F, KC.G, KC.H,
        KC.I, KC.J, KC.K, KC.L,
    ]
]

if __name__ == '__main__':
    keyboard.go()
