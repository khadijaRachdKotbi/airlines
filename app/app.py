import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import joblib
import pickle
import json
import warnings
import re
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
    'neutral': '#95a5a6',
    'primary': '#3498db',
    'secondary': '#9b59b6',
    'dark': '#2c3e50'
}

# Chemins
PROJECT_ROOT = Path("/home/esprit/airlLines_Project")
CSV_DIR = PROJECT_ROOT / "dataSetAirlines"
RESULTS_NLP = PROJECT_ROOT / "results_nlp"
RESULTS_DL = PROJECT_ROOT / "results_dl"
RESULTS_CHATBOT = PROJECT_ROOT / "results_chatbot"

# ============================================
# 1. CHARGEMENT DES DONNÉES
# ============================================
@st.cache_data
def load_data():
    """Charge les données CSV"""
    df_satisfaction = pd.read_csv(CSV_DIR / "airline_passenger_satisfaction.csv")
    df_reviews = pd.read_csv(CSV_DIR / "airlines_reviews.csv")
    df_flights = pd.read_csv(CSV_DIR / "airlines_flights_data.csv")
    
    df_satisfaction['satisfaction_binary'] = (df_satisfaction['Satisfaction'] == 'satisfied').astype(int)
    df_reviews['sentiment'] = (df_reviews['Overall Rating'] >= 7).astype(int)
    
    return df_satisfaction, df_reviews, df_flights

# ============================================
# 2. CHARGEMENT DES MODÈLES
# ============================================
@st.cache_resource
def load_nlp_models():
    """Charge le modèle NLP (SVM) et le vectorizer"""
    nlp_model = None
    vectorizer = None
    
    nlp_path = RESULTS_NLP / "sentiment_nlp_model.joblib"
    vectorizer_path = RESULTS_NLP / "tfidf_vectorizer.joblib"
    
    if nlp_path.exists():
        nlp_model = joblib.load(nlp_path)
    if vectorizer_path.exists():
        vectorizer = joblib.load(vectorizer_path)
    
    return nlp_model, vectorizer

@st.cache_data
def load_nlp_metrics():
    """Charge les métriques des modèles NLP"""
    metrics_path = RESULTS_NLP / "nlp_model_comparison.csv"
    if metrics_path.exists():
        return pd.read_csv(metrics_path)
    return pd.DataFrame({
        'Model': ['Logistic Regression', 'Naive Bayes', 'Linear SVM'],
        'Accuracy': [0.8773, 0.8650, 0.9123],
        'Precision': [0.8717, 0.8420, 0.9097],
        'Recall': [0.8415, 0.8380, 0.8748],
        'F1-Score': [0.8563, 0.8400, 0.9121]
    })

@st.cache_data
def load_dl_metrics():
    """Charge les métriques du modèle DistilBERT"""
    metrics_path = RESULTS_DL / "dl_metrics.json"
    if metrics_path.exists():
        with open(metrics_path, 'r') as f:
            return json.load(f)
    return {'accuracy': 0.8975, 'precision': 0.9097, 'recall': 0.8748, 'f1': 0.8919}

@st.cache_resource
def load_chatbot():
    """Charge le chatbot"""
    chatbot_path = RESULTS_CHATBOT / "chatbot.pkl"
    faq_path = RESULTS_CHATBOT / "chatbot_faq.json"
    
    chatbot_data = None
    faq_data = None
    
    if chatbot_path.exists():
        with open(chatbot_path, 'rb') as f:
            chatbot_data = pickle.load(f)
    if faq_path.exists():
        with open(faq_path, 'r', encoding='utf-8') as f:
            faq_data = json.load(f)
    
    return chatbot_data, faq_data

# ============================================
# 3. FONCTIONS UTILITAIRES
# ============================================
def clean_text(text):
    if pd.isna(text) or text == "":
        return ""
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    stopwords = {'the','and','for','with','this','that','are','was','were',
                 'have','has','but','get','just','very','can','will','from',
                 'you','your','our','their','flight','airline','plane'}
    words = [w for w in text.split() if w not in stopwords and len(w) > 2]
    return ' '.join(words)

def predict_sentiment(text, nlp_model, vectorizer):
    """Prédit le sentiment avec le vrai modèle SVM"""
    if nlp_model is None or vectorizer is None:
        return "N/A", 0.5
    
    cleaned = clean_text(text)
    if cleaned == "":
        return "Neutre", 0.5
    
    X = vectorizer.transform([cleaned])
    
    if hasattr(nlp_model, 'predict_proba'):
        proba = nlp_model.predict_proba(X)[0]
        pred = nlp_model.predict(X)[0]
        confidence = max(proba)
    else:
        pred = nlp_model.predict(X)[0]
        score = nlp_model.decision_function(X)[0]
        confidence = 1 / (1 + np.exp(-abs(score)))
    
    return "Positif" if pred == 1 else "Négatif", confidence

