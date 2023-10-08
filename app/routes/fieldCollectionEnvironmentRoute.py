from fastapi import APIRouter, Depends, HTTPException
from app.schemas import schemas, customs
from app.cruds import fieldCollectionEnvironmentCrud
from app.dependencies import get_db
from app.services import environmentDataService


router = APIRouter(
    prefix="/field_collection_environments",
    tags=["Field Collection Environments"],
    responses={404: {"description": "Field collection environment not found"}}
)


@router.post(
    "/",
    response_model=schemas.FieldCollectionEnvironment,
    dependencies=[Depends(get_db)],
    description="Create a new field collection definition"
)
def create(
    field_collection_environment: schemas.FieldCollectionEnvironmentCreate
):
    try:
        return fieldCollectionEnvironmentCrud.get_or_create(
            field_collection_environment=field_collection_environment
        )
    except ValueError as err:
        raise HTTPException(
            status_code=404,
            detail="Some attributes can't be founded"
        ) from err


@router.post(
    "/xls",
    response_model=schemas.FieldCollectionEnvironment,
    dependencies=[Depends(get_db)],
    description="Save and storage all data",
)
def create_by_xls(environment_data: customs.EnvironmentData):
    try:
        return environmentDataService.save_environment_data(
            environment_data=environment_data
        )
    except ValueError as err:
        raise HTTPException(
            status_code=507,
            detail="Error -> {}".format(err)
        ) from err
