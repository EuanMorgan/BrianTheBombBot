import speech_recognition as sr
from time import ctime
import time
import playsound
import os
import random
from gtts import gTTS
check = {}
r = sr.Recognizer()


# This is a voice recognition app built to solve the puzzles in the game Keep talking and nobody explodes
# https://www.bombmanual.com/print/KeepTalkingAndNobodyExplodes-BombDefusalManual-v1.pdf


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


def respond(voice_data):
    voice_data = voice_data.lower()
    if 'exit' in voice_data or 'except' in voice_data:
        exit()
    if 'oh my god' in voice_data:
        speak('Its not my fault')
    if 'wires' in voice_data or 'why is' in voice_data:
        voice_data = voice_data.split()
        defuse_wires(voice_data[1:])
    if 'hello' in voice_data:
        speak('hello, how are you?')
    if 'check' in voice_data or 'jack' in voice_data:
        speak('ready')
        global check
        voice_data = record_audio()

        voice_data = voice_data.split()

        try:
            for i in range(0, len(voice_data) - 1):
                if i % 2 == 0:
                    check[voice_data[i]] = voice_data[i+1]

            check['digit'] = stringtoint(check['digit'])
            check['batteries'] = int(stringtoint(check['batteries']))
            print(check)
        except:
            speak('sorry try again')

    if 'test' in voice_data:
        speak('roger')
    if 'thank you' in voice_data:
        speak('im a slave')
    if 'we did it' in voice_data:
        speak('excuse me i did all the hard work')
    if 'button' in voice_data or 'butter' in voice_data:
        voice_data = voice_data.split()
        voice_data = voice_data[1:]
        if len(voice_data) > 2:
            if voice_data[2] == "boat":
                voice_data[1] == "abort"
        if voice_data[0] == "read":
            voice_data[0] = "red"
        print(voice_data)
        defuse_button(voice_data)


def stringtoint(d):
    if d == 'zero':
        d = 0
    elif d == 'one':
        d = 1
    elif d == 'two' or d == 'to' or d == 'too':
        d = 2
    elif d == 'three':
        d = 3
    elif d == 'four' or d == 'for':
        d = 4
    elif d == 'five':
        d = 5
    elif d == 'six' or d == 'sex':
        d = 6
    elif d == 'seven':
        d = 7
    elif d == 'eight':
        d = 8
    elif d == 'nine':
        d = 9
    return d


digit = 0


def defuse_wires(colors):
    global digit

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


def defuse_button(button):
    # try:
    color = button[0]
    word = button[1]
    hold = False

    if color == "read":
        color = "red"
    if word == "a":  # sometimes abort heard as a boat
        word = "abort"

    if color == "blue" and word == "abort":
        hold = True
    elif (check['batteries'] > 1) and (word == "detonate"):
        speak('press and immediately release')
    elif (color == "white") and (check['car'] == "yes"):
        hold = True
    elif (check['batteries'] > 2) and (check['freak'] == "yes"):
        speak('press and immediately release')
    elif color == "yellow":
        hold = True
    elif (color == "red") and (word == "hold"):
        speak("press and immediately release")
    else:
        hold = True
    if hold:
        speak('hold, color?')
        strip = record_audio()

        if strip == "blue":
            speak('countdown 4')
        elif strip == "white":
            speak('countdown 1')
        elif strip == "yellow":
            speak('countdown 5')
        else:
            speak('countdown 1')
# except:
    # speak('try again')


time.sleep(0.5)
speak('How can I help you?')

while True:
    print(digit)
    print("hello")
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)
