# SPDX-FileCopyrightText: Copyright (c) 2024 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""Adafruit DS2482S-800 8-Channel DS18B20 Example"""

import time
import board
from adafruit_ds248x import Adafruit_DS248x

# Initialize I2C bus and DS248x
i2c = board.STEMMA_I2C()
ds248x = Adafruit_DS248x(i2c)

while True:
    for i in range(8):
        ds248x.channel = i
        print(f"Reading channel {ds248x.channel}")
        temperature = ds248x.ds18b20_temperature()
        print(f"Temperature: {temperature:.2f} °C")
        print()
        time.sleep(1)
