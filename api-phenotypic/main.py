from typing import List
from fastapi import Depends, FastAPI, HTTPException
import crud
import database
import models
import schemas
from database import db_state_default

database.db.connect()
database.db.create_tables([models.WebFile, models.Trail, models.Unit, models.Trait, models.Genotype, models.Location, models.CropOntology,
                          models.TraitOntology, models.MethodOntology, models.ScaleOntology, models.VariableOntology, models.RawCollection])
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
def create_trail(trail: schemas.Trail):
    return crud.create_trail(trail=trail)

@app.post("/unit/", response_model=schemas.Unit, dependencies=[Depends(get_db)])
def create_unit(unit: schemas.Unit):
    return crud.create_unit(unit=unit)

@app.post("/trait/", response_model=schemas.Trait, dependencies=[Depends(get_db)])
def create_trait(trait: schemas.Trait):
    return crud.create_trait(trait=trait)

@app.post("/genotype/", response_model=schemas.Genotype, dependencies=[Depends(get_db)])
def create_genotype(genotype: schemas.Genotype):
    return crud.create_genotype(genotype=genotype)