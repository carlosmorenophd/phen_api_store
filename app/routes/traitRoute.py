from fastapi import APIRouter, Depends, HTTPException
from schemas import schemas
from cruds import traitCrud
from dependencies import get_db


router = APIRouter(
    prefix="/traits",
    tags=["Trait"],
    responses={404: {"description": "Trait not found"}}
)


@router.post(
    "/",
    response_model=schemas.Trait,
    dependencies=[Depends(get_db)],
    description="Create a new Trait"
)
def create(trait: schemas.TraitCreate):
    return traitCrud.get_or_create(trait=trait)


@router.get(
    "/",
    response_model=schemas.Trait,
    dependencies=[Depends(get_db)],
)
def find_by_name(name: str):
    try:
        return traitCrud.find_by_name(name=name)
    except ValueError as err:
        raise HTTPException(
            status_code=404,
            detail="Trait not found"
        ) from err


@router.put(
    "/{id}",
    response_model=schemas.Trait,
    dependencies=[Depends(get_db)],
)
def update(id: int, trait: schemas.TraitCreate):
    try:
        return traitCrud.update(id=id, trait=trait)
    except ValueError as err:
        raise HTTPException(
            status_code=404,
            detail="Trait not found"
        ) from err


@router.get(
    "/{id}",
    response_model=schemas.Trait,
    dependencies=[Depends(get_db)],
    description="Get trait by id",
)
def find_by_id(id: int):
    try:
        return traitCrud.find_by_id(id=id)
    except ValueError as err:
        raise HTTPException(
            status_code=404,
            detail="Trait not found"
        ) from err
