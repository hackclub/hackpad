import board
import digitalio
import time
import random
import displayio
from adafruit_display_shapes.rect import Rect
from adafruit_displayio_ssd1306 import SSD1306
import adafruit_neopixel

# Pin definitions
ENCODER_A_PIN = board.GP0   # D0 (GP0) Volume Encoder A
ENCODER_B_PIN = board.GP1   # D1 (GP1) Volume Encoder B
LED_ENC_A_PIN = board.GP2   # D2 (GP2) LED Encoder A
LED_ENC_B_PIN = board.GP3   # D3 (GP3) LED Encoder B
SWITCH1_PIN = board.GP6     # D6 (GP6) Switch 1 (Ctrl+A)
SWITCH2_PIN = board.GP7     # D7 (GP7) Switch 2 (Ctrl+C)
SWITCH3_PIN = board.GP8     # D8 (GP8) Switch 3 (Ctrl+V)
LED_PIN = board.GP9         # D9 (GP9) LED Data In

# Initialize OLED display
display_bus = displayio.I2CDisplay(board.I2C(), device_address=0x3C)
display = SSD1306(display_bus, width=128, height=64)

# Initialize LED strip (NeoPixel)
strip = adafruit_neopixel.NeoPixel(LED_PIN, 1, brightness=0.5, auto_write=False)

# Initialize switch pins as input
switch1 = digitalio.DigitalInOut(SWITCH1_PIN)
switch1.switch_to_input(pull=digitalio.Pull.UP)

switch2 = digitalio.DigitalInOut(SWITCH2_PIN)
switch2.switch_to_input(pull=digitalio.Pull.UP)

switch3 = digitalio.DigitalInOut(SWITCH3_PIN)
switch3.switch_to_input(pull=digitalio.Pull.UP)

# Setup encoders (using a simple method to count steps)
last_volume_pos = 0
last_led_pos = 0
volume_level = 50  # Volume level (0 to 100)
led_brightness = 128  # LED brightness (0 to 255)

# Time setup (use built-in time module)
# Set to 12:00 PM, Feb 1, 2025
current_time = time.struct_time((2025, 2, 1, 12, 0, 0, 0, 0, 0))

# Loop
while True:
    # Read switch states
    switch1_state = not switch1.value
    switch2_state = not switch2.value
    switch3_state = not switch3.value

    # Handle encoder position changes (simulate with pin states)
    volume_pos = int(time.monotonic() * 10) % 1000  # Simulate volume change for testing
    led_pos = int(time.monotonic() * 5) % 1000      # Simulate LED brightness change

    # Update volume and LED brightness if positions change
    if volume_pos != last_volume_pos:
        volume_level = min(max(volume_pos // 10, 0), 100)  # Map to 0-100 range
        last_volume_pos = volume_pos

    if led_pos != last_led_pos:
        led_brightness = min(max(led_pos // 4, 0), 255)  # Map to 0-255 range
        strip.brightness = led_brightness / 255  # Map brightness to 0-1 range
        strip.show()
        last_led_pos = led_pos

    # Display current time
    display.fill(0)  # Clear the screen
    display.text(f"Time: {current_time.tm_hour}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}", 0, 0)
    display.text(f"Volume: {volume_level}", 0, 16)
    display.text(f"Brightness: {led_brightness}", 0, 32)

    # Color adjustment (random color or set color)
    if switch1_state:
        strip.fill((255, 0, 0))  # Red color
    elif switch2_state:
        strip.fill((0, 255, 0))  # Green color
    elif switch3_state:
        # Generate random color
        if random.choice([True, False]):
            r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            strip.fill((r, g, b))  # Random color
        else:
            strip.fill((0, 0, 255))  # Blue color

    strip.show()
    display.show()

    time.sleep(0.1)  # Update every 100 ms
