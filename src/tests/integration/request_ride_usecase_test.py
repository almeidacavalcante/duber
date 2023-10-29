import uuid

from src.application.exceptions.application_exception import ApplicationException
from src.application.usecase.get_ride_usecase import GetRideUsecase
from src.application.usecase.request_ride_usecase import (
    RequestRideInput,
    Position,
    RequestRideUsecase,
)
from src.infrastructure.repository.ride_repository_database import (
    RideRepositoryDatabase,
)


class TestRequestRideUsecase:
    def test_request_ride(self, account_repository, session, passenger):
        ride_rpository = RideRepositoryDatabase(session)
        get_ride_usecase = GetRideUsecase(ride_rpository)
        request_ride_usecase = RequestRideUsecase(ride_rpository, account_repository)

        input_data = RequestRideInput(
            passenger_id=str(passenger.account_id),
            origin=Position(lat=-20, long=-21),
            destination=Position(lat=20, long=21),
        )
        output = request_ride_usecase.execute(input_data=input_data)
        ride = get_ride_usecase.execute(ride_id=output.ride_id)

        assert ride.ride_id == output.ride_id
        assert ride.passenger_id == passenger.account_id
        assert ride.from_lat == input_data.origin.lat
        assert ride.from_long == input_data.origin.long
        assert ride.to_lat == input_data.destination.lat
        assert ride.to_long == input_data.destination.long
        assert ride.driver_id is None
        assert ride.status == "requested"

    def test_request_ride_with_invalid_passenger_id(self, account_repository, session, passenger):
        ride_rpository = RideRepositoryDatabase(session)
        request_ride_usecase = RequestRideUsecase(ride_rpository, account_repository)

        input_data = RequestRideInput(
            passenger_id=str(uuid.uuid4()),
            origin=Position(lat=-20, long=-21),
            destination=Position(lat=20, long=21),
        )
        try:
            request_ride_usecase.execute(input_data=input_data)
            assert False
        except ApplicationException as e:
            assert str(e) == "Account not found"

    def test_request_ride_with_invalid_passenger_type(self, account_repository, session, passenger):
        ride_rpository = RideRepositoryDatabase(session)
        request_ride_usecase = RequestRideUsecase(ride_rpository, account_repository)

        input_data = RequestRideInput(
            passenger_id=str(passenger.account_id),
            origin=Position(lat=-20, long=-21),
            destination=Position(lat=20, long=21),
        )
        passenger.is_passenger = False
        try:
            request_ride_usecase.execute(input_data=input_data)
            assert False
        except ApplicationException as e:
            assert str(e) == "Account is not a passenger"

    def test_request_ride_with_active_ride(self, account_repository, session, passenger):
        ride_rpository = RideRepositoryDatabase(session)
        request_ride_usecase = RequestRideUsecase(ride_rpository, account_repository)

        input_data = RequestRideInput(
            passenger_id=str(passenger.account_id),
            origin=Position(lat=-20, long=-21),
            destination=Position(lat=20, long=21),
        )
        output = request_ride_usecase.execute(input_data=input_data)

        try:
            request_ride_usecase.execute(input_data=input_data)
            assert False
        except ApplicationException as e:
            assert str(e) == "Passanger already has an active ride"
