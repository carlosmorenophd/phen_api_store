from app import models, schemas


def create(field_collection: schemas.FieldCollectionCreate):
    db_entity = models.FieldCollection.select().where(
        models.FieldCollection.location.id == field_collection.location_id and
        models.FieldCollection.trail.id == field_collection.trail_id and
        models.FieldCollection.occurrence == field_collection.occurrence and
        models.FieldCollection.cycle_year == field_collection.cycle_year
    ) | (models.FieldCollection >> None)
    if db_entity:
        return db_entity
    db_location = models.Location.get_by_id(
        id=field_collection.location_id) | (models.Location >> None)
    if not db_location:
        raise ValueError("Location is not valid")
    db_trail = models.Trail.get_by_id(
        id=field_collection.trail_id) | (models.Trail >> None)
    if not db_trail:
        raise ValueError("Trail is not valid")
    db_entity = models.FieldCollection(
        occurrence=field_collection.occurrence,
        gen_number=field_collection.gen_number,
        cycle_year=field_collection.cycle_year,
        location=db_location,
        trail=db_trail,
    )
    db_entity.save()
    return db_entity
