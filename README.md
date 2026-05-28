# 🛫 Airlines Project

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

Plateforme d'analyse et de prédiction pour les compagnies aériennes utilisant le Machine Learning et le NLP.

## 📖 Description

Ce projet fournit une suite complète d'outils pour :
- 📊 Analyse de données de vols aériens
- 🤖 Prédiction de retard et satisfaction client avec Machine Learning
- 💬 Chatbot intelligent pour le support client avec NLP
- 📈 Dashboards interactifs avec Power BI

## 🚀 Fonctionnalités

### Machine Learning
- Classification des retards de vols
- Prédiction de la satisfaction client
- Modèles Deep Learning (CNN, LSTM)

### NLP & Chatbot
- Analyse de sentiments des avis clients
- Chatbot avec embeddings sémantiques
- Support multi-langues

### Visualisation
- Dashboard Power BI interactif
- Graphiques personnalisés
- Rapports automatisés

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

## 🔧 Configuration

### Variables d'environnement (.env)
```bash
SQL_SERVER=YOUR_SERVER_IP
SQL_PORT=1433
SQL_USER=YOUR_SQL_USER
SQL_PASSWORD=YOUR_SQL_PASSWORD
```

### Configuration YAML
```yaml
sql:
  server: "YOUR_SERVER_IP"
  databases:
    dwh: "airlines_dwh"
    stg: "airlines_stg"
```

## 📂 Structure du projet

```
airlines/
├── app/              # Application principale
├── config/           # Fichiers de configuration
├── data/             # Données brutes et traitées
├── models/           # Modèles entraînés
├── notebooks/        # Jupyter notebooks
├── src/              # Code source
├── sql/              # Scripts SQL
├── reports/          # Rapports générés
└── docs/             # Documentation
```

## 🎯 Utilisation

### Lancer le dashboard
```bash
streamlit run app/main.py
```

### Entraîner les modèles
```bash
python src/train_models.py
```

### Lancer le chatbot
```bash
python src/chatbot.py
```

## 🤝 Contribution

Les contributions sont les bienvenues ! Veuillez suivre ces étapes :

1. Forker le repository
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Committer (`git commit -m 'Add AmazingFeature'`)
4. Pousser (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

**Note :** Ce projet utilise la protection de branche. Les contributions sont évaluées avant d'être fusionnées.

## 📝 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## ☕ Soutenir le projet

<a href="https://github.com/sponsors/khadijaRachdKotbi"><img src="https://img.shields.io/github/sponsors/khadijaRachdKotbi?style=social&logo=github&logoColor=ea4aaa" alt="GitHub Sponsors"></a>
<a href="https://www.buymeacoffee.com/khadijaRachdKotbi"><img src="https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me A Coffee"></a>
<a href="https://paypal.me/khadijaRachdKotbi"><img src="https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white" alt="PayPal"></a>

## 📧 Contact

- **GitHub:** [khadijaRachdKotbi](https://github.com/khadijaRachdKotbi)
- **Issues:** [airlines/issues](https://github.com/khadijaRachdKotbi/airlines/issues)
- **Discussions:** [airlines/discussions](https://github.com/khadijaRachdKotbi/airlines/discussions)

---

Développé avec ❤️ par [Khadija Rachd Kotbi](https://github.com/khadijaRachdKotbi)