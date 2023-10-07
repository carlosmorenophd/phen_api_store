from typing import List
from fastapi import APIRouter, Depends
from app.schemas import schemas
from app.cruds import unitCrud
from app.dependencies import get_db


router = APIRouter(
    prefix="/units",
    tags=["Unit"],
    responses={404: {"description": "Unit not found"}}
)


@router.post(
    "/",
    response_model=schemas.Unit,
    dependencies=[Depends(get_db)]
)
def create_unit(unit: schemas.UnitCreate):
    return unitCrud.get_or_create(unit=unit)
