import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB

print(dir(board))

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP5, board.GP6)
keyboard.row_pins = (board.GP7, board.GP8)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

rgb = RGB(pixel_pin=board.GP4, num_pixels=2)
keyboard.extensions.append(rgb)

keyboard.keymap = [ 
    [
        KC.D, KC.U,      
        KC.C, KC.K, 
    ]
]


if __name__ == '__main__':
    keyboard.go()
