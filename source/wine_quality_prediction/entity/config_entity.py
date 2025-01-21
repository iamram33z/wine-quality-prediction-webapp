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