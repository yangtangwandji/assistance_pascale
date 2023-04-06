import openai
from gtts import gTTS
import os

class ChatGPT:
    def __init__(self, api_key, model="gpt-3.5-turbo"):
        self.model = model
        self.api_key = api_key
        openai.api_key = self.api_key
        self.messages = [{"role": "system", "content": "You are a helpful assistant."}]

    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})

    def get_response(self, user_message):
        self.add_message("user", user_message)
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages
        )
        assistant_message = response.choices[0].message['content']
        self.add_message("assistant", assistant_message)
        self.speak(assistant_message)
        return assistant_message

    def speak(self, text):
        language = 'fr'
        tts = gTTS(text=text, lang=language)
        tts.save("welcome.mp3")
        os.system("welcome.mp3")