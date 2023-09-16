from typing import Union
from pydantic import BaseModel


class WebFileBase(BaseModel):
    name: Union[str, None]

class WebFileCreate(WebFileBase):
    name: str

class WebFile(WebFileBase):
    id: int
    name: str

    class Config:
        orm_mode = True


class TrailBase(BaseModel):
    id: int
    name: Union[str,None]


class UnitBase(BaseModel):
    id: int
    name: Union[str,None]


class TraitBase(BaseModel):
    id: int
    name: Union[str,None]
    number = Column(Integer),
    description: Union[str,None]
    co_trait_name: Union[str,None]
    variable_name: Union[str,None]
    co_id: Union[str,None]
    # variable_ontology_id: list[]  = []
    variable_ontology = relationship("VariableOntology", back_populates="traits")


class GenotypeBase(BaseModel):
    __tablename__ = 'Genotype'
    id: int
    c_id = Column(Integer)
    s_id = Column(Integer)
    cross_name: Union[str,None](600)
    history: Union[str,None](600)


class LocationBase(BaseModel):
    __tablename__ = 'Location'
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    country: Union[str,None](600)
    description: Union[str,None](600)
    institute_name: Union[str,None](600)
    cooperator: Union[str,None](600)
    latitude: Union[str,None](10)
    latitude_degrees = Column(Integer)
    latitude_minutes = Column(Integer)
    longitude: Union[str,None](10)
    longitude_degrees = Column(Integer)
    longitude_minutes = Column(Integer)
    altitude = Column(Integer)


class CropOntologyBase(BaseModel):
    __tablename__ = 'CropOntology'
    id = Column(Integer, primary_key=True)
    ontologyDbId: Union[str,None](50)
    name: Union[str,None](200)
    trait_ontologies = relationship("TraitOntology", back_populates="crop_ontology")


class TraitOntologyBase(BaseModel):
    __tablename__ = 'TraitOntology'
    id = Column(Integer, primary_key=True)
    traitDbId: Union[str,None](50)
    name: Union[str,None](200)
    class_family: Union[str,None](200)
    description: Union[str,None](1000)
    crop_ontology_id = Column(Integer, ForeignKey("CropOntology.id"), nullable=False)
    crop_ontology = relationship("CropOntology", back_populates="trait_ontologies")
    variable_ontologies = relationship("VariableOntology", back_populates="trait_ontology")


class MethodOntologyBase(BaseModel):
    __tablename__ = 'MethodOntology'
    id = Column(Integer, primary_key=True)
    methodDbId: Union[str,None](50)
    name = Column('', String(200))
    class_family: Union[str,None](200)
    description: Union[str,None](1000)
    formula: Union[str,None](500)
    variable_ontologies = relationship("VariableOntology", back_populates="method_ontology")


class ScaleOntologyBase(BaseModel):
    __tablename__ = 'ScaleOntology'
    id = Column(Integer, primary_key=True)
    scaleDbId: Union[str,None](50)
    name: Union[str,None](200)
    dataType: Union[str,None](200)
    validValues: Union[str,None](2000)
    variable_ontologies = relationship("VariableOntology", back_populates="scale_ontology")


class VariableOntologyBase(BaseModel):
    __tablename__ = 'VariableOntology'
    id = Column(Integer, primary_key=True)
    trait_ontology_id = Column(Integer, ForeignKey("TraitOntology.id"), nullable=False),
    trait_ontology = relationship("TraitOntology", back_populates="variable_ontologies")
    traits = relationship("Trait", back_populates="variable_ontology")
    method_ontology_id = Column(Integer, ForeignKey("MethodOntology.id"), nullable=False)
    method_ontology = relationship("MethodOntology", back_populates="variable_ontologies")
    scale_ontologies_id = Column(Integer, ForeignKey("ScaleOntology.id"), nullable=False)
    scale_ontology = relationship("ScaleOntology", back_populates="variable_ontologies")
    observation_Variable_db_id: Union[str,None](50)
    name: Union[str,None](200)
    synonyms: Union[str,None](500)
    growth_stage: Union[str,None](500)


class RawCollectionBase(BaseModel):
    id = Column(Integer, primary_key=True)
    trail_id = Column(Integer, ForeignKey("Trail.id"), nullable=False)
    trait_id = Column(Integer, ForeignKey("Trait.id"), nullable=False)
    genotype_id = Column(Integer, ForeignKey("Genotype.id"), nullable=False)
    location_id = Column(Integer, ForeignKey("Location.id"), nullable=False)
    occurrence = Column(Integer)
    cycle: Union[str,None](4)
    gen_number = Column(Integer)
    repetition = Column(Integer)
    sub_block = Column(Integer)
    value_data: Union[str,None](100)

