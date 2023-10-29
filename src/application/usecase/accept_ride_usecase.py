from dataclasses import dataclass

from pydantic import BaseModel

from src.application.exceptions.application_exception import ApplicationException
from src.infrastructure.repository.account_repository import AccountRepository
from src.infrastructure.repository.ride_repository import RideRepository


class AcceptRideInput(BaseModel):
    ride_id: str
    driver_id: str


class AcceptRideOutput(BaseModel):
    ride_id: str
    driver_id: str


class AcceptRideUsecase:
    def __init__(
        self, ride_repository: RideRepository, account_repository: AccountRepository
    ):
        self.account_repository = account_repository
        self.ride_repository = ride_repository

    def execute(self, input_data: AcceptRideInput) -> AcceptRideOutput:
        account = self.account_repository.get(input_data.driver_id)
        if not account:
            raise ApplicationException("Account not found")
        if not account.is_driver:
            raise ApplicationException("Account is not a driver")
        ride = self.ride_repository.get(input_data.ride_id)
        ride.accept(input_data.driver_id)
        active_rides = self.ride_repository.get_active_rides_by_account_id(
            input_data.driver_id
        )
        if len(active_rides) > 0:
            raise ApplicationException("Driver already has an active ride")
        self.ride_repository.save(ride)
