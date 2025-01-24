"""
This module contains the DataTransformation class which is responsible for splitting the data into train and test.
"""

# Importing Required Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from wine_quality_prediction import logger
from wine_quality_prediction.entity.config_entity import \
    DataTransformationConfig


# Defining the DataTransformation class
class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    # # Add other methods here # #

    # Defining the train_test_split method
    def train_test_split(self) -> bool:
        try:
            wine_data = pd.read_csv(self.config.input_data)

            # Splitting the data into train and test
            train, test = train_test_split(wine_data, test_size=0.2, random_state=42)

            # Saving the train and test data
            train.to_csv(self.config.train_data, index=False)
            test.to_csv(self.config.test_data, index=False)

            # Logging the status
            logger.info(
                f"Train and Test data saved successfully at {self.config.root_dir}"
            )
            logger.info(f"Train data shape: {train.shape}")
            logger.info(f"Test data shape: {test.shape}")

            return True

        except Exception as e:
            logger.exception(e)
            raise e
