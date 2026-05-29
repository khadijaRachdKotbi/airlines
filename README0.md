# 🛫 Airlines

**Customer Satisfaction Analysis Module - Part of Airlines Project**

> Comprehensive analysis of customer satisfaction and its impact on airline revenue

---

## 🎯 About This Module

This module focuses on **Customer Satisfaction Analysis** within the broader Airlines Project. It examines:

### 📊 Satisfaction Dimensions Analyzed
- **Flight Experience** : Punctuality, comfort, service quality
- **In-flight Services** : Food, entertainment, cabin crew
- **Booking Process** : Ease, price transparency, options
- **Post-flight Experience** : Baggage handling, customer support
- **Loyalty Programs** : Rewards, benefits, personalization

### 👥 Stakeholder Impact Analysis
This module analyzes how each stakeholder influences satisfaction:
- **Cabin Crew** : Direct customer interaction impact
- **Ground Staff** : Check-in, boarding, baggage efficiency
- **Management** : Policy decisions affecting experience
- **Maintenance Teams** : Aircraft condition and reliability
- **IT Systems** : Booking apps, communication channels

### 🏢 Project Context
Ce module a été développé dans le cadre d'une **Mission d'entreprise** au sein d'une équipe projet complète.

### 👥 Team Members
- **Khadija RACHDI** <Khadija.Rachdi@esprit.tn>
- **Mohamed Amine CHOURIA** <MohamedAmine.Chouria@esprit.tn>
- **Baha BEL HAJ ALI** <Baha.BelHajAli@esprit.tn>
- **Olfa HABCHI** <Olfa.Habchi@esprit.tn>
- **Zina JELLABI** <zina.jellabi@esprit.tn>
- **Yasmine CHAOUACHI** <Yasmine.Chaouachi@esprit.tn>

### 🎯 Contributions
- **Data Warehouse & ETL** : Développé par l'équipe avec SSIS
- **Staging** : Effectué avec Visual Studio (SSIS)
- **Power BI Dashboard** : Développé par l'équipe
- **Customer Satisfaction Analysis Module** : ML/NLP - Khadija RACHDI

### 💰 Revenue Impact
Understanding the **satisfaction-revenue relationship**:
```
Higher Customer Satisfaction → Repeat Business → Increased Revenue
     ↓
Positive Reviews & Word-of-Mouth → New Customers → Growth
     ↓
Brand Loyalty → Premium Pricing Power → Profitability
```

### 📊 Power BI Dashboard - Customer Satisfaction
Module inclus avec tableau de bord interactif :
- **Indicateurs clés** : Taux de satisfaction, NPS, scores par segment
- **Analyse temporelle** : Évolution de la satisfaction
- **Segmentation client** : Analyse par type de client, route, classe
- **Corrélation revenus** : Visualisation impact satisfaction → revenus
- **Alertes et KPIs** : Suivi en temps réel des métriques critiques

---

## 🚀 Quick Start

```bash
# Lancer l'application principale
streamlit run app/app.py

# Lancer un notebook spécifique
jupyter notebook notebooks/00_setup.ipynb
```

## 📋 Project Structure

```
airlines/
├── 🚀 app/                         # Application Streamlit principale
│   ├── app.py                      # Point d'entrée principal
│   └── pages/                      # Pages multi-pages
├── 📊 notebooks/                   # Jupyter notebooks d'analyse
│   ├── 00_setup.ipynb              # Configuration environnement
│   ├── 01_exploration_sql.ipynb    # Exploration données SQL
│   ├── 02_exploration_csv.ipynb    # Exploration fichiers CSV
│   ├── 03_ml_classification.ipynb   # Classification ML
│   ├── 04_nlp_sentiment.ipynb      # Analyse NLP sentiments
│   ├── 05_dl_distilbert.ipynb      # Deep Learning DistilBERT
│   └── 06_chatbot_assistant.ipynb  # Chatbot assistant
├── 📄 sql/                         # Scripts SQL
│   ├── 00_overview_tables.sql     # Vue d'ensemble tables
│   ├── 01_extraction_dwh.sql       # Extraction Data Warehouse
│   ├── 02_extraction_stg.sql       # Extraction Staging
│   ├── 03_analysis_satisfaction.sql # Analyse satisfaction
│   └── 04_scores_analysis.sql      # Analyse scores
├── 📊 dataSetAirlines/             # Jeux de données airlines
├── 📈 results/                     # Résultats ML
├── 🗣️ results_nlp/                # Résultats NLP
├── 🧠 results_dl/                  # Résultats Deep Learning
├── 💬 results_chatbot/             # Modèles chatbot
├── 📋 requirements.txt             # Dépendances Python
└── ⚙️ config/                      # Configuration
    ├── .env.example                # Exemple variables environnement
    └── config.yaml.example         # Exemple configuration YAML
```

