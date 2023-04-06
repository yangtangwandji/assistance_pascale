
from dotenv import load_dotenv
import speech_recognition as sr
import os

from src.ChatGPT import ChatGPT

r = sr.Recognizer()

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("CHATGPT_API_KEY")
    chat_gpt = ChatGPT(api_key)
    
    with sr.Microphone() as source:
        print("Dites quelque chose!")
        audio = r.listen(source)
        try:
            user_message = r.recognize_google(audio, language='fr-FR')
            print("Vous avez dit: " + user_message)
            response = chat_gpt.get_response(user_message)
        except sr.UnknownValueError:
            print("Désolé, je n'ai pas compris ce que vous avez dit")
        except sr.RequestError as e:
            print("Impossible de se connecter au service de reconnaissance vocale; {0}".format(e))
    
    print(response)

    # user_message = "is that in canada?"
    # response = chat_gpt.get_response(user_message)
    # print(response)