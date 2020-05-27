import speech_recognition as sr
from time import ctime
import time
import playsound
import os
import random
from gtts import gTTS
digit = ""
r = sr.Recognizer()
a = True


# This is a voice recognition app built to solve the puzzles in the game Keep talking and nobody explodes
# https://www.bombmanual.com/print/KeepTalkingAndNobodyExplodes-BombDefusalManual-v1.pdf


def record_audio():
    with sr.Microphone() as source:
        r.energy_threshold = 2500
        audio = r.listen(source)

        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry, didn't get that")
        except sr.RequestError:
            speak("Sorry , my speech service is down")
        if voice_data == 'sex':  # unfortunate mishearing fix
            voice_data = 'six'
        return voice_data


def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'exit' in voice_data or 'except' in voice_data:
        exit()
    if 'oh my god' in voice_data:
        speak('Its not my fault')
    if 'wires' in voice_data:
        defuse_wires()
    if 'hello' in voice_data:
        speak('hello, how are you?')
    if 'digit' in voice_data:
        speak('go')
        d = record_audio()
        global digit
        digit = d
    if 'test' in voice_data:
        speak('roger')


def defuse_wires():
    global digit
    colors = []
    while len(colors) == 0:
        try:
            speak('name wires')
            voice_data = record_audio()
            colors = voice_data.split()
            speak(voice_data)
        except:
            pass

    if len(colors) == 3:
        if 'red' not in colors:
            speak('Cut the second wire')
        elif colors[-1] == 'white':
            speak('Cut the last wire')
        elif colors.count('blue') > 1:
            speak('cut the last blue wire')
        else:
            speak('cut the last wire')
    elif len(colors) == 4:
        if (colors.count('red') > 1) and (int(digit) % 2 == 1):
            speak('cut the last red wire')
        elif (colors[-1] == 'yellow') and ('red' not in colors):
            speak('cut the first wire')
        elif colors.count('blue') == 1:
            speak('cut the first wire')
        elif colors.count('yellow') > 1:
            speak('cut the last wire')
        else:
            speak('cut the second wire')
    elif len(colors) == 5:
        if (colors[-1] == "black") and (int(digit) % 2 == 1):
            speak('cut the fourth wire')
        elif (colors.count('red') == 1) and (colors.count('yellow') > 1):
            speak('cut the first wire')
        elif colors.count('black') == 0:
            speak('cut the second wire')
        else:
            speak('cut the first wire')
    elif len(colors) == 6:
        if (colors.count('yellow') == 0) and (int(digit) % 2 == 1):
            speak('cut the third wire')
        elif (colors.count('yellow') == 1) and (colors.count('white') > 1):
            speak('cut the fourth wire')
        elif colors.count('red') == 0:
            speak('cut the last wire')
        else:
            speak('cut the fourth wire')


time.sleep(0.5)
speak('How can I help you?')

while a:
    print(digit)
    print("hello")
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)
