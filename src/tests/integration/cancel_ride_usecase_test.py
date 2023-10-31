import uuid

from src.application.exceptions.application_exception import ApplicationException
from src.application.usecase.cancel_ride_usecase import CancelRideUsecase, CancelRideInput
from src.application.usecase.get_ride_usecase import GetRideUsecase
from src.application.usecase.request_ride_usecase import RequestRideUsecase, RequestRideInput, Position
from src.infrastructure.repository.ride_repository_database import RideRepositoryDatabase


class TestCancelRideUsecase:
    def test_request_ride(self, account_repository, session, passenger):
        ride_repository = RideRepositoryDatabase(session)
        get_ride_usecase = GetRideUsecase(ride_repository)
        request_ride_usecase = RequestRideUsecase(ride_repository, account_repository)

        input_data = RequestRideInput(
            passenger_id=str(passenger.account_id),
            origin=Position(lat=-20, long=-21),
            destination=Position(lat=20, long=21),
        )
        output = request_ride_usecase.execute(input_data=input_data)

        cancel_ride_usecase = CancelRideUsecase(ride_repository=ride_repository)
        cancel_ride_usecase.execute(CancelRideInput(
            ride_id=output.ride_id,
            passenger_id=passenger.account_id
        ))

        ride = get_ride_usecase.execute(ride_id=output.ride_id)
        assert ride.status == "cancelled"