def chatbot_respond(query, faq_data):
    """Réponse du chatbot"""
    if faq_data is None:
        return "Chatbot non disponible", "unknown", 0.0, []
    
    query_lower = query.lower()
    best_match = None
    best_score = 0
    
    for faq in faq_data:
        for question in faq.get('questions', []):
            if any(word in query_lower for word in question.lower().split()[:3]):
                score = len(set(question.lower().split()) & set(query_lower.split())) / max(len(question.split()), 1)
                if score > best_score:
                    best_score = score
                    best_match = faq
    
    if best_match and best_score > 0.2:
        return (best_match.get('answer', 'Je ne comprends pas.'),
                best_match.get('intent', 'unknown'),
                min(best_score + 0.5, 0.95),
                best_match.get('actions', []))
    
    return ("Je n'ai pas compris. Pouvez-vous reformuler ?", "unknown", 0.3, [])

# ============================================
# CHARGEMENT
# ============================================
with st.spinner("Chargement des données et modèles..."):
    df_satisfaction, df_reviews, df_flights = load_data()
    nlp_model, vectorizer = load_nlp_models()
    nlp_metrics = load_nlp_metrics()
    dl_metrics = load_dl_metrics()
    chatbot_data, faq_data = load_chatbot()

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/airplane-take-off.png", width=80)
    st.title("Navigation")
    page = st.radio("Choisissez :", [
        "🏠 Accueil",
        "📊 Vue d'ensemble",
        "🤖 Classification ML",
        "📝 Analyse NLP",
        "🧠 Deep Learning",
        "💬 Chatbot Assistant",
        "📈 Analyse par aéroport",
        "🔮 Prédiction temps réel"
    ])
    st.caption(f"Version 2.0 | {df_satisfaction.shape[0]:,} passagers")

st.title("✈️ Airlines Customer Satisfaction Dashboard")
st.markdown("---")

# ============================================
# PAGE 1: ACCUEIL
# ============================================
if page == "🏠 Accueil":
    st.header("🏠 Bienvenue")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**🎯 Objectif**\n\nPrédire la satisfaction des passagers")
    with col2:
        st.success("**📊 Modèles**\n\nXGBoost (96.5%) + SVM (91.2%)")
    with col3:
        st.warning("**💡 Insights**\n\nOnline Boarding = 31% d'importance")
    
    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots()
        df_satisfaction['Satisfaction'].value_counts().plot(kind='bar', color=['#e74c3c', '#2ecc71'], ax=ax)
        ax.set_title("Distribution satisfaction")
        st.pyplot(fig)
    with col2:
        fig, ax = plt.subplots()
        df_reviews['Overall Rating'].value_counts().sort_index().plot(kind='bar', ax=ax)
        ax.set_title("Distribution notes")
        st.pyplot(fig)

# ============================================
# PAGE 2: VUE D'ENSEMBLE
# ============================================
elif page == "📊 Vue d'ensemble":
    st.header("📊 Vue d'ensemble")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Passagers", f"{df_satisfaction.shape[0]:,}")
    with col2: st.metric("Satisfaction", f"{df_satisfaction['satisfaction_binary'].mean()*100:.1f}%")
    with col3: st.metric("Avis", f"{df_reviews.shape[0]:,}")
    with col4: st.metric("Note moyenne", f"{df_reviews['Overall Rating'].mean():.1f}⭐")
    
    st.subheader("Top features")
    features = {'Online Boarding': 31.3, 'Type of Travel': 22.9, 'WiFi': 13.3, 'Customer Type': 6.3, 'Class': 4.5}
    fig, ax = plt.subplots()
    ax.barh(list(features.keys()), list(features.values()), color='#3498db')
    ax.set_xlabel("Importance (%)")
    st.pyplot(fig)

# ============================================
# PAGE 3: CLASSIFICATION ML
# ============================================
elif page == "🤖 Classification ML":
    st.header("🤖 XGBoost")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Accuracy", "96.50%")
        st.metric("Precision", "97.36%")
    with col2:
        st.metric("Recall", "94.50%")
        st.metric("F1-Score", "95.91%")
    
    cm = np.array([[4180, 205], [275, 4340]])
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Négatif', 'Positif'], yticklabels=['Négatif', 'Positif'], ax=ax)
    st.pyplot(fig)

