from app import models, schemas


def find_by_id(id: int):
    try:
        return models.Genotype.get_by_id(id)
    except Exception:
        raise ValueError("Genotype can not found")