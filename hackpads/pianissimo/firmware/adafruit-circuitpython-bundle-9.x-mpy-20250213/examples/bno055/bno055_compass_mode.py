# SPDX-FileCopyrightText: 2024 Tim Cocks for Adafruit Industries
# SPDX-License-Identifier: MIT
import math
import time
import board

import adafruit_bno055

i2c = board.I2C()

sensor = adafruit_bno055.BNO055_I2C(i2c)

# Set the sensor to compass mode
sensor.mode = adafruit_bno055.COMPASS_MODE

while True:
    values = sensor.magnetic
    print("Heading: " + str(180 + math.atan2(values[1], values[0]) * 180 / math.pi))
    time.sleep(1)
