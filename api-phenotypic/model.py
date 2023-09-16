import peewee

from database import db


class WebFile(peewee.Model):
    name = peewee.CharField()

    class Meta:
        database = db


# class Item(peewee.Model):
#     title = peewee.CharField(index=True)
#     description = peewee.CharField(index=True)
#     owner = peewee.ForeignKeyField(User, backref="items")

#     class Meta:
#         database = db

class Trail(peewee.Model):
    name = peewee.CharField(unique=True, index=True)

    class Meta:
        database = db

class Unit(peewee.Model):
    name = Column(String(300))

    class Meta:
        database = db


class Trait(peewee.Model):
    __tablename__ = 'Trait'
    id = Column(Integer, primary_key=True),
    name = Column(String(300)),
    number = Column(Integer),
    description = Column(String(500)),
    co_trait_name = Column(String(200)),
    variable_name = Column(String(200)),
    co_id = Column(String(400)),
    variable_ontology_id = Column(Integer, ForeignKey("VariableOntology.id"), nullable=True),
    variable_ontology = relationship("VariableOntology", back_populates="traits")


class Genotype(peewee.Model):
    __tablename__ = 'Genotype'
    id = Column(Integer, primary_key=True),
    c_id = Column(Integer),
    s_id = Column(Integer),
    cross_name = Column(String(600)),
    history = Column(String(600)),


class Location(peewee.Model):
    __tablename__ = 'Location'
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    country = Column(String(600))
    description = Column(String(600))
    institute_name = Column(String(600))
    cooperator = Column(String(600))
    latitude = Column(String(10))
    latitude_degrees = Column(Integer)
    latitude_minutes = Column(Integer)
    longitude = Column(String(10))
    longitude_degrees = Column(Integer)
    longitude_minutes = Column(Integer)
    altitude = Column(Integer)


class CropOntology(peewee.Model):
    __tablename__ = 'CropOntology'
    id = Column(Integer, primary_key=True)
    ontologyDbId = Column(String(50))
    name = Column(String(200))
    trait_ontologies = relationship("TraitOntology", back_populates="crop_ontology")


class TraitOntology(peewee.Model):
    __tablename__ = 'TraitOntology'
    id = Column(Integer, primary_key=True)
    traitDbId = Column(String(50))
    name = Column(String(200))
    class_family = Column(String(200))
    description = Column(String(1000))
    crop_ontology_id = Column(Integer, ForeignKey("CropOntology.id"), nullable=False),
    crop_ontology = relationship("CropOntology", back_populates="trait_ontologies")
    variable_ontologies = relationship("VariableOntology", back_populates="trait_ontology")


class MethodOntology(peewee.Model):
    __tablename__ = 'MethodOntology'
    id = Column(Integer, primary_key=True)
    methodDbId = Column(String(50))
    name = Column('', String(200))
    class_family = Column(String(200))
    description = Column(String(1000))
    formula = Column(String(500))
    variable_ontologies = relationship("VariableOntology", back_populates="method_ontology")


class ScaleOntology(peewee.Model):
    __tablename__ = 'ScaleOntology'
    id = Column(Integer, primary_key=True)
    scaleDbId = Column(String(50))
    name = Column(String(200))
    dataType = Column(String(200))
    validValues = Column(String(2000))
    variable_ontologies = relationship("VariableOntology", back_populates="scale_ontology")


class VariableOntology(peewee.Model):
    __tablename__ = 'VariableOntology'
    id = Column(Integer, primary_key=True)
    trait_ontology_id = Column(Integer, ForeignKey("TraitOntology.id"), nullable=False),
    trait_ontology = relationship("TraitOntology", back_populates="variable_ontologies")
    traits = relationship("Trait", back_populates="variable_ontology")
    method_ontology_id = Column(Integer, ForeignKey("MethodOntology.id"), nullable=False)
    method_ontology = relationship("MethodOntology", back_populates="variable_ontologies")
    scale_ontologies_id = Column(Integer, ForeignKey("ScaleOntology.id"), nullable=False)
    scale_ontology = relationship("ScaleOntology", back_populates="variable_ontologies")
    observation_Variable_db_id = Column(String(50))
    name = Column(String(200))
    synonyms = Column(String(500))
    growth_stage = Column(String(500))


class RawCollection(peewee.Model):
    __tablename__ = 'RawCollection'
    id = Column(Integer, primary_key=True)
    trail_id = Column(Integer, ForeignKey("Trail.id"), nullable=False),
    trait_id = Column(Integer, ForeignKey("Trait.id"), nullable=False),
    genotype_id = Column(Integer, ForeignKey("Genotype.id"), nullable=False),
    location_id = Column(Integer, ForeignKey("Location.id"), nullable=False),
    occurrence = Column(Integer),
    cycle = Column(String(4)),
    gen_number = Column(Integer),
    repetition = Column(Integer),
    sub_block = Column(Integer),
    value_data = Column(String(100)),


