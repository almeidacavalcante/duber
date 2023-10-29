from sqlalchemy import UUID, Column, String, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.infrastructure.database.manager import Base


class RideModel(Base):
    __tablename__ = "rides"

    ride_id = Column(String(36), primary_key=True)
    passenger_id = Column(String(36), ForeignKey("accounts.account_id"), nullable=False)
    driver_id = Column(String(36), ForeignKey("accounts.account_id"), nullable=True)
    status = Column(String(255), nullable=False)
    fare = Column(Numeric, nullable=True)
    distance = Column(Numeric, nullable=True)
    from_lat = Column(Numeric, nullable=False)
    from_long = Column(Numeric, nullable=False)
    to_lat = Column(Numeric, nullable=False)
    to_long = Column(Numeric, nullable=False)
    date = Column(DateTime, nullable=False)

    passenger = relationship("AccountModel", foreign_keys=[passenger_id])
    driver = relationship("AccountModel", foreign_keys=[driver_id])
