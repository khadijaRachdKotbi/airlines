import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Configuration de la page
st.set_page_config(
    page_title="Airlines Satisfaction Dashboard",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configuration des couleurs
COLORS = {
    'positive': '#2ecc71',
    'negative': '#e74c3c',
    'primary': '#3498db',
    'secondary': '#9b59b6'
}

# Chemins
PROJECT_ROOT = Path("/home/esprit/airlLines_Project")
CSV_DIR = PROJECT_ROOT / "dataSetAirlines"

# Chargement des données
@st.cache_data
def load_data():
    df_satisfaction = pd.read_csv(CSV_DIR / "airline_passenger_satisfaction.csv")
    df_reviews = pd.read_csv(CSV_DIR / "airlines_reviews.csv")
    df_satisfaction['satisfaction_binary'] = (df_satisfaction['Satisfaction'] == 'satisfied').astype(int)
    df_reviews['sentiment'] = (df_reviews['Overall Rating'] >= 7).astype(int)
    return df_satisfaction, df_reviews

df_satisfaction, df_reviews = load_data()

# Sidebar
st.sidebar.image("https://img.icons8.com/fluency/96/airplane-take-off.png", width=80)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choisissez une section :", [
    "📊 Vue d'ensemble",
    "🤖 Classification ML",
    "📝 Analyse NLP"
])

st.title("✈️ Airlines Customer Satisfaction Dashboard")
st.markdown("---")

# Page 1: Vue d'ensemble
if page == "📊 Vue d'ensemble":
    st.header("📊 Vue d'ensemble des données")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total passagers", f"{df_satisfaction.shape[0]:,}")
    with col2:
        satisfaction_rate = df_satisfaction['satisfaction_binary'].mean() * 100
        st.metric("Taux de satisfaction", f"{satisfaction_rate:.1f}%")
    with col3:
        st.metric("Total avis", f"{df_reviews.shape[0]:,}")
    with col4:
        avg_rating = df_reviews['Overall Rating'].mean()
        st.metric("Note moyenne", f"{avg_rating:.1f}⭐")
    
    # Graphique satisfaction
    fig, ax = plt.subplots(figsize=(8, 6))
    df_satisfaction['Satisfaction'].value_counts().plot(kind='bar', color=[COLORS['negative'], COLORS['positive']], ax=ax)
    ax.set_xlabel("Satisfaction")
    ax.set_ylabel("Nombre de passagers")
    st.pyplot(fig)

# Page 2: Classification ML
elif page == "🤖 Classification ML":
    st.header("🤖 Classification ML - XGBoost")
    st.markdown("""
    | Métrique | Score |
    |----------|-------|
    | Accuracy | **96.50%** |
    | Precision | **97.36%** |
    | Recall | **94.50%** |
    | F1-Score | **95.91%** |
    """)

# Page 3: Analyse NLP
elif page == "📝 Analyse NLP":
    st.header("📝 Analyse NLP des avis clients")
    st.image(str(PROJECT_ROOT / "results_nlp" / "wordcloud_positive.png"), caption="Mots clés - Avis POSITIFS")
    st.image(str(PROJECT_ROOT / "results_nlp" / "wordcloud_negative.png"), caption="Mots clés - Avis NÉGATIFS")

st.markdown("---")
st.caption("© 2024 Airlines Satisfaction Analysis")
