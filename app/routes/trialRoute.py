from typing import List
from fastapi import APIRouter, Depends
from schemas import schemas
from cruds import trialCrud
from dependencies import get_db


router = APIRouter(
    prefix="/trials",
    tags=["Trial"],
    responses={404: {"description": "Trial not found"}}
)


@router.post(
    "/",
    response_model=schemas.Trial,
    dependencies=[Depends(get_db)],
    description="Create a new Trial"
)
def create_trial(trial: schemas.TrialCreate):
    return trialCrud.get_or_create(trial=trial)


@router.get(
    "/",
    response_model=List[schemas.Trial],
    dependencies=[Depends(get_db)],
    description="Find Trial by name"
)
def search_trial_by_name(name: str):
    return trialCrud.find_by_name(name=name)
