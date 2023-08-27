from zipfile import ZipFile
import os, shutil, gzip

class DecompressFile:
    def __init__(self, home):
        self.home_path = home

    def unzip_file(self, source_file, destiny_folder):
        with ZipFile(source_file, 'r') as zObject:
            zObject.extractall(destiny_folder)
        zObject.close()
    
    def extract_all_gz(self, dir):
        for file in os.listdir(dir):
            if file.endswith(".gz"):
                gz_path = os.path.join(dir, file)
                print(file)
                extract_path = os.path.join(dir, file.replace(".gz", ""))
                with gzip.open(gz_path, "rb") as inFile, open(
                    extract_path, "wb"
                ) as outfile:
                    shutil.copyfileobj(inFile, outfile)
