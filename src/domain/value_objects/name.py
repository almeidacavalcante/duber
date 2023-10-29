import re


class Name:
    _value: str

    def __init__(self, value: str):
        name_pattern = r"^([a-zA-Z]{2,}\s){1,}[a-zA-Z]{2,}$"
        if not re.match(name_pattern, value):
            raise ValueError("Invalid name")
        self._value = value

    @property
    def value(self):
        return self._value
