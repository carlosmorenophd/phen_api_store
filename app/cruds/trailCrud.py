from app.schemas import schemas
from app import models


def create(trail: schemas.TrailCreate):
    db_entity = models.Trail.filter(models.Trail.name == trail.name).first()
    if db_entity:
        return db_entity
    db_entity = models.Trail(name=trail.name)
    db_entity.save()
    return db_entity


def find_by_name(name: str):
    return models.Trail.filter(models.Trail.name == name).first()
