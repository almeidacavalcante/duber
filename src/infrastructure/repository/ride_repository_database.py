from typing import List

from src.domain.ride import Ride
from src.infrastructure.models import RideModel
from src.infrastructure.repository.ride_repository import RideRepository


class RideRepositoryDatabase(RideRepository):
    def __init__(self, session):
        self.session = session

    def save(self, ride: Ride):
        ride_model = self.to_orm_model(ride)
        self.session.merge(ride_model)
        self.session.commit()

    def get(self, ride_id: str) -> Ride:
        ride_model = self.session.query(RideModel).filter_by(ride_id=ride_id).first()
        return self.to_domain_entity(ride_model)

    def get_active_rides_by_account_id(self, account_id: str) -> List[Ride]:
        return self.session.query(RideModel).filter_by(passenger_id=account_id).all()

    @staticmethod
    def to_domain_entity(ride_model: RideModel) -> Ride:
        return Ride.restore(
            ride_id=ride_model.ride_id,
            passenger_id=ride_model.passenger_id,
            status=ride_model.status,
            driver_id=ride_model.driver_id,
            from_lat=ride_model.from_lat,
            from_long=ride_model.from_long,
            to_lat=ride_model.to_lat,
            to_long=ride_model.to_long,
            date=ride_model.date,
        )

    @staticmethod
    def to_orm_model(ride: Ride) -> RideModel:
        return RideModel(
            ride_id=ride.ride_id,
            passenger_id=ride.passenger_id,
            driver_id=ride.driver_id,
            from_lat=ride.from_lat,
            from_long=ride.from_long,
            to_lat=ride.to_lat,
            to_long=ride.to_long,
            status=ride.status,
            date=ride.date,
        )

