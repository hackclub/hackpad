import time
import board
import busio
import adafruit_ssd1306
from adafruit_display_text import label
import terminalio
from kb import keyboard

i2c = busio.I2C(board.GP5, board.GP4)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
display.fill(0)
display.show()

# List of messages to display
messages = ["Hello", "I am", "HelperPad", "by", "JH"]
current_message_index = 0
last_switch_time = time.monotonic()

def update_display():
    global current_message_index, last_switch_time
    display.fill(0)
    text = messages[current_message_index]
    text_area = label.Label(terminalio.FONT, text=text, x=10, y=10)
    display.fill(0)
    display.blit(text_area)
    display.show()
    last_switch_time = time.monotonic()

def check_display_update():
    global current_message_index
    # Change the message every 7 seconds
    if time.monotonic() - last_switch_time > 7:
        current_message_index = (current_message_index + 1) % len(messages)
        update_display()

update_display()
keyboard.before_matrix_scan = check_display_update

if __name__ == '__main__':
    keyboard.go()
