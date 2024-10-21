# micropython imports
from machine import I2C, Pin, SPI
from micropython import const

# mip imports
# i2c io expander (github:mcauser/micropython-pcf8574)
from pcf8574 import PCF8574
# typing (github:josverl/micropython-stubs/mip/typing.py)
# (on host this will import native typing, on device it'll use the library)
from typing import List
# usb device (usb-device-keyboard)
from usb.device.core import get as usb_device_get
from usb.device.keyboard import KeyboardInterface, KeyCode

# define number of rows and columns
NUM_ROW: int = const(4)
NUM_COL: int = const(4)

# set the pins where the rows and columns are
ROW_PINS: List[int] = const([0, 1, 2, 3])
COL_PINS: List[int] = const([7, 6, 5, 4])

# matrix of all the key functions, size NUM_COl x NUM_ROW
KEY_MAP: List[List[int]] = const([
    [KeyCode.KP_1, KeyCode.KP_2, KeyCode.KP_3, KeyCode.PAUSE],
    [KeyCode.KP_4, KeyCode.KP_5, KeyCode.KP_6, KeyCode.KP_PLUS],
    [KeyCode.KP_7, KeyCode.KP_8, KeyCode.KP_9, KeyCode.KP_MINUS],
    [KeyCode.KP_0, KeyCode.KP_MULTIPLY, KeyCode.KP_DIVIDE, KeyCode.KP_ENTER]

])

# matrix of all the pressed keys, size NUM_COl x NUM_ROW
# everything is set to False initially
pressed_keys: List[int] = []

# interrupt flags
enc_rot_irqf: int = 0
enc_btn_irqf: int = 0


# simple function to check keymap size
def check_keymap():
    if len(KEY_MAP) != NUM_COL:
        return False
    for row in KEY_MAP:
        if len(row) != NUM_ROW:
            return False
    return True


# encoder rotation irq handler
def enc_rot_irq(pin):
    global enc_rot_irqf
    enc_rot_irqf = 1


# encoder rotation irq handler
def enc_btn_irq(pin):
    global enc_btn_irqf
    enc_btn_irqf = 1


def main():
    print(f"initializing macropad with {NUM_ROW} rows and {NUM_COL} columns")
    if not check_keymap():
        print("Failed to initialize, invalid keymap!")

    # i2c io expander setup
    print("initializing i2c")
    i2c = I2C(0, scl=Pin(7), sda=Pin(6))
    pcf = PCF8574(i2c, 0x20)
    print("successfully initialized i2c")

    # usb hid setup
    print("initializing usb")
    k = KeyboardInterface()
    usb_device_get().init(k, builtin_driver=True)
    print("successfully initialized usb")

    # turn off all COL pins
    for col_pin in COL_PINS:
        pcf.pin(col_pin, 0)

    # attach interrupts for rotary encoder
    enc_a = Pin(10, Pin.IN, Pin.PULL_UP)
    enc_a.irq(trigger=Pin.IRQ_FALLING, handler=enc_rot_irq)
    enc_b = Pin(9, Pin.IN, Pin.PULL_UP)

    # loop
    global enc_rot_irqf
    global enc_btn_irqf
    print("entering loop")
    while True:
        # clear pressed keys
        pressed_keys.clear()

        # handle set interrupt flags
        if enc_rot_irqf:
            enc_rot_irqf = 0
            if enc_b.value():
                pressed_keys.append(KeyCode.KP_MINUS)
            else:
                pressed_keys.append(KeyCode.KP_PLUS)

        # read columns of keyboard
        for col in range(0, NUM_COL):
            pcf.pin(COL_PINS[col], 1)
            for row in range(0, NUM_ROW):
                if pcf.pin(ROW_PINS[row]):
                    pressed_keys.append(KEY_MAP[col][row])
            pcf.pin(COL_PINS[col], 0)


# run main
if __name__ == '__main__':
    main()