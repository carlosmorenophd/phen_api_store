from .pathDirectory import PathDirectory
from .compressFile import DecompressFile


class WorkSpace:
    def __init__(self, path):
        self.pathDirectory = PathDirectory(home=path)
        self.decompressFile = DecompressFile(home=path)
    def clean_workspace(self):
        self.pathDirectory.clean_work_directory()
    def start_file(self, file_name):
        source_file = self.pathDirectory.get_file_from_file_directory(file=file_name)
        destiny_folder = self.pathDirectory.get_work_directory()
        self.decompressFile.unzip_file(source_file=source_file, destiny_folder=destiny_folder)
        self.decompressFile.extract_all_gz(destiny_folder)