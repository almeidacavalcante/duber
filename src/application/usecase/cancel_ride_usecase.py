from typing import Optional

from pydantic import BaseModel

from src.application.exceptions.application_exception import ApplicationException
from src.infrastructure.repository.ride_repository import RideRepository


class CancelRideInput(BaseModel):
    ride_id: str


class CancelRideOutput(BaseModel):
    ride_id: str


class CancelRideUsecase:
    def __init__(self, ride_repository: RideRepository):
        self.ride_repository = ride_repository

    def execute(self, input_data: CancelRideInput):
        ride = self.ride_repository.get(input_data.ride_id)
        ride.cancel()
        self.ride_repository.save(ride)
        return CancelRideOutput(ride_id=ride.ride_id)
