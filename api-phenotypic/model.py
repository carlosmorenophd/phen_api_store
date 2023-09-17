from peewee import Model, CharField, ForeignKeyField, IntegerField, FixedCharField, TextField
# import peewee
from database import db


# class Item(Model):
#     title = CharField(index=True)
#     description = CharField(index=True)
#     owner = peewee.ForeignKeyField(User, backref="items")

#     class Meta:
#         database = db

class WebFile(Model):
    name = CharField()

    class Meta:
        database = db

class Trail(Model):
    name = CharField(unique=True, index=True)

    class Meta:
        database = db

class Unit(Model):
    name = CharField(unique=True, index=True)

    class Meta:
        database = db


class Trait(Model):
    __tablename__ = 'Trait'
    name = CharField(unique=True, index=True)
    number = CharField()
    description = FixedCharField()
    co_trait_name = CharField(index=True)
    variable_name = CharField()
    co_id = CharField()
    # variable_ontology = ForeignKeyField(VariableOntology, backref="traits")

    class Meta:
        database = db


class Genotype(Model):
    c_id = IntegerField()
    s_id = IntegerField()
    cross_name = FixedCharField()
    history = FixedCharField()


class Location(Model):
    number = IntegerField()
    country = CharField()
    description = FixedCharField()
    institute_name = CharField()
    cooperator = CharField()
    latitude = CharField()
    latitude_degrees = IntegerField()
    latitude_minutes = IntegerField()
    longitude = CharField()
    longitude_degrees = IntegerField()
    longitude_minutes = IntegerField()
    altitude = IntegerField()

    class Meta:
        database = db


class CropOntology(Model):
    ontologyDbId = CharField()
    name = CharField()
    # trait_ontologies = ForeignKeyField(TraitOntology, backref="crop_ontology")

    class Meta:
        database = db


class TraitOntology(Model):
    traitDbId = CharField()
    name = CharField()
    class_family = CharField()
    description = TextField()
    crop_ontology = ForeignKeyField(CropOntology, backref="trait_ontologies")
    # variable_ontologies = ForeignKeyField(VariableOntology, backref="trait_ontology")

    class Meta:
        database = db


class MethodOntology(Model):
    methodDbId = CharField()
    name = CharField()
    class_family = CharField()
    description = TextField()
    formula = FixedCharField()
    # variable_ontologies = ForeignKeyField(VariableOntology, backref="method_ontology")

    class Meta:
        database = db


class ScaleOntology(Model):
    scaleDbId = CharField(unique=True, index=True)
    name = CharField()
    dataType = CharField()
    validValues = TextField()
    # variable_ontologies = ForeignKeyField(VariableOntology, backref="scale_ontology")

    class Meta:
        database = db


class VariableOntology(Model):
    name = CharField()
    synonyms = FixedCharField()
    growth_stage = FixedCharField()
    observation_variable_db_id = CharField()
    trait_ontology = ForeignKeyField(TraitOntology, backref="variable_ontologies")
    traits = ForeignKeyField(Trait, backref="variable_ontology")
    method_ontology = ForeignKeyField(MethodOntology, backref="variable_ontologies")
    scale_ontology = ForeignKeyField(ScaleOntology, backref="variable_ontologies")

    class Meta:
        database = db


class RawCollection(Model):
    occurrence = IntegerField()
    cycle = CharField()
    gen_number = IntegerField()
    repetition = IntegerField()
    sub_block = IntegerField()
    value_data = CharField()
    trail = ForeignKeyField(Trail, backref="raw_collection")
    trait = ForeignKeyField(Trait, backref="raw_collection")
    genotype = ForeignKeyField(Genotype, backref="raw_collection")
    location = ForeignKeyField(Location, backref="raw_collection")
    
    class Meta:
        database = db


