import board
from adafruit_mcp230xx.mcp23017 import MCP23017_SO
import busio
import digitalio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler

i2c = busio.I2C(board.GP13, board.GP12)
mcp = MCP23017_SO(i2c)

row3_pin = mcp.get_pin(9)
row4_pin = mcp.get_pin(8)
row3_pin.direction = digitalio.Direction.OUTPUT
row4_pin.direction = digitalio.Direction.OUTPUT

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())
layers = Layers()
keyboard.modules.append(layers)
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

keyboard.col_pins = (board.GP16,board.GP17,board.GP18,board.GP19,board.GP20,board.GP21,board.GP22,board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,board.GP5,board.GP6)
keyboard.row_pins = (board.GP10,board.GP11,row3_pin,row4_pin,board.GP14,board.GP15)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

encoder_a = mcp.get_pin(11)
encoder_b = mcp.get_pin(12)
encoder_s1 = mcp.get_pin(13)
encoder_a.direction = digitalio.Direction.INPUT
encoder_b.direction = digitalio.Direction.INPUT
encoder_s1.direction = digitalio.Direction.INPUT
encoder_a.pull = digitalio.Pull.UP
encoder_b.pull = digitalio.Pull.UP
encoder_s1.pull = digitalio.Pull.UP
encoder_handler.pins = ((encoder_a, encoder_b, encoder_s1),)

encoder_handler.map = [
    ((KC.VOLU, KC.VOLD, KC.MUTE),), 
    ((KC.RIGHT, KC.LEFT, KC.ENTER),),
]

FN = KC.MO(1)

keyboard.keymap = [
    [KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.DEL],
    [KC.GRV, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC],
    [KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS],
    [KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT],
    [KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT],
    [KC.LCTL, FN, KC.LGUI, KC.LALT, KC.SPC, KC.RALT, KC.RGUI, KC.RCTL, KC.LEFT, KC.UP, KC.DOWN, KC.RIGHT],
    [KC.TRNS, KC.AUDIO_MUTE, KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP, KC.TRNS, KC.BRIGHTNESS_DOWN, KC.BRIGHTNESS_UP, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS],
]

if __name__ == '__main__':
    keyboard.go()
