from app import models
from app.schemas import schemas


def get_or_create(field_collection: schemas.FieldCollectionCreate):
    db_location = models.Location.get_by_id(
        id=field_collection.location_id)
    if not db_location:
        raise ValueError("Location is not valid")
    db_trail = models.Trail.get_by_id(
        id=field_collection.trail_id)
    if not db_trail:
        raise ValueError("Trail is not valid")
    db_entity = models.FieldCollection.select().where(
        models.FieldCollection.location.id == field_collection.location_id and
        models.FieldCollection.trail.id == field_collection.trail_id and
        models.FieldCollection.occurrence == field_collection.occurrence and
        models.FieldCollection.description == field_collection.description and
        models.FieldCollection.agricultural_cycle == field_collection.agricultural_cycle
    )
    if db_entity:
        return db_entity
    db_entity = models.FieldCollection(
        occurrence=field_collection.occurrence,
        description=field_collection.description,
        agricultural_cycle=field_collection.agricultural_cycle,
        location=db_location,
        trail=db_trail,
    )
    db_entity.save()
    return db_entity
