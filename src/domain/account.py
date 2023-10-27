from datetime import datetime
import re
import uuid

from src.domain.document_validators import DocumentValidators
from src.domain.exceptions.domain_exception import DomainException


class Account:
    _account_id: str
    _name: str
    _email: str
    _cpf: str
    _is_passanger: bool
    _is_driver: bool
    _car_plate: str
    _verification_code: str
    _date: datetime

    def __init__(
        self,
        name: str,
        email: str,
        cpf: str,
        is_passanger: bool,
        is_driver: bool,
        car_plate: str,
    ):
        self._validate_name(name)
        self._validate_email(email)
        self._validate_cpf(cpf)
        self._validate_car_plate(car_plate, is_driver)
        self._account_id = str(uuid.uuid4())
        self._name = name
        self._email = email
        self._cpf = cpf
        self._is_passanger = is_passanger
        self._is_driver = is_driver
        self._car_plate = car_plate
        self._verification_code = str(uuid.uuid4())
        self._date = datetime.utcnow()

    @staticmethod
    def _validate_car_plate(car_plate, is_driver):
        if is_driver and not car_plate:
            raise DomainException("Car plate is required for drivers")
        car_plate_pattern = r"^[a-zA-Z]{3}-[0-9]{4}$"
        if is_driver and not re.match(car_plate_pattern, car_plate):
            raise DomainException("Invalid car plate")

    @staticmethod
    def _validate_cpf(cpf):
        if not DocumentValidators.is_valid_cpf(cpf):
            raise DomainException("Invalid CPF")

    @staticmethod
    def _validate_email(email):
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_pattern, email):
            raise DomainException("Invalid email")

    @staticmethod
    def _validate_name(name):
        name_pattern = r"^([a-zA-Z]{2,}\s){1,}[a-zA-Z]{2,}$"
        if not re.match(name_pattern, name):
            raise DomainException("Invalid name")

    @staticmethod
    def restore(account_id: str):
        pass

    @property
    def account_id(self):
        return self._account_id

    @property
    def is_passanger(self):
        return self._is_passanger

    @property
    def email(self):
        return self._email

    @property
    def name(self):
        return self._name

    @property
    def date(self):
        return self._date

    @property
    def car_plate(self):
        return self._car_plate

    @property
    def cpf(self):
        return self._cpf

    @property
    def is_driver(self):
        return self._is_driver

    @property
    def verification_code(self):
        return self._verification_code
