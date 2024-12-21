from fastapi import APIRouter, Depends, HTTPException
from schemas import schemas
from cruds import environmentDefinitionCrud
from dependencies import get_db


router = APIRouter(
    prefix="/environment_definitions",
    tags=["Environment definition"],
    responses={404: {"description": "Environment definition not found"}}
)


@router.post(
    "/",
    response_model=schemas.EnvironmentDefinition,
    dependencies=[Depends(get_db)],
    description="Create a new environment definition"
)
def create(environment_definition: schemas.EnvironmentDefinitionCreate):
    try:
        return environmentDefinitionCrud.get_or_create(
            environment_definition=environment_definition
        )
    except ValueError as err:
        raise HTTPException(
            status_code=404,
            detail="Some attributes can't be founded"
        ) from err
