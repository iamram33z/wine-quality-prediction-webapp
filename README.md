# End to End Data Science Project: Wine Quality Prediction Web Application
An End to End Data Science Project regarding a Wine Quality Predicting Web Application
#### Keywords: Data Science, Machine Learning, Web Application, Wine Quality Prediction, Flask, AWS EC2

## Table of Contents
1. [Introduction](#introduction)
2. [Data Collection](#data-collection)
3. [Data Preprocessing](#data-preprocessing)
4. [Exploratory Data Analysis](#exploratory-data-analysis)
5. [Model Building](#model-building)
6. [Model Evaluation](#model-evaluation)
7. [Model Deployment](#model-deployment)
8. [Workflows](#workflows)
9. [Conclusion](#conclusion)
10. [References](#references)
11. [Author](#author)
12. [License](#license)
13. [Acknowledgements](#acknowledgements)
14. [Appendix](#appendix)

## Introduction
This project is an end to end data science project regarding a Wine Quality Prediction Web Application. The main goal of this project is to predict the quality of the wine based on the given features. The dataset used in this project is the Wine Quality Dataset which is available on the UCI Machine Learning Repository. The dataset consists of 12 features and 1 target variable. The features are fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, alcohol, and quality. The target variable is the quality of the wine which ranges from 3 to 9. The dataset consists of 1599 samples. The dataset is preprocessed and then used to build a machine learning model. The model is then evaluated using various evaluation metrics. The model is then deployed as a web application using Flask. The web application is then deployed on AWS Cloud 9.

## Data Collection
The dataset used in this project is the Wine Quality Dataset which is available on the UCI Machine Learning Repository. The dataset consists of 12 features and 1 target variable. The features are fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, alcohol, and quality. The target variable is the quality of the wine which ranges from 3 to 9. The dataset consists of 1599 samples.

## Data Preprocessing
The dataset is preprocessed before building the machine learning model. The preprocessing steps include handling missing values, handling categorical variables, feature scaling, and splitting the dataset into training and testing sets.

## Exploratory Data Analysis
The dataset is explored using various visualizations. The relationships between the features and the target variable are visualized using scatter plots, bar plots, and box plots.

## Model Building
The dataset is used to build a machine learning model. The model is built using the Random Forest Classifier algorithm. The model is trained on the training set and then used to make predictions on the testing set.

## Model Evaluation
The model is evaluated using various evaluation metrics. The evaluation metrics used in this project are accuracy score, confusion matrix, classification report, and ROC-AUC score.

## Model Deployment
The model is deployed as a web application using Flask. The web application consists of an input form where the user can enter the values of the features and get the predicted quality of the wine.

## Workflows
The following are the workflows of the project:
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in source/config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py