from fastapi import APIRouter, Depends, HTTPException
from app.schemas import schemas
from app.cruds import locationCrud
from app.dependencies import get_db


router = APIRouter(
    prefix="/locations",
    tags=["Location"],
    responses={404: {"description": "Location not found"}}
)


@router.post(
    "/",
    response_model=schemas.Location,
    dependencies=[Depends(get_db)],
    description="Create a new Location"
)
def create_location(location: schemas.LocationCreate):
    return locationCrud.create(location=location)


# TODO: adding try and catch
@router.get(
    "/",
    response_model=schemas.Location,
    dependencies=[Depends(get_db)],
    description="Find location by number"
)
def search_location_by_number(number: int):
    return locationCrud.find_by_number(number=number)


@router.get(
    "/{id}",
    response_model=schemas.Location,
    dependencies=[Depends(get_db)],
    description="Get location by id",
)
def find_location_by_id(id: int):
    try:
        return locationCrud.find_by_id(id=id)
    except ValueError as err:
        raise HTTPException(
            status_code=404, detail="Location not found") from err
