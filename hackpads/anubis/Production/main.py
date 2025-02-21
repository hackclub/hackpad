from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.mcp23017 import MCP23017

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP3, board.GP4, board.GP2)
keyboard.row_pins = (board.GP26, board.GP27, board.GP28, board.GP29)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

mcp = MCP23017(i2c=board.I2C(), address=0x20)

direct_key_1 = KC.LCMD(KC.SPACE)
direct_key_2 = KC.LCMD(KC.TAB)

keyboard.keymap = [
    [KC.LCMD(KC.N), KC.LCMD(KC.W), KC.LCMD(KC.T)],
    [KC.LCMD(KC.F), KC.LCMD(KC.S), KC.LCMD(KC.Z)],
    [KC.LCMD(KC.X), KC.LCMD(KC.C), KC.LCMD(KC.V)],
    [KC.LCMD(KC.SPC), KC.LCMD(KC.BSPC), KC.LCMD(KC.RET)],
]

keyboard.direct_wired_keys = {
    mcp.gpio[0]: direct_key_1,
    mcp.gpio[1]: direct_key_2,
}

if __name__ == '__main__':
    keyboard.go()
