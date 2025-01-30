# Legal French Tracker 

# Problématique
La législation française est de plus en plus complexe, le suivi des évolutions réglementaires est chronophage pour les juristes. L'outil développé propose de suivre les évolutions réglementaires sur un périmètre donné (Code de commerce, code civil...) et une période (année, mois) afin de faciliter les évolutions réglementaires. L'outil commente les changements réglementaire et propose un résumé des dernières évolutions dans le but  de faire gagner du temps. Les derniers changements réglementaires peuvent être décisifs lors d'analyses juridiques ou pour la définition d'une approche a une problématique légale.

# Objectifs
Développer un outil qui récupère les dernières évolutions réglementaires dans les textes juridiques français, compare le contenu des articles (ancienne version vs nouvelle version). La restituons de ces données devra se faire dans un format tabulaire, classée de façon chronologique.

# Prérequis
- Python 3.13.0
- Register on the Légifrance Developer Portal to obtain an API key: https://piste.gouv.fr
- Légifrance API Key to access the Légifrance API. 
- Accès GPT 4o

# Fonctionnalités 
- Extraire les dernières évolutions sur le périmètre défini par l'utilisateur (code et dates)
- Enrichir ces données avec le contenu de chaque article dans sa version avant et après.  
- Commenter les changements réglementaire ligne par ligne à la fois pertinent, précis et succinct en respectant le langage juridique. 
- Faire un résumé le plus pertinent et précis possible.

# Fonctionnement de la solution: 
- Les modifications des textes législatifs sont récupérés depuis l'API Légifrance, retraités , nettoyés et transformés en un format tabulaire. 
- Les données sont enrichies avec d'autres call API pour récupérer le contenu des articles (ancienne version vs nouvelle version)
- Un LLM (GPT 4o) est utilisé pour commenter les changements.
- Le LLM fait un résumé des commentaires une restitution a l'utilisateur.

# Execution de la solution : 
Option 1: Les fichiers pour construire la base de données (tabulaire) sans passer par l'interface Streamlit sont : 
- main.py (utilise un environnement sandbox de l'API Légifrance).
- main_prod.py (utilise un environnement prod de l'API Légifrance. Aucun gain notable en performances enregistré).

	-> Pour exécuter la construction de la base de donnée : python3 main.py ou python3 main_prod.py ou python3 main_tqdm.py depuis le terminal.

Option 2: Les fichiers pour construire la base de données (tabulaire) en utilisant l'interface Streamlit sont : 
- app.py
	-> Pour démarrer l'application Streamlit : python3 app.py depuis le terminal.

Autres fichiers : 
-   Explore_LégiFrance_API.ipynb : notebook pour exploration des call api, est aussi une version notebook de l'application. 
- modules_tracker: regroupe les fichier .py pour main qui intégrent des fonctions de call API, d'authentification et de fonctions de préparations de données (nettoyage et formatage) 

# Autres fonctionnalités à venir

------------------------------------------------------------------------------------------------------------------------------------------------

# Problem Statement
French legislation is becoming increasingly complex, and tracking regulatory changes is a time-consuming task for legal professionals. The tool developed aims to monitor regulatory changes within a specific scope (e.g., Commercial Code, Civil Code) and time frame (year, month), streamlining the process of staying updated. The tool provides commentary on regulatory changes and summarizes the latest developments, saving valuable time. Recent regulatory changes can be critical for legal analysis or when defining an approach to a legal issue.

# Goals
Develop a tool that retrieves the latest regulatory changes in French legal texts and compares article content (old version vs. new version). The data must be presented in a tabular format, organized chronologically.

# Features
- Extract the latest changes within the scope defined by the user (code and dates).
- Enrich the data with the content of each article, showing both its previous and updated versions.
- Provide line-by-line commentary on regulatory changes that is relevant, precise, and concise while adhering to legal language.
- Generate a summary that is as relevant and accurate as possible.

# Prerequisites
- Python 3.13.0
- Register on the Légifrance Developer Portal to obtain an API key: https://piste.gouv.fr
- Légifrance API Key to access the Légifrance API.
- Access to GPT-4o.

# How the solution is working : 
- Legislative text modifications are retrieved from the Légifrance API, processed, cleaned, and transformed into a tabular format.
- The data is enriched with additional API calls to retrieve the content of articles (old version vs. new version).
- An LLM (GPT-4) is used to comment on the changes.
- The LLM summarizes the comments and provides a user-friendly output.

# Run the solution : 
Option 1: build the database (tabular format) without using the Streamlit interface:
- main.py (uses a sandbox environment of the Légifrance API).
- main_prod.py (uses a production environment of the Légifrance API; no significant performance improvements recorded).

Option 2: build the database (tabular format) using the Streamlit interface:
- streamlit run app.py in terminal to execute the Streamlit application.

Other files:
- Explore_LégiFrance_API.ipynb: A notebook for exploring API calls, which also serves as a notebook version of the application.
- modules_tracker: Contains .py files for main, which include API call functions, authentication mechanisms, and data preparation functions (cleaning and formatting).

# Other upcomming features

