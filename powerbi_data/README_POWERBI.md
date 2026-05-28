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
| `dax_measures.txt` | Formules DAX prêtes à copier |

## 🚀 Instructions Power BI

### 1. Importer les données
1. Ouvrir Power BI Desktop
2. **Obtenir des données** > **Dossier**
3. Sélectionner ce dossier: `/home/esprit/airlLines_Project/powerbi_data/`
4. **Combiner et charger**

### 2. Créer les mesures DAX
1. **Modélisation** > **Nouvelle mesure**
2. Copier les formules depuis `dax_measures.txt`
3. Coller dans la barre de formules

### 3. Créer les 6 pages du dashboard

#### Page 1 - Executive (Vue globale)
- **4 Cartes** (Cards): XGBoost_F1, SVM_F1, DistilBERT_F1, Global_Satisfaction_Score
- **1 Jauge**: Global_Satisfaction_Score (Min: 0, Max: 100, Target: 90)
- **3 Cartes**: Critical_Airports_Count, Chatbot_Avg_Resolution, ROI_3_Years_Value

#### Page 2 - Performance Modèles
- **Tableau**: nlp_model_comparison (toutes les colonnes)
- **Graphique radar**: Champs = Accuracy, Precision, Recall, F1-Score, ROC-AUC | Légende = Model
- **Graphique barres horizontales**: word_importance (axe = word, valeur = score, couleur = sentiment)

#### Page 3 - Analyse Sentiment
- **2 Images**: wordcloud_positive.png, wordcloud_negative.png

#### Page 4 - Analyse Aéroports
- **Top 5 pires**: Filtre mean < 0.25, Trier mean ASC
- **Top 5 meilleurs**: Trier mean DESC
- **Tableau complet**: origin_norm, mean, count

#### Page 5 - Chatbot Insights
- **Graphique treemap**: Group = intent, Valeur = question_count
- **Graphique barres**: intent vs resolution_rate

#### Page 6 - Recommandations Business
- **KPIs clés** avec indicateurs de statut
- **Actions prioritaires**:
  - Aéroports critiques (Newcastle, Bogota, Karachi)
  - Améliorer Online Boarding (impact: 31.3%)
  - Optimiser Chatbot (objectif: 90%)

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