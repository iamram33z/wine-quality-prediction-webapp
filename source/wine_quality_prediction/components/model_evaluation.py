"""
This module contains the ModelEvaluation class which is responsible for evaluating the model performance.
"""

# Importing Required Libraries
import os
from pathlib import Path
from urllib.parse import urlparse

import joblib
import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
from flask.cli import load_dotenv
from mlflow import register_model
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from wine_quality_prediction import logger
from wine_quality_prediction.entity.config_entity import ModelEvaluationConfig
from wine_quality_prediction.utils.common import save_json


# Defining the ModelEvaluation class
class ModelEvaluation:
    """
    This class is responsible for evaluating the model performance.
    """

    def __init__(self, config: ModelEvaluationConfig):
        """
        Constructor for ModelEvaluation class.
        """
        self.config = config

    def evaluate_metrics(self, actual, predicted):
        """
        This method is used to evaluate the model performance.
        """
        try:
            # Calculating the metrics
            rmse = np.sqrt(mean_squared_error(actual, predicted))
            mae = mean_absolute_error(actual, predicted)
            r2 = r2_score(actual, predicted)

            # Saving the metrics
            metrics = {"rmse": rmse, "mae": mae, "r2": r2}

            return metrics

        except Exception as e:
            logger.exception(e)
            raise e

    def log_in_mlflow(self):
        """
        This method is used to log in to MLflow.
        """
        try:
            wine_test_data = pd.read_csv(self.config.test_data)
            model = joblib.load(self.config.model)

            test_x = wine_test_data.drop(self.config.target_column, axis=1)
            test_y = wine_test_data[self.config.target_column]

            mlflow.set_registry_uri(self.config.mlflow_uri)
            tracking_uri_type_store = urlparse(self.config.mlflow_uri)

            with mlflow.start_run():
                predicted = model.predict(test_x)
                metrics = self.evaluate_metrics(test_y, predicted)

                # Saving the scores
                scores = {
                    "rmse": metrics["rmse"],
                    "mae": metrics["mae"],
                    "r2": metrics["r2"],
                }

                # Convert the string path to a Path object
                metrics_file_path = Path(self.config.metrics_file)
                save_json(path=metrics_file_path, data=scores)

                mlflow.log_params(self.config.params)
                mlflow.log_metric("rmse", metrics["rmse"])
                mlflow.log_metric("mae", metrics["mae"])
                mlflow.log_metric("r2", metrics["r2"])

                # Model registry does not support joblib files
                if tracking_uri_type_store.scheme != "file":
                    mlflow.sklearn.log_model(
                        model, artifact_path=self.config.model_name
                    )
                    mlflow.register_model(
                        model_uri=f"runs:/{mlflow.active_run().info.run_id}/{self.config.model_name}",
                        name=self.config.model_name,
                    )
                else:
                    mlflow.sklearn.log_model(model, self.config.model_name)

        except Exception as e:
            logger.exception(e)
            raise e
