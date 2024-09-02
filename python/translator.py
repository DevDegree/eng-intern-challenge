import sys

translate_words = {
    "a" : "O.....",
    "b" : "O.O...",
    "c" : "OO....",
    "d" : "OO.O..",
    "e" : "O..O..",
    "f" : "OOO...",
    "g" : "OOOO..",
    "h" : "O.OO..",
    "i" : ".OO...",
    "j" : ".OOO..",
    "k" : "O...O.",
    "l" : "O.O.O.",
    "m" : "OO..O.",
    "n" : "OO.OO.",
    "o" : "O..OO.",
    "p" : "OOO.O.",
    "q" : "OOOOO.",
    "r" : "O.OOO.",
    "s" : ".OO.O.",
    "t" : ".OOOO.",
    "u" : "O...OO",
    "v" : "O.O.OO",
    "w" : ".OOO.O",
    "x" : "OO..OO",
    "y" : "OO.OOO",
    "z" : "O..OOO",
    " " : "......",
    "1" : "O.....",
    "2" : "O.O...",
    "3" : "OO....",
    "4" : "OO.O..",
    "5" : "O..O..",
    "6" : "OOO...",
    "7" : "OOOO..",
    "8" : "O.OO..",
    "9" : ".OO...",
    "0" : ".OOO..",
    " " : "......",
}

following = {
    "capital" : ".....O",
    "decimal" : ".O...O",
    "number" : ".O.OOO",
}

translate_braille = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd', 
    'O..O..': 'e', 
    'OOO...': 'f', 
    'OOOO..': 'g', 
    'O.OO..': 'h', 
    '.OO...': 'i', 
    '.OOO..': 'j',
    'O...O.': 'k', 
    'O.O.O.': 'l', 
    'OO..O.': 'm', 
    'OO.OO.': 'n', 
    'O..OO.': 'o', 
    'OOO.O.': 'p', 
    'OOOOO.': 'q', 
    'O.OOO.': 'r', 
    '.OO.O.': 's', 
    '.OOOO.': 't', 
    'O...OO': 'u', 
    'O.O.OO': 'v', 
    '.OOO.O': 'w', 
    'OO..OO': 'x', 
    'OO.OOO': 'y', 
    'O..OOO': 'z', 
    '......': ' ', 
    '.....O': 'capital', 
    '.O.OOO': 'number',
}

translate_braille_numbers = {
    'O.....': '1', 
    'O.O...': '2', 
    'OO....': '3', 
    'OO.O..': '4', 
    'O..O..': '5', 
    'OOO...': '6', 
    'OOOO..': '7', 
    'O.OO..': '8', 
    '.OO...': '9', 
    '.OOO..': '0', 
}

def determine_braille(word):
    for w in word:
        if w != '.' and w != 'O':
            return False
    return True
        
def braille_to_text(word):
    output = ""
    i = 0
    while i < len(word):
        if translate_braille[word[i:i+6]] == "capital":
            output += translate_braille[word[i+6:i+12]].upper()
            i += 12
        elif translate_braille[word[i:i+6]] == "number":
            i += 6
            while i < len(word) and translate_braille[word[i:i+6]] != " ":
                output += translate_braille_numbers[word[i:i+6]]
                i += 6
        else:
            output += translate_braille[word[i:i+6]]
            i += 6
    return output

def text_to_braille(words):
    output = ""
    setNumber = False
    for w in words:

        if w.isupper():
            output += following["capital"]
            w = w.lower()
        elif w.isdigit():
            output += following["number"] if not setNumber else ""
            setNumber = True
        elif w == " ":
            setNumber = False
        output += translate_words[w]
    return output

sentence = " ".join(sys.argv[1:])

is_braille = determine_braille(sentence)

if is_braille:
    output = braille_to_text(sentence)
else:
    output = text_to_braille(sentence)

print(output)
