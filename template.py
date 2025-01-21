"""
This script creates the project structure for the wine_quality_prediction project.
"""

# Import Libraries
import logging
import os
from pathlib import Path

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Project Details
PROJECT_NAME = "WINE_QUALITY_PREDICTION"
project_path = Path(os.getcwd())

# File Details
list_of_files = [
    ".github/workflows/.gitkeep",
    ".github/workflows/CI.yml",
    f"source/{PROJECT_NAME}/__init__.py",
    f"source/{PROJECT_NAME}/components/__init__.py",
    f"source/{PROJECT_NAME}/components/data_ingestion.py",
    f"source/{PROJECT_NAME}/utils/__init__.py",
    f"source/{PROJECT_NAME}/utils/common.py",
    f"source/{PROJECT_NAME}/config/__init__.py",
    f"source/{PROJECT_NAME}/config/configuration.py",
    f"source/{PROJECT_NAME}/pipeline/__init__.py",
    f"source/{PROJECT_NAME}/pipeline/stage_01_data_ingestion.py",
    f"source/{PROJECT_NAME}/entity/__init__.py",
    f"source/{PROJECT_NAME}/entity/config_entity.py",
    f"source/{PROJECT_NAME}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    "notebooks/trial1.ipynb",
    "templates/index.html",
    "tests/test_main.py",
    "tasks.py",
    ".coveragerc",
]

# Create directories and files if they do not exist
for file_path in list_of_files:
    file = Path(file_path)
    if not file.parent.exists():
        file.parent.mkdir(parents=True, exist_ok=True)
        logging.info("Created directory: %s", file.parent)
    else:
        logging.info("Directory already exists: %s", file.parent)

    if not file.exists():
        file.touch()
        logging.info("Created file: %s", file)
    else:
        logging.info("File already exists: %s", file)
