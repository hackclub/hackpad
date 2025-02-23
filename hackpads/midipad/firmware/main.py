import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

keyboard.col_pins = (board.GP26, board.GP27, board.GP28, board.GP29)
keyboard.row_pins = (board.GP1, board.GP2, board.GP4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# TODO: rotary encoder pins

keyboard.keymap = [
    # WIP: Will output MIDI instead of typing
]

if __name__ == '__main__':
    keyboard.go()
