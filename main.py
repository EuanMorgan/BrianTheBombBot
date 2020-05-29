import speech
import time
from time import ctime
from defuse.wires import defuse_wires
from defuse.button import defuse_button
from defuse.keypad import defuse_keypad
from defuse.password import defuse_password
from defuse.simon import defuse_simon
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
        if 'foul' in voice_data:
            voice_data[voice_data.index('foul')] = 'vowel'
        if 'bowel' in voice_data:
            voice_data[voice_data.index('bowel')] = 'vowel'
        if 'powell' in voice_data:
            voice_data[voice_data.index('powell')] = 'vowel'
        if 'barrel' in voice_data:
            voice_data[voice_data.index('barrel')] = 'vowel'
        try:
            for i in range(0, len(voice_data) - 1):
                if i % 2 == 0:
                    check[voice_data[i]] = voice_data[i+1]

            
            
            print(check)
            
            incomplete = True

            while incomplete:
                incomplete = False  

                if ('digit' not in check.keys()) or (not str(check['digit']).isdigit()):
                    incomplete = True
                    speech.speak('repeat the digit')
                    check['digit'] = speech.record_audio()
                    check['digit'] = stringtoint(check['digit'])
                if ('batteries' not in check.keys()) or (not str(check['batteries']).isdigit()):
                    incomplete = True
                    speech.speak('repeat battery number')
                    check['batteries'] = speech.record_audio()
                    check['batteries'] = stringtoint(check['batteries'])
                if ('parallel' not in check.keys()) or (not str(check['parallel']) in ['yes','no']):
                    incomplete = True
                    speech.speak('repeat parallel yes/no')
                    check['parallel'] = speech.record_audio()
                if ('freak' not in check.keys()) or (not str(check['freak']) in ['yes','no']):
                    incomplete = True
                    speech.speak('repeat freak yes/no')
                    check['freak'] = speech.record_audio()
                if ('car' not in check.keys()) or (not str(check['car']) in ['yes','no']):
                    incomplete = True
                    speech.speak('repeat car yes/no')
                    check['car'] = speech.record_audio()
                if ('vowel' not in check.keys()) or (not str(check['vowel']) in ['yes','no']):
                    incomplete = True
                    speech.speak('repeat vowel yes/no')
                    check['vowel'] = speech.record_audio()
            print(check)
            speech.speak('Bomb initialisation complete')
        except:
            speech.speak('sorry try again')
    if 'wires' in voice_data or 'why is' in voice_data:
        print("hello")
        voice_data = voice_data.split()
        if 'bread' in voice_data:
            voice_data[voice_data.index('bread')] = "red"
        if 'why' in voice_data and 'is' in voice_data:
            defuse_wires(voice_data[2:], check)
        else:
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
            if "lampeter" in voice_data:
                voice_data[voice_data.index('lampeter')] = "lambda"
            if "lander" in voice_data:
                voice_data[voice_data.index('lander')] = "lambda"
            if len(voice_data) != len(set(voice_data)):
                speech.speak('sorry, try again')
            else:
                print(voice_data)
                defuse_keypad(voice_data,check)
        else:
            speech.speak('sorry, try again')
    if 'simon' in voice_data:
        voice_data = voice_data.split()
        voice_data = voice_data[1:]
        voice_data[0] = stringtoint(voice_data[0])
        
        if len(voice_data) == 3 or len(voice_data) == 4:
            if 'strikes' in voice_data:
                voice_data.pop(voice_data.index['strikes'])
            if 'flashing' in voice_data:
                voice_data.pop(voice_data.index['flashing'])

        if len(voice_data) == 2 or set(voice_data[1:]).issubset(['blue','red','yellow','green']):
            if 'read' in voice_data or 'bread' in voice_data:
                voice_data[1] = 'red'
            if '0gn' in voice_data:
                voice_data = ['0','green']
            if '1gn' in voice_data:
                voice_data = ['1', 'green']
            if '2gn' in voice_data:
                voice_data = ['2','green']
            if 'zerocream' in voice_data:
                voice_data = ['0','green']
            print(voice_data)
            defuse_simon(voice_data, check)


        else:
            speech.speak('try again')
        
    if 'password' in voice_data:
        defuse_password()
    if 'exit' in voice_data or 'except' in voice_data or 'accent' in voice_data:
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
    if 'skip' in voice_data:
        check ={'batteries':'2','digit':'2', 'parallel':'no', 'car':'no','freak':'yes','vowel':'yes'}
        print(check)
        speech.speak('bomb initialisation default config')

def stringtoint(d):
    if d == 'zero':
        d = 0
    elif d == 'one' or d == 'wan':
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


speech.speak('How can I help you?')

while True:
    print("READY")
    voice_data = speech.record_audio()
    print(voice_data)
    respond(voice_data)
