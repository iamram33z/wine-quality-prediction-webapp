"""
Sample application to demonstrate the usage of the Calculator class.
"""

# Import Necessary Libraries
import os
import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from wine_quality_prediction.pipeline.prediction import WineQualityPrediction

# Create an instance of the Flask class
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/train", methods=["GET", "POST"])
def train():
    if request.method == "POST":
        os.system("python main.py")
        return "Model Trained Successfully!"
    elif request.method == "GET":
        return "This endpoint triggers model training. Use POST to start training."


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        try:
            # Read the input data from the form
            fixed_acidity = float(request.form["fixed_acidity"])
            volatile_acidity = float(request.form["volatile_acidity"])
            citric_acid = float(request.form["citric_acid"])
            residual_sugar = float(request.form["residual_sugar"])
            chlorides = float(request.form["chlorides"])
            free_sulfur_dioxide = float(request.form["free_sulfur_dioxide"])
            total_sulfur_dioxide = float(request.form["total_sulfur_dioxide"])
            density = float(request.form["density"])
            pH = float(request.form["pH"])
            sulphates = float(request.form["sulphates"])
            alcohol = float(request.form["alcohol"])

            # Create a dictionary of the input data
            input_data = {
                "fixed_acidity": fixed_acidity,
                "volatile_acidity": volatile_acidity,
                "citric_acid": citric_acid,
                "residual_sugar": residual_sugar,
                "chlorides": chlorides,
                "free_sulfur_dioxide": free_sulfur_dioxide,
                "total_sulfur_dioxide": total_sulfur_dioxide,
                "density": density,
                "pH": pH,
                "sulphates": sulphates,
                "alcohol": alcohol
            }

            # Convert the input data to a DataFrame
            input_df = pd.DataFrame([input_data])

            # Mapping of input feature names to the feature names used during model training
            feature_name_mapping = {
                "fixed_acidity": "fixed acidity",
                "volatile_acidity": "volatile acidity",
                "citric_acid": "citric acid",
                "residual_sugar": "residual sugar",
                "chlorides": "chlorides",
                "free_sulfur_dioxide": "free sulfur dioxide",
                "total_sulfur_dioxide": "total sulfur dioxide",
                "density": "density",
                "pH": "pH",
                "sulphates": "sulphates",
                "alcohol": "alcohol"
            }

            # Rename the columns in the input DataFrame
            input_df.rename(columns=feature_name_mapping, inplace=True)

            # Create an instance of the WineQualityPrediction class
            prediction = WineQualityPrediction()
            predictor = prediction.predict(input_df)

            # Return the prediction
            return render_template("result.html", prediction=str(predictor))

        except Exception as e:
            return "An error occurred. Please check the input data."

    else:
        return "An error occurred."

# Main Function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)