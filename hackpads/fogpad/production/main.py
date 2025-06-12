import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.i2c import I2CScanner # Use the special I2C-aware scanner
from kmk.modules.encoder import Encoder
from kmk.extensions.oled import OLED, OledData

# 1. Keyboard and Hardware Definition
# ------------------------------------
# This firmware is based on the provided schematic for a Xiao RP2040 board.
keyboard = KMKKeyboard()

# Use the I2CScanner because the matrix shares pins with the OLED display.
# The I2C address of the display (0x3C) must be provided to the scanner.
keyboard.scanner = I2CScanner(
    i2c_bus=busio.I2C(scl=board.GP7, sda=board.GP6),
    device_addr=0x3C
)

# GPIO pin configuration based on the schematic and your clarification.
# Col 1: GPIO6, Col 2: GPIO3, Col 3: GPIO0
keyboard.col_pins = (board.GP6, board.GP3, board.GP0)
# Row 1: GPIO1, Row 2: GPIO7
keyboard.row_pins = (board.GP1, board.GP7)

# 2. OLED Display Extension
# --------------------------
# The I2C bus is already defined in the I2CScanner, so we can reuse it.
oled_ext = OLED(
    OledData(
        corner_one=OledData.logo_kmk_faded,
        corner_two=OledData.layer_name,
        to_display_center=OledData.encoder_react,
    ),
    i2c=keyboard.scanner.i2c_bus, # Use the scanner's I2C bus
    device_addr=0x3C,
    width=128,
    height=64,
    flip_vertical=False,
    flip_horizontal=False,
)

# 3. Rotary Encoder Module
# -------------------------
encoder_handler = Encoder()

# Define the GPIO pins for the two rotary encoders based on the schematic.
# Format: (pin_A, pin_B, optional_press_pin)
# Encoder push buttons are handled in the main keymap matrix.
encoder_handler.pins = (
    # Knob 1: Connected to GPIO26 and GPIO27
    (board.GP26, board.GP27, None,),
    # Knob 2: Connected to GPIO28 and GPIO29
    (board.GP28, board.GP29, None,),
)

# Define the actions for each encoder rotation.
encoder_handler.map = [
    (
        # Knob 1: Volume Control
        (KC.VOLD, KC.VOLU),

        # Knob 2: Media Scrubber
        (KC.MPRV, KC.MNXT),
    ),
]

# 4. Attach Extensions and Modules
# ---------------------------------
keyboard.extensions.append(oled_ext)
keyboard.modules.append(encoder_handler)

# 5. Keymap Definition
# ---------------------
# This keymap matches your 3x2 matrix layout.
#
# Schematic Mapping:
# [SW5_Push (Knob1), SW1, SW6_Push (Knob2)]
# [SW2,              SW3, SW4             ]

# A useful default layout:
# Knob pushes control Mute and Play/Pause.
# The 4 switches are mapped to arrow keys.
KC_K1P = KC.MUTE   # Knob 1 Push
KC_K2P = KC.MPLY   # Knob 2 Push

keyboard.keymap = [
    [
      KC_K1P,  KC.UP,    KC_K2P,
      KC.LEFT, KC.DOWN,  KC.RIGHT
    ]
]


# 6. Run the Keyboard
# --------------------
if __name__ == '__main__':
    keyboard.go()
