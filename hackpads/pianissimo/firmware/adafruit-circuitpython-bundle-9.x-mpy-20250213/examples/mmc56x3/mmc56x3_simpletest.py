# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Display magnetometer data once per second"""

import time

import board

import adafruit_mmc56x3

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_mmc56x3.MMC5603(i2c)

while True:
    mag_x, mag_y, mag_z = sensor.magnetic
    temp = sensor.temperature

    print(f"X:{mag_x:10.2f}, Y:{mag_y:10.2f}, Z:{mag_z:10.2f} uT\tTemp:{temp:6.1f}*C")
    print("")
    time.sleep(1.0)
