"""Program entry point.

This module defines the core behaviour of the prototype: its connection to
Wi-Fi, publishing to the HiveMQ MQTT broker, and data burst and deep sleep
timing.
"""

import time

import alarm
import supervisor

from config import GranularityConfig
from connection import connect_to_wifi
from mqtt_publisher import MQTTPublisher

try:
    # Connect to Wi-Fi
    pool, ssl_context = connect_to_wifi()

    # Initialise MQTT topic
    mqtt_publisher = MQTTPublisher(pool, ssl_context)
    mqtt_publisher.connect()

    # Publish a number of data bursts, then enter deep sleep
    for _ in range(GranularityConfig.NUM_BURSTS):
        mqtt_publisher.publish()
        time.sleep(GranularityConfig.INTER_BURST)

    # Alarm for next wakeup
    time_alarm = alarm.time.TimeAlarm(
        monotonic_time=time.monotonic() + GranularityConfig.SLEEP_TIME
    )
    alarm.exit_and_deep_sleep_until_alarms(time_alarm)

# Soft reboot if errors are encountered
except Exception as e:
    print(f"Error: {str(e)}")
    print("Performing a soft reboot.")
    supervisor.reload()
