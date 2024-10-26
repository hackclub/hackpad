print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.handlers.sequences import send_string

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0, board.GP1, board.GP2)
keyboard.row_pins = (board.GP3, board.GP4, board.GP5)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.MOD(KC.LCMD, KC.T), send_string("https://classroom.google.com/"), KC.ENTER], [KC.MOD(KC.LCMD, KC.T), send_string("https://discord.com/channels/1234637010753294388/1234637014603665456"), KC.ENTER], [KC.MOD(KC.LCMD, KC.T), send_string("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox"), KC.ENTER],
    [KC.MOD(KC.LCMD, KC.T), send_string("https://drive.google.com/drive/u/0/home"), KC.ENTER], [KC.MOD(KC.LCMD, KC.T), send_string("https://millburn.powerschool.com/guardian/home.html"), KC.ENTER], [KC.MOD(KC.LCMD, KC.T), send_string("https://fusion.online.autodesk.com"), KC.ENTER],
]

if __name__ == '__main__':
    keyboard.go()
