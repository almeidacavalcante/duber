from sqlalchemy import Column, String, Boolean, DateTime, UUID

from src.infrastructure.database.manager import Base


class AccountModel(Base):
    __tablename__ = 'accounts'

    account_id = Column(String(36), primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    cpf = Column(String(11), nullable=False)
    is_passenger = Column(Boolean, nullable=False)
    is_driver = Column(Boolean, nullable=False)
    car_plate = Column(String(7), nullable=True)
    date = Column(DateTime, nullable=False)
    is_verified = Column(Boolean, nullable=False)
    verification_code = Column(String(255), nullable=False)
