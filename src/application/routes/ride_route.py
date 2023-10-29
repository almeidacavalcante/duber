from fastapi import APIRouter, Query, Body
from starlette.responses import Response

from src.application.usecase.accept_ride_usecase import (
    AcceptRideUsecase,
    AcceptRideInput,
)
from src.application.usecase.get_ride_usecase import GetRideUsecase
from src.application.usecase.request_ride_usecase import (
    RequestRideInput,
    RequestRideUsecase,
)


def ride_router(
    get_ride_usecase: GetRideUsecase,
    accept_ride_usecase: AcceptRideUsecase,
    request_ride_usecase: RequestRideUsecase,
):
    router = APIRouter()

    @router.get(
        "/get_ride",
        status_code=200,
        description="Get ride",
    )
    async def get_ride(
        response: Response,
        ride_id: str = Query(..., description="Ride id"),
    ):
        try:
            output = get_ride_usecase.execute(ride_id=ride_id)
            return output
        except Exception as e:
            raise e

    @router.get(
        "/accept_ride",
        status_code=200,
        description="Accept ride",
    )
    async def get_ride(
        response: Response,
        ride_id: str = Query(..., description="Ride id"),
        driver_id: str = Query(..., description="Driver id"),
    ):
        try:
            input_data = AcceptRideInput(ride_id=ride_id, driver_id=driver_id)
            output = accept_ride_usecase.execute(input_data=input_data)
            return output
        except Exception as e:
            raise e

    @router.post(
        "/request_ride",
        status_code=200,
        description="Request ride",
    )
    async def get_ride(
        response: Response,
        payload: RequestRideInput = Body(..., description="Request Ride Paylaod"),
    ):
        try:
            output = request_ride_usecase.execute(input_data=payload)
            return output
        except Exception as e:
            raise e

    return router
