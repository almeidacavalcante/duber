from src.domain.document_validators import DocumentValidators


class CPF:
    _value: str

    def __init__(self, value: str):
        if not DocumentValidators.is_valid_cpf(value):
            raise ValueError("Invalid CPF")
        self._value = value

    @property
    def value(self):
        return self._value