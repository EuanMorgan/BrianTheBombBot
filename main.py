import speech
import time
from time import ctime
from defuse.wires import defuse_wires
from defuse.button import defuse_button
from defuse.keypad import defuse_keypad
check = {}

# This is a voice recognition app built to solve the puzzles in the game Keep talking and nobody explodes
# https://www.bombmanual.com/print/KeepTalkingAndNobodyExplodes-BombDefusalManual-v1.pdf

def respond(voice_data):
    global check
    voice_data = voice_data.lower()
    if 'check' in voice_data or 'jack' in voice_data:
        speech.speak('ready')
        global check
        voice_data = speech.record_audio()

        voice_data = voice_data.split()

        try:
            for i in range(0, len(voice_data) - 1):
                if i % 2 == 0:
                    check[voice_data[i]] = voice_data[i+1]

            check['digit'] = stringtoint(check['digit'])
            check['batteries'] = int(stringtoint(check['batteries']))
            print(check)
        except:
            speech.speak('sorry try again')
    if 'wires' in voice_data or 'why is' in voice_data:
        voice_data = voice_data.split()
        defuse_wires(voice_data[1:], check)
    if 'button' in voice_data or 'butter' in voice_data:
        voice_data = voice_data.split()
        voice_data = voice_data[1:]
        if len(voice_data) > 2:
            if voice_data[2] == "boat":
                voice_data[1] == "abort"
        if voice_data[0] == "read":
            voice_data[0] = "red"
        print(voice_data)
        defuse_button(voice_data,check)
    if 'keypad' in voice_data or 'key pad' in voice_data or 'leappad' in voice_data:
        voice_data = voice_data.split()
        voice_data = voice_data[1:]
        if len(voice_data) == 4:
            if('i' in voice_data):
                voice_data[voice_data.index('i')] = "eye"
            if('6' in voice_data):
                voice_data[voice_data.index('6')] = "six"
            if('ballooned' in voice_data):
                voice_data[voice_data.index('ballooned')] = "balloon"
            if len(voice_data) != len(set(voice_data)):
                speech.speak('sorry, try again')
            else:
                print(voice_data)
                defuse_keypad(voice_data,check)
        else:
            speech.speak('sorry, try again')
    if 'exit' in voice_data or 'except' in voice_data:
        exit()
    if 'oh my god' in voice_data:
        speech.speak('Its not my fault')
    if 'hello' in voice_data:
        speech.speak('hello, how are you?')
    if 'test' in voice_data:
        speech.speak('roger')
    if 'thank you' in voice_data:
        speech.speak('im a slave')
    if 'we did it' in voice_data:
        speech.speak('excuse me i did all the hard work')

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

time.sleep(0.5)
speech.speak('How can I help you?')

while True:
    print("READY")
    voice_data = speech.record_audio()
    print(voice_data)
    respond(voice_data)
