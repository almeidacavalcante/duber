from datetime import datetime
import re
import uuid

from src.domain.exceptions.domain_exception import DomainException
from src.domain.value_objects.car_plate import CarPlate
from src.domain.value_objects.cpf import CPF
from src.domain.value_objects.email import Email
from src.domain.value_objects.name import Name


class Account:
    _account_id: str
    _name: Name
    _email: Email
    _cpf: CPF
    _is_passenger: bool
    _is_driver: bool
    _car_plate: CarPlate
    _verification_code: str
    _date: datetime

    def __init__(
        self,
        name: str,
        email: str,
        cpf: str,
        is_passenger: bool,
        is_driver: bool,
        car_plate: str,
    ):
        self._validate_driver(car_plate, is_driver)
        self._account_id = str(uuid.uuid4())
        self._name = Name(name)
        self._email = Email(email)
        self._cpf = CPF(cpf)
        self._is_passenger = is_passenger
        self._is_driver = is_driver
        self._verification_code = str(uuid.uuid4())
        self._date = datetime.utcnow()

    def _validate_driver(self, car_plate, is_driver):
        if is_driver and not car_plate:
            raise DomainException("Car plate is required for drivers")
        if is_driver:
            self._car_plate = CarPlate(car_plate)

    @staticmethod
    def restore(account_id: str):
        pass

    @property
    def account_id(self):
        return self._account_id

    @property
    def is_passenger(self):
        return self._is_passenger

    @property
    def email(self):
        return self._email.value

    @property
    def name(self):
        return self._name.value

    @property
    def date(self):
        return self._date

    @property
    def car_plate(self):
        return self._car_plate.value

    @property
    def cpf(self):
        return self._cpf.value

    @property
    def is_driver(self):
        return self._is_driver

    @property
    def verification_code(self):
        return self._verification_code
