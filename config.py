"""Various configurations and constants."""

import os

import board

from sensors.bme680 import BME680Sensor
from sensors.sen0114 import SEN0114Sensor
from utils import timestamp


class WifiConfig:
    """Wi-Fi information and secrets."""

    SSID = os.getenv("WIFI_SSID")
    PASSWORD = os.getenv("WIFI_PASSWORD")


class MQTTConfig:
    """HiveMQ MQTT broker information and secrets."""

    BROKER = os.getenv("MQTT_BROKER")
    PORT = os.getenv("MQTT_PORT")

    USERNAME = os.getenv("MQTT_USERNAME")
    PASSWORD = os.getenv("MQTT_PASSWORD")

    TOPIC = os.getenv("MQTT_TOPIC")


class DeviceConfig:
    """Device sensors and layout."""

    ID = os.getenv("DEVICE_ID")

    BME680_1 = BME680Sensor(board.GP17, board.GP16, temperature_offset=1)
    SEN0114_1 = SEN0114Sensor(board.GP27)

    BME680_2 = BME680Sensor(board.GP19, board.GP18, temperature_offset=1)
    SEN0114_2 = SEN0114Sensor(board.GP28)

    # Prototype structure with callable data-fetching methods
    # In the prototype, Level 1 is the top level, level 2 is the bottom level
    PAYLOAD_META = {
        "time": timestamp,
        "device_id": ID,
        "data": {
            "1": {
                "bme680": {
                    "temperature_c": BME680_1.temperature,
                    "gas_ohm": BME680_1.gas,
                    "relativehumidity_pct": BME680_1.relativehumidity,
                    "pressure_hpa": BME680_1.pressure,
                    "altitude_m": BME680_1.altitude,
                },
                "sen0114": {
                    "moisture": SEN0114_1.moisture,
                },
            },
            "2": {
                "bme680": {
                    "temperature_c": BME680_2.temperature,
                    "gas_ohm": BME680_2.gas,
                    "relativehumidity_pct": BME680_2.relativehumidity,
                    "pressure_hpa": BME680_2.pressure,
                    "altitude_m": BME680_2.altitude,
                },
                "sen0114": {
                    "moisture": SEN0114_2.moisture,
                },
            },
        },
    }


class GranularityConfig:
    """Publishing granularity settings."""

    NUM_BURSTS = 5
    INTER_BURST = 1

    SLEEP_TIME = 10
