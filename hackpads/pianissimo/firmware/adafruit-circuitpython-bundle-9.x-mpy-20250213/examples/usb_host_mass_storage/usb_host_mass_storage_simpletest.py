# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Scott Shawcroft for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

import time
import os
import storage
import usb.core

import adafruit_usb_host_mass_storage

device = None
while device is None:
    print("searching for devices")
    for device in usb.core.find(find_all=True):
        print("pid", hex(device.idProduct))
        print("vid", hex(device.idVendor))
        print("man", device.manufacturer)
        print("product", device.product)
        print("serial", device.serial_number)
        break
    if not device:
        time.sleep(5)

print("mounting")
msc = adafruit_usb_host_mass_storage.USBMassStorage(device)
vfs = storage.VfsFat(msc)
storage.mount(vfs, "/usb_drive")

l = os.listdir("/usb_drive")
print(l)

if "hello.txt" in l:
    print("hello.txt:")
    with open("/usb_drive/hello.txt", "r") as f:
        print(f.read())

with open("/usb_drive/hello.txt", "w") as f:
    f.write("Hello from the USB host device!")
