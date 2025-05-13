# SPDX-FileCopyrightText: 2022 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import digitalio
import adafruit_adxl37x

i2c = board.STEMMA_I2C()  # uses board.SCL and board.SDA
accelerometer = adafruit_adxl37x.ADXL375(i2c)

interrupt = digitalio.DigitalInOut(board.GP3)  # Set interrupt dio pin

print("Accelerometer starting...")
accelerometer.data_rate = (
    accelerometer.DataRate.RATE_800_HZ
)  # Set Data Rate of accelerometer
accelerometer.range = adafruit_adxl37x.Range.RANGE_200_G  # Set Full Data Range 200g
accelerometer.enable_data_ready_interrupt()  # Enable Data Ready Interrupt

while True:
    if interrupt.value:
        # ADXL375 interrupt pin stays HIGH until data is read, so simply reading the logic state
        # is sufficient instead of having to catch the rising edge.
        print("%f %f %f m/s^2" % accelerometer.acceleration)
