# SPDX-FileCopyrightText: 2024 Tyeth Gundry for Adafruit Industries
# SPDX-License-Identifier: MIT

# retrieve user rate info via adafruit_circuitpython_adafruitio with native wifi networking
import ssl
import time  # pylint: disable=unused-import
import adafruit_requests
import socketpool
import wifi
from adafruit_io.adafruit_io import IO_HTTP

# Add a secrets.py to your filesystem that has a dictionary called secrets with "ssid" and
# "password" keys with your WiFi credentials. DO NOT share that file or commit it into Git or other
# source control.

# pylint: disable=no-name-in-module,wrong-import-order
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

# Set your Adafruit IO Username and Key in secrets.py
# (visit io.adafruit.com if you need to create an account,
# or if you need your Adafruit IO key.)
aio_username = secrets["aio_username"]
aio_key = secrets["aio_key"]

print("Connecting to %s" % secrets["ssid"])
wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Connected to %s!" % secrets["ssid"])


pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())
# Initialize an Adafruit IO HTTP API object
io = IO_HTTP(aio_username, aio_key, requests)

print("===============\nUser Rate info:\n===============")
print("\n".join([f"{k:<30}\t=\t{v}" for (k, v) in io.get_user_rate_info().items()]))

print(f"Throttle limit: {io.get_throttle_limit()}")
print(f"Remaining throttle limit: {io.get_remaining_throttle_limit()}")


# # Uncomment these lines to retrieve all user info as one big json object:
# print("Waiting 5seconds before fetching full user info (a lot of JSON output)")
# time.sleep(5)
# try:
#     print("\n\nFull User info:")
#     print(io.get_user_info())
# except MemoryError as me:
#     print(
#         "Board ran out of memory when processing all that user info json."
#         + "This is expected on most boards (ESP32-S3 should work)"
#     )
#     raise me
# except Exception as e:
#     print("Unexpected error!")
#     raise e

print("\n\nDone!")
