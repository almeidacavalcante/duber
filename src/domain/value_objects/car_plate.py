import re


class CarPlate:
    _value: str

    def __init__(self, value: str):
        car_plate_pattern = r"^[A-Z]{3}-[0-9]{4}$"
        if not re.match(car_plate_pattern, value):
            raise ValueError("Invalid car plate")
        self._value = value

    @property
    def value(self):
        return self._value