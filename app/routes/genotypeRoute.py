from fastapi import APIRouter, Depends, HTTPException
from schemas import schemas
from cruds import genotypeCrud
from dependencies import get_db
from typing import Union

router = APIRouter(
    prefix="/genotypes",
    tags=["Genotype"],
    responses={404: {"description": "Genotype not found"}},
)


@router.post(
    "/",
    response_model=schemas.Genotype,
    dependencies=[Depends(get_db)],
    tags=["Genotype"],
)
def create_genotype(genotype: schemas.GenotypeCreate):
    return genotypeCrud.create(genotype=genotype)


@router.get(
    "/ids",
    response_model=schemas.Genotype,
    dependencies=[Depends(get_db)],
)
def find_genotype_by_ids(c_id: int, s_id: int):
    try:
        return genotypeCrud.find_by_ids(c_id=c_id, s_id=s_id)
    except ValueError as err:
        raise HTTPException(status_code=404, detail="Genotype not found") from err
    
    
@router.get(
    "/c_id",
    response_model=schemas.Genotype,
    dependencies=[Depends(get_db)],
)
def find_genotype_by_c_id(c_id: int):
    try:
        return genotypeCrud.find_by_ids(c_id=c_id, s_id=None)
    except ValueError as err:
        raise HTTPException(status_code=404, detail="Genotype not found") from err


@router.get(
    "/s_id",
    response_model=schemas.Genotype,
    dependencies=[Depends(get_db)],
)
def find_genotype_by_s_id(s_id: int):
    try:
        return genotypeCrud.find_by_ids(c_id=None, s_id=s_id)
    except ValueError as err:
        raise HTTPException(status_code=404, detail="Genotype not found") from err


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
        raise HTTPException(status_code=404, detail="Genotype not found") from err
