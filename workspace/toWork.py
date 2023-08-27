from .pathDirectory import PathDirectory
from .compressFile import unzip_file, extract_all_gz


class WorkSpace:
    def __init__(self, path):
        self.pathDirectory = PathDirectory(home=path)

    def clean_workspace(self):
        self.pathDirectory.clean_work_directory()

    def start_file(self, file_name):
        source_file = self.pathDirectory.get_file_from_file_directory(file=file_name)
        destiny_folder = self.pathDirectory.get_work_directory()
        unzip_file(source_file=source_file, destiny_folder=destiny_folder)
        extract_all_gz(destiny_folder)
