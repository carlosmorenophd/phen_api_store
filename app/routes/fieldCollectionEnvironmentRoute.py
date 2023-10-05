from fastapi import APIRouter, Depends, HTTPException
from app import schemas
from app.cruds import fieldCollectionEnvironmentCrud
from app.dependencies import get_db


router = APIRouter(
    prefix="/field_collection_environment",
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
        return fieldCollectionEnvironmentCrud.create(
            field_collection_environment=field_collection_environment
        )
    except ValueError as err:
        raise HTTPException(
            status_code=404,
            detail="Some attributes can't be founded"
        ) from err
