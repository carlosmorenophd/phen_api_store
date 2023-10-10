from app import models
from app.schemas import schemas


def find_by_id(id: int):
    try:
        return models.Location.get_by_id(id)
    except Exception:
        raise ValueError("Location can not found")


def find_by_country_number(number: int, country: str):
    return models.Location.select().where(
        models.Location.number == number,
        models.Location.country == country,
    ).first()


def create(location: schemas.Location):
    db_entity = models.Location.filter(
        models.Location.number == location.number
    ).first()
    if db_entity:
        return db_entity
    db_entity = models.Location(
        number=location.number,
        country=location.country,
        institute_name=location.institute_name,
        cooperator=location.cooperator,
        latitude=location.latitude,
        latitude_degrees=location.latitude_degrees,
        latitude_minutes=location.latitude_minutes,
        longitude=location.longitude,
        longitude_degrees=location.longitude_degrees,
        longitude_minutes=location.longitude_minutes,
        altitude=location.altitude,
    )
    db_entity.save()
    return db_entity


def find_by_number(number: int):
    return models.Location.filter(models.Location.number == number).first()
