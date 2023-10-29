import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine

from src.application import config
from src.application.routes.ride_route import ride_router
from src.application.usecase.accept_ride_usecase import AcceptRideUsecase
from src.application.usecase.get_account_usecase import GetAccountUsecase
from src.application.usecase.get_ride_usecase import GetRideUsecase
from src.application.usecase.request_ride_usecase import RequestRideUsecase
from src.infrastructure.database.manager import SessionLocal
from src.infrastructure.repository.account_repository_database import AccountRepositoryDatabase
from src.infrastructure.repository.ride_repository_database import RideRepositoryDatabase

session = SessionLocal()

account_repository = AccountRepositoryDatabase(session)
ride_rpository = RideRepositoryDatabase(session)

accept_ride_usecase = AcceptRideUsecase(ride_rpository, account_repository)
get_ride_usecase = GetRideUsecase(ride_rpository)
get_account_usecase = GetAccountUsecase(account_repository)
request_ride_usecase = RequestRideUsecase(ride_rpository, account_repository)

app = FastAPI()

app.include_router(
    ride_router(get_ride_usecase, accept_ride_usecase, request_ride_usecase),
    prefix="/api/v1/ride",
    tags=["Ride"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)



