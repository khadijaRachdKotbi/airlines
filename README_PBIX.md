# Dashboard Power BI

## ⭐ MÉTHODE CHOISIS

## 📁 Fichiers csv résultats modèles ML/DL pour Power BI

## 📊 Feuilles incluses

| # | Feuille | Contenu |
|---|---------|---------|
| 1 | XGBoost_Metrics | Métriques XGBoost |
| 2 | Models_Comparison | Comparaison des modèles |
| 3 | Airports | Satisfaction par aéroport |
| 4 | Features | Feature importance |
| 5 | Chatbot | Métriques chatbot |
| 6 | Business_KPIs | KPIs business |
| 7 | 📋 Instructions | Instructions détaillées |
| 8 | 📐 DAX_Measures | Formules DAX à copier |
| 9 | 📈 KPIs | KPIs consolidés |
| 10 | 💡 Recommandations | Actions prioritaires |
| 11 | 🎨 Visuels_Config | Configuration des visuels |

## 🚀 Pages du Dashboard

### 1. Executive
- 4 Cartes KPI: XGBoost, SVM , DistilBERT , Global 
- 1 Jauge: Score global vs objectif
- 3 Cartes: Aéroports critiques, Chatbot, ROI à atteindre (+25%)

### 2. Performance Modèles
- Tableau comparatif des modèles
- Graphique radar (Accuracy, Precision, Recall, F1, ROC-AUC)
- Graphique barres: Feature importance

### 4. Analyse Aéroports
- Top 5 pires aéroports
- Top 5 meilleurs aéroports

### 5. Chatbot Insights
- Volume par intention (Top: Reservation - 25 questions)
- Taux de résolution par intention

### 6. Business Insights
- ROI projeté: +25%
- Délai: 6 mois
- Recommandations prioritaires

## 📝 Mesures DAX (Power BI)

```
XGBoost_F1 = 95.91
SVM_F1 = 91.21
DistilBERT_F1 = 89.19
Customer_Satisfaction_Target = 90
Global_Satisfaction_Score = ([XGBoost_F1]*0.5)+([SVM_F1]*0.3)+([DistilBERT_F1]*0.2)
Critical_Airports_Count = CALCULATE(COUNTROWS(airport_satisfaction_filtered), [mean] < 0.20)
Chatbot_Avg_Resolution = AVERAGE(chatbot_metrics[resolution_rate])
ROI_3_Years_Value = 25
Time_to_ROI_Value = 6
```

## 💡 Actions Prioritaires

| Priorité | Action | Impact | Délai |
|----------|--------|--------|-------|
| P0 | Améliorer Online Boarding | 31.3% | 1 mois |
| P0 | Action sur Newcastle | Moyen | 2 mois |
| P0 | Action sur Bogota | Moyen | 2 mois |
| P0 | Action sur Karachi | Moyen | 2 mois |
| P1 | Optimiser Chatbot vers 90% | Moyen | 3 mois |
| P1 | Continuer entraînement XGBoost | Faible | 1 mois |

## 🔗 Fichiers sources

Données brutes dans `/home/esprit/airlLines_Project/powerbi_data/`:
- `xgboost_metrics.csv`
- `nlp_model_comparison.csv`
- `airport_satisfaction_filtered.csv`
- `word_importance.csv`
- `chatbot_metrics.csv`
- `business_kpis.csv`
- `wordcloud_positive.png`
- `wordcloud_negative.png`