# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import os

import adafruit_connection_manager
import board
import busio
from adafruit_wiznet5k.adafruit_wiznet5k import WIZNET5K
from digitalio import DigitalInOut

import adafruit_minimqtt.adafruit_minimqtt as MQTT

# Add settings.toml to your filesystem. Add your Adafruit IO username and key as well.
# DO NOT share that file or commit it into Git or other source control.

aio_username = os.getenv("aio_username")
aio_key = os.getenv("aio_key")

cs = DigitalInOut(board.D10)
spi_bus = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Initialize ethernet interface with DHCP
eth = WIZNET5K(spi_bus, cs)
### Topic Setup ###

# MQTT Topic
# Use this topic if you'd like to connect to a standard MQTT broker
mqtt_topic = "test/topic"

# Adafruit IO-style Topic
# Use this topic if you'd like to connect to io.adafruit.com
# mqtt_topic = 'aio_user/feeds/temperature'

### Code ###


# Define callback methods which are called when events occur
def connect(client, userdata, flags, rc):
    # This function will be called when the client is connected
    # successfully to the broker.
    print("Connected to MQTT Broker!")
    print(f"Flags: {flags}\n RC: {rc}")


def disconnect(client, userdata, rc):
    # This method is called when the client disconnects
    # from the broker.
    print("Disconnected from MQTT Broker!")


def subscribe(client, userdata, topic, granted_qos):
    # This method is called when the client subscribes to a new feed.
    print(f"Subscribed to {topic} with QOS level {granted_qos}")


def unsubscribe(client, userdata, topic, pid):
    # This method is called when the client unsubscribes from a feed.
    print(f"Unsubscribed from {topic} with PID {pid}")


def publish(client, userdata, topic, pid):
    # This method is called when the client publishes data to a feed.
    print(f"Published to {topic} with PID {pid}")


pool = adafruit_connection_manager.get_radio_socketpool(eth)
ssl_context = adafruit_connection_manager.get_radio_ssl_context(eth)

# Set up a MiniMQTT Client
# NOTE: We'll need to connect insecurely for ethernet configurations.
client = MQTT.MQTT(
    broker=os.getenv("broker"),
    username=os.getenv("username"),
    password=os.getenv("password"),
    is_ssl=False,
    socket_pool=pool,
    ssl_context=ssl_context,
)

# Connect callback handlers to client
client.on_connect = connect
client.on_disconnect = disconnect
client.on_subscribe = subscribe
client.on_unsubscribe = unsubscribe
client.on_publish = publish

print("Attempting to connect to %s" % client.broker)
client.connect()

print("Subscribing to %s" % mqtt_topic)
client.subscribe(mqtt_topic)

print("Publishing to %s" % mqtt_topic)
client.publish(mqtt_topic, "Hello Broker!")

print("Unsubscribing from %s" % mqtt_topic)
client.unsubscribe(mqtt_topic)

print("Disconnecting from %s" % client.broker)
client.disconnect()
