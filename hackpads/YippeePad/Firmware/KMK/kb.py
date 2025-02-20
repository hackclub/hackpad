import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.mcp23017 import MCP23017
from kmk.modules.encoder import EncoderHandler

class CustomKeyboard(KMKKeyboard):
    def __init__(self):
        super().__init__()

        # Define MCP23017 Expander for 12 switches
        self.mcp = MCP23017(address=0x20)  # Default I2C address
        self.modules.append(self.mcp)

        # Define key matrix pins
        self.col_pins = (self.mcp.gpioa[0], self.mcp.gpioa[1], self.mcp.gpioa[2])
        self.row_pins = (self.mcp.gpiob[0], self.mcp.gpiob[1], self.mcp.gpiob[2], self.mcp.gpiob[3])
        self.diode_orientation = DiodeOrientation.COL2ROW

        # Rotary Encoder Setup
        self.encoder_handler = EncoderHandler()
        self.encoder_handler.pins = [(board.GP6, board.GP7), (board.GP8, board.GP9)]
        self.modules.append(self.encoder_handler)