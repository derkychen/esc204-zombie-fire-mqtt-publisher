"""Defines utility functions used in the connection to Wi-Fi."""

import time

import adafruit_connection_manager
import adafruit_ntp
import rtc
import wifi

from config import WifiConfig


def _attempt_connection():
    """Attempt to connect to Wi-Fi. Synchronise onboard RTC.

    Returns:
        tuple: A tuple containing
            - SocketPool: Pool of socket resources.
            - SSLContext: SSL certificates and configurations.
    """
    try:
        wifi.radio.connect(WifiConfig.SSID, WifiConfig.PASSWORD)

        pool = adafruit_connection_manager.get_radio_socketpool(wifi.radio)
        ssl_context = adafruit_connection_manager.get_radio_ssl_context(
            wifi.radio
        )

        ntp = adafruit_ntp.NTP(pool, tz_offset=0, cache_seconds=3600)
        rtc.RTC().datetime = ntp.datetime

        print(f"Connected to {WifiConfig.SSID}.")

        return pool, ssl_context

    except ConnectionError as e:
        print(f"Connection failed: {str(e)}")

        return None, None


def connect_to_wifi(max_attempts=None):
    """Connect Pico W to Wi-Fi.

    Attempt to connect to Wi-Fi indefinitely unless a connection is achieved or
    an optional maximum number of attempts is reached.

    Args:
        max_attempts (int, optional): The maximum number of attempts before
            giving up.
    """
    attempt = 1
    while max_attempts is None or attempt <= max_attempts:
        pool, ssl_context = _attempt_connection()

        if pool and ssl_context:
            return pool, ssl_context

        attempt += 1
        time.sleep(10)
