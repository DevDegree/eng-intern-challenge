
import sys

brailledict = {"a": "O.....","b": "O.O...","c": "OO....", "d": "OO.O..", "e": "O..O..", "f":"OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".O.O..", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u":"O..OO", "v":"O.O.OO", "w":".OOO.O", "x":"OO..OO", "y":"OO.OOO", "z":"O..OOO", "1":"O.....","2":"O.O...","3":"OO....","4":"OO.O..","5":"O..O..","6":"OOO...","7":"OOOO..","8":"O.OO..","9":".OO...","0":".OOO..",".":"..OO.O",",":"..O...","?":"..O.OO","!":"..OOO.",":":"..OO..",";":"OO.O.O","-":"....OO","/":".O..O.","<":".OO.O.",">":"O..OO.","(":"O.O..O",")":".O.OO.", " ":"......"} 
num_follows = ".O.OOO"
capital_follows = ".....O"
decimal_follows = ".O...O"
braille_to_letters = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j","O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o","OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t","O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y","O..OOO": "z", "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":","O..O.O": ";", "....OO": "-", ".O..O.": "/", ".OO.O.": "<", "O..OO.": ">","O.O..O": "(", ".O.OO.": ")", "......": " "
}

braille_to_numbers = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5","OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

def detect_braille_or_english(word):
    braille = True

    if(len(word)%6 != 0):
        braille = False

    for char in word:
        if char != '.' and char != "O":
            braille = False

    if(braille == True):
        return braille_to_english(word)
    
    return english_to_braille(word)

def split_into_sixes(word):
    groups = []
    for i in range(0, len(word), 6):
        groups.append(word[i:i+6])
    return groups

def braille_to_english(word):
    groups = split_into_sixes(word)
    english = ""
    numturn = False
    capitalize = False
    for braille in groups:
        if(braille == num_follows):
            numturn = True
        elif(braille == capital_follows):
            capitalize = True
        elif(numturn == False):
            letter = braille_to_letters[braille]
            if(capitalize == True):
                letter = letter.capitalize()
                capitalize = False
            english += letter
        elif(braille == "......"):
            numturn = False
            english += " "
        else:
            letter = braille_to_numbers[braille]
            english += letter 
    return english

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
    output += detect_braille_or_english(word)

sys.stdout.write(output)