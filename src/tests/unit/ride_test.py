from src.domain.exceptions.domain_exception import DomainException
from src.domain.ride import Ride


def test_ride_creation():
    ride = Ride("passanger_id", 1.0, 1.0, 1.0, 1.0)
    assert ride.ride_id is not None
    assert True


def test_ride_acceptance():
    ride = Ride("passanger_id", 1.0, 1.0, 1.0, 1.0)
    ride.accept("driver_id")
    assert ride.status == "accepted"
    assert ride.driver_id == "driver_id"
    assert True


def test_ride_acceptance_twice():
    ride = Ride("passanger_id", 1.0, 1.0, 1.0, 1.0)
    ride.accept("driver_id")
    try:
        ride.accept("driver_id")
        assert False
    except DomainException:
        assert True

