"""
This module contains the DataValidationPipeline class which is responsible for validating the data.
"""

# Importing necessary libraries
from wine_quality_prediction.components.data_validation import DataValidation
from wine_quality_prediction.config.configuration import ConfigurationManager
from wine_quality_prediction import logger

# Defining the DataValidationPipeline Stage
STAGE_NAME = "STAGE 02: DATA VALIDATION"

# Defining the DataValidationPipeline class
class DataValidationPipeline:
    def __init__(self):
        pass

    @staticmethod
    def main():
        # Instantiating the ConfigurationManager class
        config_manager = ConfigurationManager()
        # Getting the data validation configuration
        data_validation_config = config_manager.get_data_validation_config()
        # Instantiating the DataValidation class
        data_validation = DataValidation(data_validation_config)
        # Validating the data
        data_validation.validate_all_columns()


if __name__ == "__main__":
    try:
        logger.info(f">>>>> Starting {STAGE_NAME} <<<<<")
        DataValidationPipeline.main()
        logger.info(f">>>>> Completed {STAGE_NAME} <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e