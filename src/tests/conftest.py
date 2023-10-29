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


@pytest.fixture(scope="module")
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


@pytest.fixture(scope="module")
def account_repository(session):
    account_repository = AccountRepositoryDatabase(session)
    return account_repository


@pytest.fixture(scope="module")
def ride_repository(session):
    ride_repository = RideRepositoryDatabase(session)
    return ride_repository


@pytest.fixture(scope="module")
def account(session):
    return AccountModel(
        account_id=str(uuid.uuid4()),
        is_driver=False,
        is_passenger=False,
        name="John Doe",
        email=f"{uuid.uuid4()}@example.com",
        cpf=GeradorCpf.gerar().rawValue,
        is_verified=True,
        verification_code=str(uuid.uuid4()),
        car_plate=None,
        date=datetime.utcnow(),
    )


@pytest.fixture(scope="module")
def passenger(account_repository, session, account):
    account.is_passenger = True
    session.add(account)
    session.commit()
    yield account
    rides = (
        session.query(RideModel)
        .filter(RideModel.passenger_id == account.account_id)
        .all()
    )
    for ride in rides:
        session.delete(ride)
    session.delete(account)
    session.commit()


@pytest.fixture(scope="module")
def driver(account_repository, session, account):
    account.is_driver = True
    session.add(account)
    session.commit()
    yield account
    rides = (
        session.query(RideModel)
        .filter(RideModel.passenger_id == account.account_id)
        .all()
    )
    for ride in rides:
        session.delete(ride)
    session.delete(account)
    session.commit()
