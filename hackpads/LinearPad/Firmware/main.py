import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.extensions.oled import Oled, OledDisplayMode, OledReactionType, OledData

# Initialize keyboard instance
keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

# Define row and column pins based on the schematic
COL_PINS = [board.PA02_A0_D0, board.PA04_A1_D1, board.PA10_A2_D2]
ROW_PINS = [board.PB08_A7_D7, board.PA09_A8_D8, board.PA11_A3_D3]

# Define encoder pins
ENC_SWA = board.D14
ENC_SWB = board.D10
ENC_A = board.PA06_A10_D10_MISO
ENC_B = board.PA07_A9_D9_MOSI
ENC_C = board.GND

# Define OLED display pins
OLED_SCL = board.PA09_A8_D8_SCK
OLED_SDA = board.PA08_A4_D4_SDA
OLED_VCC = board.VCC
OLED_GND = board.GND

# Define LED chain
LED_PIN = board.PA03_A3_D3  # First LED connected to this pin
LED_CHAIN = 6  # Number of chained LEDs

# Define power and ground
VCC_3V3 = board.VCC  # 3.3V
GND = board.GND  # Ground
VCC_5V = board.PA14_A5_D5  # 5V

# Define the key matrix
keyboard.matrix = MatrixScanner(
    row_pins=ROW_PINS,
    col_pins=COL_PINS,
    value_when_pressed=False,
    interval=10,
)

# Define the keymap corresponding to the matrix layout
keyboard.keymap = [
    [KC.SW6, KC.SW7, KC.ENC_SWA],
    [KC.SW10, KC.SW11, KC.SW8],
    [KC.SW2, KC.SW3, KC.SW4],
]

# Initialize OLED display
oled = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC, 1:["White Screen"]},
        corner_two={0:OledReactionType.LAYER, 1:["1","2","3","4"]},
        corner_three={0:OledReactionType.LAYER, 1:["BASE","LOWER","RAISE","ADJUST"]},
        corner_four={0:OledReactionType.LAYER, 1:["qwerty","nums","shifted","leds"]},
    ),
    toDisplay=OledDisplayMode.TXT,
    flip=False,
)
keyboard.extensions.append(oled)

# Initialize RGB LEDs
rgb = RGB(
    pixel_pin=LED_PIN,
    num_pixels=LED_CHAIN,
    animation_mode=AnimationModes.STATIC,
    val=100,
    hue=170,  # Light blue color
)
keyboard.extensions.append(rgb)

# Initialize encoder handler
encoder_handler = EncoderHandler()
encoder_handler.pins = ((ENC_A, ENC_B, ENC_C),)
encoder_handler.map = (((KC.VOLD, KC.VOLU),),)  # Encoder controls volume
keyboard.modules.append(encoder_handler)

# Initialize media keys for sound control
media_keys = MediaKeys()
keyboard.extensions.append(media_keys)

# Start KMK
if __name__ == '__main__':
    keyboard.go()