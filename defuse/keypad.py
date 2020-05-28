import sys
sys.path.append('../')
import speech

def defuse_keypad(symbols,check):
    choices = ["balloon", "pyramid", "lambda", "lightning", "spaceship", "hotel", "eye", "omega", "november",
               "echo", "copyright", "nose", "spiral", "white", "inkblot", "question", "puzzle", "together", "six", "paragraph", "guitar", "smile", "trail",
               "trident", "charlie", "snake", "black"]

    answers = [["balloon", "pyramid", "lambda", "lightning", "spaceship", "hotel", "eye"],
               ["echo", "balloon", "eye", "spiral", "white", "hotel", "question"],
               ["copyright", "nose", "spiral", "inkblot",
                   "trail", "lambda", "white"],
               ["six", "paragraph", "guitar", "spaceship",
                   "inkblot", "question", "smile"],
               ["trident", "smile", "guitar", "charlie",
                "paragraph", "snake", "black"],
               ["six", "echo", "puzzle", "together", "trident", "november", "omega"]]

    if (set(symbols).issubset(choices)):
        pass
    else:
        speech.speak('sorry try again')

    column = -1

    if(set(symbols).issubset(answers[0])):
        column = 0
    elif(set(symbols).issubset(answers[1])):
        column = 1
    elif(set(symbols).issubset(answers[2])):
        column = 2
    elif(set(symbols).issubset(answers[3])):
        column = 3
    elif(set(symbols).issubset(answers[4])):
        column = 4
    elif(set(symbols).issubset(answers[5])):
        column = 5

    if column == -1:
        speech.speak('sorry try again')
    else:
        string = ""
        indexes = []

        for i in range(0, len(symbols)):
            indexes.append(answers[column].index(symbols[i]))

        indexes.sort()

        for i in indexes:
            string += answers[column][i] + ", "

        speech.speak(string)