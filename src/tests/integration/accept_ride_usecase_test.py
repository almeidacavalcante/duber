from src.application.usecase.accept_ride_usecase import AcceptRideUsecase
from src.infrastructure.database.manager import SessionLocal
from src.infrastructure.repository.account_repository_database import AccountRepositoryDatabase
from src.infrastructure.repository.ride_repository_database import RideRepositoryDatabase


class TestAcceptRideUsecase:

    def test_accept_ride(self):
        session = SessionLocal()

        account_repository = AccountRepositoryDatabase(session)
        ride_rpository = RideRepositoryDatabase(session)

        accept_ride_usecase = AcceptRideUsecase(ride_rpository, account_repository)



        accept_ride_usecase.execute()
