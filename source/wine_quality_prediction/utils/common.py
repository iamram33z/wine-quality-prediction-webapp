"""
Common Utility Functions for Wine Quality Prediction Project are defined here.
"""

# Importing Required Libraries
import os
from box.exceptions import BoxValueError
from box import ConfigBox
import yaml
from wine_quality_prediction import logger
import json
import joblib
from ensure import ensure_annotations
from pathlib import Path
from typing import Any, Dict, List, Tuple


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read the YAML file and return the ConfigBox object.

    Args:
    path_to_yaml: Path to the YAML file.

    Returns:
    ConfigBox object.

    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info(f"YAML file loaded successfully from the path: {path_to_yaml}")
        return ConfigBox(config)
    except FileNotFoundError:
        logger.error(f"File not found at the specified location: {path_to_yaml}")
        raise FileNotFoundError("yaml file not found")
    except BoxValueError:
        logger.error(f"Error occurred while loading the YAML file from the path: {path_to_yaml}")
        raise BoxValueError("Error occurred while loading the YAML file")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        raise e


@ensure_annotations
def create_directory(path_to_directories: list, verbose: True):
    """
    Create directories if not exists.

    Args:
    path_to_directories: List of paths to directories.
    verbose: Print the logs.

    Returns:
    None

    """
    for directory in path_to_directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            if verbose:
                logger.info(f"Directory created at the path: {directory}")
        else:
            if verbose:
                logger.info(f"Directory already exists at the path: {directory}")


@ensure_annotations
def save_jason(path: Path, data:dict):
    """
    Save the data in JSON format.

    Args:
        path (Path): Path to save the JSON file.
        data (dict): Data to save in JSON format.

    Returns:
        None
    """
    with open(path, "w") as json_file:
        content = json.load(json_file)

    logger.info(f"json file loaded successfully from the path: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_binary(path: Path, data: Any):
    """
    Save the data in binary format.

    Args:
        path (Path): Path to save the binary file.
        data (Any): Data to save in binary format.

    Returns:
        None
    """
    with open(path, "wb") as binary_file:
        joblib.dump(data, binary_file)
    logger.info(f"Binary file saved successfully at the path: {path}")


@ensure_annotations
def load_binary(path: Path) -> Any:
    """
    Load the binary file.

    Args:
        path (Path): Path to load the binary file.

    Returns:
        Any: Data loaded from the binary file.
    """
    with open(path, "rb") as binary_file:
        data = joblib.load(binary_file)
    logger.info(f"Binary file loaded successfully from the path: {path}")
    return data


@ensure_annotations
def get_size(p) -> str:
    """
    Get the size of the file.

    Args:
        p: Path to the file.

    Returns:
        str: Size of the file.
    """
    size = os.path.getsize(p)
    for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return size