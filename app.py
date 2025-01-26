import streamlit as st
import pandas as pd
import io

# Import de vos fonctions et variables
from modules_simili.get_token import get_token
from credentials import client_id, client_secret
from modules_simili.LegiFR_call_funct import *
from modules_simili.dataprep_funct import *

# Titre centré et stylisé
st.markdown(
    """
    <h1 style='text-align: center; color: navy;'>Legal French Tracker</h1>
    """,
    unsafe_allow_html=True
)

# Liste des textes juridiques et leurs Cid correspondants
codes = {
    "Code civil": "LEGITEXT000006070721",
    "Code de commerce": "LEGITEXT000005634379",
    "Code des assurances": "LEGITEXT000006073984",
    "Code monétaire et financier": "LEGITEXT000006072026",
    "Code pénal": "LEGITEXT000006070719",
    "Code du travail": "LEGITEXT000006072050",
    "Code de la consommation": "LEGITEXT000006069565",
    "Code de la sécurité sociale": "LEGITEXT000006073189",
    "Code de procédure civile": "LEGITEXT000006070716",
    "Code de procédure pénale": "LEGITEXT000006071154",
    "Code de l'environnement": "LEGITEXT000006074220",
    "Code général des impôts": "LEGITEXT000006069574"
}

# Liste déroulante pour sélectionner le texte juridique
selected_code = st.selectbox(
    "Sélectionnez un code juridique :",
    options=list(codes.keys()),  # Affiche les noms des codes
)

# Récupération du Cid correspondant au texte sélectionné
textCid = codes[selected_code]

# Zone pour saisir l'intervalle d'années
annee_debut = st.text_input("Entrez la date de début (année ou format JJ-MM-AAAA) :", value="2020")
annee_fin = st.text_input("Entrez la date de fin (année ou format JJ-MM-AAAA) :", value="2021")

# Bouton d'exécution
if st.button("Lancer le tracker"):
    # 1) Récupération du token
    try:
        access_token = get_token()
        st.success("Étape 0 - Récupération du token réussie")
    except Exception as e:
        st.error(f"Erreur lors de la récupération du token : {e}")

    # 2) Test de connexion Ping Pong
    try:
        if ping_pong_test(access_token) == 'pong':
            st.success("Test Ping Pong : connexion réussie")
        else:
            st.error("Test Ping Pong : échec de connexion")
    except Exception as e:
        st.error(f"Erreur lors du test Ping Pong : {e}")

    # 3) Récupération des données
    try:
        json_output = get_text_modif_byDateslot_textCid_extract_content(
            access_token, textCid, annee_debut, annee_fin
        )
        st.success("Étape 1 - Requête API LégiFrance effectuée avec succès")
    except Exception as e:
        st.error(f"Étape 1 - Échec : {e}")

    # 4) Formatage des données
    try:
        panda_output = transform_json_to_dataframe(json_output)
        st.success("Étape 2 - Formatage des données réussi")
    except Exception as e:
        st.error(f"Étape 2 - Échec : {e}")

    # 5) Ajout de l'ancien contenu
    try:
        ajout_col_AV(panda_output)
        st.success("Étape 3 - Ajout de l'ancien contenu (AV) réussi")
    except Exception as e:
        st.error(f"Étape 3 - Échec : {e}")

    # 6) Ajout du nouveau contenu
    try:
        ajout_col_coutenu_NV(panda_output)
        st.success("Étape 4 - Ajout du nouveau contenu (NV) réussi")
    except Exception as e:
        st.error(f"Étape 4 - Échec : {e}")

    # 7) Ajout de la colonne comparative
    try:
        compare_AV_vs_NV(panda_output)
        st.success("Étape 5 - Ajout de la colonne de comparaison réussi")
    except Exception as e:
        st.error(f"Étape 5 - Échec : {e}")

    # 8) Export en mémoire et bouton de téléchargement
    try:
        # On convertit la base pandas_output en Excel dans un buffer
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            panda_output.to_excel(writer, index=False, sheet_name='Données')
        st.success("Étape 6 - Fichier Excel préparé pour téléchargement")

        st.write("Aperçu des données :")
        st.dataframe(panda_output.head(10))  # On montre les 10 premières lignes

        st.download_button(
            label="Télécharger le fichier Excel",
            data=buffer.getvalue(),
            file_name="DB_Legifrance.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    except Exception as e:
        st.error(f"Étape 6 - Échec : {e}")
        
        
        