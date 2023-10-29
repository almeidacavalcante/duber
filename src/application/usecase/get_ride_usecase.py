from src.domain.ride import Ride
from src.infrastructure.repository.ride_repository import RideRepository


class GetRideUsecase:
    def __init__(self, ride_repository: RideRepository):
        self.ride_respository = ride_repository

    def execute(self, ride_id: str) -> Ride:
        return self.ride_respository.get(ride_id)
