import models
import schemas


def create_web_file(web_file: schemas.WebFile):
    db_webFile = models.WebFile(name= web_file.name)
    return db_webFile
