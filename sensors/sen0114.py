"""Framework for the SKU: SEN0114 sensor."""

import analogio


class SEN0114Sensor:
    """Wrapper class for the SEN0114 sensor."""

    def __init__(self, pin):
        """Initialise a SEN0114Sensor object.

        Args:
            pin (Pin): The analog input pin used by the sensor.
        """
        self.analogin = analogio.AnalogIn(pin)

    def moisture(self):
        """Soil moisture indicator.

        Returns:
            int: The raw analog input pin reading (unsigned 16 bit integer).
        """
        return self.analogin.value
