"""Framework for the Bosch Sensortec BME680 sensor."""

import adafruit_bme680
import busio


class BME680Sensor:
    """Wrapper class for the BME680 sensor."""

    def __init__(self, scl, sda, temperature_offset=0, address=0x76):
        """Initialise a BME680Sensor object.

        Args:
            scl (Pin): SCL pin.
            sda (Pin): SDA pin.
            temperature_offset (float, optional): Optional offset for
                temperature reading, determined upon calibration.
            address (int): Address of the device.
        """
        bme260_i2c = busio.I2C(scl, sda)
        bme680 = adafruit_bme680.Adafruit_BME680_I2C(
            bme260_i2c, address=address
        )

        # Calibrate using Toronto's pressure (hPa) at sea level
        bme680.sea_level_pressure = 1013.4
        self._temperature_offset = temperature_offset
        self._sensor = bme680

    def temperature(self):
        """Measured temperature.

        Returns:
            float: Temperature in degrees Celsius.
        """
        return self._sensor.temperature + self._temperature_offset

    def gas(self):
        """Measured air quality.

        Returns:
            float: Gas resistance in Ohms.
        """
        return self._sensor.gas

    def relativehumidity(self):
        """Measured relative humidity.

        Returns:
            float: Relative humidity percentage.
        """
        return self._sensor.relative_humidity

    def pressure(self):
        """Measured pressure.

        Returns:
            float: Air pressure in hectopascals.
        """
        return self._sensor.pressure

    def altitude(self):
        """Measured altitude.

        Returns:
            float: Altitude in metres.
        """
        return self._sensor.altitude
