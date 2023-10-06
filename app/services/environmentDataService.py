from app.schemas import customs
from app import models
from app.cruds import locationCrud, trailCrud


def save_environment_data(environment_data: customs.EnvironmentData) -> str:
    db_location = locationCrud.find_by_country_number(
        country=environment_data.location_country,
        number=environment_data.location_number,
    )
    if not db_location:
        raise ValueError("Can not find location : {}".format(
            environment_data.location_number
        ))
    db_trail = trailCrud.find_by_name(
        name=environment_data.trial_name,
    )
    if not db_trail:
        raise ValueError("Can not found trail {}".format(
            environment_data.trial_name
        ))
    environment_definition_id = models.EnvironmentDefinition.select(
        models.EnvironmentDefinition.id
    ).where(
        models.EnvironmentDefinition.name == environment_data.trait_name and
        models.EnvironmentDefinition.number == environment_data.trait_number
    ).scalar()
    if not environment_definition_id:
        db_environment_definition = models.EnvironmentDefinition(
            number=environment_data.trait_number,
            name=environment_data.trait_name
        )
        db_environment_definition.save()
        environment_definition_id = db_environment_definition.id
    unit_id = models.Unit.select(
        models.Unit.id
    ).where(
        models.Unit.name == environment_data.unit_name
    ).scalar()
    if not unit_id:
        db_unit = models.Unit(name=environment_data.unit_name)
        db_unit.save()
        unit_id = db_unit.id
    field_collection_id = models.FieldCollection.select(
        models.FieldCollection.id
    ).where(
        models.FieldCollection.occurrence == environment_data.occurrence and
        models.FieldCollection.agricultural_cycle == environment_data.agricultural_cycle and
        models.FieldCollection.location.id == db_location.id and
        models.FieldCollection.trail.id == db_trail.id and
        models.FieldCollection.description == environment_data.description
    ).scalar()
    if not field_collection_id:
        db_field_collection = models.FieldCollection(
            occurrence=environment_data.occurrence,
            agricultural_cycle=environment_data.agricultural_cycle,
            description=environment_data.description,
            location_id=db_location.id,
            trail_id=db_trail.id,
        )
        db_field_collection.save()
        field_collection_id = db_field_collection.id

    return "OK"
