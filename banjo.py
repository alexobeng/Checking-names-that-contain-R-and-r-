# banjo.py
import re

# Hint: Remember, you can slice strings to extract specific letters!

def playing_banjo(name):
    '''This function checks to see if someone plays
    the banjo based on their name. Names beginning
    with "R" or "r" play the banjo, while others do not.'''

    if re.search("R",name):
        print(f"{name}  played the banjo")
    

    elif re.search("r",name):
        print(f"{name} played the banjo")
        

    else:
        print(f"{name} does not play banjo")

# Test cases to see if you are correct
playing_banjo('Leah')
playing_banjo('michael')
playing_banjo('brian')
playing_banjo('Ryan')
playing_banjo('rolf')
