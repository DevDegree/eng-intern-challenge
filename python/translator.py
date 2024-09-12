import sys
import re

english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......', 'capital': '.....O', 
    'number': '.O.OOO'
}

numbers_to_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..'
}

braille_to_english = dict((v,k) for k,v in english_to_braille.items())
braille_to_numbers = dict((v,k) for k,v in numbers_to_braille.items())

def convert_to_english(braille_str: str) -> str:
    if braille_str == '': return ''

    english_letters = []
    capitalize = False
    number = False

    # Use regex expression to separate the braille text into lengths of 6
    list_of_braille = re.findall('......', braille_str)

    for braille in list_of_braille:
        letter = braille_to_english.get(braille)

        if letter == 'capital':
            capitalize = True
            
        elif letter == 'number':
            number = True
            
        elif letter == ' ':
            number = False
            english_letters.append(letter)

        elif capitalize:
            capitalize = False
            uppercase_letter = chr(ord(letter) - 32) # Use ascii value to find uppercase letter
            english_letters.append(uppercase_letter)

        elif number:
            english_letters.append(braille_to_numbers.get(braille))

        else:
            english_letters.append(letter)
            
    return "".join(english_letters)

def convert_to_braille(english_str: str) -> str:
    if english_str == '': return ''

    braille_letters = []
    number = False

    for letter in english_str:
        if 65 <= ord(letter) <= 90: # Check if this is a capital letter A - Z
            braille_letters.append(english_to_braille.get('capital'))
            lowercase_letter = chr(ord(letter) + 32)
            braille_letters.append(english_to_braille.get(lowercase_letter))
            
        elif 48 <= ord(letter) <= 57: # Check if this is a number 0 - 9
            if number is False: # For numbers we only need the number braille once
                braille_letters.append(english_to_braille.get('number'))
                number = True
            braille_letters.append(numbers_to_braille.get(letter))

        else:
            braille_letters.append(english_to_braille.get(letter))
            if letter == ' ': # We are no longer writing a number after a space
                number = False

    return "".join(braille_letters)

def is_braille(input: str) -> bool:
    # Check if the input only has O or . and the length is a multiple of 6
    if re.fullmatch('[O.]*', input) and len(input) % 6 == 0:
        return True
    return False

def main():
    input = ' '.join(sys.argv[1:])

    if is_braille(input):
        sys.stdout.write(convert_to_english(input))
    else:
        sys.stdout.write(convert_to_braille(input))

if __name__ == "__main__":
    main()