# /home/esprit/airlLines_Project/app/pages/1_📊_Data_Overview.py
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Data Overview", layout="wide")
st.title("📊 Data Overview")

PROJECT_ROOT = Path("/home/esprit/airlLines_Project")
CSV_DIR = PROJECT_ROOT / "dataSetAirlines"

df_satisfaction = pd.read_csv(CSV_DIR / "airline_passenger_satisfaction.csv")
df_reviews = pd.read_csv(CSV_DIR / "airlines_reviews.csv")

st.subheader("Aperçu des données")
col1, col2 = st.columns(2)

with col1:
    st.write("**Données satisfaction passagers**")
    st.dataframe(df_satisfaction.head())
    st.caption(f"Shape: {df_satisfaction.shape}")

with col2:
    st.write("**Données avis clients**")
    st.dataframe(df_reviews.head())
    st.caption(f"Shape: {df_reviews.shape}")
