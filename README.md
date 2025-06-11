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
    - [Procédure de nettoyage (Mod 0 et plus)](#procédure-de-nettoyage-mod-0-et-plus)
- [Réflexions éthiques (Mod 1):](#réflexions-éthiques-mod-1)
- [Nettoyages des données (Mod 2)](#nettoyages-des-données-mod-2)

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
│   ├── data_numeric_only.csv                       # Donnée source
│   ├── df_data_numeric_cleaned.csv                 # Données filtrées et nettoyées
│   ├── data-all-68482f115ac04033078508.csv         # Donnée source numérique et catégorique
│   ├── df_data_ALL_cleaned.csv                     # Données filtrées et nettoyées
│   ├── df_data_all_cleaned_data_analyste_reviewed.csv        # Données filtrées et nettoyées
│   └── df_data_all_cleaned_ethical_analyste_reviewed.csv     # Données filtrées et nettoyées
├── .gitignore
├── README.md
├── ethique_note_0.ipynb              # Notebook du projet pour la partie numérique
├── ethique_note_1.ipynb              # Notebook du projet pour la partie numérique et catégorique
└── requirements.txt
```


## Utilisation
- Lancer le notebook `ethique_note_0.ipynb` pour suivre l'analyse et le nettoyage des données.
- Lancer le notebook `ethique_note_1.ipynb` pour suivre l'analyse et le nettoyage des données éthiques.

## Annexes
### Procédure de nettoyage (Mod 0 et plus)
1. **Chargement des données** : Importation du dataset et affichage des premières lignes.
2. **Analyse** : Visualisation des données manquantes (`missingno`) et exploration des relations (`seaborn`).
3. **Nettoyage** : Suppression des colonnes inutiles, gestion des valeurs manquantes, filtrage des données pertinentes.
4. **Sauvegarde** : Export du dataset nettoyé pour une utilisation ultérieure.

> Pour plus de détails et de visualisations, consulter le notebook associé.

# Réflexions éthiques (Mod 1):
la démarche de nettoyage et de préparation des données a été  guidée par des principes éthiques pour garantir l'intégrité et la responsabilité dans le traitement des données. 


- Chaque étape du processus de nettoyage est documentée pour la traçabilité des données.
- On a évité les biais dans le traitement des données pour garantir une représentation équitable de tous les groupes. (par exemple le sexe et la nationalité)


# Nettoyages des données (Mod 2)
