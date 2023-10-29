from dataclasses import dataclass

from pydantic import BaseModel

from src.application.exceptions.application_exception import ApplicationException
from src.domain.ride import Ride
from src.infrastructure.repository.account_repository import AccountRepository
from src.infrastructure.repository.ride_repository import RideRepository


class Position(BaseModel):
    lat: float
    long: float


class RequestRideInput(BaseModel):
    passenger_id: str
    origin: Position
    destination: Position


class RequestRideOutput(BaseModel):
    ride_id: str


class RequestRideUsecase:
    def __init__(
        self, ride_repository: RideRepository, account_repository: AccountRepository
    ):
        self.ride_repository = ride_repository
        self.account_repository = account_repository

    def execute(self, input_data: RequestRideInput):
        account = self.account_repository.get(input_data.passenger_id)
        if not account:
            raise ApplicationException("Account not found")
        if not account.is_passenger:
            raise ApplicationException("Account is not a passenger")
        active_rides = self.ride_repository.get_active_rides_by_account_id(
            input_data.passenger_id
        )
        if len(active_rides) > 0:
            raise ApplicationException("Passanger already has an active ride")
        ride = Ride(
            passenger_id=input_data.passenger_id,
            from_lat=input_data.origin.lat,
            from_long=input_data.origin.long,
            to_lat=input_data.destination.lat,
            to_long=input_data.destination.long,
        )
        self.ride_repository.save(ride)
        return RequestRideOutput(ride_id=ride.ride_id)
