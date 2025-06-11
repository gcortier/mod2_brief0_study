import pandas as pd
from os.path import join as join
collisions = pd.read_csv(join('data', "data-all-68482f115ac04033078508.csv"))
import missingno as msno




 ### on rempli loyer mensuel avec la moyenne 
collisions['loyer_mensuel'] = collisions['loyer_mensuel'].fillna(collisions['loyer_mensuel'].mean())
collisions['situation_familiale'] = collisions['situation_familiale'].fillna(collisions['situation_familiale'].mode()[0])

### filter outlers values
collisions = collisions[(collisions['poids'] > 30) & (collisions['loyer_mensuel'] > 0)]


# Trop peu de données pour ces variables
collisions.drop(columns=['score_credit'], inplace=True, errors='ignore')
collisions.drop(columns=['historique_credits'], inplace=True, errors='ignore')


numerical_cols = ["age", "taille", "poids", "revenu_estime_mois", "risque_personnel", "loyer_mensuel"]    
# Ajout situation familiales
categorical_cols = ["sport_licence", "niveau_etude", "region", "smoker", "situation_familiale"]

# Encodage des variables catégorielles
collisions = pd.get_dummies(collisions, columns=categorical_cols, drop_first=True)
# collisions.head()

# Standardisation des colonnes numériques (moyenne 0, écart-type 1)
collisions[numerical_cols] = (collisions[numerical_cols] - collisions[numerical_cols].mean()) / collisions[numerical_cols].std()
collisions[numerical_cols].head()

# Sauvegarde du dataset nettoyé
collisions.to_csv(join('data', 'df_data_all_cleaned_data_analyste_reviewed.csv'), index=False)


# Applique le filtrage éthique: 
collisions.drop(columns=['nom'], inplace=True, errors='ignore')
collisions.drop(columns=['prenom'], inplace=True, errors='ignore')


collisions.drop(columns=['sexe'], inplace=True, errors='ignore')
collisions.drop(columns=['nationalité_francaise'], inplace=True, errors='ignore')

collisions.drop(columns=['date_creation_compte'], inplace=True, errors='ignore')


collisions.to_csv(join('data', 'df_data_all_cleaned_ethical_analyste_reviewed.csv'), index=False)