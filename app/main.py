from fastapi import Depends, FastAPI, HTTPException
from fastapi_pagination import add_pagination
import uvicorn
import database
import models
from schemas import schemas
from cruds import crud, webFileCrud
from routes import (
    environmentDefinitionRoute,
    fieldCollectionEnvironmentRoute,
    fieldCollectionRoute,
    locationRoute,
    rawRoute,
    traitRoute,
    genotypeRoute,
    trialRoute,
    unitRoute,
)
from dependencies import get_db
from os import getenv
from dotenv import load_dotenv

load_dotenv()
database.db.connect()
database.db.create_tables(
    [
        models.CropOntology,
        models.EnvironmentDefinition,
        models.FieldCollection,
        models.FieldCollectionEnvironment,
        models.Genotype,
        models.Location,
        models.MethodOntology,
        models.RawCollection,
        models.ScaleOntology,
        models.Trial,
        models.Trait,
        models.TraitOntology,
        models.Unit,
        models.VariableOntology,
        models.WebFile,
    ]
)
database.db.close()

app = FastAPI()

sleep_time = 10

app.include_router(environmentDefinitionRoute.router)
app.include_router(fieldCollectionEnvironmentRoute.router)
app.include_router(fieldCollectionRoute.router)
app.include_router(genotypeRoute.router)
app.include_router(locationRoute.router)
app.include_router(rawRoute.router)
app.include_router(trialRoute.router)
app.include_router(traitRoute.router)
app.include_router(unitRoute.router)


@app.post(
    "/web_files/",
    response_model=schemas.WebFile,
    dependencies=[Depends(get_db)]
)
def create_web_file(web_file: schemas.WebFileCreate):
    return webFileCrud.get_or_create(web_file=web_file)


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
def create_variable_ontology(
    variable_ontology: schemas.VariableOntologyCreate
):
    return crud.create_variable_ontology(variable_ontology=variable_ontology)


add_pagination(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
