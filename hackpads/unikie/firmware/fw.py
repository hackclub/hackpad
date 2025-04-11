import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeyMatrixScanner
from kmk.modules.encoder import EncoderHandler
from kmk.modules.display.oled import Oled
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mcp23017 import MCP23017

keyboard = KMKKeyboard()

i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c, addr=0x20)

keyboard.matrix = KeyMatrixScanner(
    column_pins=[mcp.GPB0, mcp.GPB1, mcp.GPB2, mcp.GPB3, mcp.GPB4,],
    row_pins=[mcp.GPA4, mcp.GPA0, mcp.GPA1, mcp.GPA2, mcp.GPA3,],
    diode_orientation=KeyMatrixScanner.DIODE_COL2ROW
)

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = [
    (mcp.GPA0, mcp.GPB4), 
    (mcp.GPA1, mcp.GPB4),
    (mcp.GPA2, mcp.GPB4),
    (mcp.GPA3, mcp.GPB4),
    (mcp.GPA4, mcp.GPB4)
]

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),),
    ((KC.BRIU, KC.BRID),), # these are for test now, I'll change these to multiple layers and they'll be be for Hue, S,L and brush sizes in PS and colors or sizes in figma/AI and I'll add more controls based on softwares I use
    ((KC.BRIU, KC.BRID),),
    ((KC.MPLY, KC.MSTP),),
    ((KC.BRIU, KC.BRID),),
]

oled = Oled(i2c, addr=0x3C)
oled.set_display_text(lambda: "heyy, I'm unikie")
keyboard.modules.append(oled)

keyboard.keymap = [
    [KC.Q, KC.W, KC.E, KC.A, KC.S, 
     KC.D, KC.F, KC.Z, KC.X, KC.C, 
     KC.V, KC.LSFT, KC.RSFT, KC.SPC, KC.DEL]
]

if __name__ == "__main__":
    keyboard.go()
