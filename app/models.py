from peewee import CharField, ForeignKeyField, IntegerField, Model, TextField

from app.database import db


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
    name = CharField(unique=True, index=True)
    number = CharField()
    description = TextField()
    co_trait_name = CharField(index=True)
    variable_name = CharField()
    co_id = CharField()

    class Meta:
        database = db


class Genotype(Model):
    c_id = IntegerField()
    s_id = IntegerField()
    cross_name = CharField(index=True)
    history_name = TextField()

    class Meta:
        database = db


class Location(Model):
    number = IntegerField()
    country = CharField()
    description = TextField()
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
    formula = TextField()

    class Meta:
        database = db


class ScaleOntology(Model):
    scale_db_id = CharField(unique=True, index=True)
    name = CharField()
    data_type = CharField()
    valid_values = TextField()

    class Meta:
        database = db


class VariableOntology(Model):
    name = CharField()
    synonyms = TextField()
    growth_stage = TextField()
    observation_variable_db_id = CharField()
    trait_ontology = ForeignKeyField(
        TraitOntology, backref="variable_ontologies")
    trait = ForeignKeyField(Trait, backref="variable_ontology")
    method_ontology = ForeignKeyField(
        MethodOntology, backref="variable_ontologies")
    scale_ontology = ForeignKeyField(
        ScaleOntology, backref="variable_ontologies")

    class Meta:
        database = db


class FieldCollection(Model):
    cycle = CharField(max_length=4)
    gen_number = IntegerField()
    genotype = ForeignKeyField(Genotype, backref="field_collections")
    location = ForeignKeyField(Location, backref="field_collections")
    trail = ForeignKeyField(Trail, backref="field_collections")

    class Meta:
        database = db


class EnvironmentDefinition(Model):
    trait_no = IntegerField()
    trait_name = CharField(max_length=300)

    class Meta:
        database = db


class FieldCollectionEnvironment(Model):
    field_collection = ForeignKeyField(
        FieldCollection, backref="field_environments")
    environment_definition = ForeignKeyField(
        EnvironmentDefinition, backref="field_environments")
    unit = ForeignKeyField(Unit, backref="field_environments")
    value_data = CharField(max_length=200)

    class Meta:
        database = db


class RawCollection(Model):
    hash_raw = CharField(max_length=500)
    occurrence = IntegerField()
    repetition = IntegerField()
    sub_block = IntegerField()
    plot = IntegerField()
    trait = ForeignKeyField(Trait, backref="raw_collections")
    unit = ForeignKeyField(Unit, backref="raw_collections")
    field = ForeignKeyField(FieldCollection, backref="raw_collections")
    value_data = CharField()

    class Meta:
        database = db
