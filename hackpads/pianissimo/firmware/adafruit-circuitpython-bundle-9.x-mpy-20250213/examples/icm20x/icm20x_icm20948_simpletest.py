# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time

import board

import adafruit_icm20x

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
icm = adafruit_icm20x.ICM20948(i2c)

while True:
    print("Acceleration: X:{:.2f}, Y: {:.2f}, Z: {:.2f} m/s^2".format(*icm.acceleration))
    print("Gyro X:{:.2f}, Y: {:.2f}, Z: {:.2f} rads/s".format(*icm.gyro))
    print("Magnetometer X:{:.2f}, Y: {:.2f}, Z: {:.2f} uT".format(*icm.magnetic))
    print("")
    time.sleep(0.5)
