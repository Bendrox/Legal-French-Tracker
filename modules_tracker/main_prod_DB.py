#imports tiers + standards
from tqdm import tqdm
import requests
import sys

# Import des modules locaux
from modules_tracker.get_token import get_token, get_token_prod
from modules_tracker.LegiFR_call_prod_funct import ping_pong_test_prod, ajout_col_AV_prod, ajout_col_coutenu_NV_prod, get_text_modif_byDateslot_textCid_extract_content_prod
from modules_tracker.dataprep_funct import transform_json_to_dataframe,compare_AV_vs_NV

access_token_prod = get_token_prod()

# Test connection 

try:
    if ping_pong_test_prod(access_token_prod) == 'pong':
        print("Connexion réussie (Ping Pong Test)")
    else:
        print("Connexion échouée (Ping Pong Test)")
except Exception as e:
    print(f"Erreur lors du test de connexion : {e}")
    
    
# Step 1: Retreiving data from Léfifrance  

try: 
    json_output =  get_text_modif_byDateslot_textCid_extract_content_prod(access_token_prod, "LEGITEXT000006072026", "2020", "2021")
    print("Etape 1: Requête API LégiFrance")
except Exception as e:
    print(f"Échec : Une erreur est survenue lors du Call. Détails : {e}")
    
    
# Step 2: Formating data

try: 
    panda_output= transform_json_to_dataframe(json_output)
    print("Etape 2: Formatage des données récupérées")
except Exception as e:
    print(f"Etape 2: Échec : Une erreur est survenue lors du formatage des données. Détails : {e}")


#Step 3:  adding a new colomun content of OLD version 

print("Début de l'étape 3")
print("Etape 3 en cours")

try: 
    ajout_col_AV_prod(panda_output)
    print("Etape 3: Ajout de l'ancien contenu des articles avec succès")
except Exception as e:
    print(f"Etape 3: Échec, une erreur est survenue lors du Call. Détails : {e}")
    
    
#Step 4:  adding a new colomun content of new version 

print("Début de l'étape 4")
print("Etape 4 en cours")
try: 
    ajout_col_coutenu_NV_prod(panda_output)
    print("Etape 4: Ajout du nouveau contenu des articles avec succès !")
except Exception as e:
    print(f"Échec 4: Échec, une erreur est survenue lors du Call. Détails : {e}")


#Step 5: adding a colomun to compare content

try: 
    compare_AV_vs_NV(panda_output)
    print("Etape 5: Ajout de la colonne comparative")
except Exception as e:
    print(f"Échec 5: Échec, une erreur est survenue lors du Call. Détails : {e}")


#Step 6: Exporting database of LegiFrance

try:
    panda_output.to_excel("data_output/Legifrance_DB_TrackChange.xlsx")
    print("Etape 6: Fichier Excel a été exporté avec succès !")
except Exception as e:
    print(f"Etape 6: Échec : Une erreur est survenue lors de l'enregistrement. Détails : {e}")

