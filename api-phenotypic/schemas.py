from typing import Any, List, Union
from peewee import ModelSelect
from pydantic import BaseModel
from pydantic.utils import GetterDict


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, ModelSelect):
            return list(res)
        return res


class WebFileBase(BaseModel):
    name: str

class WebFileCreate(WebFileBase):
    pass

class WebFile(WebFileBase):
    id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class TrailBase(BaseModel):
    name: str

class TrailCreate(TrailBase):
    pass

class Trail(TrailBase):
    id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class UnitBase(BaseModel):
    name: str

class UnitCreate(UnitBase):
    pass

class Unit(UnitBase):
    id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class TraitBase(BaseModel):
    name: str
    number: str
    description: str
    co_trait_name: str
    variable_name: str
    co_id: str


class TraitCreate(TraitBase):
    pass


class Trait(TraitBase):
    id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict



class GenotypeBase(BaseModel):
    c_id: int
    s_id: int
    cross_name: str
    history_name: str


class GenotypeCreate(GenotypeBase):
    pass


class Genotype(GenotypeBase):
    id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class LocationBase(BaseModel):
    number: int
    country: str
    description: str
    institute_name: str
    cooperator: str
    latitude: str
    latitude_degrees: int
    latitude_minutes: int
    longitude: str
    longitude_degrees: int
    longitude_minutes: int
    altitude: int


class LocationCreate(LocationBase):
    pass


class Location(LocationBase):
    id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class CropOntologyBase(BaseModel):
    ontology_db_id: str
    name: str


class CropOntologyCreate(CropOntologyBase):
    pass


class CropOntology(CropOntologyBase):
    id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class TraitOntologyBase(BaseModel):
    trait_db_id: str
    name: str
    class_family: str
    description: str


class TraitOntologyCreate(TraitOntologyBase):
    pass


class TraitOntology(TraitOntologyBase):
    id: int
    crop_ontology_id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict



class MethodOntologyBase(BaseModel):
    method_db_id: str
    name: str
    class_family: str
    description: str
    formula: str


class MethodOntologyCreate(MethodOntologyBase):
    pass


class MethodOntology(MethodOntologyBase):
    id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict



class ScaleOntologyBase(BaseModel):
    scale_db_id: str
    name: str
    dataType: str
    validValues: str


class ScaleOntologyCreate(ScaleOntologyBase):
    pass


class ScaleOntology(ScaleOntologyBase):
    id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict

class VariableOntologyBase(BaseModel):
    name: str
    synonyms: str
    growth_stage: str
    observation_variable_db_id: str


class VariableOntologyCreate(VariableOntologyBase):
    pass


class VariableOntology(VariableOntologyBase):
    id: int
    trait_ontology_id: int
    trait_id: int
    method_ontology_id: int
    scale_ontology_id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict




class RawCollectionBase(BaseModel):
    occurrence: int
    cycle: str
    gen_number:int
    repetition: int
    sub_block: int
    value_data:str


class RawCollectionCreate(RawCollectionBase):
    pass


class RawCollection(RawCollectionBase):
    id: int
    trail_id: int
    trait_id: int
    genotype_id: int
    location_id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
