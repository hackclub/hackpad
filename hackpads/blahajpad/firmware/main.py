import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.scanners.digitalio import MatrixScanner
from kmk.modules.i2c import I2C
from adafruit_mcp230xx.mcp23017 import MCP23017
from kmk.extensions.media_keys import MediaKeys
keyboard.extensions.append(MediaKeys())

# Rotary encoder
from kmk.modules.encoder import EncoderHandler

encoder_handler = EncoderHandler()
keyboard.modules = [layers, encoder_handler]

encoder_handler.pins = (
    (board.GP8, board.GP7, board.GP6),
    )

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE)), # Layer 1
    ((KC.BRID, KC.BRIU, KC.NO)), # Layer 2
]




# MCP nonsense
i2c = I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c)

for pin in range(8):
    mcp.get_pin(pin + 8).direction = digitalio.Direction.OUTPUT  # GPB0-GPB7
    mcp.get_pin(pin).direction = digitalio.Direction.INPUT  # GPA0-GPA7
    mcp.get_pin(pin).pull = digitalio.Pull.UP

class MCP23017Scanner(MatrixScanner):
    def __init__(self, cols, rows, diode_orientation):
        super().__init__(cols, rows, diode_orientation)
        self.mcp = mcp

    def scan_for_changes(self):
        for col in range(len(self.cols)):
            self.mcp.get_pin(self.cols[col]).value = False
            for row in range(len(self.rows)):
                val = not self.mcp.get_pin(self.rows[row]).value
                if val != self.matrix[row][col]:
                    self.matrix[row][col] = val
                    self.len_states += 1
                    self.states[self.len_states - 1] = KeyEvent(row, col, val)
            self.mcp.get_pin(self.cols[col]).value = True
        return self.len_states






# Keyboard stuff
keyboard = KMKKeyboard()

keyboard.col_pins = (13, 14, 15, 16)
keyboard.row_pins = (8, 9, 10, 11, 12)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.matrix = MCP23017Scanner(
    keyboard.col_pins,
    keyboard.row_pins,
    keyboard.diode_orientation
)

keyboard.keymap = [
    # 'standard' layer
    [
        KC.NLCK,  KC.PSLS, KC.PAST, KC.BSPC,
        KC.P7,    KC.P8,   KC.P9,   KC.PLUS,
        KC.P4,    KC.P5,   KC.P6,
        KC.P1,    KC.P2,   KC.P3,   KC.PENT
        KC.P0,             KC.PDOT
    ]
    # 'macro' layer (will add app-specific macros later)
    [
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS
        KC.TRNS,           KC.TRNS
    ]
]

if __name__ == '__main__':
    keyboard.go()