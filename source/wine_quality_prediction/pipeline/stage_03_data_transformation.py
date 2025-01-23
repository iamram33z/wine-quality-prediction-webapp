"""
This module contains the DataTransformationPipeline class which is responsible for performing the data transformation
"""

# Importing necessary libraries
from wine_quality_prediction.components.data_transformation import DataTransformation
from wine_quality_prediction.config.configuration import ConfigurationManager
from wine_quality_prediction import logger

# Defining the DataTransformationPipeline Stage
STAGE_NAME = "STAGE 03: DATA TRANSFORMATION"

# Defining the DataTransformationPipeline class
class DataTransformationPipeline:
    def __init__(self):
        pass

    @staticmethod
    def main():
        try:
            # Verifying the Data Validation Status
            with open("artifacts/data_validation/status.txt", "r") as f:
                data_validation_status = f.read().split(" ")[-1]

            if data_validation_status == "True":
                # Instantiating the ConfigurationManager class
                config_manager = ConfigurationManager()
                # Getting the data transformation configuration
                data_transformation_config = config_manager.get_data_transformation_config()
                # Instantiating the DataTransformation class
                data_transformation = DataTransformation(config=data_transformation_config)
                # Transforming the data
                data_transformation.train_test_split(),
            else:
                raise Exception("Data Validation Failed. Please validate the data before proceeding to Data Transformation.")


        except Exception as e:
            logger.exception(e)
            raise e

if __name__ == "__main__":
    try:
        logger.info(f">>>>> Starting {STAGE_NAME} <<<<<")
        DataTransformationPipeline.main()
        logger.info(f">>>>> Completed {STAGE_NAME} <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e




