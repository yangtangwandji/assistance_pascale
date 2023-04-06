import openai
from gtts import gTTS
import os

class ChatGPT:
    """
    Classe représentant un assistant personnel capable de converser avec l'utilisateur en utilisant
    le modèle de langage GPT-3 de OpenAI. L'assistant peut répondre à des requêtes formulées par l'utilisateur
    et lire les réponses à haute voix à l'aide de la synthèse vocale gTTS.

    Attributs:
        - model (str): Le nom du modèle de langage GPT-3 à utiliser pour la génération de texte.
        - api_key (str): La clé API de OpenAI pour l'authentification.
        - messages (list): Une liste de dictionnaires représentant les messages échangés entre l'utilisateur
          et l'assistant. Chaque dictionnaire a deux clés: "role" (string) qui indique le rôle de la personne
          qui a envoyé le message ("user" ou "assistant") et "content" (string) qui contient le texte du message.

    Méthodes:
        - __init__(self, api_key: str, model: str = "gpt-3.5-turbo"): Initialise la classe avec les
          paramètres de modèle et de clé API. Initialise également la liste de messages avec un message
          de bienvenue du système.
        - add_message(self, role: str, content: str): Ajoute un message à la liste des messages échangés.
        - get_response(self, user_message: str) -> str: Utilise le modèle de langage GPT-3 pour générer
          une réponse à partir du message de l'utilisateur, ajoute la réponse à la liste des messages
          échangés et lit la réponse à haute voix en utilisant gTTS. La méthode renvoie également la réponse
          générée.
        - speak(self, text: str): Convertit le texte donné en une voix synthétique en utilisant la synthèse vocale
          gTTS et joue le fichier audio résultant à l'aide du module os.

    """
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        """
        Initialise la classe avec les paramètres de modèle et de clé API. Initialise également la liste de messages
        avec un message de bienvenue du système.

        Args:
            - api_key (str): La clé API de OpenAI pour l'authentification.
            - model (str): Le nom du modèle de langage GPT-3 à utiliser pour la génération de texte.
        """
        self.model = model
        self.api_key = api_key
        openai.api_key = self.api_key
        self.messages = [{"role": "system", "content": "You are a helpful assistant."}]

    def add_message(self, role: str, content: str):
        """
        Ajoute un message à la liste des messages échangés.

        Args:
            - role (str): Le rôle de la personne qui a envoyé le message ("user" ou "assistant").
            - content (str): Le contenu textuel du message.
        """
        self.messages.append({"role": role, "content": content})

    def get_response(self, user_message: str) -> str:
        """
        Utilise le modèle de langage GPT-3 pour générer une réponse à partir du message de l
