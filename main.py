"""
This is the main module of the project.
"""

# Import the Libraries
from wine_quality_prediction import logger
from wine_quality_prediction.pipeline.stage_01_data_ingestion import DataIngestionPipeline

# Defining the DataIngestionPipeline Stage
STAGE_NAME = "STAGE 01: DATA INGESTION"

# Main Function
def main():
    try:
        logger.info(">>>>> Starting the Data Ingestion Pipeline <<<<<")
        DataIngestionPipeline.main()
        logger.info(">>>>> Data Ingestion Pipeline Completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

# Entry Point of the Script

if __name__ == "__main__":
    main()

