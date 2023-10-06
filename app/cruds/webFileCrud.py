from app import models


def get_or_create(name: str):
    return models.WebFile.get_or_create(name=name)
