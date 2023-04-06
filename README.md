# assistance_pascale conversation basé sur l'API OpenAI GPT-3

Ce projet est un assistant de conversation simple basé sur l'API OpenAI GPT-3. Il utilise la classe openai.ChatCompletion pour générer des réponses en fonction de l'historique de la conversation.

# Installation

Ce projet utilise pipenv pour la gestion des dépendances et de l'environnement virtuel. Pour l'installer, exécutez la commande suivante :

bash

Copy code

pip install pipenv

Ensuite, clonez ce dépôt et installez les dépendances :

bash

Copy code

git clone https://github.com/yangtangwandji/assistance_pascale.git

cd your\_project

pipenv install

# Configuration

Pour utiliser l'API OpenAI GPT-3, vous aurez besoin d'une clé API. Vous pouvez en obtenir une en créant un compte sur le site d'OpenAI.

Une fois que vous avez votre clé API, vous devez la stocker dans un fichier .env à la racine du projet, comme ceci :

text

Copy code

CHATGPT\_API\_KEY=votre\_clé\_api

# Utilisation

Pour utiliser l'assistant de conversation, exécutez le script main.py :

bash

```

pipenv run python main.py

```

L'assistant vous demandera d'entrer votre message et vous renverra une réponse en fonction de votre entrée.

# Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

# License

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
