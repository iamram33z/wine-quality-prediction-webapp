"""
This module contains the DataIngestion class which is responsible for downloading the data from the source URL and extracting the data from the zip file.
"""

# Importing Required Libraries
import os
import urllib.request as request
import zipfile
from pathlib import Path

from wine_quality_prediction import logger
from wine_quality_prediction.entity.config_entity import DataIngestionConfig
from wine_quality_prediction.utils.common import get_size


# Defining the DataIngestion class
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self, headers=None):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL, filename=self.config.local_data_file
            )
            logger.info(
                f"Data downloaded from the source URL: %s with the following info: \n{headers}",
                self.config.source_URL,
            )
        else:
            logger.info(
                f"Data already exists at the path: %s with the following size info: \n{get_size(Path(self.config.local_data_file))}",
                self.config.local_data_file,
            )

    def extract_zip(self):
        unzip_path = self.config.unzip_dir
        if not os.path.exists(unzip_path):
            with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info("Data extracted to the path: %s", unzip_path)
            logger.info("Size of the extracted data:")

        else:
            logger.info("Data already extracted at the path: %s", unzip_path)
            get_size(unzip_path)
