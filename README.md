# Application Web de Création et de Jeu de Quiz

Ce projet est une application web interactive réalisée en **Python** à l'aide de **Streamlit**. Elle permet aux utilisateurs de créer leurs propres quiz dans des thèmes spécifiques, de créer leurs questions et de jouer à ces quiz tout en suivant récupérant leur score final.
---

## Fonctionnalités

### 1. **Création de Quiz**
- Les utilisateurs peuvent créer un quiz dans le thème de leur choix.
- Chaque quiz contient plusieurs questions avec des réponses multiples.
- Les données des quiz sont sauvegardées sous forme de fichiers JSON pour une gestion facile.

### 2. **Jouer à un Quiz**
- Les quiz créés peuvent être parcourus, question par question.
- Le score des bonnes réponses est calculé automatiquement.
- Une interface conviviale guide l'utilisateur tout au long du jeu.

### 3. **Validation des Entrées**
- Les phases de validation (nom du thème, contenu des questions, réponses, et index des réponses correctes) sont régies par des règles strictes définies avec **Pydantic**.
- L'utilisateur est notifié en cas de saisies invalides.

---

## Pré-requis

### Installation des dépendances :
1. Clonez le dépôt du projet :

   ```bash
   git clone <https://github.com/ludivineRB/interactive_application.git>
   cd <interactive_application>

2. Clonez le dépôt du projet :

   ```bash
    pip install -r requirements.txt

## Lancement de l'Application
1. Assurez-vous que les dépendances sont installées.

2. Démarrez l'application avec la commande suivante :
   ```bash
    streamlit run streamlit_app.py

3. Ouvrez l'application dans votre navigateur via le lien fourni par Streamlit (généralement http://localhost:8501).

## Organisation des Fichiers
- streamlit_app.py : Point d'entrée de l'application.
- json_functions.py : Contient les fonctions de manipulation des fichiers JSON (chargement et sauvegarde des quiz).
- Dossier theme/ : Stocke les fichiers JSON des différents thèmes de quiz créés.

## A propos des technologies utilisées
- Python : Langage principal du projet.
- Streamlit : Framework utilisé pour construire l'interface web interactive.
- Pydantic : Utilisé pour valider les données saisies par les utilisateurs.
- JSON : Format utilisé pour stocker les questions et réponses des quiz.

## Contribuer au projet
Si vous souhaitez contribuer :

    1. Faites un fork du dépôt.
    2. Créez une branche pour votre fonctionnalité ou correction :
        ```bash
        git checkout -b nouvelle-fonctionnalite
    3. Proposez une pull request avec vos modifications.

## Auteurs
Projet réalisé par ludivineRB avec toute l'équipe de la techIA de Simplon Lille. N'hésitez pas à nous contacter pour toute question ou suggestion !