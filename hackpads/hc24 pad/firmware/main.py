from machine import Pin, I2C, RTC
import neopixel
import time
import usb_hid
import colorsys
import ssd1315

NUM_LEDS = 28  
LED_PIN = 18   
BUTTON_PINS = [0, 1, 2, 3, 7, 6, 9, 10]  
KEYS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  

np = neopixel.NeoPixel(Pin(LED_PIN), NUM_LEDS)

buttons = [Pin(pin, Pin.IN, Pin.PULL_UP) for pin in BUTTON_PINS]

keyboard_device = usb_hid.devices[0]

i2c = I2C(0, scl=Pin(19), sda=Pin(18))  
display = ssd1315.SSD1315_I2C(128, 64, i2c)  

rtc = RTC()

transition_speed = 0.01  
hue = 0

def hsv_to_rgb(h, s, v):
    """Convert HSV to RGB."""
    if s == 0.0:
        r = g = b = int(v * 255)
        return (r, g, b)

    i = int(h * 6.0)
    f = (h * 6.0) - i
    p = v * (1.0 - s)
    q = v * (1.0 - s * f)
    t = v * (1.0 - s * (1.0 - f))
    i = i % 6

    if i == 0:
        r, g, b = v, t, p
    elif i == 1:
        r, g, b = q, v, p
    elif i == 2:
        r, g, b = p, v, t
    elif i == 3:
        r, g, b = p, q, v
    elif i == 4:
        r, g, b = t, p, v
    elif i == 5:
        r, g, b = v, p, q

    return (int(r * 255), int(g * 255), int(b * 255))

def set_button_leds(color):
    """Set color for the button LEDs."""
    for i in range(16):  
        np[i] = color
    np.write()

def set_transition_leds():
    """Set color for the transition LEDs."""
    global hue
    for i in range(16, NUM_LEDS):  
        np[i] = hsv_to_rgb(hue, 1, 1)
    np.write()
    hue += transition_speed
    if hue > 1:
        hue -= 1

def check_buttons():
    """Check button presses and handle LEDs and keystrokes."""
    for i, button in enumerate(buttons):
        if not button.value():  

            set_button_leds((0, 0, 255))

            if i < len(KEYS):
                keyboard_device.send(KEYS[i])
            return

    set_button_leds((0, 0, 0))  
    set_transition_leds()

def display_time():
    """Display the current time on the SSD1315 display."""

    t = rtc.datetime()
    hours = t[4]
    minutes = t[5]
    seconds = t[6]

    display.fill(0)

    time_str = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)

    display.text(time_str, 0, 0)
    display.show()

while True:
    check_buttons()
    display_time()
    time.sleep(0.1)
