from app import models, schemas


def create(
    environment_definition: schemas.EnvironmentDefinitionCreate
):
    db_entity = models.EnvironmentDefinition.select().where(
        models.EnvironmentDefinition.trait_no ==
        environment_definition.trait_no and
        models.EnvironmentDefinition.trait_name ==
        environment_definition.trait_name
    ) | (models.EnvironmentDefinition >> None)
    if db_entity:
        return db_entity
    db_entity = models.EnvironmentDefinition(
        trait_no=environment_definition.trait_no,
        trait_name=environment_definition.trait_name,
    )
    db_entity.save()
    return db_entity
