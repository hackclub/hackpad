import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
import adafruit_requests as requests
import adafruit_espatcontrol.adafruit_espatcontrol_socket as socket
from adafruit_espatcontrol import adafruit_espatcontrol

COL0 = board.D3
COL1 = board.D2
COL2 = board.D1
COL3 = board.D0
ROW0 = board.D8
ROW1 = board.D9
ROW2 = board.D10
TX = board.D6
RX = board.D7
i2c = busio.I2C(board.GP_SCL, board.GP_SDA)
uart = busio.UART(TX, RX, receiver_buffer_size=2048)

keyboard = KMKKeyboard()

keyboard.col_pins = (COL0, COL1, COL2, COL3)
keyboard.row_pins = (ROW1, ROW2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.LCTRL(KC.C), KC.LCTRL(KC.V), KC.LGUI(KC.V), KC.LCTRL(KC.H),
     KC.BRIGHTNESS_UP, KC.BRIGHTNESS_DOWN, KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN,
     KC.MEDIA_PREV_TRACK, KC.MEDIA_PLAY_PAUSE, KC.MEDIA_NEXT_TRACK, KC.MEDIA_MUTE]
]
keyboard.extensions.append(MediaKeys())

driver = SSD1306(i2c=i2c, device_address=0x3C)
display = Display(
    display=driver,
    width=128,
    height=32,
    brightness=1,
    entries=[
        TextEntry(text="MeroPad", x=0, y=0, y_anchor='M'),
    ]
)
keyboard.extensions.append(display)

esp = adafruit_espatcontrol.ESP_ATcontrol(uart, 115200, debug=False)
requests.set_socket(socket, esp)
esp.soft_reset()
esp.connect({"ssid": "my_wifi_ssid", "password": "my_wifi_password"})

def http_request():
    requests.request(
        method="post",
        url="https://ntfy.sh/meropad",
        data="Hello World!".encode(encoding="utf-8")
    )

KC.LCTRL(KC.H).before_press_handler(http_request)

if __name__ == '__main__':
    keyboard.go()