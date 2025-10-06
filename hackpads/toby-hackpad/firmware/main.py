print("toby's lil hackpad!")

# Basic imports for OrpheusPad
import board
import busio
from adafruit_mcp230xx.mcp23017 import MCP23017
from kmk.extensions.RGB import RGB
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.encoder import EncoderHandler
from kmk.scanners.mcp import KMKScannerMCP230XX  # MCP23017 scanner for KMK

# Initialize I2C with correct SDA (GPIO6) and SCL (GPIO7)
i2c = busio.I2C(board.GP7, board.GP6)  # SDA = GPIO6, SCL = GPIO7

# Initialize MCP23017
mcp = MCP23017(i2c)

# Initialize Keyboard
keyboard = KMKKeyboard()

# Configure MCP23017 scanner for KMK
keyboard.matrix = KMKScannerMCP230XX(
    i2c=i2c,
    mcp230xx_cls=MCP23017,
    columns=5,  # Adjust as needed
    rows=2,  # Adjust as needed
    column_pins=[0, 1, 2, 3, 4],  # MCP23017 GPIOs for columns (GPA0-GPA4)
    row_pins=[5, 6, 7, 14,
              15],  # MCP23017 GPIOs for rows (GPA5-GPA7, GPB6-GPB7)
)

# RGB Configuration
rgb = RGB(pixel_pin=board.GP0, num_pixels=12)  # LED on GPIO0
keyboard.extensions.append(rgb)

# Encoder Configuration
encoder_handler = EncoderHandler()
encoder_handler.pins = (
    (board.GP2, board.GP1, board.GP3),  # Encoder #1
)
encoder_handler.map = [
    ((KC.UP, KC.DOWN), ),
]

keyboard.modules.append(encoder_handler)

# Define Keymap
keyboard.keymap = [[
    KC.A, KC.B, KC.C, KC.D, KC.E, KC.F, KC.G, KC.H, KC.I, KC.J
]]

if __name__ == '__main__':
    keyboard.go()
