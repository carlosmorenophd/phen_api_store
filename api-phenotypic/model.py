from peewee import (
    CharField,
    FixedCharField,
    ForeignKeyField,
    IntegerField,
    Model,
    TextField,
)

# import peewee
from database import db


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
    __tablename__ = "Trait"
    name = CharField(unique=True, index=True)
    number = CharField()
    description = FixedCharField()
    co_trait_name = CharField(index=True)
    variable_name = CharField()
    co_id = CharField()

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
    ontology_db_id = CharField()
    name = CharField()

    class Meta:
        database = db


class TraitOntology(Model):
    trait_db_id = CharField()
    name = CharField()
    class_family = CharField()
    description = TextField()
    crop_ontology = ForeignKeyField(CropOntology, backref="trait_ontologies")

    class Meta:
        database = db


class MethodOntology(Model):
    method_db_id = CharField()
    name = CharField()
    class_family = CharField()
    description = TextField()
    formula = FixedCharField()

    class Meta:
        database = db


class ScaleOntology(Model):
    scale_db_id = CharField(unique=True, index=True)
    name = CharField()
    dataType = CharField()
    validValues = TextField()

    class Meta:
        database = db


class VariableOntology(Model):
    name = CharField()
    synonyms = FixedCharField()
    growth_stage = FixedCharField()
    observation_variable_db_id = CharField()
    trait_ontology = ForeignKeyField(TraitOntology, backref="variable_ontologies")
    trait = ForeignKeyField(Trait, backref="variable_ontology")
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
    trail = ForeignKeyField(Trail, backref="raw_collections")
    trait = ForeignKeyField(Trait, backref="raw_collections")
    genotype = ForeignKeyField(Genotype, backref="raw_collections")
    location = ForeignKeyField(Location, backref="raw_collections")

    class Meta:
        database = db
