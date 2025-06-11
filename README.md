# Brief 0 Nettoyage de Données Numériques

Projet de nettoyage, préparation et visualisation de données numériques pour l'entraînement de modèles d'apprentissage automatique.

## Sommaire
- [Brief 0 Nettoyage de Données Numériques](#brief-0-nettoyage-de-données-numériques)
  - [Sommaire](#sommaire)
  - [Description](#description)
  - [Installation](#installation)
  - [Structure du projet](#structure-du-projet)
  - [Utilisation](#utilisation)
  - [Annexes](#annexes)
    - [Procédure de nettoyage](#procédure-de-nettoyage)

## Description
Analyser, nettoyer et transformer les données numériques afin de produire un dataset fiable, propre, cohérent et directement exploitable, en appliquant des techniques rigoureuses de traitement de données et en garantissant leur intégrité.

## Installation
1. **Créer un environnement virtuel**
   ```bash
   python -m venv .venv
   ```
2. **Activer l'environnement**
   - Windows (PowerShell) :
     ```bash
     .\.venv\Scripts\Activate.ps1
     ```
   - Windows (CMD) :
     ```bash
     .\.venv\Scripts\activate.bat
     ```
   - macOS / Linux :
     ```bash
     source .venv/bin/activate
     ```
3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

> **Astuce** : Mise à jour après chaque install du fichier requirements.txt :
> ```bash
> pip freeze > requirements.txt
> ```

## Structure du projet
```
.
├── data/
│   ├── data_numeric_only.csv         # Donnée source
│   └── df_data_numeric_cleaned.csv   # Données filtrées et nettoyées
├── .gitignore
├── README.md
├── ethique_note_0.ipynb              # Notebook du projet
└── requirements.txt
```


## Utilisation
- Lancer le notebook `ethique_note_0.ipynb` pour suivre l'analyse et le nettoyage des données.

## Annexes
### Procédure de nettoyage
1. **Chargement des données** : Importation du dataset et affichage des premières lignes.
2. **Analyse** : Visualisation des données manquantes (`missingno`) et exploration des relations (`seaborn`).
3. **Nettoyage** : Suppression des colonnes inutiles, gestion des valeurs manquantes, filtrage des données pertinentes.
4. **Sauvegarde** : Export du dataset nettoyé pour une utilisation ultérieure.

> Pour plus de détails et de visualisations, consulte le notebook associé.

