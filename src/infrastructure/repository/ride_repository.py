from abc import abstractmethod, ABC

from src.domain.ride import Ride


class RideRepository(ABC):
    @abstractmethod
    def save(self, ride: Ride):
        pass

    @abstractmethod
    def get(self, ride_id: str):
        pass

    @abstractmethod
    def get_active_rides_by_account_id(self, passanger_id: str):
        pass
