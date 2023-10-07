from fastapi import APIRouter, Depends, HTTPException
from app.schemas import schemas
from app.cruds import fieldCollectionCrud
from app.dependencies import get_db


router = APIRouter(
    prefix="/field_collections",
    tags=["Field Collection"],
    responses={404: {"description": "Field not found"}}
)


@router.post(
    "/",
    response_model=schemas.FieldCollection,
    dependencies=[Depends(get_db)],
    description="Create a new field collection"
)
def create(field_collection: schemas.FieldCollectionCreate):
    try:
        return fieldCollectionCrud.create(field_collection=field_collection)
    except ValueError as err:
        raise HTTPException(
            status_code=404,
            detail="Some attributes can't be founded"
        ) from err
