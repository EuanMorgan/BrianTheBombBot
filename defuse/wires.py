import sys
sys.path.append('../')
import speech


def defuse_wires(colors,check):

    if len(colors) == 3:
        if 'red' not in colors:
            speech.speak('Cut the second wire')
        elif colors[-1] == 'white':
            speech.speak('Cut the last wire')
        elif colors.count('blue') > 1:
            speech.speak('cut the last blue wire')
        else:
            speech.speak('cut the last wire')
    elif len(colors) == 4:
        if (colors.count('red') > 1) and (int(check['digit']) % 2 == 1):
            speech.speak('cut the last red wire')
        elif (colors[-1] == 'yellow') and ('red' not in colors):
            speech.speak('cut the first wire')
        elif colors.count('blue') == 1:
            speech.speak('cut the first wire')
        elif colors.count('yellow') > 1:
            speech.speak('cut the last wire')
        else:
            speech.speak('cut the second wire')
    elif len(colors) == 5:
        if (colors[-1] == "black") and (int(check['digit']) % 2 == 1):
            speech.speak('cut the fourth wire')
        elif (colors.count('red') == 1) and (colors.count('yellow') > 1):
            speech.speak('cut the first wire')
        elif colors.count('black') == 0:
            speech.speak('cut the second wire')
        else:
            speech.speak('cut the first wire')
    elif len(colors) == 6:
        if (colors.count('yellow') == 0) and (int(check['digit']) % 2 == 1):
            speech.speak('cut the third wire')
        elif (colors.count('yellow') == 1) and (colors.count('white') > 1):
            speech.speak('cut the fourth wire')
        elif colors.count('red') == 0:
            speech.speak('cut the last wire')
        else:
            speech.speak('cut the fourth wire')
