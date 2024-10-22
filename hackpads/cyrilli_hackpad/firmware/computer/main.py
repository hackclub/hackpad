# This program requires the 'wtype' command to be installed on the computer.

from serial import Serial
import json, subprocess, time

keymap = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k"
]

port = input ("Enter the port name (e.g. /dev/ttyACM0 for Linux): ")
ser = Serial (port, write_timeout = 0.1)

while ser.readline () != b"HackPad\n":
    ser.write (b"HkPd\n")
    time.sleep (0.2)

keys = (0, ) * 11
while True:
    response = json.reads (ser.readline ().decode ("utf-8"))
    keys1, enc, rx = response ["keys"], response ["enc"], response ["rx"]

    # TODO: debouncing
    for j, (k, k1) in enumerate (zip (keys, keys1)):
        if k < k1: # Keydown
            subprocess.run (["wtype", "-P", keymap [j]])
        elif k > k1: # Keyup
            subprocess.run (["wtype", "-p", keymap [j]])
    keys = keys1
    
    # TODO: sensitivity
    enc = sum (enc)
    for i in range (abs (enc)):
        if enc < 0:
            subprocess.run (["wtype", "-k", "XF86AudioLowerVolume"])
        else:
            subprocess.run (["wtype", "-k", "XF86AudioRaiseVolume"])
    
    # Do something with rx
    print (rx)

    # Send the response (tx)