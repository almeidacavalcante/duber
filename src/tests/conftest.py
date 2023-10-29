from datetime import datetime
import uuid

from bradocs4py import GeradorCpf
import pytest

from src.infrastructure.database.manager import SessionLocal
from src.infrastructure.models import AccountModel, RideModel
from src.infrastructure.repository.account_repository_database import (
    AccountRepositoryDatabase,
)
from src.infrastructure.repository.ride_repository_database import (
    RideRepositoryDatabase,
)


@pytest.fixture(scope="function")
def session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


@pytest.fixture(scope="function")
def account_repository(session):
    account_repository = AccountRepositoryDatabase(session)
    return account_repository


@pytest.fixture(scope="function")
def ride_repository(session):
    ride_repository = RideRepositoryDatabase(session)
    return ride_repository


@pytest.fixture(scope="function")
def passenger_account(session):
    return AccountModel(
        account_id=str(uuid.uuid4()),
        is_driver=False,
        is_passenger=True,
        name="John Doe Passenger",
        email=f"{uuid.uuid4()}@example.com",
        cpf=GeradorCpf.gerar().rawValue,
        is_verified=True,
        verification_code=str(uuid.uuid4()),
        car_plate=None,
        date=datetime.utcnow(),
    )

@pytest.fixture(scope="function")
def driver_account(session):
    return AccountModel(
        account_id=str(uuid.uuid4()),
        is_driver=True,
        is_passenger=False,
        name="Mark Driver",
        email=f"{uuid.uuid4()}@example.com",
        cpf=GeradorCpf.gerar().rawValue,
        is_verified=True,
        verification_code=str(uuid.uuid4()),
        car_plate=None,
        date=datetime.utcnow(),
    )


@pytest.fixture(scope="function")
def passenger(account_repository, session, passenger_account):
    passenger_account.is_passenger = True
    session.add(passenger_account)
    session.commit()
    yield passenger_account
    rides = (
        session.query(RideModel)
        .filter(RideModel.passenger_id == passenger_account.account_id)
        .all()
    )
    for ride in rides:
        session.delete(ride)
    session.delete(passenger_account)
    session.commit()


@pytest.fixture(scope="function")
def driver(account_repository, session, driver_account):
    driver_account.is_driver = True
    session.add(driver_account)
    session.commit()
    yield driver_account
    rides = (
        session.query(RideModel)
        .filter(RideModel.driver_id == driver_account.account_id)
        .all()
    )
    for ride in rides:
        session.delete(ride)
    session.delete(driver_account)
    session.commit()
