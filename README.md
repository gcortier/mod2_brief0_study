
###### Le `.venv` 


```bash
python -m venv .venv
```


* **Windows (PowerShell) :**
    ```bash
    .\.venv\Scripts\Activate.ps1
    ```
* **Windows (CMD) :**
    ```bash
    .\.venv\Scripts\activate.bat
    ```
* **macOS / Linux :**
    ```bash
    source .venv/bin/activate
    ```


###### Le `requirements.txt`


Assure-toi que ton `.venv` est activé, puis :

```bash
pip install -r requirements.txt
```


#### 🗺️ Architecture : Où va quoi dans notre petit monde ? 🗺️


.
├── data/
│   ├── data_numeric_only.csv         => La donnée source
│   └── df_data_numeric_cleaned.csv   => La données filtrée et nettoyée
├── .gitignore
├── README.md
├── ethique_note_0  => Le notebook du projet
└── requirements.txt
```

###### `data/` (Le garde-manger du projet)
Ici, c'est là que nos précieuses données vivent.
* `df_new.csv` : Les données fraîches du jour, prêtes à être dévorées par notre IA.
* `df_old.csv` : Les classiques, les vétérans, ceux qui ont tout vu. On les garde par nostalgie (et pour la rétrospective).

###### `figures/` (L'analyste visuelle)
Sauvegarde des images des courbes de coût et autres graphiques pour visualiser les performances de notre modèle.

###### `models/` (Le garage à cerveaux)
Ce dossier, c'est notre caverne d'Ali Baba des cerveaux artificiels.
* `models.py` : Les plans de nos futurs cyborgs... euh, de nos modèles. C'est ici que l'on définit l'architecture de nos NN et autres merveilles.
* `model_2024_08.pkl` : Une version sauvegardée de notre modèle. On l'a encapsulé pour qu'il ne s'échappe pas et ne domine pas le monde... pas encore.
* `preprocessor.pkl` : L'outil magique qui prépare les données avant de les donner à manger au modèle. Sans lui, c'est l'indigestion assurée !

###### `modules/` (La boîte à outils de MacGyver)
Ce sont nos couteaux suisses du code. Chaque fichier est un expert dans son domaine.
* `evaluate.py` : Le juge impitoyable qui dit si notre modèle est un génie ou un cancre.
* `preprocess.py` : Le chef cuisinier des données. Il les nettoie, les coupe, les assaisonne pour qu'elles soient parfaites pour notre IA.
* `print_draw.py` : L'artiste du groupe. Il transforme nos chiffres barbares en beaux graphiques pour que même ta grand-mère puisse comprendre (enfin, presque).

---

On espère que cette petite virée dans notre projet t'a plu. N'hésite pas à jeter un œil au `main.py` pour lancer le grand spectacle !

*Fait avec amour, code et une bonne dose de caféine (et un peu de folie).*


# TD => GOGOGO
## setup

- ### Génération requirements.txt à chaque installation de module
```bash
pip freeze > requirements.txt
```

- ### Installations manuelle des requis : 
```bash
pip install missingno
pip install seaborn
```

## Annexes / data

### Procédure : 
Voir le notebook associé pour les graphs et details.
Analyse du dataset `data_numeric_only.csv` pour en extraire les données pertinentes, les nettoyer et les préparer pour l'entraînement du modèle.
### Étapes :
1. **Chargement des données** : Importation du dataset et affichage des premières lignes pour une première inspection.
2. **Analyse des données** : Utilisation de `missingno` pour visualiser les données manquantes et `seaborn` pour explorer les relations entre les variables.
3. **Nettoyage des données** : Suppression des colonnes inutiles, gestion des valeurs manquantes et filtrage des données pour ne conserver que celles pertinentes.
4. **Enregistrement des données nettoyées** : Sauvegarde du dataset nettoyé dans un nouveau fichier CSV pour une utilisation ultérieure.