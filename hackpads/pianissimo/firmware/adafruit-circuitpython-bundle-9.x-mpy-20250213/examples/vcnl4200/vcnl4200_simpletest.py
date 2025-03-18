# SPDX-FileCopyrightText: Copyright (c) 2024 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time

import board

import adafruit_vcnl4200

i2c = board.I2C()

sensor = adafruit_vcnl4200.Adafruit_VCNL4200(i2c)

while True:
    print(f"Proximity is: {sensor.proximity}")
    print(f"Ambient is: {sensor.lux}")
    time.sleep(0.1)
