from typing import List
from fastapi import APIRouter, Depends
from app.schemas import schemas
from app.cruds import trailCrud
from app.dependencies import get_db


router = APIRouter(
    prefix="/trails",
    tags=["Trail"],
    responses={404: {"description": "Trail not found"}}
)


@router.post(
    "/",
    response_model=schemas.Trail,
    dependencies=[Depends(get_db)],
    tags=["Trail"],
    description="Create a new Trail"
)
def create_trail(trail: schemas.TrailCreate):
    return trailCrud.create(trail=trail)


@router.get(
    "/",
    response_model=List[schemas.Trail],
    dependencies=[Depends(get_db)],
    tags=["Trail"],
    description="Find Trail by name"
)
def search_trial_by_name(name: str):
    return trailCrud.find_by_name(name=name)
