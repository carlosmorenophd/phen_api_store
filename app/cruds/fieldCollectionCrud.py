from app import models
from app.schemas import schemas


def get_or_create(
    field_collection: schemas.FieldCollectionCreate
):
    db_location = models.Location.get_by_id(
        field_collection.location_id
    )
    if not db_location:
        raise ValueError("Location is not valid")
    db_trial = models.Trial.get_by_id(
        field_collection.trial_id
    )
    if not db_trial:
        raise ValueError("Trial is not valid")
    db_web = models.WebFile.get_by_id(
        field_collection.web_file_id
    )
    if not db_web:
        raise ValueError("Web file is not valid")
    return get_or_create_object(
        field_collection=models.FieldCollection(
            agricultural_cycle=field_collection.agricultural_cycle,
            description=field_collection.description,
            location=db_location,
            occurrence=field_collection.occurrence,
            trial=db_trial,
            web_file=db_web,
        )
    )


def get_or_create_object(field_collection: models.FieldCollection):
    db_entity = models.FieldCollection.select().where(
        models.FieldCollection.location == field_collection.location &
        models.FieldCollection.trial == field_collection.trial &
        models.FieldCollection.occurrence == field_collection.occurrence &
        models.FieldCollection.description == field_collection.description &
        models.FieldCollection.web_file == field_collection.web_file &
        models.FieldCollection.agricultural_cycle ==
        field_collection.agricultural_cycle
    ).first()
    if db_entity:
        return db_entity
    field_collection.save()
    return field_collection


def find_by_raw_data(
    occurrence: int,
    description: str,
    agricultural_cycle: str,
    web_file: models.WebFile,
    trial: models.Trial,
    location: models.Location,
):
    db_entity = models.FieldCollection.select().where(
        models.FieldCollection.occurrence == occurrence &
        models.FieldCollection.agricultural_cycle == agricultural_cycle &
        models.FieldCollection.web_file == web_file &
        models.FieldCollection.description == description &
        models.FieldCollection.trial == trial &
        models.FieldCollection.location == location
    ).first()
    if not db_entity:
        raise ValueError("Can't found field collection {}, {}, {}".format(
            occurrence, agricultural_cycle, web_file.id))
    return db_entity
