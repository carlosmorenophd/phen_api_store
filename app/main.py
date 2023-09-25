from typing import List

from fastapi import Depends, FastAPI, HTTPException

from app import crud, database, models, schemas
from app.database import db_state_default

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
        models.RawCollection,
    ]
)
database.db.close()

app = FastAPI()

sleep_time = 10


async def reset_db_state():
    database.db._state._state.set(db_state_default.copy())
    database.db._state.reset()


def get_db(db_state=Depends(reset_db_state)):
    try:
        database.db.connect()
        yield
    finally:
        if not database.db.is_closed():
            database.db.close()


@app.post("/web_files/", response_model=schemas.WebFile, dependencies=[Depends(get_db)])
def create_web_file(web_file: schemas.WebFileCreate):
    return crud.create_web_file(web_file=web_file)


@app.post("/trails/", response_model=schemas.Trail, dependencies=[Depends(get_db)])
def create_trail(trail: schemas.TrailCreate):
    return crud.create_trail(trail=trail)


@app.post("/units/", response_model=schemas.Unit, dependencies=[Depends(get_db)])
def create_unit(unit: schemas.UnitCreate):
    return crud.create_unit(unit=unit)


@app.post("/traits/", response_model=schemas.Trait, dependencies=[Depends(get_db)])
def create_trait(trait: schemas.TraitCreate):
    return crud.create_trait(trait=trait)


@app.post(
    "/genotypes/", response_model=schemas.Genotype, dependencies=[Depends(get_db)]
)
def create_genotype(genotype: schemas.GenotypeCreate):
    return crud.create_genotype(genotype=genotype)


@app.post(
    "/locations/", response_model=schemas.Location, dependencies=[Depends(get_db)]
)
def create_location(location: schemas.LocationCreate):
    return crud.create_location(location=location)


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
)
def create_raw_collection(raw_collection: schemas.RawCollectionCreate):
    return crud.create_raw_collection(raw_collection=raw_collection)


# Fix to find and adding try
@app.get(
    "/trails/",
    response_model=List[schemas.Trail],
    dependencies=[Depends(get_db)],
)
def search_trial_by_name(name: str):
    return crud.search_trail_by_name(name=name)


# Fix to find and adding try
@app.get(
    "/locations/",
    response_model=schemas.Location,
    dependencies=[Depends(get_db)],
)
def search_location_by_number(number: int):
    return crud.search_location_by_number(number=number)


@app.get(
    "/genotypes/",
    response_model=schemas.Genotype,
    dependencies=[Depends(get_db)],
)
def find_genotype_by_ids(c_id: int, s_id: int):
    try:
        return crud.find_genotype_by_ids(c_id=c_id, s_id=s_id)
    except ValueError as err:
        raise HTTPException(
            status_code=404, detail="Genotype not found") from err


@app.get(
    "/traits/",
    response_model=schemas.Trait,
    dependencies=[Depends(get_db)],
    tags=["trait"],
)
def find_trait_by_name(name: str):
    try:
        return crud.find_trait_by_name(name=name)
    except ValueError as err:
        raise HTTPException(status_code=404, detail="Trait not found") from err


@app.put(
    "/traits/{id}",
    response_model=schemas.Trait,
    dependencies=[Depends(get_db)],
    tags=["trait"],
)
def update_trait(id: int, trait: schemas.TraitCreate):
    try:
        return crud.update_trait(id=id, trait=trait)
    except ValueError as err:
        raise HTTPException(status_code=404, detail="Trait not found") from err