## ✨ Features

### Machine Learning
- **Classification des retards de vols** : Prédiction des retards
- **Satisfaction client** : Analyse des facteurs de satisfaction
- **XGBoost** : Modèle gradient boosting optimisé

### NLP & Sentiment Analysis
- **TF-IDF Vectorization** : Représentation textuelle
- **Logistic Regression** : Classification de sentiments
- **Word Cloud Visualization** : Nuages de mots positifs/négatifs

### Deep Learning
- **DistilBERT (Transformer)** : Fine-tuning pour analyse de sentiments
  - Modèle Transformer léger (40% plus petit que BERT)
  - Transfer learning depuis HuggingFace
  - Architecture encoder-only optimisée
- **Transfer Learning** : Utilisation de modèles pré-entraînés
- **Performance Metrics** : Comparaison ML vs DL

### Chatbot Intelligent
- **Semantic Embeddings** : all-MiniLM-L6-v2
- **FAQ System** : Réponses automatiques aux questions courantes
- **Context-Aware** : Compréhension contextuelle

### SQL Integration
- **SQL Server Integration** : Connexion base de données airlines
- **Data Warehouse (DWH)** : Conçu et implémenté par l'équipe avec SSIS
- **ETL Process** : Développé par l'équipe avec SSIS
- **Staging** : Effectué avec Visual Studio (SSIS)
- **Query Templates** : Scripts SQL prêts à l'emploi

### 📊 Power BI Dashboard
Dashboard interactif développé par l'équipe dans le cadre du projet Airlines :
- **Indicateurs clés** : Taux de satisfaction, NPS, scores par segment
- **Analyse temporelle** : Évolution de la satisfaction
- **Segmentation client** : Analyse par type de client, route, classe
- **Corrélation revenus** : Visualisation impact satisfaction → revenus
- **Alertes et KPIs** : Suivi en temps réel des métriques critiques

## 📊 Available Models

**Supervised Learning:**
- XGBoost pour classification satisfaction
- Logistic Regression pour sentiments
- Random Forest pour retards

**Deep Learning:**
- DistilBERT fine-tuned pour sentiment analysis
- Transfer learning depuis modèles HuggingFace

**NLP Models:**
- TF-IDF + Logistic Regression
- all-MiniLM-L6-v2 embeddings pour chatbot

---

## ☕ Soutenir le Projet

Si Airlines Project vous a été utile dans votre recherche, vos études ou vos projets, envisagez un soutien symbolique pour maintenir et améliorer cette ressource open-source.

### 🎯 Pourquoi soutenir?

- 🔧 **Maintenir le code à jour** avec les dernières bibliothèques ML/NLP
- 📚 **Améliorer la documentation** et les tutoriels
- 🚀 **Développer de nouvelles fonctionnalités** (temps réel, nouveaux modèles)
- 🎓 **Former la communauté** au ML appliqué aux compagnies aériennes
- 🌍 **Rendre l'analyse de données accessible** à tous

### 💰 Options de soutien

<a href="https://github.com/sponsors/khadijaRachdKotbi">
    <img src="https://img.shields.io/github/sponsors/khadijaRachdKotbi?style=social&logo=github&logoColor=ea4aaa" alt="GitHub Sponsors">
</a>

<a href="https://www.buymeacoffee.com/khadijaRachdKotbi">
    <img src="https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me A Coffee">
</a>

<a href="https://paypal.me/khadijaRachdKotbi">
    <img src="https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white" alt="PayPal">
</a>

### 🎁 Impact de votre soutien

| Montant | Impact Concret |
|---------|---------------|
| **1€** | ☕ Un café pour maintenir la motivation pendant les sessions de debug |
| **5€** | 📝 Une heure d'amélioration de la documentation ou d'une fonctionnalité |
| **10€** | ✨ Développement d'une nouvelle visualisation ou métrique |
| **25€** | 🚀 Amélioration significative (nouvel algorithme, temps réel, etc.) |
| **50€** | 🏆 Support de parrainage mensuel - reconnaissance spéciale |

