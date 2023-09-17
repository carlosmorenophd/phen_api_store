import time
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
    db_web_file = crud.get_user_by_name(name=web_file.name)
    if db_web_file:
        return db_web_file
    return crud.create_web_file(webFile=web_file)
