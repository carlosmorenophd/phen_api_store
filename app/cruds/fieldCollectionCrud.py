from app import models, schemas


def create(field_collection: schemas.FieldCollectionCreate):
    db_entity = models.FieldCollection.select().where(
        models.FieldCollection.genotype.id == field_collection.genotype_id and
        models.FieldCollection.location.id == field_collection.location_id and
        models.FieldCollection.cycle == field_collection.cycle
    ) | (models.FieldCollection >> None)
    if db_entity:
        return db_entity
    db_genotype = models.Genotype.get_by_id(
        id=field_collection.genotype_id) | (models.Genotype >> None)
    if not db_genotype:
        raise ValueError("Genotype is not valid")
    db_location = models.Location.get_by_id(
        id=field_collection.location_id) | (models.Location >> None)
    if not db_location:
        raise ValueError("Location is not valid")
    db_entity = models.FieldCollection(
        gen_number=field_collection.gen_number,
        cycle=field_collection.cycle,
        genotype=db_genotype,
        location=db_location
    )
    db_entity.save()
    return db_entity
