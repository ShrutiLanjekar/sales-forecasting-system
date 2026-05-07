import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Sales Forecast Dashboard",
    layout="wide"
)

# ---------------- TITLE & API STATUS ----------------

col1, col2 = st.columns([3,1])

with col1:

    st.title("📈 Sales Forecasting Dashboard")
    st.markdown(
    "Forecast next 8 weeks of sales using Machine Learning"
    )

with col2:

    try:

        api_response = requests.get(
            "http://127.0.0.1:8000/"
        )

        if api_response.status_code == 200:

            st.success("API Running")

        else:

            st.error("API Offline")

    except:

        st.error("Connection Failed")

# ---------------- SIDEBAR ----------------

st.sidebar.header("Model Information")

st.sidebar.success("Best Model: XGBoost")

st.sidebar.info("Forecast Horizon: 56 Days")

# ---------------- STATE SELECTION ----------------

df = pd.read_csv(
    "data/processed/final_processed.csv"
)

states = sorted(
    df['State'].unique().tolist()
)

selected_state = st.selectbox(
    "Select State",
    states
)

# ---------------- BUTTON ----------------

if st.button("Generate Forecast"):

    try:

        response = requests.post(
            "http://127.0.0.1:8000/forecast",
            params={
                "state": selected_state
            }
        )

        data = response.json()

        forecast_df = pd.DataFrame(
            data['forecast']
        )

        # ---------------- METRICS ----------------

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Average Forecast",
            f"{forecast_df['sales'].mean():,.0f}"
        )

        col2.metric(
            "Maximum Forecast",
            f"{forecast_df['sales'].max():,.0f}"
        )

        col3.metric(
            "Minimum Forecast",
            f"{forecast_df['sales'].min():,.0f}"
        )

        # ---------------- TABLE ----------------

        st.subheader("Forecast Data")

        st.dataframe(
            forecast_df,
            use_container_width=True
        )

        # ---------------- CHART ----------------

        st.subheader("Forecast Trend")

        fig = px.line(
            forecast_df,
            x='date',
            y='sales',
            title=f"{selected_state} Sales Forecast",
            markers=True
        )

        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Forecasted Sales",
            template="plotly_dark"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    except Exception as e:

        st.error(f"API Error: {e}")