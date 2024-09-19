
import sys

brailledict = {"a": "O.....","b": "O.O...","c": "OO....", "d": "OO.O..", "e": "O..O..", "f":"OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".O.O..", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u":"O..OO", "v":"O.O.OO", "w":".OOO.O", "x":"OO..OO", "y":"OO.OOO", "z":"O..OOO", "1":"O.....","2":"O.O...","3":"OO....","4":"OO.O..","5":"O..O..","6":"OOO...","7":"OOOO..","8":"O.OO..","9":".OO...","0":".OOO..",".":"..OO.O",",":"..O...","?":"..O.OO","!":"..OOO.",":":"..OO..",";":"OO.O.O","-":"....OO","/":".O..O.","<":".OO.O.",">":"O..OO.","(":"O.O..O",")":".O.OO.", " ":"......"} 
num_follows = ".O.OOO"
capital_follows = ".....O"
decimal_follows = ".O...O"
englishdict = {}

def braille_to_english():
    return "Hello world"

def english_to_braille(word):
    braille = ''
    numturn = False
    for char in word:
        if char.isnumeric() == True and numturn == False:
            numturn = True
            braille += num_follows
        if char == " ":
            numturn = False
        if char == ".":
            braille += decimal_follows + (brailledict[char])
        if char.isupper() == True:
            braille += capital_follows
        if char.lower() in brailledict:
            braille += (brailledict[char.lower()])
    return braille


words = [arg for arg in sys.argv[1:]]
output = ""
first_word = True
for word in words:
    if first_word == False:
        output += brailledict[" "]
    else:
        first_word = False
    output += english_to_braille(word)

sys.stdout.write(output)