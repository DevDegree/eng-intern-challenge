# dict.py
import sys

# dictionary containing braille values for english letter keys
brl_letter_dict = {
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

# dictionary containing braille values for numeric keys
brl_number_dict = {
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

# takes braille dictionary and swaps the kays and values to create english dicts 
eng_letter_dict = {b: e for e, b in brl_letter_dict.items()}
eng_number_dict = {b: e for e, b in brl_number_dict.items()}

# if word is Braille, returns true
# else, returns false (i.e. word is English)
def is_braille(word) -> bool:
    if len(word) < 6:
        return False
    for char in word:
        if char not in ('O', '.'):
            return False
    return True

# takes english input and returns braille string
def eng_to_braille(word) -> str:
    result = ''
    is_number = False
    for i in word: 
        if i.isdigit(): 
            if not is_number:
                result += (brl_letter_dict['number'])
                is_number = True
            result += brl_number_dict[i]
        else: 
            if i.isalpha() and i.isupper():
                result += (brl_letter_dict['capital'])
                i = i.lower()
            elif i == ' ': 
                is_number = False
            result += brl_letter_dict[i]
    return result

# takes braille input and returns english string
def braille_to_eng(word) -> str:
    result = ''
    is_capital = False
    is_number = False
    for i in range (5,len(word),6): 
        curr = word[i-5:i+1]
        if eng_letter_dict[curr] == 'capital': 
            is_capital = True
        elif eng_letter_dict[curr] == 'number': 
            is_number = True
        else: 
            if is_capital: 
                result += eng_letter_dict[curr].upper()
                is_capital = False
            elif is_number:
                result += eng_number_dict[curr]
            else: 
                if curr == ' ': 
                    is_number = False
                result += eng_letter_dict[curr]

    return result

if __name__ == "__main__":
    input = ' '.join(sys.argv[1:])
    if is_braille(input):
        print(braille_to_eng(input))
    else: 
        print(eng_to_braille(input))
