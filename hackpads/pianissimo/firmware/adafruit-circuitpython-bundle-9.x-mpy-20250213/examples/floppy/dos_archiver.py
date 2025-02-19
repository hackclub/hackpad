# SPDX-FileCopyrightText: Copyright (c) 2024 Jeff Epler for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

"""DOS floppy archiver for Adafruit Floppsy

Insert an SD card & hook up your floppy drive.
Open the REPL / serial connection
Insert a floppy and press Enter to archive it
Do this for as many floppies as you like."""

import os
import sdcardio
import board
import storage
import usb_cdc
import adafruit_aw9523
import adafruit_floppy

i2c = board.I2C()  # uses board.SCL and board.SDA
aw = adafruit_aw9523.AW9523(i2c)
aw.directions = 0
KEY_BITS = 0xF

floppy = adafruit_floppy.Floppy(
    densitypin=board.DENSITY,
    indexpin=board.INDEX,
    selectpin=board.SELECT,
    motorpin=board.MOTOR,
    directionpin=board.DIRECTION,
    steppin=board.STEP,
    track0pin=board.TRACK0,
    protectpin=board.WRPROT,
    rddatapin=board.RDDATA,
    sidepin=board.SIDE,
    readypin=board.READY,
    wrdatapin=board.WRDATA,
    wrgatepin=board.WRGATE,
    floppydirectionpin=board.FLOPPY_DIRECTION,
    floppyenablepin=board.FLOPPY_ENABLE,
)

_image_counter = 0
last_filename = None


def open_next_image(extension="img"):
    """Return an opened numbered file on the sdcard, such as "img01234.jpg"."""
    global _image_counter, last_filename  # pylint: disable=global-statement
    try:
        os.stat("/sd")
    except OSError as exc:  # no SD card!
        raise RuntimeError("No SD card mounted") from exc
    while True:
        filename = "/sd/dsk%04d.%s" % (_image_counter, extension)
        _image_counter += 1
        try:
            os.stat(filename)
        except OSError:
            break
    print("Writing to", filename)
    last_filename = filename
    return open(filename, "wb")


def smart_input(prompt):
    print(end=prompt)

    console = usb_cdc.console
    serial_connected = console.connected
    console.flush()
    keys = aw.inputs & KEY_BITS

    while True:
        new_connected = console.connected
        if new_connected and not serial_connected:
            print(end="\r")
            print(end=prompt)
        serial_connected = new_connected

        if n := console.in_waiting:
            console.read(n)
            break

        new_keys = aw.inputs & KEY_BITS
        if ~new_keys & keys:  # A bit went to 0 -> a key was pressed
            break
        keys = new_keys

    print()


print("\033[H\033[2JFloppy Archiver")
print("Archive standard DOS floppies to SD card in IMG format")
print()

try:
    sdcard = sdcardio.SDCard(board.SPI(), board.SD_CS)
    vfs = storage.VfsFat(sdcard)
    storage.mount(vfs, "/sd")
    print("Mounted SD card.")
except Exception as e:
    print("Failed to mount SD card:")
    print(e)
    raise SystemExit  # pylint: disable=raise-missing-from

dev = None
blockdata = bytearray(512)
baddata = b"BADDATA0" * 64
assert len(baddata) == len(blockdata)

while True:
    if dev is not None:
        dev.floppy.keep_selected = False
    vfsstat = vfs.statvfs(vfs)
    avail = vfsstat[0] * vfsstat[4] / 1024 / 1024
    print(f"/sd: {avail:.1f}MiB available")
    smart_input("Insert disk and press any key")

    try:
        if dev is None:
            dev = adafruit_floppy.FloppyBlockDevice(floppy, keep_selected=True)
        else:
            dev.floppy.keep_selected = True
            dev.autodetect()
    except OSError as e:
        print(e)
        continue

    dev.readblocks(0, blockdata)
    label = blockdata[43:54].decode("ascii", "replace").strip()
    fstype = blockdata[54:61].decode("ascii", "replace").strip()
    print(f"\033[H\033[2JArchiving {label!r} ({fstype!r})")

    bad_blocks = good_blocks = 0
    total_blocks = dev.count()
    pertrack = dev.sectors * dev.heads
    with open_next_image() as f:
        for i in range(total_blocks):
            if i % pertrack == 0:
                print(end=f"{i//pertrack:02d}")
            try:
                dev.readblocks(i, blockdata)
                print(end=".")
                f.write(blockdata)
                good_blocks += 1
            except Exception as e:  # pylint: disable=broad-exception-caught
                bad_blocks += 1
                print(end="!")
                f.write(baddata)
            if i % pertrack == (pertrack // 2 - 1):
                print(end="|")
            if i % pertrack == (pertrack - 1):
                print()

    print()
    print(f"Archived {label!r} to {last_filename.split('/')[-1]}")
    print(f"{good_blocks} good + {bad_blocks} bad blocks")
    print(f"out of {total_blocks} ({total_blocks//2}KiB)")
    print()
