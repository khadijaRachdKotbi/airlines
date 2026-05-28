# 🚀 Démarrage Rapide Power BI

## ✅ Solution: Excel complet pour Power BI

Le fichier `Airlines_PowerBI_Data.xlsx` contient **TOUT** ce qu'il vous faut.

---

## Étape 1: Ouvrir Power BI Desktop

Si vous n'avez pas Power BI Desktop:
- Téléchargez: https://www.microsoft.com/fr-fr/power-platform/products/power-bi-desktop

---

## Étape 2: Importer les données

1. Cliquez sur **Obtenir des données** 📥
2. Sélectionnez **Classeur Excel** 📊
3. Naviguez vers: `~/airlLines_Project/Airlines_PowerBI_Data.xlsx`
4. Cliquez sur **Charger** ✅

Power BI va charger toutes les feuilles automatiquement.

---

## Étape 3: Créer les mesures DAX

1. Cliquez sur l'onglet **Modélisation** 🧩
2. Cliquez sur **Nouvelle mesure** ➕
3. Ouvrez la feuille **📐 DAX_Measures** dans Excel
4. **Copiez/Collez** chaque formule:

```
XGBoost_F1 = 95.91
SVM_F1 = 91.21
DistilBERT_F1 = 89.19
Global_Satisfaction_Score = ([XGBoost_F1]*0.5)+([SVM_F1]*0.3)+([DistilBERT_F1]*0.2)
```

---

## Étape 4: Créer les visuels

Référez-vous à la feuille **🎨 Visuels_Config** pour la configuration.

### Page 1: Executive

| Visuel | Données | Champs |
|--------|---------|--------|
| Card | Mesure | XGBoost_F1 |
| Card | Mesure | SVM_F1 |
| Card | Mesure | DistilBERT_F1 |
| Gauge | Mesure | Global_Satisfaction_Score |

### Page 2: Performance Modèles

| Visuel | Données | Champs |
|--------|---------|--------|
| Table | Models_Comparison | Toutes colonnes |
| Radar | Models_Comparison | Légende: Model, Valeurs: Accuracy, Precision, Recall, F1-Score, ROC-AUC |
| Bar Chart | Features | Axe: word, Valeur: score |

---

## 📁 Vos fichiers

```
~/airlLines_Project/
├── Airlines_PowerBI_Data.xlsx  ⭐ Fichier principal
├── powerbi_data/               📁 Données sources
│   ├── xgboost_metrics.csv
│   ├── wordcloud_positive.png
│   └── ...
├── README_PBIX.md              📖 Documentation
└── QUICKSTART.md               📖 Ce fichier
```

---

## 🎯 Résultat attendu

Votre dashboard aura 6 pages avec:
- KPIs en temps réel
- Comparaison des modèles ML
- Analyse des sentiments
- Aéroports critiques identifiés
- Insights chatbot
- Recommandations business

---

## ❓ Problème?

- **Erreur d'importation**: Vérifiez que le fichier Excel n'est pas ouvert
- **Mesures DAX qui ne fonctionnent pas**: Vérifiez les noms des colonnes dans Power BI
- **Besoin d'aide**: Consultez la feuille **📋 Instructions** dans le fichier Excel

---

📊 **Temps estimé**: 15-20 minutes pour créer un dashboard complet !