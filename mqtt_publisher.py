"""Defines framework used for MQTT publishing."""

import json

import adafruit_minimqtt.adafruit_minimqtt as aio_mqtt

from config import DeviceConfig, MQTTConfig
from utils import eval_payload_meta


def _connect(client, userdata, flags, rc):
    """Callback upon connection to MQTT broker.

    Args:
        client (MQTT): The MQTT instance for this callback.
        userdata (Any): Private user-defined data.
        flags (dict): Message flags (QoS, retain, etc.).
        rc (int): Success if zero, failure if non-zero.

    """
    print("Connected to MQTT Broker.")


def _disconnect(client, userdata, rc):
    """Callback upon disconnection from MQTT broker.

    Args:
        client (MQTT): The MQTT instance for this callback.
        userdata (Any): Private user-defined data.
        rc (int): Success if zero, failure if non-zero.
    """
    print("Disconnected from MQTT Broker.")


def _publish(client, userdata, topic, pid):
    """Callback upon disconnection from MQTT broker.

    Args:
        client (MQTT): The MQTT instance for this callback.
        userdata (Any): Private user-defined data.
        topic (str): The topic the client published to.
        pid (int): Packet identifier.

    """
    print(f"Published to {topic}.")


class MQTTPublisher:
    """MQTT Publisher wrapper class."""

    def __init__(self, pool, ssl_context):
        """Initialise a MQTTTopic object.

        Args:
            pool (SocketPool): Pool of socket resources.
            ssl_context (SSLContext): SSL certificates and configurations.
        """
        self._mqtt_client = aio_mqtt.MQTT(
            broker=MQTTConfig.BROKER,
            port=MQTTConfig.PORT,
            username=MQTTConfig.USERNAME,
            password=MQTTConfig.PASSWORD,
            is_ssl=True,
            socket_pool=pool,
            ssl_context=ssl_context,
        )

        self._mqtt_client.on_connect = _connect
        self._mqtt_client.on_disconnect = _disconnect
        self._mqtt_client.on_publish = _publish

    def connect(self):
        """Connect to MQTT broker."""
        self._mqtt_client.connect()

    def publish(self):
        """Publish data to broker with a timestamp."""
        data = eval_payload_meta(DeviceConfig.PAYLOAD_META)
        json_payload = json.dumps(data)

        self._mqtt_client.publish(MQTTConfig.TOPIC, json_payload)
