from fastapi import APIRouter, Depends, HTTPException
from app.schemas import customs
from app.dependencies import get_db
from app.services import environmentDataService


router = APIRouter(
    prefix="/environment_data",
    tags=["Environment file xls"],
)


@router.post(
    "/",
    response_model=str,
    dependencies=[Depends(get_db)],
    description="Save and storage all data",
)
def create(environment_data: customs.EnvironmentData):
    try:
        return environmentDataService.save_environment_data(
            environment_data=environment_data
        )
    except ValueError as err:
        raise HTTPException(
            status_code=507,
            detail="Error -> {}".format(err)
        ) from err
