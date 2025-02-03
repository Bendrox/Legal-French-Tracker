📜 Legal French Tracker

   
🚀 Problématique

La législation française devient de plus en plus complexe, et le suivi des évolutions réglementaires est chronophage pour les juristes. Legal French Tracker permet de suivre les évolutions réglementaires sur un périmètre défini (ex : Code de commerce, Code civil) et une période précise (année, mois). L'outil commente les changements réglementaires et propose un résumé des dernières évolutions, permettant ainsi d'optimiser l'analyse juridique.

🎯 Objectifs

Récupération automatique des dernières évolutions réglementaires.

Comparaison des textes (ancienne vs nouvelle version).

Restitution des changements sous un format tabulaire, classé chronologiquement.

Génération de résumés clairs et référencés.

🛠 Prérequis

Python 3.13.0

Clé API Légifrance : Inscription sur le portail développeur de Légifrance

Accès à GPT-4o

Fonctionnalités

✅ Extraction des dernières évolutions réglementaires selon un périmètre défini (codes, dates).✅ Enrichissement des données avec les versions avant/après de chaque article.✅ Commentaires ligne par ligne en respectant le langage juridique.✅ Résumé précis et pertinent des modifications.

⚙️ Fonctionnement de la solution

Récupération des modifications législatives via l'API Légifrance.

Nettoyage et transformation des données en format tabulaire.

Enrichissement des données via d'autres appels API pour comparer les versions.

Utilisation de GPT-4o pour analyser et commenter les changements.

Génération d'un résumé clair et synthétique.

🚀 Exécution de la solution

Option 1 : Construction de la base de données sans interface Streamlit

Exécute l'un des fichiers suivants :

python3 main.py  # Mode sandbox de l'API Légifrance
python3 main_prod.py  # Mode production de l'API Légifrance

Option 2 : Exécution avec l'interface Streamlit

streamlit run streamlit_app.py

📂 Autres fichiers

- Explore_LégiFrance_API.ipynb : Notebook d'exploration des appels API.📌 modules_tracker/ : Contient les scripts Python pour les appels API, l'authentification et la préparation des données.

🔮 Fonctionnalités à venir

-  Visualisation interactive des changements dans une interface web.

-  Système de notifications pour informer des mises à jour critiques.

- Contribuer : les suggestions sont les bienvenues !


------------------------------------------------------------------------------------------------------------------------------------------------

🚀 Problem Statement
French legislation is becoming increasingly complex, and tracking regulatory changes is a time-consuming task for legal professionals. The tool developed aims to monitor regulatory changes within a specific scope (e.g., Commercial Code, Civil Code) and time frame (year, month), streamlining the process of staying updated. The tool provides commentary on regulatory changes and summarizes the latest developments, saving valuable time. Recent regulatory changes can be critical for legal analysis or when defining an approach to a legal issue.

🎯 Goals
Develop a tool that retrieves the latest regulatory changes in French legal texts and compares article content (old version vs. new version). The data must be presented in a tabular format, organized chronologically. The tool is also able to provide a complete summary with references of all changes.

# Features
- Extract the latest changes within the scope defined by the user (code and dates).
- Enrich the data with the content of each article, showing both its previous and updated versions.
- Provide line-by-line commentary on regulatory changes that is relevant, precise, and concise while adhering to legal language.
- Generate a summary that is as relevant and accurate as possible.

🛠 Prerequisites
- Python 3.13.0
- Register on the Légifrance Developer Portal to obtain an API key: https://piste.gouv.fr
- Légifrance API Key to access the Légifrance API.
- Access to GPT-4o.

⚙️ How the solution is working : 
- Legislative text modifications are retrieved from the Légifrance API, processed, cleaned, and transformed into a tabular format.
- The data is enriched with additional API calls to retrieve the content of articles (old version vs. new version).
- An LLM (GPT-4) is used to comment on the changes.
- The LLM summarizes the comments and provides a user-friendly output.

🚀  Run the solution : 
Option 1: build the database (tabular format) without using the Streamlit interface:
- main.py (uses a sandbox environment of the Légifrance API).
- main_prod.py (uses a production environment of the Légifrance API; no significant performance improvements recorded) but a significate reliability in the responses.

Option 2: build the database (tabular format) using the Streamlit interface:
- streamlit run streamlit_app.py in terminal to execute the Streamlit application.

Other files:
- Explore_LégiFrance_API.ipynb: A notebook for exploring API calls, which also serves as a notebook version of the application.
- modules_tracker: Contains .py files for main, which include API call functions, authentication mechanisms, and data preparation functions (cleaning and formatting).

🔮 Other upcomming features

- Interactive visualization of changes in a web interface.

- Notification system to inform about critical updates.

- Contributor: suggestions are welcome!
