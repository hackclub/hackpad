import board
import digitalio
import displayio
import adafruit_displayio_ssd1306
import supervisor
import time
import neopixel
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.handlers.sequences import simple_key_sequence
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.extensions.international import International
from kmk.extensions.lock_status import LockStatus
from kmk.modules.split import Split
from kmk.extensions.led import LED
from kmk.extensions.oled import Oled, OledDisplayMode, OledReactionType
from kmk.modules.oneshot import OneShot
from kmk.modules.bluetooth import Bluetooth

keyboard = KMKKeyboard()

keyboard.row_pins = (board.IO13, board.IO14, board.IO21, board.IO47, board.IO48, board.IO35, board.IO36)

keyboard.col_pins = (board.IO4, board.IO5, board.IO6, board.IO7, board.IO15, board.IO16, board.IO17, 
                     board.IO18, board.IO8, board.IO3, board.IO9, board.IO10, board.IO11, board.IO12)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

layers = Layers()
modtap = ModTap()
oneshot = OneShot()
bluetooth = Bluetooth()

media_keys = MediaKeys()
international = International()
lock_status = LockStatus()

NUM_LEDS = 91
led_pin = board.IO19  
pixels = neopixel.NeoPixel(led_pin, NUM_LEDS, brightness=0.5, auto_write=False)

i2c = busio.I2C(board.IO1, board.IO2)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

wpm = 0
last_key_time = time.monotonic()
key_press_count = 0
led_mode = 0 
led_brightness = 0.5
custom_mode_active = False
custom_color = [255, 0, 0]  
custom_color_index = 0
custom_color_input = ""

def calculate_wpm():
    global wpm, last_key_time, key_press_count
    current_time = time.monotonic()
    time_diff = current_time - last_key_time
    
    if time_diff > 1.0:
        wpm = int((key_press_count / 5) * (60 / time_diff))
        key_press_count = 0
        last_key_time = current_time
    
    return wpm

def update_oled():
    global wpm, custom_mode_active, custom_color_index, custom_color_input
    
    display.fill(0)
    display.text("KMK Keyboard", 0, 0, 1)
    
    if custom_mode_active:
        if custom_color_index == 0:
            display.text(f"R:{custom_color_input}", 0, 16, 1)
        elif custom_color_index == 1:
            display.text(f"G:{custom_color_input}", 0, 16, 1)
        elif custom_color_index == 2:
            display.text(f"B:{custom_color_input}", 0, 16, 1)
    else:
        if bluetooth.active:
            display.text("BT Mode", 0, 8, 1)
        else:
            display.text("USB Mode", 0, 8, 1)
        
        display.text(f"WPM: {calculate_wpm()}", 0, 16, 1)
        
        if led_mode == 0:
            led_mode_text = "LED: Off"
        elif led_mode == 1:
            led_mode_text = "LED: RGB"
        else:
            led_mode_text = "LED: Custom"
        
        display.text(led_mode_text, 0, 24, 1)
    
    display.show()

def update_leds():
    global led_mode, led_brightness, custom_color

    if led_mode == 0:
        pixels.fill((0, 0, 0))
    elif led_mode == 1:
        for i in range(NUM_LEDS):
            pixel_index = (i * 256 // NUM_LEDS)
            pixels[i] = wheel(pixel_index & 255)
    elif led_mode == 2:
        r, g, b = custom_color
        pixels.fill((r, g, b))
    
    pixels.brightness = led_brightness
    pixels.show()

def wheel(pos):
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b)

def on_pre_process(keyboard):
    global key_press_count, custom_mode_active, custom_color_input, custom_color_index, custom_color
    
    if custom_mode_active:
        for key in keyboard.active_keys:
            if key.code >= 30 and key.code <= 39:
                custom_color_input += str(key.code - 30)
                update_oled()
            elif key.code == 42:  
                if custom_color_input:
                    custom_color_input = custom_color_input[:-1]
                    update_oled()
            elif key.code == 40:
                if custom_color_input:
                    value = min(255, max(0, int(custom_color_input)))
                    custom_color[custom_color_index] = value
                    custom_color_index = (custom_color_index + 1) % 3
                    custom_color_input = ""
                    
                    if custom_color_index == 0: 
                        custom_mode_active = False
                        update_leds()
                    
                    update_oled()
        
        keyboard.active_keys = []
        return
    
    if keyboard.active_keys:
        key_press_count += len(keyboard.active_keys)
        update_oled()

