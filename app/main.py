from typing import List
from fastapi import Depends, FastAPI, HTTPException
from fastapi_pagination import Page, add_pagination, paginate
from app import database, models, schemas
from app.cruds import crud, locationCrud, genotypeCrud
from app.services import rawService
from app.routes import (
    fieldCollectionRoute,
    fieldCollectionEnvironmentRoute,
    environmentDefinitionRoute,
    traitRoute,
)
from app.dependencies import get_db


database.db.connect()
database.db.create_tables(
    [
        models.WebFile,
        models.Trail,
        models.Unit,
        models.Trait,
        models.Genotype,
        models.Location,
        models.CropOntology,
        models.TraitOntology,
        models.MethodOntology,
        models.ScaleOntology,
        models.VariableOntology,
        models.FieldCollection,
        models.EnvironmentDefinition,
        models.FieldCollectionEnvironment,
        models.RawCollection,
    ]
)
database.db.close()

app = FastAPI()

sleep_time = 10

app.include_router(fieldCollectionRoute.router)
app.include_router(fieldCollectionEnvironmentRoute.router)
app.include_router(environmentDefinitionRoute.router)
app.include_router(traitRoute.router)


@app.post(
    "/web_files/",
    response_model=schemas.WebFile,
    dependencies=[Depends(get_db)]
)
def create_web_file(web_file: schemas.WebFileCreate):
    return crud.create_web_file(web_file=web_file)


@app.post(
    "/trails/",
    response_model=schemas.Trail,
    dependencies=[Depends(get_db)],
    tags=["Trail"],
    description="Create a new Trail"
)
def create_trail(trail: schemas.TrailCreate):
    return crud.create_trail(trail=trail)


@app.post(
    "/units/",
    response_model=schemas.Unit,
    dependencies=[Depends(get_db)]
)
def create_unit(unit: schemas.UnitCreate):
    return crud.create_unit(unit=unit)


@app.post(
    "/genotypes/", response_model=schemas.Genotype,
    dependencies=[Depends(get_db)],
    tags=["Genotype"],
)
def create_genotype(genotype: schemas.GenotypeCreate):
    return crud.create_genotype(genotype=genotype)


@app.post(
    "/locations/",
    response_model=schemas.Location,
    dependencies=[Depends(get_db)],
    tags=["Location"],
    description="Create a new Location"
)
def create_location(location: schemas.LocationCreate):
    return locationCrud.create_location(location=location)


@app.post(
    "/crop_ontologies/",
    response_model=schemas.CropOntology,
    dependencies=[Depends(get_db)],
)
def create_crop_ontology(crop_ontology: schemas.CropOntologyCreate):
    return crud.create_crop_ontology(crop_ontology=crop_ontology)


@app.post(
    "/trait_ontologies/",
    response_model=schemas.TraitOntology,
    dependencies=[Depends(get_db)],
)
def create_trait_ontology(trait_ontology: schemas.TraitOntologyCreate):
    try:
        return crud.create_trait_ontology(trait_ontology=trait_ontology)
    except ValueError as err:
        raise HTTPException(
            status_code=404, detail="Crop trait not found") from err


@app.post(
    "/method_ontologies/",
    response_model=schemas.MethodOntology,
    dependencies=[Depends(get_db)],
)
def create_method_ontology(method_ontology: schemas.MethodOntologyCreate):
    return crud.create_method_ontology(method_ontology=method_ontology)


@app.post(
    "/scale_ontologies/",
    response_model=schemas.ScaleOntology,
    dependencies=[Depends(get_db)],
)
def create_scale_ontology(scale_ontology: schemas.ScaleOntologyCreate):
    return crud.create_scale_ontology(scale_ontology=scale_ontology)


@app.post(
    "/variable_ontologies/",
    response_model=schemas.VariableOntology,
    dependencies=[Depends(get_db)],
    tags=["Variable Ontologies"]
)
def create_variable_ontology(variable_ontology: schemas.VariableOntologyCreate):
    return crud.create_variable_ontology(variable_ontology=variable_ontology)


@app.post(
    "/raw_collections/",
    response_model=schemas.RawCollection,
    dependencies=[Depends(get_db)],
    tags=["Raw Collection"],
)
def create_raw_collection(raw_collection: schemas.RawCollectionCreate):
    return crud.create_raw_collection(raw_collection=raw_collection)


@app.get(
    "/trails/",
    response_model=List[schemas.Trail],
    dependencies=[Depends(get_db)],
    tags=["Trail"],
    description="Find Trail by name"
)
def search_trial_by_name(name: str):
    return crud.search_trail_by_name(name=name)


# Fix to find and adding try
@app.get(
    "/locations/",
    response_model=schemas.Location,
    dependencies=[Depends(get_db)],
    tags=["Location"],
    description="Find location by number"
)
def search_location_by_number(number: int):
    return crud.search_location_by_number(number=number)


@app.get(
    "/genotypes/",
    response_model=schemas.Genotype,
    dependencies=[Depends(get_db)],
    tags=["Genotype"],
)
def find_genotype_by_ids(c_id: int, s_id: int):
    try:
        return crud.find_genotype_by_ids(c_id=c_id, s_id=s_id)
    except ValueError as err:
        raise HTTPException(
            status_code=404, detail="Genotype not found") from err


@app.post(
    "/raw_collections/search/",
    response_model=Page[schemas.RawCollection],
    dependencies=[Depends(get_db)],
    tags=["Raw Collection"],
    description="Search by any attribute",
)
def search_raw_collections(raw_collection: schemas.RawCollectionFilter):
    return paginate(crud.search_raw_collection(
        id=id,
        raw_collection=raw_collection
    ))


@app.get(
    "/special_query/ids/{target}",
    response_model=list[schemas.ResponseTarget],
    dependencies=[Depends(get_db)],
    tags=["special_query"],
    description="Get all id on database",
)
def search_raw_collections_query(target: schemas.EntityTarget):
    return crud.special_query_ids(target=target)


@app.get(
    "/locations/{id}",
    response_model=schemas.Location,
    dependencies=[Depends(get_db)],
    tags=["Location"],
    description="Get location by id",
)
def find_location_by_id(id: int):
    try:
        return locationCrud.find_by_id(id=id)
    except ValueError as err:
        raise HTTPException(
            status_code=404, detail="Location not found") from err


@app.get(
    "/genotypes/{id}",
    response_model=schemas.Genotype,
    dependencies=[Depends(get_db)],
    tags=["Genotype"],
    description="find Genotype by id",
)
def find_genotype_by_id(id: int):
    try:
        return genotypeCrud.find_by_id(id=id)
    except ValueError as err:
        raise HTTPException(
            status_code=404, detail="Genotype not found") from err


@app.post(
    "/raw_all/search",
    response_model=str,
    dependencies=[Depends(get_db)],
    tags=["Raw"],
    deprecated="23-10-02- To delete use /raw_all/trait"
)
def get_raw_by_genotype_id(raw_filter: schemas.RawAllFilter):
    return rawService.get_raw_join_all(raw_filter=raw_filter)


@app.post(
    "/raw_all/trait",
    response_model=str,
    dependencies=[Depends(get_db)],
    tags=["Raw"]
)
def get_raw_by_genotype_id_all_trait(raw_filter: schemas.RawAllFilter):
    return rawService.get_raw_join_all_trait(raw_filter=raw_filter)


add_pagination(app)
