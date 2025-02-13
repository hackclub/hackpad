# SPDX-FileCopyrightText: Copyright (c) 2025 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time

import board

import adafruit_ina228

i2c = board.I2C()
ina228 = adafruit_ina228.INA228(i2c)
print("Adafruit INA228 Test")

print(f"Bus conversion time: {ina228.conversion_time_bus} microseconds")
print(f"Shunt conversion time: {ina228.conversion_time_shunt} microseconds")
print(f"Samples averaged: {ina228.averaging_count}")

while True:
    print("\nCurrent Measurements:")
    print(f"Current: {ina228.current:.2f} mA")
    print(f"Bus Voltage: {ina228.voltage:.2f} V")
    print(f"Shunt Voltage: {ina228.shunt_voltage*1000:.2f} mV")
    print(f"Power: {ina228.power:.2f} mW")
    print(f"Energy: {ina228.energy:.2f} J")
    print(f"Temperature: {ina228.temperature:.2f} °C")
    time.sleep(1)
