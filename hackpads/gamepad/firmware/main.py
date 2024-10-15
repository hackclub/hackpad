import time
import board
import digitalio
import adafruit_displayio_ssd1306 
import displayio
from adafruit_matrixkeypad import Matrix_Keypad
from adafruit_display_text import label
import terminalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

displayio.release_displays()
i2c = board.I2C()  
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
WIDTH = 128
HEIGHT = 64
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

cols = [digitalio.DigitalInOut(x) for x in (board.P0, board.P3, board.p4, board.P2, board.P1)]
rows = [digitalio.DigitalInOut(x) for x in (board.P26, board.P27, board.P28)]

keys = [
    ["1", "2", "3", "4", "5"],
    ["6", "7", "8", "9", "10"],
    ["11", "12", "Mode1", "Mode2", "Mode3"]
]
keypad = Matrix_Keypad(rows, cols, keys)

current_mode = 0
modes = ["Mode 1", "Mode 2", "Mode 3"]
def display_mode():
    splash = displayio.Group()
    display.show(splash)
    text_area = label.Label(terminalio.FONT, text=f"Current Mode: {modes[current_mode]}", x=10, y=30)
    splash.append(text_area)

display_mode()  

while True:
    keys_pressed = keypad.pressed_keys
    if keys_pressed:
        for key in keys_pressed:
            print(key)
            if key == "Mode1":
                current_mode = 0
                display_mode()  
            elif key == "Mode2":
                current_mode = 1
                display_mode()  
            elif key == "Mode3":
                current_mode = 2
                display_mode()
            elif key == "10":
                k = Keyboard()
                k.press(Keyboard.LEFT_CONTROL, Keyboard.LEFT_ALT, Keyboard.LEFT_SHIFT, Keyboard.M)
                k.release_all()
            elif key == "11":
                k = Keyboard()
                k.press(Keyboard.LEFT_GUI, Keyboard.L)
                k.release_all()
            elif key == "12":
                k = Keyboard()
                k.press(Keyboard.LEFT_CONTROL, Keyboard.LEFT_ALT, Keyboard.LEFT_SHIFT, Keyboard.T)
                k.release_all()
            else:
                if current_mode == 0:
                    if key == "1":
                        k = Keyboard()
                        k.send(Keyboard.F13)
                    elif key == "2":
                        ConsumerControl().send(ConsumerControlCode.VOLUME_INCREMENT)
                    elif key == "3":
                        k = Keyboard()
                        k.send(Keyboard.F14)
                    elif key == "4":
                        ConsumerControl().send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
                    elif key == "5":
                        ConsumerControl().send(ConsumerControlCode.PLAY_PAUSE)
                    elif key == "6":
                        ConsumerControl().send(ConsumerControlCode.SCAN_NEXT_TRACK)
                    elif key == "7":
                        ConsumerControl().send(ConsumerControlCode.BRIGHTNESS_INCREMENT)
                    elif key == "8":
                        ConsumerControl().send(ConsumerControlCode.VOLUME_DECREMENT)
                    elif key == "9":
                        ConsumerControl().send(ConsumerControlCode.BRIGHTNESS_DECREMENT)
                elif current_mode == 1:
                    if key == "1":
                        k = Keyboard()
                        k.send(Keyboard.F15)
                    elif key == "2":
                        k = Keyboard()
                        k.send(Keyboard.F16)
                    elif key == "3":
                        k = Keyboard()
                        k.send(Keyboard.F17)
                    elif key == "4":
                        k = Keyboard()
                        k.send(Keyboard.F18)
                    elif key == "5":
                        k = Keyboard()
                        k.send(Keyboard.F19)
                    elif key == "6":
                        k = Keyboard()
                        k.send(Keyboard.F20)
                    elif key == "7":
                        k = Keyboard()
                        k.send(Keyboard.F21)
                    elif key == "8":
                        k = Keyboard()
                        k.send(Keyboard.F22)
                    elif key == "9":
                        k = Keyboard()
                        k.send(Keyboard.F23)
                elif current_mode == 2:
                    # Will implement Tetris when the hardware is ready
                    pass

    time.sleep(0.1)
