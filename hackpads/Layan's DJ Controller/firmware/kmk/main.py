# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

i2c = busio.I2C(scl=board.SCL, sda=board.SDA, frequency=100000)
mcp = MCP23017(i2c, address=0x20)

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D0, board.D1, board.D2, board.D3, board.D7, board.D8, board.D9, mcp.get_pin(0), mcp.get_pin(1), mcp.get_pin(2), mcp.get_pin(3),
        mcp.get_pin(4), mcp.get_pin(5), mcp.get_pin(6), mcp.get_pin(7), mcp.get_pin(8), mcp.get_pin(9), mcp.get_pin(10), mcp.get_pin(11),
        mcp.get_pin(12), mcp.get_pin(13), mcp.get_pin(14), mcp.get_pin(15)]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D, KC.E, KC.F, KC.G, KC.H, KC.I, KC.J, KC.K, KC.L, KC.M, KC.N, KC.O, KC.P, KC.Q, KC.R, KC.S, KC.T, KC.U, KC.V, KC.W]
]

# I want to interface the pins with VirtualDJ and I will have to get the slide potentiometer and rotary encoder outputs for this so I will do it when I have the hardware to test on

# Start kmk!
if __name__ == '__main__':
    keyboard.go()