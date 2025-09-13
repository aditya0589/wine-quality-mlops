import os
import urllib.request as request
import zipfile
from src.project.utils import logger
from src.project.utils.common import get_size
from pathlib import Path
from src.project.entity.config_entity import (DataIngestionConfig)



import os
from urllib import request

class DataIngestion:
    def __init__(self, config):
        self.config = config

    def download_file(self):
        # Make sure directory exists
        os.makedirs(os.path.dirname(self.config.local_data_file), exist_ok=True)

        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            print(f"{filename} downloaded with headers:\n{headers}")
        else:
            print("File already exists.")


    def extract_zip_file(self):
        """
        extracts data into the data diresctory
        the functions returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
