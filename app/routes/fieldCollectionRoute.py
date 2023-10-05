from fastapi import APIRouter, Depends, HTTPException
from app import schemas, database
from app.database import db_state_default
from app.cruds import fieldCollectionCrud


router = APIRouter(
    prefix="/field_collection",
    tags=["Field Collection"],
    responses={404: {"description": "Field not found"}}
)


async def reset_db_state():
    database.db._state._state.set(db_state_default.copy())
    database.db._state.reset()


def get_db(db_state=Depends(reset_db_state)):
    try:
        database.db.connect()
        yield
    finally:
        if not database.db.is_closed():
            database.db.close()


@router.post(
    "/",
    response_model=schemas.FieldCollection,
    dependencies=[Depends(get_db)]
)
def create(field_collection: schemas.FieldCollectionCreate):
    try:
        return fieldCollectionCrud.create(field_collection=field_collection)
    except ValueError as err:
        raise HTTPException(
            status_code=404, detail="Crop trait not found") from err
