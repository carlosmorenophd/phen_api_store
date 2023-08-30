from .pathDirectory import PathDirectory
from .compressFile import unzip_file, extract_all_gz
from database.schema import Database
from database.xlsToDatabase import get_locations, get_genotypes, get_raw_collections


class WorkSpace:
    def __init__(self, path):
        self.pathDirectory = PathDirectory(home=path)
        self.database = Database()

    def clean_workspace(self):
        self.pathDirectory.clean_work_directory()

    def prepare_folder_files(self, file_name):
        source_file = self.pathDirectory.get_file_from_file_directory(file=file_name)
        destiny_folder = self.pathDirectory.get_work_directory()
        unzip_file(source_file=source_file, destiny_folder=destiny_folder)
        extract_all_gz(destiny_folder)

    def storage_on_database(self):
        self.database.insert_location(get_locations(self.pathDirectory.get_work_directory()))
        self.database.insert_genotypes(get_genotypes(self.pathDirectory.get_work_directory()))
        self.database.insert_raw(get_raw_collections(self.pathDirectory.get_work_directory()))
