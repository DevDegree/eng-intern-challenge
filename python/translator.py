# translator.py
import sys

brl_letter_translator = {
    'capital': '.....O',
    'number': '.O.OOO',
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',
}

brl_number_translator = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
}

# takes braille dictionary and flips keys to values and values to keys to create english dicts
eng_letter_translator = {b: e for e, b in brl_letter_translator.items()}
eng_number_translator = {b: e for e, b in brl_number_translator.items()}

# if word is Braille, returns true
# else, returns false (i.e. word is English)
def is_braille(word) -> bool:
    braille_characters = {'O', '.'}
    input_characters = set(word)
    return (input_characters.issubset(braille_characters) and len(word) >= 6)

# takes english input (word) and return braille string
def eng_to_braille(word) -> str:
    result = ''
    number = False
    letter = True
    for i in word: 
        if i.isdigit(): 
            if not number:
                result += (brl_letter_translator['number'])
                number = True
            result += brl_number_translator[i]
        else: 
            if i.isalpha() and i.isupper():
                result += (brl_letter_translator['capital'])
                i = i.lower()
            elif i == ' ': 
                number = False
            result += brl_letter_translator[i]
    return result

# takes braille input (word) and returns english
def braille_to_eng(word) -> str:
    result = ''
    is_capital = False
    is_number = False
    for i in range (5,len(word),6): 
        curr = word[i-5:i+1]
        if eng_letter_translator[curr] == 'capital': 
            is_capital = True
        elif eng_letter_translator[curr] == 'number': 
            is_number = True
        else: 
            if is_capital: 
                result += eng_letter_translator[curr].upper()
                is_capital = False
            elif is_number:
                result += eng_number_translator[curr]
            else: 
                if curr == ' ': 
                    is_number = False
                result += eng_letter_translator[curr]

    return result

if __name__ == "__main__":
    input = ' '.join(sys.argv[1:])
    if is_braille(input):
        print(braille_to_eng(input))
    else: 
        print(eng_to_braille(input))
