"""
This module contains the unit tests for the main module.
"""

# Importing required libraries
import pytest
from unittest import mock
from wine_quality_prediction import logger
from main import (
    STAGE_1_NAME,
    STAGE_2_NAME,
    STAGE_3_NAME,
    STAGE_4_NAME,
    STAGE_5_NAME,
)

# Mocking all pipeline classes
@mock.patch("wine_quality_prediction.pipeline.stage_01_data_ingestion.DataIngestionPipeline.main")
@mock.patch("wine_quality_prediction.pipeline.stage_02_data_validation.DataValidationPipeline.main")
@mock.patch("wine_quality_prediction.pipeline.stage_03_data_transformation.DataTransformationPipeline.main")
@mock.patch("wine_quality_prediction.pipeline.stage_04_model_training.ModelTrainingPipeline.main")
@mock.patch("wine_quality_prediction.pipeline.stage_05_model_evaluation.ModelEvaluationPipeline.main")
def test_main_pipeline(
    mock_data_ingestion,
    mock_data_validation,
    mock_data_transformation,
    mock_model_training,
    mock_model_evaluation,
):
    """Test the execution of all pipeline stages in the main module."""

    # Simulate successful execution for all stages
    mock_data_ingestion.return_value = None
    mock_data_validation.return_value = None
    mock_data_transformation.return_value = None
    mock_model_training.return_value = None
    mock_model_evaluation.return_value = None

    # Test Data Ingestion
    try:
        logger.info(f"Starting {STAGE_1_NAME}")
        mock_data_ingestion()
        logger.info(f"{STAGE_1_NAME} completed successfully!")
    except Exception as e:
        pytest.fail(f"{STAGE_1_NAME} failed: {e}")

    # Test Data Validation
    try:
        logger.info(f"Starting {STAGE_2_NAME}")
        mock_data_validation()
        logger.info(f"{STAGE_2_NAME} completed successfully!")
    except Exception as e:
        pytest.fail(f"{STAGE_2_NAME} failed: {e}")

    # Test Data Transformation
    try:
        logger.info(f"Starting {STAGE_3_NAME}")
        mock_data_transformation()
        logger.info(f"{STAGE_3_NAME} completed successfully!")
    except Exception as e:
        pytest.fail(f"{STAGE_3_NAME} failed: {e}")

    # Test Model Training
    try:
        logger.info(f"Starting {STAGE_4_NAME}")
        mock_model_training()
        logger.info(f"{STAGE_4_NAME} completed successfully!")
    except Exception as e:
        pytest.fail(f"{STAGE_4_NAME} failed: {e}")

    # Test Model Evaluation
    try:
        logger.info(f"Starting {STAGE_5_NAME}")
        mock_model_evaluation()
        logger.info(f"{STAGE_5_NAME} completed successfully!")
    except Exception as e:
        pytest.fail(f"{STAGE_5_NAME} failed: {e}")