import speech_recognition as sr
import playsound
from gtts import gTTS
import os
import random

r = sr.Recognizer()


def record_audio():
    with sr.Microphone() as source:
        r.energy_threshold = 4000
        audio = r.listen(source)

        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            # speak("Sorry, didn't get that")
            pass
        except sr.RequestError:
            speak("Sorry , my speech service is down")
        if voice_data == 'sex':  # unfortunate mishearing fix
            voice_data = 'six'
        return voice_data.lower()


def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
