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



# Main Function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)