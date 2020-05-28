import sys
sys.path.append('../')
import speech
def defuse_password():
    alphabet = {'alpha':'a', 'bravo':'b','charlie':'c', 'delta':'d', 'echo':'e', 'foxtrot':'f', 'golf':'g',"hotel":"h", 
    'india':'i', 'juliet':'j', 'kilo':'k', 'lima':'l', 'mike':'m', 'november':'n', 'oscar':'o', 'papa':'p', 'quebec':'q', 
    'romeo':'r', 'sierra':'s', 'tango':'t', 'uniform':'u', 'victor':'v', 'whiskey':'w', 'xray':'x', 'yankee':'y', 'zulu':'z'}

    passwords = ["about","after","again","below","could",
                "every","first","found","great","house",
                "large","learn","never","other","place",
                "plant","point","right","small","sound",
                "spell","still","study","their","there",
                "these","thing","think","three","water",
                "where","which","world","would","write"]

    column = 0

    letters = [[],[],[]]
    wrong = False
    while column < 3:
        speech.speak('column ' + str(column + 1))
        voice_data = speech.record_audio()
        print(voice_data)
        if 'exit' in voice_data:
            letters = None
            break
        voice_data = voice_data.split()
        for i in voice_data:
            if i == "whisky":
                i = "whiskey"
            if i == "x-ray":
                i = "xray"
            if i == "ecco":
                i = "echo"
            if i in alphabet.keys():
                letters[column].append(alphabet[i])
            else:
                wrong = True
                break
        print(letters)
        if len(letters[column]) != 6:
            wrong = True
        if wrong:
            wrong = False
            letters[column] = []
        else:
            column+=1

    try:
        answers = []
        for i in letters[0]:
            for j in letters[1]:
                for k in letters[2]:
                    for p in passwords:
                        if p.startswith(i+j+k):
                            answers.append(p)
        print(answers)
        if len(answers) == 1:
            speech.speak("The password is " + answers[0])
            spell_password(answers[0])
        elif len(answers) > 1:
            speech.speak("The password is either " + answers[0])
            spell_password(answers[0])
            for i in range(0,len(answers)):
                if i != 0:
                    speech.speak('or ' + answers[i])
                    spell_password(answers[i])
        else:
            speech.speak("Error try again")


        print(letters)
    except:
        pass

def spell_password(p):
    #TODO: make it so you can stop spelling
    letters = ""
    for i in p:
        letters+= i + " "
    speech.speak(letters)


    
        