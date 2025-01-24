"""
This module contains the ConfigurationManager class which is responsible for reading the configuration files and returning the configuration objects.
"""

# Importing necessary libraries
from wine_quality_prediction.constants import *
from wine_quality_prediction.entity.config_entity import (
    DataIngestionConfig, DataTransformationConfig, DataValidationConfig,
    ModelEvaluationConfig, ModelTrainingConfig)
from wine_quality_prediction.utils.common import (create_directory, read_yaml,
                                                  save_json)


# Defining the ConfigurationManager class
class ConfigurationManager:
    def __init__(
        self,
        config_file_path: Path = CONFIG_FILE_PATH,
        params_file_path: Path = PARAMS_FILE_PATH,
        schema_file_path: Path = SCHEMA_FILE_PATH,
    ):

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
            unzip_dir=config.unzip_dir,
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
            all_schema=schema,
        )

        return data_validation_config_

    # Defining the get_data_transformation_config method
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directory([config.root_dir], verbose=True)

        data_transformation_config_ = DataTransformationConfig(
            root_dir=config.root_dir,
            input_data=config.input_data,
            train_data=config.train_data,
            test_data=config.test_data,
        )

        return data_transformation_config_

    # Defining the get_model_training_config method
    def get_model_training_config(self) -> ModelTrainingConfig:
        config = self.config.model_training
        params = self.params.RandomForest
        schema = self.schema.TARGET_COLUMN

        create_directory([config.root_dir], verbose=True)

        model_training_config_ = ModelTrainingConfig(
            root_dir=config.root_dir,
            train_data=config.train_data,
            test_data=config.test_data,
            model_name=config.model_name,
            n_estimators=params.n_estimators,
            max_depth=params.max_depth,
            random_state=params.random_state,
            target_column=schema.name,
        )

        return model_training_config_

    # Defining the get_model_evaluation_config method
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.RandomForest
        schema = self.schema.TARGET_COLUMN

        create_directory([config.root_dir], verbose=True)

        model_evaluation_config_ = ModelEvaluationConfig(
            root_dir=config.root_dir,
            model_name=config.model_name,
            model=config.model,
            test_data=config.test_data,
            target_column=schema.name,
            metrics_file=config.metrics_file,
            mlflow_uri=config.mlflow_uri,
            params=params,  # since I want all the parameters
        )

        return model_evaluation_config_
