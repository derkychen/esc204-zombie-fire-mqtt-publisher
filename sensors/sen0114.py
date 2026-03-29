"""sensors/sen0114.py.

Framework for the SKU: SEN0114 sensor.
"""

import analogio


class SEN0114Sensor:
    def __init__(self, pin):
        """Initialise a SEN0114Sensor object with an AnalogIn pin."""
        self.analogin = analogio.AnalogIn(pin)

    def moisture(self):
        """Return the raw AnalogIn pin reading."""
        return self.analogin.value
