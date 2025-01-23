"""
This module contains the ModelTraining class which is used to train the model.
"""

# Importing required libraries
import os
import pandas as pd
from wine_quality_prediction import logger
from wine_quality_prediction.entity.config_entity import ModelTrainingConfig
from sklearn.ensemble import RandomForestRegressor
import joblib

# Defining the ModelTraining class
class ModelTraining:
    """
    This class is used to train the model.
    """
    def __init__(self, config: ModelTrainingConfig):
        """
        Constructor for ModelTraining class.
        """
        self.config = config

    def train_model(self):
        """
        This method is used to train the model.
        """
        try:
            # Reading the data
            wine_train_data = pd.read_csv(self.config.train_data)

            train_x = wine_train_data.drop(self.config.target_column, axis=1)
            test_x = wine_train_data.drop(self.config.target_column, axis=1)
            train_y = wine_train_data[self.config.target_column]
            test_y = wine_train_data[self.config.target_column]

            # Instantiating the model
            model = RandomForestRegressor(n_estimators=self.config.n_estimators,
                                          max_depth=self.config.max_depth,
                                          random_state=self.config.random_state)

            # Training the model
            model.fit(train_x, train_y)

            # Saving the model
            joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))

        except Exception as e:
            logger.exception(e)
            raise e