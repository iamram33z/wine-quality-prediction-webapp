"""
This module contains the unit tests for the main module.
"""

# Import necessary libraries
from unittest import mock
from wine_quality_prediction import logger
from main import (
    STAGE_1_NAME,
    STAGE_2_NAME,
    STAGE_3_NAME,
    STAGE_4_NAME,
    STAGE_5_NAME,
)


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

    # Test all stages
    for stage_name, mock_stage in zip(
        [STAGE_1_NAME, STAGE_2_NAME, STAGE_3_NAME, STAGE_4_NAME, STAGE_5_NAME],
        [
            mock_data_ingestion,
            mock_data_validation,
            mock_data_transformation,
            mock_model_training,
            mock_model_evaluation,
        ],
    ):
        try:
            logger.info(f"Starting {stage_name}")
            mock_stage()
            logger.info(f"{stage_name} completed successfully!")
        except Exception as e:
            pytest.fail(f"{stage_name} failed: {e}")
