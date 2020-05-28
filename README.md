Brian the Bomb Bot is a speech recognition app written in Python to solve all the puzzles in the game 'Keep Talking and Nobody Explodes'




INITIAL BOMB CHECK

When the game first loads, you should give Brian all the information he needs about the bomb.

Say:
check

Brian Responds:
Ready

Say:
digit [0-9] - this is the last digit of the serial number
batteries [0-9] - how many individual batteries are on the bomb
vowel [yes/no] - if the serial number contains a vowel
parallel [yes/no] - if the bomb has a parallel port
car [yes/no] - if there is a lit indicator labelled 'CAR'
freak [yes/no] - if there is a lit indicator labelled 'FRK'

example:
you: check
brian: ready
you: digit 9, batteries 2, vowel no, parallel yes, car no, freak yes


ON THE SUBJECT OF WIRES

Say:
wires [your wire colours in order]

Example:
you: wires red black yellow yellow
brian: cut the last wire


ON THE SUBJECT OF THE BUTTON

Say:
button [color] [text]

If Brian says: 'hold, color?'
Hold the button then tell Brian the color of the light strip
Brian responds saying countdown [number] which means release the button when the countdown displays a [number]

Example:
you: button red abort
brian: press and immediately release

you: button yellow detonate
brian: hold color
you: white
brian: countdown 1


ON THE SUBJECT OF KEYPADS

Say:
keypad [four symbols] - see the symbols.jpg for all the symbol names

Brian responds with the order you should press them

Example:
you: keypad spaceship balloon lambda pyramid
brian: balloon pyramid lambda spaceship
