from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.neopixel import Neopixel
from lib.adafruit_hid.keyboard import Keyboard
from lib.adafruit_hid.keycode import Keycode
import board
import busio
import digitalio
import time
from adafruit_ssd1306 import SSD1306_I2C
from adafruit_dht import DHT11  
from mcp23008 import MCP23008  


keyboard = KMKKeyboard()


i2c = busio.I2C(scl=board.SCL, sda=board.SDA)
mcp = MCP23008(i2c)


rows = [mcp.get_pin(i) for i in range(4)]  # GP0, GP1, GP2, GP3
cols = [mcp.get_pin(i) for i in range(4, 7)]  # GP4, GP5, GP6


for row in rows:
    row.switch_to_input(pull=mcp.Pull.UP)
for col in cols:
    col.switch_to_input(pull=mcp.Pull.UP)


keyboard.row_pins = rows 
keyboard.col_pins = cols  
keyboard.diode_orientation = DiodeOrientation.COLUMNS


keyboard.keymap = [
    [KC.N1, KC.N2, KC.N3],  # First row also i will adjust them as needed later as it would e very much time consuming to adjust them now
    [KC.N4, KC.N5, KC.N6],  # Second row
    [KC.N7, KC.N8, KC.N9],  # Third row
    [KC.KP_PLUS, KC.N0, KC.KP_MINUS],  # Fourth row
]

pixel = Neopixel(pin=board.D0, num_pixels=12, colors=[(255, 0, 0)], brightness=0.2)
keyboard.modules.append(pixel)


encoder1_a = digitalio.DigitalInOut(board.D6)
encoder1_b = digitalio.DigitalInOut(board.D10)
encoder2_a = digitalio.DigitalInOut(board.D3)
encoder2_b = digitalio.DigitalInOut(board.D9)


encoder1_a.switch_to_input(pull=digitalio.Pull.UP)
encoder1_b.switch_to_input(pull=digitalio.Pull.UP)
encoder2_a.switch_to_input(pull=digitalio.Pull.UP)
encoder2_b.switch_to_input(pull=digitalio.Pull.UP)


oled = SSD1306_I2C(128, 64, i2c)


dht_sensor = DHT11(digitalio.DigitalInOut(board.D2))  # DHT11 sensor on D2 pin


encoder1_pos = 0
encoder2_pos = 0


def read_distance():
   
    return 50  #its for now i will add the sensor code later


while True:
    keyboard.process()
    
    
    try:
        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity
    except Exception as e:
        temperature = None
        humidity = None
        print("Failed to read DHT11:", e)


    if not encoder1_a.value:
        if not encoder1_b.value: 
            encoder1_pos += 1
            keyboard.send(KC.VOLD)  
        else:  
            encoder1_pos -= 1
            keyboard.send(KC.VOLU)  

    
    if not encoder2_a.value:
        if not encoder2_b.value:  
            encoder2_pos += 1
            keyboard.send(KC.MPRV)  
        else:  
            encoder2_pos -= 1
            keyboard.send(KC.MNXT)  

    
    distance = read_distance()
    volume_level = max(0, min(100, 100 - distance))  # conveting distance to volume level

   #oled
    oled.fill(0)  
    oled.text("Temp: {}C".format(temperature), 0, 0)
    oled.text("Hum: {}%".format(humidity), 0, 10)
    oled.text("Distance: {}cm".format(distance), 0, 20)
    oled.text("Volume: {}".format(volume_level), 0, 30)
    oled.show()  

    time.sleep(0.01)  #for rest lol
