from fastapi import APIRouter, Depends
from app.schemas import schemas, customs
from app.cruds import rawCrud
from app.dependencies import get_db
from fastapi_pagination import Page, paginate
from app.services import rawService


router = APIRouter(
    prefix="/raw_collections",
    tags=["Raw Collections"],
    responses={404: {"description": "Trait not found"}}
)


@router.post(
    "/",
    response_model=schemas.RawCollection,
    dependencies=[Depends(get_db)],
)
def create_raw_collection(raw_collection: schemas.RawCollectionCreate):
    return rawCrud.create(raw_collection=raw_collection)


@router.post(
    "/xls",
    response_model=customs.RawData,
    dependencies=[Depends(get_db)],
)
def create_raw_data(raw_data: customs.RawData):
    return rawService.save_raw_data(raw_data=raw_data)


@router.post(
    "/search/",
    response_model=Page[schemas.RawCollection],
    dependencies=[Depends(get_db)],
    description="Search by any attribute",
)
def search_raw_collections(raw_collection: customs.RawCollectionFilter):
    return paginate(rawCrud.search(
        id=id,
        raw_collection=raw_collection
    ))


@router.get(
    "/list/ids/{target}",
    response_model=list[customs.ResponseTarget],
    dependencies=[Depends(get_db)],
    description="Get all id on database",
)
def search_raw_collections_query(target: customs.EntityTarget):
    return rawCrud.list_query_ids(target=target)


@router.post(
    "/all/search/v1",
    response_model=str,
    dependencies=[Depends(get_db)],
    deprecated="23-10-02- To delete use /raw_all/trait"
)
def get_raw_by_genotype_id(raw_filter: customs.RawAllFilter):
    return rawService.get_raw_join_all(raw_filter=raw_filter)


@router.post(
    "/all/search",
    response_model=str,
    dependencies=[Depends(get_db)],
)
def get_raw_by_genotype_id_all_trait(raw_filter: customs.RawAllFilter):
    return rawService.get_raw_join_all_trait(raw_filter=raw_filter)
