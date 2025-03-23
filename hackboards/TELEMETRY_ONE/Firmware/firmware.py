import board
import digitalio
import time
from adafruit_matrixkeypad import Matrix_Keypad
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

rows = [board.GP8, board.GP7, board.GP6, board.GP5, board.GP4, board.GP15]
cols = [board.GP13, board.GP14, board.GP12, board.GP0, board.GP22, board.GP21, board.GP20, board.GP19, board.GP18, board.GP17, board.GP16, board.GP10, board.GP11, board.GP9, board.GP2]

row_pins = [digitalio.DigitalInOut(pin) for pin in rows]
column_pins = [digitalio.DigitalInOut(pin) for pin in cols]

keypad = Matrix_Keypad(row_pins, column_pins)

keyboard = Keyboard()

keymap = [
    [Keycode.ESC, Keycode.F1, Keycode.F2, Keycode.F3, Keycode.F4, Keycode.F5, Keycode.F6, Keycode.F7, Keycode.F8, Keycode.F9, Keycode.F10, Keycode.F11, Keycode.F12],
    [Keycode.GRAVE_ACCENT, Keycode.NUMBER_1, Keycode.NUMBER_2, Keycode.NUMBER_3, Keycode.NUMBER_4, Keycode.NUMBER_5, Keycode.NUMBER_6, Keycode.NUMBER_7, Keycode.NUMBER_8, Keycode.NUMBER_9, Keycode.NUMBER_0, Keycode.MINUS, Keycode.EQUALS, Keycode.BACKSPACE, Keycode.DELETE],
    [Keycode.TAB, Keycode.Q, Keycode.W, Keycode.E, Keycode.R, Keycode.T, Keycode.Y, Keycode.U, Keycode.I, Keycode.O, Keycode.P, Keycode.LEFT_BRACKET, Keycode.RIGHT_BRACKET, Keycode.BACKSLASH, Keycode.PAGE_UP],
    [Keycode.CAPS_LOCK, Keycode.A, Keycode.S, Keycode.D, Keycode.F, Keycode.G, Keycode.H, Keycode.J, Keycode.K, Keycode.L, Keycode.SEMICOLON, Keycode.QUOTE, None, Keycode.ENTER, Keycode.PAGE_DOWN],
    [Keycode.LEFT_SHIFT, None, Keycode.Z, Keycode.X, Keycode.C, Keycode.V, Keycode.B, Keycode.N, Keycode.M, Keycode.COMMA, Keycode.PERIOD, Keycode.FORWARD_SLASH, Keycode.RIGHT_SHIFT, Keycode.UP_ARROW, None],
    [Keycode.LEFT_CONTROL, Keycode.APPLICATION, Keycode.LEFT_ALT, None, None, None, Keycode.SPACE, None, None, None, Keycode.RIGHT_ALT, None, Keycode.LEFT_ARROW, Keycode.DOWN_ARROW, Keycode.RIGHT_ARROW]
]

while True:
    keys = keypad.pressed_keys
    if keys:
        for key in keys:
            for row in range(len(rows)):
                for col in range(len(cols)):
                    if keypad.keypad[row][col] == key:
                        keycode = keymap[row][col]
                        if keycode is not None:
                            keyboard.press(keycode)
                        break
            time.sleep(0.1) 
        keyboard.release_all()
    time.sleep(0.05)
