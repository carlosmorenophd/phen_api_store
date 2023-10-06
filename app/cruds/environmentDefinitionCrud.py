from app import models
from app.schemas import schemas


def get_or_create(
    environment_definition: schemas.EnvironmentDefinitionCreate
):
    return models.EnvironmentDefinition.get_or_create(
        name=environment_definition.name,
        number=environment_definition.number,
    )
