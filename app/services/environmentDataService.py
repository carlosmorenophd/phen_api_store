from app.schemas import customs, schemas
from app.cruds import (
    environmentDefinitionCrud,
    fieldCollectionCrud,
    fieldCollectionEnvironmentCrud,
    locationCrud,
    trailCrud,
    unitCrud,
    webFileCrud,
)


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
    db_environment_definition = environmentDefinitionCrud.get_or_create(
        environment_definition=schemas.EnvironmentDefinitionCreate(
            name=environment_data.trait_name,
            number=environment_data.trait_number,
        )
    )
    db_unit = unitCrud.get_or_create(
        unit=schemas.UnitCreate(
            name=environment_data.unit_name,
        )
    )
    db_web_file = webFileCrud.get_or_create(
        web_file=schemas.WebFileCreate(
            name=environment_data.web_file_name
        )
    )
    db_field_collection = fieldCollectionCrud.get_or_create(
        field_collection=schemas.FieldCollectionCreate(
            agricultural_cycle=environment_data.agricultural_cycle,
            description=environment_data.description,
            location_id=db_location.id,
            occurrence=environment_data.occurrence,
            trail_id=db_trail.id,
            web_file_id=db_web_file.id,
        )
    )
    db_field_collection_environment = fieldCollectionEnvironmentCrud.get_or_create(
        field_collection_environment=schemas.FieldCollectionEnvironmentCreate(
            value_data=environment_data.value_data,
            environment_definition_id=db_environment_definition.id,
            field_collection_id=db_field_collection.id,
            unit_id=db_unit.id
        )
    )
    print("Result:::", db_field_collection_environment,
          type(db_field_collection_environment))
    return db_field_collection_environment