### 🏆 Reconnaissance des Supporters

Tous les contributeurs recevront:
- 📋 **Mention** dans le README et crédits du projet
- ⭐ **Badge "Supporter"** dans les issues et discussions
- 📰 **Accès prioritaire** au support technique
- 🎉 **Invitation** aux événements et webinaires du projet
- 📊 **Rapports détaillés** sur l'impact de leur contribution

---

### 📞 Contact et Contribution

**Questions? Idées d'amélioration?**
- 📧 Contact: khadija_rachdi@yahoo.fr
- 🐛 Issues: [Signaler un problème](https://github.com/khadijaRachdKotbi/airlines/issues)
- 💡 Suggestions: [Ouvrir une discussion](https://github.com/khadijaRachdKotbi/airlines/discussions)

**Participez au projet:**
1. ⭐ **Star** ce repository si vous le trouvez utile
2. 🍴 **Fork** et proposez des améliorations
3. 📢 **Partagez** autour de vous
4. ☕ **Soutenez** le développement

---

*Chaque contribution, même symbolique, aide à rendre l'analyse de données accessible à tous. Merci pour votre soutien!* 🙏

## 📦 Installation

```bash
# Cloner le repository
git clone https://github.com/khadijaRachdKotbi/airlines.git
cd airlines

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou venv\Scripts\activate  # Windows

# Installer les dépendances
pip install -r requirements.txt

# Configurer l'environnement
cp config/.env.example config/.env
cp config/config.yaml.example config/config.yaml
# Éditer config/.env et config/config.yaml avec vos paramètres
```

### 🔑 Dépendances Clés

- **🤗 Transformers** : Modèles Transformer (DistilBERT)
- **🐑 XGBoost** : Gradient boosting pour classification
- **📊 Scikit-learn** : ML classique et métriques
- **💬 Sentence-Transformers** : Embeddings pour chatbot
- **🌐 Streamlit** : Dashboard interactif

## 🔧 Configuration

### Variables d'environnement (.env)
```bash
SQL_SERVER=YOUR_SERVER_IP
SQL_PORT=1433
SQL_USER=YOUR_SQL_USER
SQL_PASSWORD=YOUR_SQL_PASSWORD
SQL_DATABASE_DWH=airlines_dwh
SQL_DATABASE_STG=airlines_stg
```

---

## 🙏 Acknowledgments

This project was born from a deep passion for data science and machine learning, and would not have been possible without the support of many inspiring people.

### 👨‍🏫 To My Professors
A special thank you to **Mr. Taher Bellakhdhar** for giving me this incredible opportunity and for believing in my potential. Your guidance and mentorship have been invaluable throughout this journey.

To all my professors at the engineering school who ignited my love for research and data science - your dedication to education has shaped who I am today.

### 🏫 To My Engineering School
Thank you for providing an environment where curiosity meets innovation. This project is a testament to the quality education and support I received.

### 👨‍👩‍👧 To My Family
- **To my daughter**: Your smile illuminates my life and gives me the strength to pursue my dreams every single day.
- **To my husband**: Thank you for your endless patience, support, and encouragement throughout this journey.
- **To my sister**: Your belief in me means everything.
- **To my entire family**: Your love and support have been my foundation.

### 👥 To My Classmates
To all my fellow students in the engineering cycle - thank you for sharing this experience, for the late-night study sessions, the discussions, and the growth we've shared together.

### 💝 Message to All
This project is my way of giving back to the community that has given me so much. I hope that Airlines Project will help other students, researchers, and educators in their journey to understand and apply machine learning to real-world airline industry challenges.

*With gratitude and love,*
*Khadija Rachdi Kotbi*

---

## 💖 Support This Work

If this project has helped you in your studies, research, or teaching, please consider supporting its continued development:

- ⭐ **Star** the repository on GitHub
- 🍴 **Fork** it and improve it
- 💝 **Become a sponsor** (see section above)
- 📢 **Share** it with others who might benefit

Every contribution, whether technical or financial, helps make data science education accessible to all!

---

*Built with ❤️ using Streamlit, Scikit-learn, Transformers & Plotly*
*Created with passion for the data science and airline community*
*Developed as part of an Airlines Corporate Mission Project*