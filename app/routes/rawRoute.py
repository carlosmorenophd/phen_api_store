from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page, paginate
from app.schemas import schemas, customs
from app.cruds import rawCrud
from app.dependencies import get_db
from app.services import rawService, environmentDataService


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
    response_model=schemas.RawCollection,
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
    "/all/search",
    response_model=str,
    dependencies=[Depends(get_db)],
)
def get_raw_by_genotype_id_all_trait(raw_filter: customs.RawAllFilter):
    return rawService.get_raw_join_all_trait(raw_filter=raw_filter)


@router.post(
    "/field/search",
    response_model=str,
    dependencies=[Depends(get_db)],
    description="Create a new field collection",
)
async def search(raw_collection_field: customs.RawCollectionFieldFilter):
    try:
        rawService.search_field_data(raw_collection_field=raw_collection_field, name_csv = "test.csv")
        return "OK"
    except ValueError as err:
        raise HTTPException(
            status_code=404,
            detail= "Error -> {}".format(err)
        )
    