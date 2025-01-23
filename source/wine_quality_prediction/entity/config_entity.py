"""
This module contains the configuration entity for data ingestion.
"""

# Importing required libraries
from dataclasses import dataclass
from pathlib import Path

# Defining the DataIngestionConfig class for data ingestion configuration
@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Configuration for data ingestion.
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


# Defining the DataValidationConfig class for data validation configuration
@dataclass(frozen=True)
class DataValidationConfig:
    """
    Configuration for data validation.
    """
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict

# Defining the DataTransformationConfig class for data transformation configuration
@dataclass(frozen=True)
class DataTransformationConfig:
    """
    Configuration for data transformation.
    """
    root_dir: Path
    input_data: Path
    train_data: Path
    test_data: Path

# Defining the DataTrainingConfig class for data training configuration
@dataclass(frozen=True)
class ModelTrainingConfig:
    """
    Configuration for model training.
    """
    root_dir: Path
    train_data: Path
    test_data: Path
    model_name: str
    n_estimators: int
    max_depth: int
    random_state: int
    target_column: str

# Defining the ModelEvaluationConfig class for model evaluation configuration
@dataclass(frozen=True)
class ModelEvaluationConfig:
    """
    Configuration for model evaluation.
    """
    root_dir: Path
    model_name: str
    model: Path
    test_data: Path
    target_column: str
    metrics_file: Path
    metrics: dict
    mlflow_uri: str
    params: dict