def on_pre_process_key(keyboard, key, is_pressed):
    global led_mode, led_brightness, custom_mode_active
    
    ctrl_pressed = KC.LCTRL in keyboard.active_keys or KC.RCTRL in keyboard.active_keys
    alt_pressed = KC.LALT in keyboard.active_keys or KC.RALT in keyboard.active_keys
    shift_pressed = KC.LSHIFT in keyboard.active_keys or KC.RSHIFT in keyboard.active_keys
    
    if ctrl_pressed and alt_pressed and key == KC.PAUS and is_pressed:
        led_mode = (led_mode + 1) % 3
        update_leds()
        update_oled()
        return False
    
    if ctrl_pressed and alt_pressed and key == KC.PGUP and is_pressed:
        custom_mode_active = True
        custom_color_index = 0
        custom_color_input = ""
        update_oled()
        return False
    
    if ctrl_pressed and alt_pressed and shift_pressed and key == KC.UP and is_pressed:
        led_brightness = min(1.0, led_brightness + 0.05)
        update_leds()
        update_oled()
        return False
    
    if ctrl_pressed and alt_pressed and shift_pressed and key == KC.DOWN and is_pressed:
        led_brightness = max(0.0, led_brightness - 0.05)
        update_leds()
        update_oled()
        return False
    
    return True

pause_break_pin = digitalio.DigitalInOut(board.IO36)
pause_break_pin.direction = digitalio.Direction.INPUT
pause_break_pin.pull = digitalio.Pull.UP

if not pause_break_pin.value:
    bluetooth.active = True

keyboard.before_matrix_scan(on_pre_process)
keyboard.before_hid_send(on_pre_process_key)

keyboard.keymap = [
    [
        # Row 1
        KC.ESC,  KC.F1,   KC.F2,  KC.F3,  KC.F4,  KC.F5,  KC.F6,  KC.F7,  KC.F8,  KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.PSCR,
        # Row 2
        KC.GRV,  KC.N1,   KC.N2,  KC.N3,  KC.N4,  KC.N5,  KC.N6,  KC.N7,  KC.N8,  KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC,
        # Row 3
        KC.TAB,  KC.Q,    KC.W,   KC.E,   KC.R,   KC.T,   KC.Y,   KC.U,   KC.I,   KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS,
        # Row 4
        KC.CAPS, KC.A,    KC.S,   KC.D,   KC.F,   KC.G,   KC.H,   KC.J,   KC.L,   KC.SCLN, KC.QUOT, KC.ENT,  KC.DEL,  KC.NO,
        # Row 5
        KC.LSFT, KC.Z,    KC.X,   KC.C,   KC.V,   KC.B,   KC.N,   KC.M,   KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT, KC.UP,   KC.END,
        # Row 6
        KC.LCTL, KC.LGUI, KC.LALT, KC.NO, KC.NO, KC.SPC, KC.RALT, KC.RGUI, KC.APP, KC.RCTL, KC.LEFT, KC.DOWN, KC.RGHT, KC.PGDN,
        # Row 7
        KC.NO,   KC.NO,   KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,   KC.SLCK, KC.PAUS, KC.INS,  KC.HOME, KC.PGUP,
    ],
]

keyboard.modules = [layers, modtap, oneshot, bluetooth]

keyboard.extensions = [media_keys, international, lock_status]

def main():
    update_oled()
    
    last_oled_update = time.monotonic()
    last_led_update = time.monotonic()
    
    keyboard.go()
    
    while True:
        current_time = time.monotonic()
        
        if current_time - last_oled_update >= 0.1:
            update_oled()
            last_oled_update = current_time
        
        if current_time - last_led_update >= 0.05:
            update_leds()
            last_led_update = current_time
        
        time.sleep(0.001) 

if __name__ == "__main__":
    main()