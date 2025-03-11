import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

keyboard.col_pins = (board.GP21, board.GP20, board.GP19, board.GP18)
keyboard.row_pins = (board.GP22, board.GP23, board.GP24, board.GP25)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
  # This is TBD, will figure out when I get the actual thing
]

if __name__ == '__main__':
    keyboard.go()
