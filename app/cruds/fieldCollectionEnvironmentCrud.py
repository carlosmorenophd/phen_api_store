from app import models
from app.schemas import schemas


def create(
    field_collection_environment: schemas.FieldCollectionEnvironmentCreate
):
    db_entity = models.FieldCollectionEnvironment.select().where(
        models.FieldCollectionEnvironment.field_collection.id ==
        field_collection_environment.field_collection_id and
        models.FieldCollectionEnvironment.environment_definition.id ==
        field_collection_environment.environment_definition_id and
        models.FieldCollectionEnvironment.unit.id ==
        field_collection_environment.unit_id and
        models.FieldCollectionEnvironment.value_data ==
        field_collection_environment.value_data
    ) | (models.FieldCollectionEnvironment >> None)
    if db_entity:
        return db_entity
    db_field_collection = models.FieldCollection.get_by_id(
        id=field_collection_environment.field_collection_id
    )
    if not db_field_collection:
        raise ValueError("Field collection is not valid")
    db_environment_definition = models.EnvironmentDefinition.get_by_id(
        id=field_collection_environment.environment_definition_id
    )
    if not db_environment_definition:
        raise ValueError("Environment definition is not valid")
    db_unit = models.Unit.get_by_id(
        id=field_collection_environment.unit_id
    )
    if not db_unit:
        raise ValueError("Unit is not valid")
    db_entity = models.FieldCollectionEnvironment(
        value_data=field_collection_environment.value_data,
        unit=db_unit,
        field_collection=db_field_collection,
        environment_definition=db_environment_definition
    )
    db_entity.save()
    return db_entity
