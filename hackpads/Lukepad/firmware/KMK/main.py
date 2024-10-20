print("Starting")

import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import I2CExpander
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, SSD1306
from kmk.modules.layers import Layers
from kmk.extensions.RGB import RGB
from kmk.extensions.media_keys import MediaKeys
from adafruit_mcp230xx.mcp23017 import Direction
from adafruit_mcp3xxx.analog import MCP3008
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

keyboard = KMKKeyboard()


#Keypad
keyboard.col_pins = (board.GP8, board.GP9, board.GP10)
keyboard.row_pins = (board.GP7,board.GP6, board.GP3, board.GP2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


#I2C Config
i2c = busio.I2C(board.GP4, board.GP5)
#Expander
mcp = MCP23017(i2c, address=0x20)
#OLED
driver = SSD1306(i2c=i2c,device_address=0x3C)
display = Display(display=driver, width=128, height=64)
display.entries = [
    TextEntry(text="Lukepad", x=64, y=32, x_anchor="M", y_anchor="M"), # text in the Middle of screen
]

keyboard.extensions.append(display)

#Encoders
encoder_handler = EncoderHandler()
encoder_handler.pins = ((mcp.get_pin(GPB4), mcp.get_pin(GPB5), None, False), (mcp.get_pin(GPB6), mcp.get_pin(GPB7), None, False))
encoder1_button = mcp.get_pin(GPB0)
encoder2_button = mcp.get_pin(GPB1)
encoder1_button.direction = Direction.Input
encoder2_button.direction = Direction.Input

#RGB Lights
LED1_R = mcp.get_pin(GPA7)
LED1_G = mcp.get_pin(GPA6)
LED1_B = mcp.get_pin(GPA5)
LED2_R = mcp.get_pin(GPA4)
LED2_G = mcp.get_pin(GPA3)
LED2_B = mcp.get_pin(GPA2)

LED1_R.direction = Direction.OUTPUT
LED1_G.direction = Direction.OUTPUT
LED1_B.direction = Direction.OUTPUT
LED2_R.direction = Direction.OUTPUT
LED2_G.direction = Direction.OUTPUT
LED2_B.direction = Direction.OUTPUT


#Toggle Switch
Toggle = mcp.get_pin(GPA1)
Toggle.direction = Direction.INPUT

#Side Switch
Side1 = mcp.get_pin(GPB2)
Side2 = mcp.get_pin(GPB3)

Side1.direction = Direction.INPUT
Side2.direction = Direction.INPUT

#Slider
Slider = mcp.get_pin(GPA0)
Slider.direction = Direction.INPUT

#Keyboard Map
keyboard.keymap = [
    [
        KC.MUTE, KC.MPLY, KC.ESCAPE,
        KC.F1, KC.F2, KC.F3,
        KC.F5, KC.F6, KC.F7,
        KC.F9, KC.F10, KC.F11,
    ],  # Layer 0: Function Layer
    [
        KC.MUTE, KC.MPLY, KC.ESCAPE,
        KC.F1, KC.F2, KC.F3,
        KC.F5, KC.F6, KC.F7,
        KC.F9, KC.F10, KC.F11,
    ],  # Layer 1: Calculator
    [
        KC.MUTE, KC.MPLY, KC.ESCAPE,
        KC.F1, KC.F2, KC.F3,
        KC.F5, KC.F6, KC.F7,
        KC.F9, KC.F10, KC.F11,
    ],  # Layer 2: Function Layer
]

#Encoder Map
encoder_handler.map = [ 
    (( KC.VOLD, KC.VOLU), ( KC.BRID, KC.BRIU)),  # Layer 0
    (( KC.VOLD, KC.VOLU), ( KC.BRID, KC.BRIU)),  # Layer 1
    (( KC.VOLD, KC.VOLU), ( KC.BRID, KC.BRIU)),  # Layer 2
]
def check_encoder_button():
    if not encoder1_button.value:
        display.entries = [
            TextEntry(text="Hola!", x=64, y=32, x_anchor="M", y_anchor="M"), # text in the Middle of screen
        ]
    else:
        display.entries = [
            TextEntry(text="Lukepad", x=64, y=32, x_anchor="M", y_anchor="M"), # text in the Middle of screen
        ]


#Slider

def set_volume(level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(level, None)

def read_slider_and_change_volume():
    last_slider_value = -1  # Initialize with an invalid value

    while True:
        # Read the analog value from the slider
        slider_value = adc.read(slider_pin)

        # Check if the slider value has changed significantly
        if last_slider_value == -1 or abs(slider_value - last_slider_value) > 10:  # Threshold for change
            # Map the slider value (assuming 0-1023 for a 10-bit ADC)
            volume_level = int((slider_value / 1023) * 1)  # Scale to 0.0 to 1.0
            
            # Set the system volume
            set_volume(volume_level)

            # Print volume level for debugging
            print(f"Volume Level: {volume_level * 100:.1f}%")  # Show as percentage

            last_slider_value = slider_value  # Update last slider value

        time.sleep(0.1)  # Small delay to prevent overwhelming the system

#Layer Swapping
layer_manager = Layers()
keyboard.extensions.append(layer_manager)

current_layer = 0

def update_layer():
    global current_layer
    if Side1.value:  # Check if Side1 is pressed
        current_layer = 0  # Layer 0
    elif Side2.value:  # Check if Side2 is pressed
        current_layer = 1  # Layer 1
    else:  # Both off, default to Layer 2
        current_layer = 2  # Layer 2
    layer_manager.set_active_layer(current_layer)  # Set the active layer

# Attach the update_layer function to the keyboard's polling mechanism
keyboard.register_polling(update_layer)


#RGB Control: Scrolling
def scroll_colors():
    for r in range(0, 256, 5):  # Red
        LED1_R.value = r
        LED1_G.value = 0
        LED1_B.value = 0
        LED2_R.value = r
        LED2_G.value = 0
        LED2_B.value = 0
        time.sleep(0.01)

    for g in range(0, 256, 5):  # Green
        LED1_R.value = 0
        LED1_G.value = g
        LED1_B.value = 0
        LED2_R.value = 0
        LED2_G.value = g
        LED2_B.value = 0
        time.sleep(0.01)

    for b in range(0, 256, 5):  # Blue
        LED1_R.value = 0
        LED1_G.value = 0
        LED1_B.value = b
        LED2_R.value = 0
        LED2_G.value = 0
        LED2_B.value = b
        time.sleep(0.01)

def main_loop():
    while True:
        scroll_colors()


if __name__ == '__main__':
    keyboard.go()