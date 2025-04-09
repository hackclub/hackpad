import time
from machine import Pin, I2C
import neopixel
from mcp23017 import MCP23017
from ssd1306 import SSD1306_I2C
from keyboard import Keyboard
from keymap import get_keycode

COL_PINS = list(range(0, 20)) + [22]
I2C_SCL_PIN = 20
I2C_SDA_PIN = 21
ROTARY_A_PIN = 26
ROTARY_B_PIN = 27
ROTARY_BTN_PIN = 28
NEOPIXEL_PINS = [6, 9, 10, 11, 12]
NEOPIXEL_COUNT = 106
MCP23017_ADDR = 0x20

i2c = I2C(0, scl=Pin(I2C_SCL_PIN), sda=Pin(I2C_SDA_PIN), freq=400_000)
mcp = MCP23017(i2c, MCP23017_ADDR)

row_pins = []
for i in range(6):
    row_pin = mcp.get_pin(i)
    row_pin.dir(mcp.OUT)
    row_pins.append(row_pin)

col_pins = []
for pin_num in COL_PINS:
    p = Pin(pin_num, Pin.IN, Pin.PULL_DOWN)
    col_pins.append(p)

nps = {}
for pin in NEOPIXEL_PINS:
    nps[pin] = neopixel.NeoPixel(Pin(pin), NEOPIXEL_COUNT)

rotary_a = Pin(ROTARY_A_PIN, Pin.IN, Pin.PULL_UP)
rotary_b = Pin(ROTARY_B_PIN, Pin.IN, Pin.PULL_UP)
rotary_btn = Pin(ROTARY_BTN_PIN, Pin.IN, Pin.PULL_UP)

encoder_position = 0
last_a_val = rotary_a.value()

display = SSD1306_I2C(128, 64, i2c)
def update_oled(text):
    display.fill(0)
    display.text(text, 0, 0)
    display.show()

def scan_matrix():
    num_rows = len(row_pins)
    num_cols = len(col_pins)
    matrix_states = []
    for r in range(num_rows):
        row_pins[r].value(0)
        row_data = []
        for c in range(num_cols):
            row_data.append(col_pins[c].value())
        matrix_states.append(row_data)
        row_pins[r].value(1)
    return matrix_states

def set_all_pixels(r, g, b):
    for np_obj in nps.values():
        for i in range(NEOPIXEL_COUNT):
            np_obj[i] = (r, g, b)
        np_obj.write()

def set_pixel(chain_pin, idx, r, g, b):
    if chain_pin in nps and 0 <= idx < NEOPIXEL_COUNT:
        nps[chain_pin][idx] = (r, g, b)
        nps[chain_pin].write()

def read_rotary():
    global encoder_position, last_a_val
    change = 0
    current_a = rotary_a.value()
    if current_a != last_a_val:
        if rotary_b.value() != current_a:
            encoder_position += 1
            change = 1
        else:
            encoder_position -= 1
            change = -1
    last_a_val = current_a
    return change

kb = Keyboard()

def main():
    update_oled("Keyboard ready")
    set_all_pixels(0, 10, 0)
    
    prev_matrix = [[0 for _ in range(len(col_pins))] for _ in range(len(row_pins))]
    menu_index = 0
    
    layer_colors = [
        (0, 10, 0),
        (0, 0, 10),
        (10, 0, 10),
    ]
    
    while True:
        matrix = scan_matrix()
        
        changed = False
        pressed_keys = []
        
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] != prev_matrix[r][c]:
                    changed = True
                    prev_matrix[r][c] = matrix[r][c]
                    
                    keycode, modifier = get_keycode(r, c, kb.current_layer)
                    
                    if matrix[r][c] == 1:
                        pressed_keys.append((r, c))
                        led_r, led_g, led_b = 255, 255, 255
                        
                        kb.add_keycode(keycode, modifier)
                        
                    else:
                        led_r, led_g, led_b = layer_colors[kb.current_layer]
                        
                        kb.remove_keycode(keycode, modifier)
                
                if matrix[r][c] == 1:
                    pressed_keys.append((r, c))
        
        if changed:
            kb.send()
            
            current_color = layer_colors[kb.current_layer]
            set_all_pixels(*current_color)
            
            for r, c in pressed_keys:
                if r < len(NEOPIXEL_PINS) and c < NEOPIXEL_COUNT:
                    set_pixel(NEOPIXEL_PINS[min(r, len(NEOPIXEL_PINS)-1)], c, 255, 255, 255)
            
            if kb.current_layer > 0:
                display_text = f"Layer: {kb.current_layer}"
            elif pressed_keys:
                display_text = "Keys: " + ", ".join([f"R{r}C{c}" for r, c in pressed_keys])
            else:
                display_text = "Ready"
            
            update_oled(display_text)
        
        delta = read_rotary()
        if delta != 0:
            if delta > 0:
                menu_index += 1
            else:
                menu_index -= 1
            
            update_oled(f"Volume: {menu_index}")
        
        if rotary_btn.value() == 0:
            kb.current_layer = (kb.current_layer + 1) % 2
            set_all_pixels(*layer_colors[kb.current_layer])
            update_oled(f"Layer: {kb.current_layer}")
            time.sleep(0.3)
        
        time.sleep(0.01)

if __name__ == "__main__":
    main()
