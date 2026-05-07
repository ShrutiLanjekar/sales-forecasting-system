# End-to-End Time Series Forecasting System with API

## Project Overview

This project is a production-ready sales forecasting system developed for forecasting the next 8 weeks of sales for multiple states using historical sales data.

The system trains and compares multiple forecasting models, automatically selects the best performing model, and exposes predictions through a FastAPI REST API with a Streamlit dashboard frontend.

---

# Objective

The objective of this project is to:

- Forecast next 8 weeks of sales
- Handle missing dates and missing values
- Capture seasonality and trends
- Compare multiple forecasting models
- Automatically select the best model
- Serve predictions via REST API
- Create a production-style forecasting pipeline

---

# Models Implemented

The following forecasting models were implemented and compared:

1. SARIMA
2. Facebook Prophet
3. XGBoost Regressor
4. LSTM Deep Learning Model

---

# Feature Engineering

The following features were created for machine learning forecasting:

## Lag Features
- lag_1
- lag_7
- lag_30

## Rolling Features
- rolling_mean_7
- rolling_mean_30
- rolling_std_7

## Date Features
- day_of_week
- month
- quarter
- week_of_year
- year

## Holiday Features
- US holiday flag

---

# Project Workflow

1. Data Cleaning & Preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Time Series Train-Validation Split
5. Model Training
6. Model Evaluation
7. Model Comparison
8. Best Model Selection
9. Final Forecast Generation
10. API Deployment using FastAPI
11. Dashboard Development using Streamlit

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- Scikit-learn
- XGBoost
- TensorFlow / Keras
- Prophet
- Statsmodels
- FastAPI
- Streamlit

---

# Project Structure

```bash
forecasting_system/
│
├── api/
│   └── app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│
├── notebooks/
│
├── outputs/
│
├── dashboard.py
│
├── requirements.txt
│
└── README.md