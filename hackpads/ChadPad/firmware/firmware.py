import board
import digitalio
import adafruit_hid.keycode
from adafruit_hid.keyboard import Keyboard
import neopixel
import time

buttons = [
    digitalio.DigitalInOut(board.P26), 
    digitalio.DigitalInOut(board.P7), 
    digitalio.DigitalInOut(board.P3), 
    digitalio.DigitalInOut(board.P27), 
    digitalio.DigitalInOut(board.P29), 
    digitalio.DigitalInOut(board.P4),  
    digitalio.DigitalInOut(board.P28), 
    digitalio.DigitalInOut(board.P1),  
    digitalio.DigitalInOut(board.P2),  
]

for button in buttons:
    button.switch_to_input(pull=digitalio.Pull.UP)


num_pixels = 13
pixels = neopixel.NeoPixel(board.D4, num_pixels, brightness=0.2, auto_write=False)


keyboard = Keyboard()


def set_led_color(index, color):
    pixels[index] = color
    pixels.show()

while True:
    for i, button in enumerate(buttons):
        if not button.value:  
            if i == 0:
                keyboard.press(adafruit_hid.keycode.Keycode.7)
            elif i == 1:
                keyboard.press(adafruit_hid.keycode.Keycode.8)
            elif i == 2:
                keyboard.press(adafruit_hid.keycode.Keycode.9)
            elif i == 3:
                keyboard.press(adafruit_hid.keycode.Keycode.4)
            elif i == 4:
                keyboard.press(adafruit_hid.keycode.Keycode.5)
            elif i == 5:
                keyboard.press(adafruit_hid.keycode.Keycode.6)
            elif i == 6:
                keyboard.press(adafruit_hid.keycode.Keycode.1)
            elif i == 7:
                keyboard.press(adafruit_hid.keycode.Keycode.2)
            elif i == 8:
                keyboard.press(adafruit_hid.keycode.Keycode.3)
            
            set_led_color(i, (255, 0, 0)) 
            
            time.sleep(0.1)
            keyboard.release_all()

        else:
            set_led_color(i, (0, 0, 0))
            
    time.sleep(0.01) 
