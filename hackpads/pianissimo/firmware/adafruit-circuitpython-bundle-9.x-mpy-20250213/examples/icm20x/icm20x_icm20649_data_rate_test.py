# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time

import board

from adafruit_icm20x import ICM20649, AccelRange, GyroRange

i2c = board.I2C()  # uses board.SCL and board.SDA

ism = ICM20649(i2c, address=0x69)

ism.accelerometer_range = AccelRange.RANGE_4G
print("Accelerometer range set to: %d g" % AccelRange.string[ism.accelerometer_range])

ism.gyro_range = GyroRange.RANGE_500_DPS
print("Gyro range set to: %d DPS" % GyroRange.string[ism.gyro_range])

ism.gyro_data_rate = 1100  # 1100 max
ism.accelerometer_data_rate = 1125  # 1125 max

print(f"Gyro rate: {ism.gyro_data_rate:f}")
print(f"Accel rate: {ism.accelerometer_data_rate:f}")

ism.gravity = 9.8

previousTime = time.monotonic_ns()
while True:
    if ism.data_ready:
        currentTime = time.monotonic_ns()
        print("\033[2J")
        print(
            "Accel X:{:5.2f} Y:{:5.2f} Z:{:5.2f} ms^2 "
            "Gyro X:{:8.3f} Y:{:8.3f} Z:{:8.3f} degrees/s Sample Rate: {:8.1f} Hz".format(
                *ism.acceleration, *ism.gyro, (1 / (currentTime - previousTime))
            )
        )
        previousTime = currentTime
