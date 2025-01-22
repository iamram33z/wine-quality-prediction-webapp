"""
This module contains the ConfigurationManager class which is responsible for reading the configuration files and returning the configuration objects.
"""

# Importing necessary libraries
from wine_quality_prediction.constants import *
from wine_quality_prediction.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from wine_quality_prediction.utils.common import read_yaml, create_directory

# Defining the ConfigurationManager class
class ConfigurationManager:
    def __init__(self,
            config_file_path: Path = CONFIG_FILE_PATH,
            params_file_path: Path = PARAMS_FILE_PATH,
            schema_file_path: Path = SCHEMA_FILE_PATH):

            self.config = read_yaml(config_file_path)
            self.params = read_yaml(params_file_path)
            self.schema = read_yaml(schema_file_path)

            create_directory([self.config.artifacts_root], verbose=True)


# Defining the get_data_ingestion_config method
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directory([config.root_dir], verbose=True)

        data_ingestion_config_ = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config_

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directory([config.root_dir], verbose=True)

        data_validation_config_ = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir,
            all_schema=schema
        )

        return data_validation_config_

# Defining the get_data_transformation_config method
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directory([config.root_dir], verbose=True)

        data_transformation_config_ = DataTransformationConfig(
            root_dir=config.root_dir,
            input_data=config.input_data,
            train_data = config.train_data,
            test_data = config.test_data
        )

        return data_transformation_config_
