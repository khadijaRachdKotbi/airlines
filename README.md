# 🛫 Airlines

**Customer Satisfaction Analysis Module – Part of Airlines Project**

> ML / NLP / Deep Learning analysis of customer satisfaction and its impact on airline revenue.

---

## 🎯 Objective

Understand the **satisfaction → loyalty → revenue** relationship using:

- **ML** : XGBoost, Random Forest
- **NLP** : TF‑IDF, sentiment analysis, word clouds
- **DL** : Fine‑tuned DistilBERT (Transformers)
- **Chatbot** : FAQ with semantic embeddings

---

## 👥 Team & Contributions

| Contribution | Owner |
|--------------|-------|
| **Satisfaction module (ML/NLP/DL/Chatbot)** | Khadija RACHDI + Mohamed Amine Chouria|
| Data Warehouse & ETL (SSIS) | Project team |
| Staging (Visual Studio) | Project team |
| Power BI dashboard | Project team |

---

## 🚀 Quick Start

```bash
streamlit run app/app.py
jupyter notebook notebooks/00_setup.ipynb
📦 Installation
bash
git clone https://github.com/khadijaRachdKotbi/airlines.git
cd airlines
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp config/.env.example config/.env
✨ Key Features
Category	Models / Tools
ML	XGBoost, Random Forest
NLP	TF‑IDF, Logistic Regression
Deep Learning	DistilBERT (fine‑tuned)
Chatbot	all‑MiniLM‑L6‑v2 embeddings
Visualisation	Streamlit, Power BI, word clouds
📊 Power BI Dashboard
Team‑developed dashboard with:

Satisfaction KPIs & NPS

Temporal trends

Customer segmentation

Satisfaction → revenue correlation

🔧 Configuration (.env)
text
SQL_SERVER=YOUR_SERVER_IP
SQL_USER=YOUR_SQL_USER
SQL_PASSWORD=YOUR_SQL_PASSWORD
SQL_DATABASE_DWH=airlines_dwh
📞 Contact & Support
Email : khadija_rachdi@yahoo.fr

Issues : GitHub Issues

📄 License
MIT – see LICENSE

🙏 Acknowledgments
See ACKNOWLEDGMENTS.md

💖 Support this project
See SPONSOR.md

Built with ❤️ using Streamlit, Scikit‑learn, Transformers & Plotly