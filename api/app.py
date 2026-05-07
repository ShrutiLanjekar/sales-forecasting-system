from fastapi import FastAPI

import pandas as pd

import joblib

from datetime import datetime

app = FastAPI()

model = joblib.load(
    "../models/final_forecasting_model.pkl"
)

features = [
    'lag_1',
    'lag_7',
    'lag_30',
    'rolling_mean_7',
    'rolling_mean_30',
    'rolling_std_7',
    'day_of_week',
    'month',
    'quarter',
    'week_of_year',
    'year',
    'is_holiday'
]

@app.get("/")
def home():
    
    return {
        "message": "Forecast API Running"
    }

@app.get("/model-info")
def model_info():
    
    return {
        "model": "XGBoost"
    }

@app.post("/forecast")
def forecast(state: str):

    future_dates = pd.date_range(
        start=datetime.today(),
        periods=56
    )

    future_df = pd.DataFrame({
        'Date': future_dates
    })

    future_df['day_of_week'] = (
        future_df['Date'].dt.dayofweek
    )

    future_df['month'] = (
        future_df['Date'].dt.month
    )

    future_df['quarter'] = (
        future_df['Date'].dt.quarter
    )

    future_df['week_of_year'] = (
        future_df['Date']
        .dt.isocalendar()
        .week
        .astype(int)
    )

    future_df['year'] = (
        future_df['Date'].dt.year
    )

    future_df['lag_1'] = 100

    future_df['lag_7'] = 100

    future_df['lag_30'] = 100

    future_df['rolling_mean_7'] = 100

    future_df['rolling_mean_30'] = 100

    future_df['rolling_std_7'] = 10

    future_df['is_holiday'] = 0

    predictions = model.predict(
        future_df[features]
    )

    forecast_results = []

    for date, pred in zip(
      future_df['Date'],
      predictions):

       forecast_results.append({
         "date": str(date.date()),
         "sales": float(pred)
       })

    return {
     "state": state.title(),
     "forecast": forecast_results
    }