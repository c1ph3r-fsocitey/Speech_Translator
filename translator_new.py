import speech_recognition as sr
from translate import Translator
from gtts import gTTS
from playsound import playsound
import os

while True:
    r = sr.Recognizer()
    translator = Translator(to_lang="fr")
    with sr.Microphone() as source:
        print("Speak now!")
        audio = r.listen(source)
        try:
            speech_text = r.recognize_google(audio)
            print(speech_text)
            if speech_text == "exit":
                break
        except sr.UnknownValueError:
            print("Could not understand.")
        except sr.RequestError:
            print("Could not request results.")

        translated_text = translator.translate(speech_text)

        print(translated_text)

        voice = gTTS(text=translated_text, lang="fr")
        voice.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")
