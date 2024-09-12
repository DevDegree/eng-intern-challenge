#Shopify Assessment
import sys

#English to Braille conversion dictionary
braille_conversion= {
    'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 'D': 'OO.O..', 'E': 'O..O..',
    'F': 'OOO...', 'G': 'OOOO..', 'H': 'O.OO..', 'I': '.OO...', 'J': '.OOO..',
    'K': 'O...O.', 'L': 'O.O.O.', 'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.',
    'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.', 'S': '.OO.O.', 'T': '.OOOO.',
    'U': 'O...OO', 'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO', 'Y': 'OO.OOO', 'Z': 'O..OOO',
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    ' ': '......','.' : '..OO.O',',': '..O...','?':'..O.OO','!' : '..OOO.',':':'..OO..','-':'....OO', '/': '.O..O.','<': '.OO..O','>':'O..OO.', '(': 'O.O..O', ')': '.O.OO.'
}
#Braille to English conversion dictionary
english_conversion_alpha = {
    'O.....': 'A', 'O.O...': 'B', 'OO....': 'C', 'OO.O..': 'D', 'O..O..': 'E',
    'OOO...': 'F', 'OOOO..': 'G', 'O.OO..': 'H', '.OO...': 'I', '.OOO..': 'J',
    'O...O.': 'K', 'O.O.O.': 'L', 'OO..O.': 'M', 'OO.OO.': 'N', 'O..OO.': 'O',
    'OOO.O.': 'P', 'OOOOO.': 'Q', 'O.OOO.': 'R', '.OO.O.': 'S', '.OOOO.': 'T',
    'O...OO': 'U', 'O.O.OO': 'V', '.OOO.O': 'W', 'OO..OO': 'X', 'OO.OOO': 'Y', 'O..OOO': 'Z' , '......': ' ', '..OO.O': '.',
    '..O...': ',', '..O.OO': '?', '..OOO.': '!', '..OO..': ':', '....OO': '-', '.O..O.': '/',
    '.OO..O': '<', 'O..OO.': '>', 'O.O..O': '(', '.O.OO.': ')'
}
english_conversion_number = {'.OOO..': '0', 'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9'}

#print(english_conversion)

#Detect the input string language
#Detect the input string language
def detect_language(given_string):
    s = given_string.replace(' ', '')
    if all(c in 'O.' for c in s):
        return 'braille'
    else:
        return 'english'

def english_to_braille(text):
    braille = []
    is_number = False
    for char in text:
        if char.isdigit():
            if not is_number:
                braille.append('.O.OOO')
                is_number = True
            braille.append(braille_conversion[char])
        elif char == ' ':
            braille.append('......')
            is_number = False
        else:
            if is_number:
                is_number = False
            if char.isupper():
                braille.append('.....O')
                braille.append(braille_conversion[char.upper()])
            else:
                braille.append(braille_conversion.get(char.upper(), '......'))

    return ''.join(braille)

# Convert Braille to English
def braille_to_english(braille_text):
    english = []
    is_capital = False
    is_number = False
    for i in range(0, len(braille_text), 6):
        braille_char = braille_text[i:i + 6]

        if braille_char == '......':
            english.append(' ')
            is_number = False
        elif braille_char == '.....O':
            is_capital = True
        elif braille_char == '.O.OOO':
            is_number = True
        else:
            if is_number:
                english.append(english_conversion_number[braille_char])
            else:
                letter = english_conversion_alpha[braille_char]
                if is_capital:
                    letter = letter.upper()
                    is_capital = False
                    english.append(letter)
                else:
                    letter = letter.lower()
                    english.append(letter)
    return ''.join(english)

def main():
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        return

    given_string = ' '.join(sys.argv[1:])
    a = detect_language(given_string)
    if a == 'english':
        print(english_to_braille(given_string))
    else:
        print(braille_to_english(given_string))
if __name__ == '__main__':
    main()