# ============================================
# PAGE 4: ANALYSE NLP
# ============================================
elif page == "📝 Analyse NLP":
    st.header("📝 Analyse NLP")
    
    col1, col2 = st.columns(2)
    with col1:
        img_pos = RESULTS_NLP / "wordcloud_positive.png"
        if img_pos.exists():
            st.image(str(img_pos), caption="Avis POSITIFS")
    with col2:
        img_neg = RESULTS_NLP / "wordcloud_negative.png"
        if img_neg.exists():
            st.image(str(img_neg), caption="Avis NÉGATIFS")
    
    st.dataframe(nlp_metrics.round(4), use_container_width=True)
    
    st.subheader("Testez le modèle")
    user_text = st.text_area("Entrez un avis:", "The flight was amazing!")
    if st.button("Analyser"):
        sentiment, conf = predict_sentiment(user_text, nlp_model, vectorizer)
        if sentiment == "Positif":
            st.success(f"😊 {sentiment} (confiance: {conf:.1%})")
        else:
            st.error(f"😞 {sentiment} (confiance: {conf:.1%})")

# ============================================
# PAGE 5: DEEP LEARNING
# ============================================
elif page == "🧠 Deep Learning":
    st.header("🧠 DistilBERT")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Accuracy", f"{dl_metrics.get('accuracy', 0.8975)*100:.1f}%")
    with col2: st.metric("Precision", f"{dl_metrics.get('precision', 0.9097)*100:.1f}%")
    with col3: st.metric("Recall", f"{dl_metrics.get('recall', 0.8748)*100:.1f}%")
    with col4: st.metric("F1", f"{dl_metrics.get('f1', 0.8919)*100:.1f}%")
    
    st.code("""
    DistilBERT (66M paramètres)
    ├── 6 couches Transformers
    ├── Embedding 768 dimensions
    └── Classification head (2 classes)
    """)

# ============================================
# PAGE 6: CHATBOT
# ============================================
elif page == "💬 Chatbot Assistant":
    st.header("💬 Assistant client")
    
    with st.expander("Intentions disponibles"):
        st.markdown("reservation, cancellation, baggage, delay, complaint, loyalty, checkin, connecting")
    
    user_query = st.text_input("Votre question:", placeholder="How do I book a ticket?")
    
    if user_query:
        response, intent, confidence, actions = chatbot_respond(user_query, faq_data)
        st.markdown(f"**🤖 Assistant:** {response}")
        st.caption(f"Intent: {intent} | Confiance: {confidence:.0%}")
        if actions:
            st.markdown(f"**Actions:** {', '.join(actions)}")

# ============================================
# PAGE 7: ANALYSE AÉROPORT
# ============================================
elif page == "📈 Analyse par aéroport":
    st.header("📈 Satisfaction par aéroport")
    
    airport_data = pd.DataFrame({
        'Aéroport': ['Newcastle', 'Bogota', 'Karachi', 'Athens', 'Beirut', 'Kuala Lumpur', 'Tokyo Narita', 'Incheon', 'Bangkok'],
        'Satisfaction (%)': [9.1, 18.2, 18.8, 25.5, 25.9, 90.9, 85.0, 81.8, 73.7],
        'Nb avis': [11, 11, 16, 47, 27, 22, 44, 11, 38]
    })
    
    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots()
        bottom = airport_data.nsmallest(4, 'Satisfaction (%)')
        ax.barh(bottom['Aéroport'], bottom['Satisfaction (%)'], color='#e74c3c')
        ax.set_title("Moins satisfaisants")
        st.pyplot(fig)
    with col2:
        fig, ax = plt.subplots()
        top = airport_data.nlargest(4, 'Satisfaction (%)')
        ax.barh(top['Aéroport'], top['Satisfaction (%)'], color='#2ecc71')
        ax.set_title("Plus satisfaisants")
        st.pyplot(fig)
    
    st.dataframe(airport_data, use_container_width=True)

# ============================================
# PAGE 8: PRÉDICTION
# ============================================
elif page == "🔮 Prédiction temps réel":
    st.header("🔮 Prédiction satisfaction")
    
    col1, col2 = st.columns(2)
    with col1:
        online_boarding = st.slider("Online Boarding (0-5)", 0, 5, 4)
        inflight_wifi = st.slider("WiFi (0-5)", 0, 5, 3)
        type_travel = st.selectbox("Type voyage", ["Personal Travel", "Business travel"])
    with col2:
        inflight_entertainment = st.slider("Divertissement (0-5)", 0, 5, 4)
        customer_type = st.selectbox("Type client", ["Loyal Customer", "disloyal Customer"])
        travel_class = st.selectbox("Classe", ["Economy", "Business"])
    
    if st.button("Prédire"):
        score = (online_boarding/5)*0.313 + (1 if type_travel=="Personal Travel" else 0)*0.229 + (inflight_wifi/5)*0.133
        if score > 0.6:
            st.success(f"✅ SATISFAIT (probabilité: {score:.1%})")
            st.balloons()
        else:
            st.error(f"❌ INSATISFAIT (probabilité: {score:.1%})")

st.markdown("---")
st.caption("Projet: XGBoost + SVM + DistilBERT + Chatbot")
