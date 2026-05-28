# Dashboard Power BI - Airlines Project

## 📁 Contenu du dossier

| Fichier | Description |
|---------|-------------|
| `xgboost_metrics.csv` | Métriques du modèle XGBoost |
| `nlp_model_comparison.csv` | Comparaison des modèles NLP |
| `airport_satisfaction_filtered.csv` | Satisfaction par aéroport |
| `word_importance.csv` | Importance des mots/features |
| `chatbot_metrics.csv` | Métriques du chatbot |
| `business_kpis.csv` | KPIs business |
| `wordcloud_positive.png` | Nuage de mots positifs |
| `wordcloud_negative.png` | Nuage de mots négatifs |

## 🚀 Instructions Power BI

### 1. Importer les données
1. Ouvrir Power BI Desktop
2. **Obtenir des données** > **Dossier**
3. Sélectionner ce dossier: `/home/esprit/airlLines_Project/powerbi_data/`
4. **Combiner et charger**

### 2. Créer les mesures DAX
1. **Modélisation** > **Nouvelle mesure**

### 3. Créer les pages du dashboard

## 📊 KPIs Principaux

| KPI | Valeur | Objectif | Statut |
|-----|--------|----------|--------|
| Satisfaction XGBoost | 95.91% | 90% | ✅ Atteint |
| Satisfaction SVM | 91.21% | 90% | ✅ Atteint |
| Satisfaction DistilBERT | 89.19% | 85% | ✅ Atteint |
| Score Global | ~93.5% | 90% | ✅ Atteint |
| Aéroports critiques | 3 | 0 | ⚠️ Action |
| Résolution Chatbot | 85% | 90% | 🟡 En cours |
| ROI 3 ans | +25% | +25% | 🎯 Objectif |

## 🎯 Prochaines actions recommandées

1. **Priorité 1**: Améliorer les 3 aéroports critiques (< 20% satisfaction)
2. **Priorité 2**: Renforcer le processus d'Online Boarding (impact majeur)
3. **Priorité 3**: Améliorer le taux de résolution du chatbot (85% → 90%)