import re


class Email:
    _value: str

    def __init__(self, value: str):
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_pattern, value):
            raise ValueError("Invalid email")
        self._value = value

    @property
    def value(self):
        return self._value
