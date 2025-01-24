"""
This file contains the class for prediction.
"""


# Import Necessary Libraries
import joblib
import os
import numpy as np
import pandas as pd
from pathlib import Path

# Get the directories
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
grandparent_dir = parent_dir.parent
great_grandparent_dir = grandparent_dir.parent

# Class for Prediction
class WineQualityPrediction:
    def __init__(self):
        # Load the model
        self.model = joblib.load(f"{great_grandparent_dir}/artifacts/model_training/random_forest_model.joblib")

    def predict(self, input_data_: pd.DataFrame) -> str:
        # Make Prediction
        prediction_ = self.model.predict(input_data_)

        # Make the prediction as String percentage
        prediction_ = f"{prediction_[0]:.2f}%"
        return prediction_