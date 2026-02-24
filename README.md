Student Dropout Predictor

An end-to-end machine learning web application designed to predict the likelihood of university student attrition. The system analyzes academic performance, demographic attributes, and financial indicators to generate early risk assessments that can support institutional decision-making and timely intervention.

Live Application:
https://akash-student-dropout.streamlit.app

Project Overview

Student dropout is a significant challenge in higher education institutions. Early identification of at-risk students enables academic counselors and administrators to take preventive action.

This project implements a complete machine learning pipeline — from data preprocessing and feature selection to model deployment — and delivers real-time predictions through a web-based interface.

System Architecture

The application follows a structured predictive modeling workflow:

Data Preprocessing

Cleaned and structured raw tabular data using Pandas

Handled missing values and categorical encoding

Prepared data for model training

Feature Selection

Performed correlation analysis

Selected six highly relevant predictors

Reduced input complexity while maintaining model performance

Model Development

Implemented a Random Forest Classifier using Scikit-learn

Captured non-linear relationships within student performance data

Trained and validated on real-world educational records

Model Serialization

Saved the trained model using Joblib (.pkl format)

Enabled efficient inference during deployment

Deployment

Developed an interactive frontend using Streamlit

Integrated real-time inference with the serialized model

Deployed via Streamlit Community Cloud

Key Features

Real-time dropout probability prediction

Binary classification: High Risk or On Track

Probability-based confidence scores

Focused input metrics for streamlined user interaction

Web-based interface for accessibility

Input Features

The model evaluates students using the following core indicators:

Tuition fee status

Scholarship status

Age at enrollment

First semester approved units

Second semester approved units

Second semester grade average

Dataset

The model was trained on the "Predict Students' Dropout and Academic Success" dataset sourced from the UCI Machine Learning Repository.

Over 4,400 student records

Includes academic, demographic, and financial attributes

Real-world higher education data

Technology Stack

Python 3

Pandas (data preprocessing)

Scikit-learn (machine learning)

Joblib (model serialization)

Streamlit (frontend and deployment)

Project Structure
student-dropout-predictor/
│
├── train_model.py
├── dropout_model_lite.pkl
├── requirements.txt
└── README.md
Future Enhancements

Implementation of additional models (e.g., gradient boosting methods)

Hyperparameter optimization and cross-validation

Model interpretability using SHAP or feature importance visualization

API-based deployment using FastAPI

Database integration for institutional scalability
