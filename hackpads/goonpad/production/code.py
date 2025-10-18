from machine import Pin, I2C
import time
import neopixel
import ssd1306
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Configure Key Matrix
rows = [Pin(pin, Pin.OUT) for pin in [A3, D7, D8]]  # Adjust as per schematic
cols = [Pin(pin, Pin.IN, Pin.PULL_DOWN) for pin in [D6, D9]]  # Adjust as per schematic

# Configure Neopixel LEDs
num_pixels = 9  # Adjust based on the schematic
np = neopixel.NeoPixel(Pin(D10), num_pixels)  # Adjust data pin

# Configure OLED Display
i2c = I2C(0, scl=Pin(4), sda=Pin(5))  # Adjust pins
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

# Configure USB HID
kbd = Keyboard(usb_hid.devices)

# Configure Rotary Encoder
encoder_a = Pin(A1, Pin.IN, Pin.PULL_UP)
encoder_b = Pin(A2, Pin.IN, Pin.PULL_UP)
encoder_button = Pin(A0, Pin.IN, Pin.PULL_UP)
encoder_pos = 0

def encoder_changed(pin):
    global encoder_pos
    if encoder_b.value() == 1:
        encoder_pos += 1
    else:
        encoder_pos -= 1
    update_oled(f"Encoder: {encoder_pos}")

encoder_a.irq(trigger=Pin.IRQ_RISING, handler=encoder_changed)

def scan_keys():
    for row_idx, row in enumerate(rows):
        row.value(1)  # Activate row
        for col_idx, col in enumerate(cols):
            if col.value():
                return keymap[row_idx][col_idx]
        row.value(0)  # Deactivate row
    return None

def update_oled(text):
    oled.fill(0)
    oled.text(text, 0, 0)
    oled.show()

def update_leds():
    for i in range(num_pixels):
        np[i] = (0, 50, 0)  # Green color
    np.write()

while True:
    key = scan_keys()
    if key:
        kbd.send(key)
        update_oled(f"Key: {chr(key)}")
        update_leds()
    if not encoder_button.value():
        kbd.send(Keycode.ENTER)
        update_oled("Encoder Button Pressed")
    time.sleep(0.1)
 # type: ignore