Live Application: [akash-student-dropout.streamlit.app]
Project Overview
This project is an end-to-end Machine Learning web application designed to predict the likelihood of university student attrition. By analyzing historical academic performance, demographic data, and financial indicators, the system provides early-warning alerts to academic counselors, enabling data-driven and timely intervention strategies.
System Architecture
The application follows a standard predictive modeling pipeline:
Data Ingestion & Preprocessing: Cleaning and structuring raw tabular data using Pandas.
Feature Selection: Dimensionality reduction to isolate the 6 most highly correlated predictors of student dropout to streamline user input.
Predictive Modeling: Utilizing a Random Forest Classifier to identify complex, non-linear patterns within the student profile data.
Interactive Dashboard: A reactive frontend built with Streamlit that takes real-time user inputs, passes them through the serialized model (.pkl), and outputs a probabilistic risk assessment.
Technology Stack
Language: Python 3
Data Manipulation: Pandas
Machine Learning: Scikit-Learn (Random Forest)
Model Serialization: Joblib
Web Framework & Deployment: Streamlit, Streamlit Community Cloud
Key Features
Real-Time Inference: Instantaneous calculation of dropout probability based on dynamically adjusted parameters.
Optimized Input Metrics: The model evaluates students based on core metrics, including:
Tuition fee status
Active scholarship status
Age at enrollment
1st and 2nd-semester approved units
2nd-semester grade averages
Actionable Output: Classifies students into "High Risk" or "On Track" categories, paired with confidence percentages to guide administrative action.
Dataset
The model was trained on the "Predict Students' Dropout and Academic Success" dataset (originally sourced from the UCI Machine Learning Repository), containing comprehensive academic and demographic records for over 4,400 higher education students.
