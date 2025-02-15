# 📜 Legal French Tracker

   
🚀 Problématique

La législation française devient de plus en plus complexe, et le suivi des évolutions réglementaires est chronophage pour les juristes. Legal French Tracker permet de suivre les évolutions réglementaires sur un périmètre défini (ex : Code de commerce, Code civil) et une période précise (année, mois). L'outil commente les changements réglementaires et propose un résumé des dernières évolutions, permettant ainsi d'optimiser l'analyse juridique.

🎯 Objectifs

- Récupération automatique des dernières évolutions réglementaires.

- Comparaison des textes (ancienne vs nouvelle version).

- Restitution des changements sous un format tabulaire, classé chronologiquement.

- Génération de résumés clairs et référencés.

🔍 Fonctionnalités

✅ Extraction des dernières évolutions réglementaires selon un périmètre défini (codes, dates).✅ Enrichissement des données avec les versions avant/après de chaque article.✅ Commentaires ligne par ligne en respectant le langage juridique.✅ Résumé précis et pertinent des modifications.

🛠 Prérequis

- Python 3.13.0

- Clé API Légifrance : Inscription sur le portail développeur de Légifrance

- Accès à GPT-4o Azure 


⚙️ Fonctionnement de la solution

- Récupération des modifications législatives via l'API Légifrance.

- Nettoyage et transformation des données en format tabulaire.

- Enrichissement des données via d'autres appels API pour comparer les versions.

- Utilisation de GPT-4o pour analyser et commenter les changements.

- Génération d'un résumé clair et synthétique.

🚀 Exécution de la solution

- Option 1: Exécution avec l'interface Streamlit: streamlit run streamlit_app.py

- Option 2: Exécution avec docker 

🛠 Améliorations du code à venir: 

- Mise en place de l'importation des librairies / modules internes avec __init__.py 

- Amélioration de la conformité du code a PEP 8

- CI / CD 

🔮 Fonctionnalités à venir

- LLMops

- Mesure qualité du commentaire LLM

- Explorer alternatives autres LLM. 

------------------------------------------------------------------------------------------------------------------------------------------------

🚀 Problem Statement
French legislation is becoming increasingly complex, and tracking regulatory changes is a time-consuming task for legal professionals. The tool developed aims to monitor regulatory changes within a specific scope (e.g., Commercial Code, Civil Code) and time frame (year, month), streamlining the process of staying updated. The tool provides commentary on regulatory changes and summarizes the latest developments, saving valuable time. Recent regulatory changes can be critical for legal analysis or when defining an approach to a legal issue.

🎯 Goals

Develop a tool that retrieves the latest regulatory changes in French legal texts and compares article content (old version vs. new version). The data must be presented in a tabular format, organized chronologically. The tool is also able to provide a complete summary with references of all changes.

🔍 Features
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

🚀 Run the solution

- Option 1: Execution with the Streamlit interface: streamlit run streamlit_app.py

- Option 2: Execution with docker

🛠 Upcoming code improvements:

- Enhance of the import of internal libraries / modules with __init__.py

- Improve the code compliance with PEP 8

- CI / CD

🔮 Upcoming features

- LLMops

- Quality measurement of the LLM comment

- Alternative comments with other models