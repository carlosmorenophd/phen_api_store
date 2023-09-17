from os import getenv
from typing import List

import crud
import models
import schemas
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException
from uvicorn import run

import database
from database import db_state_default

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


@app.post("/trail/", response_model=schemas.Trail, dependencies=[Depends(get_db)])
def create_trail(trail: schemas.TrailCreate):
    return crud.create_trail(trail=trail)


@app.post("/unit/", response_model=schemas.Unit, dependencies=[Depends(get_db)])
def create_unit(unit: schemas.UnitCreate):
    return crud.create_unit(unit=unit)


@app.post("/trait/", response_model=schemas.Trait, dependencies=[Depends(get_db)])
def create_trait(trait: schemas.TraitCreate):
    return crud.create_trait(trait=trait)


@app.post("/genotype/", response_model=schemas.Genotype, dependencies=[Depends(get_db)])
def create_genotype(genotype: schemas.GenotypeCreate):
    return crud.create_genotype(genotype=genotype)


@app.post("/location/", response_model=schemas.Location, dependencies=[Depends(get_db)])
def create_location(location: schemas.LocationCreate):
    return crud.create_location(location=location)


@app.post(
    "/crop_ontology/",
    response_model=schemas.CropOntology,
    dependencies=[Depends(get_db)],
)
def create_crop_ontology(crop_ontology: schemas.CropOntologyCreate):
    return crud.create_crop_ontology(crop_ontology=crop_ontology)


@app.post(
    "/trait_ontology/",
    response_model=schemas.TraitOntology,
    dependencies=[Depends(get_db)],
)
def create_trait_ontology(trait_ontology: schemas.TraitOntologyCreate):
    return crud.create_trait_ontology(trait_ontology == trait_ontology)


if __name__ == "__main__":
    load_dotenv()
    run(app, host="127.0.0.1", port=int(getenv("API_PORT")), reload=True)
