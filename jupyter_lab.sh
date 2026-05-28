#!/bin/bash

# Script de démarrage Jupyter Lab pour le projet airlines

# Activation de l'environnement conda
source ~/miniconda3/bin/activate airlines

# Vérification de l'environnement
echo "🐍 Environnement: $CONDA_DEFAULT_ENV"
echo "📁 Projet: $(pwd)"

# Démarrage Jupyter Lab
echo "🚀 Démarrage de Jupyter Lab..."
jupyter lab \
    --notebook-dir=/home/esprit/airlLines_Project \
    --ip=0.0.0.0 \
    --port=8888 \
    --no-browser \
    --allow-root \
    --NotebookApp.token='' \
    --NotebookApp.password=''