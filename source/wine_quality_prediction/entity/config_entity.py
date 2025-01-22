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