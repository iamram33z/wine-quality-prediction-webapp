"""
This is the main module of the project.
"""

from colorama import Fore, Style
from wine_quality_prediction import logger
from wine_quality_prediction.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from wine_quality_prediction.pipeline.stage_02_data_validation import DataValidationPipeline
from wine_quality_prediction.pipeline.stage_03_data_transformation import DataTransformationPipeline
from wine_quality_prediction.pipeline.stage_04_model_training import ModelTrainingPipeline


# Initialize colorama
import colorama
from wine_quality_prediction.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline


colorama.init(autoreset=True)


# Defining the DataIngestionPipeline Stage & Main Function
STAGE_1_NAME = "STAGE 01: DATA INGESTION"
try:
    logger.info(f"{Fore.BLUE}>>>>> Starting the {STAGE_1_NAME} <<<<<{Style.RESET_ALL}")
    DataIngestionPipeline.main()
    logger.info(f"{Fore.GREEN}>>>>> The {STAGE_1_NAME} Pipeline Completed <<<<<{Style.RESET_ALL}")
except Exception as e:
    logger.exception(e)
    raise e


# Defining the DataValidationPipeline Stage & Main Function
STAGE_2_NAME = "STAGE 02: DATA VALIDATION"
try:
    logger.info(f"{Fore.BLUE}>>>>> Starting the {STAGE_2_NAME} <<<<<{Style.RESET_ALL}")
    DataValidationPipeline.main()
    logger.info(f"{Fore.GREEN}>>>>> The {STAGE_2_NAME} Pipeline Completed <<<<<{Style.RESET_ALL}")
except Exception as e:
    logger.exception(e)
    raise e


# Defining the DataTransformationPipeline Stage & Main Function
STAGE_3_NAME = "STAGE 03: DATA TRANSFORMATION"
try:
    logger.info(f"{Fore.BLUE}>>>>> Starting the {STAGE_3_NAME} <<<<<{Style.RESET_ALL}")
    DataTransformationPipeline.main()
    logger.info(f"{Fore.GREEN}>>>>> The {STAGE_3_NAME} Pipeline Completed <<<<<{Style.RESET_ALL}")
except Exception as e:
    logger.exception(e)
    raise e


# Defining the ModelTrainingPipeline Stage & Main Function
STAGE_4_NAME = "STAGE 04: MODEL TRAINING"
try:
    logger.info(f"{Fore.BLUE}>>>>> Starting the {STAGE_4_NAME} <<<<<{Style.RESET_ALL}")
    ModelTrainingPipeline.main()
    logger.info(f"{Fore.GREEN}>>>>> The {STAGE_4_NAME} Pipeline Completed <<<<<{Style.RESET_ALL}")
except Exception as e:
    logger.exception(e)
    raise e


# Defining the ModelEvaluationPipeline Stage & Main Function
STAGE_5_NAME = "STAGE 05: MODEL EVALUATION"
try:
    logger.info(f"{Fore.BLUE}>>>>> Starting the {STAGE_5_NAME} <<<<<{Style.RESET_ALL}")
    ModelEvaluationPipeline.main()
    logger.info(f"{Fore.GREEN}>>>>> The {STAGE_5_NAME} Pipeline Completed <<<<<{Style.RESET_ALL}")
except Exception as e:
    logger.exception(e)
    raise e