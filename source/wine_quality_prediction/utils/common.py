"""
Common Utility Functions for Wine Quality Prediction Project are defined here.
"""

# Importing Required Libraries
import json
import os
from pathlib import Path
from typing import Any, Dict

import joblib
import yaml
from box import ConfigBox
from box import BoxError as BoxValueError
from ensure import ensure_annotations
from wine_quality_prediction import logger


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
        with open(path_to_yaml, "r", encoding="utf-8") as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info("YAML file loaded successfully from the path: %s", path_to_yaml)
        return ConfigBox(config)
    except FileNotFoundError as exc:
        logger.error("File not found at the specified location: %s", path_to_yaml)
        raise FileNotFoundError("yaml file not found") from exc
    except BoxValueError as exc:
        logger.error(
            "Error occurred while loading the YAML file from the path: %s", path_to_yaml
        )
        raise BoxValueError("Error occurred while loading the YAML file") from exc
    except Exception as e:
        logger.error("Error occurred: %s", e)
        raise e


@ensure_annotations
def create_directory(path_to_directories: list, verbose: bool = True):
    """
    Create directories if not exists.

    Args:
    path_to_directories: List of paths to directories.
    verbose: Print the logs.

    Returns:
    None

    """
    for directory in path_to_directories:
        if isinstance(directory, (str, Path)):
            if not os.path.exists(directory):
                os.makedirs(directory)
                if verbose:
                    logger.info("Directory created at the path: %s", directory)
            else:
                if verbose:
                    logger.info("Directory already exists at the path: %s", directory)
        else:
            raise TypeError(f"Expected str or Path, got {type(directory)}")


@ensure_annotations
def save_json(path: Path, data: Dict):
    """
    Save the data in JSON format.

    Args:
        path (Path): Path to save the JSON file.
        data (Dict): Data to save in JSON format.

    Returns:
        None
    """
    with open(path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file)
    logger.info("JSON file saved successfully at the path: %s", path)


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
    logger.info("Binary file saved successfully at the path: %s", path)


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
    logger.info("Binary file loaded successfully from the path: %s", path)
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
    for unit in ["bytes", "KB", "MB", "GB", "TB"]:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return size
