from datetime import datetime
import uuid

from src.domain.exceptions.domain_exception import DomainException


class Ride:
    _ride_id: str
    _passenger_id: str
    _driver_id: str
    _from_lat: float
    _from_long: float
    _to_lat: float
    _to_long: float
    _status: str

    def __init__(
        self,
        passenger_id: str,
        from_lat: float,
        from_long: float,
        to_lat: float,
        to_long: float,
    ):
        self._ride_id = str(uuid.uuid4())
        self._status = "requested"
        self._date = datetime.utcnow()
        self._passenger_id = passenger_id
        self._driver_id = None
        self._from_lat = from_lat
        self._from_long = from_long
        self._to_lat = to_lat
        self._to_long = to_long

    @classmethod
    def restore(
        cls,
        ride_id: str,
        passenger_id: str,
        driver_id: str,
        from_lat: float,
        from_long: float,
        to_lat: float,
        to_long: float,
        status: str,
        date: datetime,
    ):
        ride = cls(
            passenger_id=passenger_id,
            from_lat=from_lat,
            from_long=from_long,
            to_lat=to_lat,
            to_long=to_long,
        )
        ride._ride_id = ride_id
        ride._driver_id = driver_id
        ride._status = status
        ride._date = date
        return ride

    def accept(self, driver_id: str):
        if self._status != "requested":
            raise DomainException("Ride is not requested")
        self._status = "accepted"
        self._driver_id = driver_id

    @property
    def ride_id(self):
        return self._ride_id

    @property
    def passenger_id(self):
        return self._passenger_id

    @property
    def driver_id(self):
        return self._driver_id

    @property
    def to_lat(self):
        return self._to_lat

    @property
    def from_lat(self):
        return self._from_lat

    @property
    def date(self):
        return self._date

    @property
    def to_long(self):
        return self._to_long

    @property
    def status(self):
        return self._status

    @property
    def from_long(self):
        return self._from_long
