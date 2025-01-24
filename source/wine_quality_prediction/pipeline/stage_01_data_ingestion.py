"""
This module contains the code for the first stage of the pipeline, i.e., Data Ingestion.
"""

from wine_quality_prediction import logger
# Importing necessary libraries
from wine_quality_prediction.components.data_ingestion import DataIngestion
from wine_quality_prediction.config.configuration import ConfigurationManager

# Defining the DataIngestionPipeline Stage
STAGE_NAME = "STAGE 01: DATA INGESTION"


# Defining the DataIngestionPipeline class
class DataIngestionPipeline:
    def __init__(self):
        pass

    @staticmethod
    def main():
        # Instantiating the ConfigurationManager class
        config_manager = ConfigurationManager()
        # Getting the data ingestion configuration
        data_ingestion_config = config_manager.get_data_ingestion_config()
        # Instantiating the DataIngestion class
        data_ingestion = DataIngestion(data_ingestion_config)
        # Downloading the data
        data_ingestion.download_data()
        # Extracting the data
        data_ingestion.extract_zip()


if __name__ == "__main__":
    try:
        logger.info(f">>>>> Starting {STAGE_NAME} <<<<<")
        DataIngestionPipeline.main()
        logger.info(f">>>>> Completed {STAGE_NAME} <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
