import sys
sys.path.append('../')
import speech

def defuse_simon(data, check):

    #RGBY

    vowel = [{'red':'blue','blue':'red','green':'yellow','yellow':'green'},{'red':'yellow','blue':'green','green':'blue','yellow':'red'},{'red':'green','blue':'red','green':'yellow','yellow':'blue'}]
    no_vowel = [{'red':'blue','blue':'yellow','green':'green','yellow':'red'},{'red':'red','blue':'blue','green':'yellow','yellow':'green'},{'red':'yellow','blue':'green','green':'blue','yellow':'red'}]

    if check['vowel'] == 'yes':
        ans = vowel[int(data[0])]
    elif check['vowel'] == 'no':
        ans = no_vowel[int(data[0])]
    else:
        speech.speak('error with vowel check')  
    
    try:
        sequence = ""
        
        for i in data[1:]:
            sequence += ans[i] + ", "
        
        speech.speak(sequence + "next")
        go = True
        while go:
            colour = speech.record_audio()
            if 'stop' in colour or 'exit' in colour or 'done' in colour or 'finished' in colour:
                go = False
            else:
                if len(colour.split()) != 1:
                    speech.speak('just say one colour')
                elif colour in ans.keys():
                    sequence += ans[colour] + ", "
                    speech.speak(sequence + ", ")
                    speech.speak('next')
                else:
                    speech.speak('say one colour')
    except:
        speech.speak('error try again')