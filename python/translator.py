#create dictionaries for English and Braille characters
english_braille = {
    # Lowercase letters
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',

    # Capital letter indicator (used before capital letters)
    'CAPITAL': '.....O',

    # Numbers (with number indicator before numbers)
    'NUMBER': '..O.OO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',

    # Space
    ' ': ' '
}

braille_english = {
    # Lowercase letters
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z',

    # Numbers (numbers are preceded by the number indicator)
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',

    # Space
    ' ': ' ',

    # Special indicators
    '.....O': 'CAPITAL',  # Capital letter indicator
    '..O.OO': 'NUMBER'    # Number indicator
}

# function to convert english to braille
def english_to_braille(english):
   translated_sentence = []

   for char in english:
       if char.isupper():
           #capital letter indicator
           translated_sentence.append(english_braille['CAPITAL'])
           #add the symbol for the actual letter in lower case
           translated_sentence.append(english_braille[char.lower()])
       elif char.isdigit():
           # number letter indicator
           translated_sentence.append(english_braille['NUMBER'])
           translated_sentence.append(english_braille[char])
       else:
           translated_sentence.append(english_braille[char])
   return ''.join(translated_sentence)

def braille_to_english(braille):
   translated_sentence = []

   for char in braille:
       if char.isupper():
           translated_sentence.append(english_braille['.....O'])
       translated_sentence.append(english_braille[char])
   return ''.join(translated_sentence)