import models
from schemas import schemas
from typing import Union

def find_by_id(id: int):
    try:
        return models.Genotype.get_by_id(id)
    except Exception:
        raise ValueError("Genotype can not found")


def create(genotype: schemas.Genotype):
    db_entity = models.Genotype.filter(
        models.Genotype.c_id == genotype.c_id
    ).filter(
        models.Genotype.s_id == genotype.s_id
    ).first()
    if db_entity:
        return db_entity
    db_entity = models.Genotype(
        c_id=genotype.c_id,
        s_id=genotype.s_id,
        cross_name=genotype.cross_name,
        history_name=genotype.history_name,
    )
    db_entity.save()
    return db_entity


def find_by_ids(c_id: Union[int, None], s_id: Union[int, None]):
    query = models.Genotype.select()
    if c_id != None:
        query = query.where(
            models.Genotype.c_id == c_id
        )
    if s_id != None:
        query = query.where(
            models.Genotype.s_id == s_id
        )
    if s_id == None and c_id == None:
        raise ValueError(
            "You need to pass some value to search")    
    query = query.execute()
    if not query:
        raise ValueError(
            "The genotype does not exist {}-{}".format(c_id, s_id))
    return query[0]
