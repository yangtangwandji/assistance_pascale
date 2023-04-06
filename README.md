# assistance_pascale conversation basé sur l'API OpenAI GPT-3

Ce projet est un assistant de conversation simple basé sur l'API OpenAI GPT-3. Il utilise la classe openai.ChatCompletion pour générer des réponses en fonction de l'historique de la conversation.

# Installation
vous devez utiliser python 3.9.13

Veuillez créer un fichier .env à la racine du projet et y ajouter la clé API en utilisant la variable d'environnement suivante:
```
CHATGPT_API_KEY=<votre clé API ici>
```

Ce projet utilise pipenv pour la gestion des dépendances et de l'environnement virtuel. Pour l'installer, exécutez la commande suivante :

```
pip install pipenv
```

Ensuite, clonez ce dépôt et installez les dépendances :

```
git clone https://github.com/yangtangwandji/assistance_pascale.git
```
installer les dependanses :
```
pipenv install python-dotenv SpeechRecognition gTTS pydub openai PyAudio
```

Active lancer l'environnement virtuel

```
pipenv shell
```

# Configuration

Pour utiliser l'API OpenAI GPT-3, vous aurez besoin d'une clé API. Vous pouvez en obtenir une en créant un compte sur le site d'OpenAI.

Une fois que vous avez votre clé API, vous devez la stocker dans un fichier .env à la racine du projet, comme ceci :

text

```
CHATGPT\_API\_KEY=votre\_clé\_api
```

# Utilisation

Pour utiliser l'assistant de conversation, exécutez le script main.py :

```
pipenv run python main.py
```

L'assistant vous demandera d'entrer votre message et vous renverra une réponse en fonction de votre entrée.

# Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

# License

