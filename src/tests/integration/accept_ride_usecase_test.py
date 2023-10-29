from src.application.usecase.accept_ride_usecase import AcceptRideUsecase, AcceptRideInput
from src.application.usecase.request_ride_usecase import RequestRideUsecase, RequestRideInput, Position


class TestAcceptRideUsecase:

    def test_accept_ride(self, account_repository, ride_repository, passenger, driver):
        accept_ride_usecase = AcceptRideUsecase(ride_repository, account_repository)
        request_ride_usecase = RequestRideUsecase(ride_repository, account_repository)

        input_data = RequestRideInput(
            passenger_id=str(passenger.account_id),
            origin=Position(lat=-20, long=-21),
            destination=Position(lat=20, long=21),
        )
        output = request_ride_usecase.execute(input_data=input_data)
        accept_ride_output = accept_ride_usecase.execute(AcceptRideInput(
            ride_id=output.ride_id,
            driver_id=str(driver.account_id)
        ))

        assert accept_ride_output.ride_id == output.ride_id

