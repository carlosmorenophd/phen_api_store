import models
import schemas


def create_web_file(web_file: schemas.WebFile):
    db_find = models.WebFile.filter(models.WebFile.name == web_file.name).first()
    if db_find:
        return db_find
    db_entity = models.WebFile(name=web_file.name)
    db_entity.save()
    return db_entity


def create_trail(trail: schemas.Trail):
    db_entity = models.Trail.filter(models.Trail.name == trail.name).first()
    if db_entity:
        return db_entity
    db_entity = models.Trail(name=trail.name)
    db_entity.save()
    return db_entity


def create_unit(unit: schemas.Unit):
    db_entity = models.Unit.filter(models.Unit.name == unit.name).first()
    if db_entity:
        return db_entity
    db_entity = models.Unit(name=unit.name)
    db_entity.save()
    return db_entity


def create_trait(trait: schemas.Trait):
    db_entity = models.Trait.filter(
        models.Trait.name == trait.name and models.Trait.number == trait.number
    ).first()
    if db_entity:
        return db_entity
    db_entity = models.Trait(
        name=trait.name,
        number=trait.number,
        description=trait.description,
        co_trait_name=trait.co_trait_name,
        variable_name=trait.variable_name,
        co_id=trait.co_id,
    )
    db_entity.save()
    return db_entity


def create_genotype(genotype: schemas.Genotype):
    db_entity = models.Genotype.filter(
        models.Genotype.c_id == genotype.c_id and models.Genotype.s_id == genotype.s_id
    ).first()
    if db_entity:
        return db_entity
    db_entity = models.Genotype(
        c_id=genotype.c_id,
        s_id=genotype.s_id,
        cross_name=genotype.cross_name,
        history_name=genotype.history_name,
    )
    db_entity.save()
    return db_entity


def create_location(location: schemas.Location):
    db_entity = models.Location.filter(
        models.Location.number == location.number
    ).first()
    if db_entity:
        return db_entity
    db_entity = models.Location(
        number=location.number,
        country=location.country,
        description=location.description,
        institute_name=location.institute_name,
        cooperator=location.cooperator,
        latitude=location.latitude,
        latitude_degrees=location.latitude_degrees,
        latitude_minutes=location.latitude_minutes,
        longitude=location.longitude,
        longitude_degrees=location.longitude_degrees,
        longitude_minutes=location.longitude_minutes,
        altitude=location.altitude,
    )
    db_entity.save()
    return db_entity


def create_crop_ontology(crop_ontology: schemas.CropOntology):
    db_entity = models.CropOntology.filter(
        models.CropOntology.name == crop_ontology.name
    ).first()
    if db_entity:
        return db_entity
    db_entity = models.CropOntology(
        name=crop_ontology.name, ontology_db_id=crop_ontology.ontology_db_id
    )
    db_entity.save()
    return db_entity


def create_trait_ontology(trait_ontology: schemas.TraitOntology):
    db_entity = models.TraitOntology.filter(
        models.TraitOntology.trait_db_id == trait_ontology.trait_db_id
    ).first()
    if db_entity:
        return db_entity
    crop_ontology = models.CropOntology.filter(id == trait_ontology.crop_ontology_id)
    db_entity = models.TraitOntology(
        trait_db_id=trait_ontology.trait_db_id,
        name=trait_ontology.name,
        class_family=trait_ontology.class_family,
        description=trait_ontology.description,
        crop_ontology=crop_ontology,
    )
    db_entity.save()
    return db_entity


def create_method_ontology(entity: schemas.MethodOntology):
    db_entity = models.MethodOntology.filter(
        models.MethodOntology.method_db_id == entity.method_db_id
    ).first()
    if db_entity:
        return db_entity
    db_entity = models.MethodOntology(
        method_db_id=entity.method_db_id,
        name=entity.name,
        class_family=entity.class_family,
        description=entity.description,
        formula=entity.formula,
    )
    db_entity.save()
    return db_entity


# class MethodOntology(Model):


#     class Meta:
#         database = db


# class ScaleOntology(Model):
#     scale_db_id = CharField(unique=True, index=True)
#     name = CharField()
#     dataType = CharField()
#     validValues = TextField()

#     class Meta:
#         database = db


# class VariableOntology(Model):
#     name = CharField()
#     synonyms = TextField()
#     growth_stage = TextField()
#     observation_variable_db_id = CharField()
#     trait_ontology = ForeignKeyField(TraitOntology, backref="variable_ontologies")
#     trait = ForeignKeyField(Trait, backref="variable_ontology")
#     method_ontology = ForeignKeyField(MethodOntology, backref="variable_ontologies")
#     scale_ontology = ForeignKeyField(ScaleOntology, backref="variable_ontologies")

#     class Meta:
#         database = db


# class RawCollection(Model):
#     occurrence = IntegerField()
#     cycle = CharField()
#     gen_number = IntegerField()
#     repetition = IntegerField()
#     sub_block = IntegerField()
#     value_data = CharField()
#     trail = ForeignKeyField(Trail, backref="raw_collections")
#     trait = ForeignKeyField(Trait, backref="raw_collections")
#     genotype = ForeignKeyField(Genotype, backref="raw_collections")
#     location = ForeignKeyField(Location, backref="raw_collections")
