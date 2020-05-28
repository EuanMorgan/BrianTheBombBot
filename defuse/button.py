import sys
sys.path.append('../')
import speech

def defuse_button(button,check):

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
        speech.speak('press and immediately release')
    elif (color == "white") and (check['car'] == "yes"):
        hold = True
    elif (check['batteries'] > 2) and (check['freak'] == "yes"):
        speech.speak('press and immediately release')
    elif color == "yellow":
        hold = True
    elif (color == "red") and (word == "hold"):
        speech.speak("press and immediately release")
    else:
        hold = True
    if hold:
        speech.speak('hold, color?')
        strip = speech.record_audio()

        if strip == "blue":
            speech.speak('countdown 4')
        elif strip == "white":
            speech.speak('countdown 1')
        elif strip == "yellow":
            speech.speak('countdown 5')
        else:
            speech.speak('countdown 1')