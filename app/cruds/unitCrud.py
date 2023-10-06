from app.schemas import schemas
from app import models


def get_or_create(unit: schemas.Unit):
    return models.Unit.get_or_create(
        name=unit.name
    )
