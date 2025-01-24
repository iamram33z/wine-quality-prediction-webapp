"""
This file contains the class for prediction.
"""


# Import Necessary Libraries
import joblib
import numpy as np
import pandas as pd
from pathlib import Path

# Class for Prediction
class WineQualityPrediction:
    def __init__(self):
        self.model = joblib.load(Path("artifacts/model_training/random_forest_model.joblib"))

    def predict(self, data):
        # Make Prediction
        prediction = self.model.predict(data)

        return prediction