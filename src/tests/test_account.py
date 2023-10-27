from random import random

from src.domain.account import Account
from src.domain.exceptions.domain_exception import DomainException


def test_accounte_creation():
    account = Account(
        "John Doe",
        f"{random()}@gmail.com",
        "93306816035",
        True,
        False,
        "",
    )
    assert account.account_id is not None
    assert True


def test_accounte_creation_with_invalid_email():
    try:
        account = Account(
            "John Doe",
            "invalid_email",
            "93306816035",
            True,
            False,
            "",
        )
        assert False
    except DomainException:
        assert True


def test_accounte_creation_with_invalid_cpf():
    try:
        account = Account(
            "John Doe",
            f"{random()}@gmail.com",
            "invalid_cpf",
            True,
            False,
            "",
        )
        assert False
    except DomainException:
        assert True


def test_accounte_creation_with_invalid_car_plate():
    try:
        account = Account(
            "John Doe",
            f"{random()}@gmail.com",
            "93306816035",
            True,
            True,
            "invalid_car_plate",
        )
        assert False
    except DomainException:
        assert True

