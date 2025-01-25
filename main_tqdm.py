from tqdm import tqdm
from modules_simili.get_token import get_token, get_token_prod
from credentials import client_id, client_secret
from modules_simili.LegiFR_call_funct import *
from modules_simili.dataprep_funct import *
import requests

# Initialisation des tokens
access_token = get_token()
access_token_prod = get_token_prod()

# Initialisation des étapes pour le tracking
steps = [
    "Test de connexion",
    "Récupération des données de LégiFrance",
    "Formatage des données",
    "Ajout de l'ancien contenu",
    "Ajout du nouveau contenu",
    "Comparaison des contenus",
    "Exportation des données"
]

# Barre de progression
for i, step in enumerate(tqdm(steps, desc="Suivi des étapes")):
    try:
        if i == 0:  # Test de connexion
            if ping_pong_test(access_token) == 'pong':
                print("Étape 1 réussie : Test de connexion OK")
            else:
                raise Exception("Échec du test de connexion")

        elif i == 1:  # Étape 1 - Récupération des données
            json_output = get_text_modif_byDateslot_textCid_extract_content(access_token, "LEGITEXT000006072026", "2020", "2021")
            print("Étape 2 réussie : Données récupérées")

        elif i == 2:  # Étape 2 - Formatage des données
            panda_output = transform_json_to_dataframe(json_output)
            print("Étape 3 réussie : Données formatées")

        elif i == 3:  # Étape 3 - Ajout de l'ancien contenu
            ajout_col_AV(panda_output)
            print("Étape 4 réussie : Ancien contenu ajouté")

        elif i == 4:  # Étape 4 - Ajout du nouveau contenu
            ajout_col_coutenu_NV(panda_output)
            print("Étape 5 réussie : Nouveau contenu ajouté")

        elif i == 5:  # Étape 5 - Comparaison des contenus
            compare_AV_vs_NV(panda_output)
            print("Étape 6 réussie : Comparaison ajoutée")

        elif i == 6:  # Étape 6 - Exportation
            panda_output.to_excel("data_output/Legifrance_DB_TrackChange.xlsx")
            print("Étape 7 réussie : Fichier exporté")

    except Exception as e:
        print(f"Erreur lors de l'étape '{step}' : {e}")
        break  # Arrête l'exécution si une erreur survient