import models
import schemas


def create_web_file(web_file: schemas.WebFile):
    db_entity = models.WebFile.filter(
        models.WebFile.name == web_file.name).first()
    if db_entity:
        return db_entity
    db_save = models.WebFile(name=web_file.name)
    db_save.save()
    return db_save


def create_trail(trail: schemas.Trail):
    db_entity = models.Trail.filter(models.Trail.name == trail.name).first()
    if db_entity:
        return db_entity
    return models.Trail(name=trail.name)


def create_unit(unit: schemas.Unit):
    db_entity = models.Unit.filter(models.Unit.name == unit.name).first()
    if db_entity:
        return db_entity
    return models.Unit(name=unit.name)


def create_trait(trait: schemas.Trait):
    db_entity = models.Trait.filter(
        models.Trait.name == trait.name and models.Trait.number == trait.number)
    if db_entity:
        return db_entity
    return models.Trait(name=trait.name, number=trait.number, description=trait.description, co_trait_name=trait.co_trait_name, variable_name=trait.variable_name, co_id=trait.co_id)

def create_genotype(genotype: schemas.Genotype):
    db_entity = models.Genotype.filter(models.Genotype.c_id == genotype.c_id and models.Genotype.s_id == genotype.s_id)
    if db_entity:
        return db_entity
    return models.Genotype(c_id = genotype.c_id, s_id = genotype.s_id, cross_name = genotype.cross_name, history_name = genotype.history_name)

# class Location(Model):
#     number = IntegerField()
#     country = CharField()
#     description = TextField()
#     institute_name = CharField()
#     cooperator = CharField()
#     latitude = CharField()
#     latitude_degrees = IntegerField()
#     latitude_minutes = IntegerField()
#     longitude = CharField()
#     longitude_degrees = IntegerField()
#     longitude_minutes = IntegerField()
#     altitude = IntegerField()

#     class Meta:
#         database = db


# class CropOntology(Model):
#     ontology_db_id = CharField()
#     name = CharField()

#     class Meta:
#         database = db


# class TraitOntology(Model):
#     trait_db_id = CharField()
#     name = CharField()
#     class_family = CharField()
#     description = TextField()
#     crop_ontology = ForeignKeyField(CropOntology, backref="trait_ontologies")

#     class Meta:
#         database = db


# class MethodOntology(Model):
#     method_db_id = CharField()
#     name = CharField()
#     class_family = CharField()
#     description = TextField()
#     formula = TextField()

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
