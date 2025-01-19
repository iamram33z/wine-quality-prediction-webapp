# Import Libraries
import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Project Details
project_name = "Wine-Quality-Prediction"
project_path = Path(os.getcwd())

# File Details
list_of_files = [
    ".github/workflows/.gitkeep",
    ".github/workflows/CI.yml",
    f"source/{project_name}/__init__.py",
    f"source/{project_name}/components/__init__.py",
    f"source/{project_name}/utils/__init__.py",
    f"source/{project_name}/utils/common.py",
    f"source/{project_name}/config/__init__.py",
    f"source/{project_name}/config/configuration.py",
    f"source/{project_name}/pipeline/__init__.py",
    f"source/{project_name}/entity/__init__.py",
    f"source/{project_name}/entity/config_entity.py",
    f"source/{project_name}/constants/__init__.py",
    "config/config.yml",
    "params.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    "research/trial1.ipynb",
    "templates/index.html",
    "tests/test_main.py",

]

# Create directories and files if they do not exist
for file_path in list_of_files:
    file = Path(file_path)
    if not file.parent.exists():
        file.parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory: {file.parent}")
    else:
        logging.info(f"Directory already exists: {file.parent}")

    if not file.exists():
        file.touch()
        logging.info(f"Created file: {file}")
    else:
        logging.info(f"File already exists: {file}")
