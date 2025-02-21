import board
import busio

from kmk.extensions.display import Display, TextEntry, ImageEntry

# For SSD1306
from kmk.extensions.display.ssd1306 import SSD1306

# Replace SCL and SDA according to your hardware configuration.
i2c_bus = busio.I2C(board.GP_SCL, board.GP_SDA)

driver = SSD1306(
    # Mandatory:
    i2c=i2c_bus,
    # Optional:
    device_address=0x3C,
)

# For SH1106
from kmk.extensions.display.sh1106 import SH1106

# Replace SCK and MOSI according to your hardware configuration.
spi_bus = busio.SPI(board.GP_SCK, board.GP_MOSI)

# Replace command, chip_select, and reset according to your hardware configuration.
driver = SH1106(
    # Mandatory:
    spi=spi_bus,
    command=board.GP_DC,
    chip_select=board.GP_CS,
    reset=board.GP_RESET,
)

# For displays initialized by CircuitPython by default
# IMPORTANT: breaks if a display backend from kmk.extensions.display is also in use
from kmk.extensions.display.builtin import BuiltInDisplay

# Replace display, sleep_command, and wake_command according to your hardware configuration.
driver = BuiltInDisplay(
    # Mandatory:
    display=board.DISPLAY
    sleep_command=0xAE
    wake_command=0xAF
)

# For all display types
display = Display(
    # Mandatory:
    display=driver,
    # Optional:
    width=128, # screen size
    height=32, # screen size
    flip = False, # flips your display content
    flip_left = False, # flips your display content on left side split
    flip_right = False, # flips your display content on right side split
    brightness=0.8, # initial screen brightness level
    brightness_step=0.1, # used for brightness increase/decrease keycodes
    dim_time=20, # time in seconds to reduce screen brightness
    dim_target=0.1, # set level for brightness decrease
    off_time=60, # time in seconds to turn off screen
    powersave_dim_time=10, # time in seconds to reduce screen brightness
    powersave_dim_target=0.1, # set level for brightness decrease
    powersave_off_time=30, # time in seconds to turn off screen
)