from fastapi import APIRouter, Depends, HTTPException
from app.schemas import schemas
from app.cruds import genotypeCrud
from app.dependencies import get_db


router = APIRouter(
    prefix="/genotype",
    tags=["Genotype"],
    responses={404: {"description": "Genotype not found"}}
)


@router.post(
    "/", response_model=schemas.Genotype,
    dependencies=[Depends(get_db)],
    tags=["Genotype"],
)
def create_genotype(genotype: schemas.GenotypeCreate):
    return genotypeCrud.create(genotype=genotype)


@router.get(
    "/",
    response_model=schemas.Genotype,
    dependencies=[Depends(get_db)],
)
def find_genotype_by_ids(c_id: int, s_id: int):
    try:
        return genotypeCrud.find_by_ids(c_id=c_id, s_id=s_id)
    except ValueError as err:
        raise HTTPException(
            status_code=404, detail="Genotype not found") from err


@router.get(
    "/{id}",
    response_model=schemas.Genotype,
    dependencies=[Depends(get_db)],
    description="find Genotype by id",
)
def find_genotype_by_id(id: int):
    try:
        return genotypeCrud.find_by_id(id=id)
    except ValueError as err:
        raise HTTPException(
            status_code=404, detail="Genotype not found") from err