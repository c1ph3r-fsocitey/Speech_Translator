import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os

while True:  
    r = sr.Recognizer()
    translator = Translator()
    with sr.Microphone() as source:
        print("speak now!")
        audio = r.listen(source)
        try:
            speech_text = r.recognize_google(audio)
            print(speech_text)
            if(speech_text == "exit"):
                break
        except sr.UnknownValueError():
            print("could not understand")
        except sr.RequestError():
            print("cold not understand")
        translated_text = translator.translate(speech_text, dest="fr")
        translated_text_only = translated_text.text
        
        print(translated_text_only)
        
        voice = gTTS(translated_text_only, lang="fr")
        voice.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")