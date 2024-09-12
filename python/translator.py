import sys

# Dictionary to map English letters to Braille
english_to_braille_letters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......'
}

english_to_braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
    '0': '.OOO..'
}

braille_to_english_letters = {v: k for k, v in english_to_braille_letters.items()}

braille_to_english_numbers = {v: k for k, v in english_to_braille_numbers.items()}

SPACE = '......'
CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'

def is_braille(s):
    """Checks if the input string is in valid Braille format."""
    return all(c in 'O.' for c in s) and len(s) % 6 == 0

def english_to_braille_translate(s):
    """Translates English string to Braille."""
    braille = []
    i = 0
    while i < len(s):
        char = s[i]
        if char == ' ' or char.islower(): # if character is a space or a lowercase letter 
            braille.append(english_to_braille_letters[char])
            i += 1
        elif char.isupper(): # if character is a uppercase letter
            braille.append(CAPITAL_FOLLOWS)
            braille.append(english_to_braille_letters[char.lower()])
            i += 1
        elif char.isnumeric(): # if character is a number
            braille.append(NUMBER_FOLLOWS)
            braille.append(english_to_braille_numbers[s[i]])
            while (i + 1 < len(s) and s[i + 1].isnumeric()):
                braille.append(english_to_braille_numbers[s[i + 1]])
                i += 1
            if i + 1 < len(s) and s[i + 1].isalpha():
                braille.append(SPACE)
            i += 1
    return ''.join(braille)

def braille_to_english_translate(s):
    """Translates Braille string to English."""
    english = []
    # Split Braille string into chunks of 6 characters
    braille_chars = [s[i:i + 6] for i in range(0, len(s), 6)]
    i = 0
    while i < len(braille_chars):
        char = braille_chars[i]
        if char == CAPITAL_FOLLOWS:
            english_char = braille_to_english_letters[braille_chars[i + 1]]
            english.append(english_char.upper())
            i += 2
        elif char == NUMBER_FOLLOWS:
            i += 1
            english.append(braille_to_english_numbers[braille_chars[i]])
            while (i + 1 < len(braille_chars) and braille_chars[i + 1] != SPACE):
                english.append(braille_to_english_numbers[braille_chars[i + 1]])
                i += 1
            i += 1
        else:
            english_char = braille_to_english_letters[braille_chars[i]]
            english.append(english_char)
            i += 1
    return ''.join(english)

def translate(input_string):
    """Detects the type of string and translates accordingly."""
    if is_braille(input_string):
        return braille_to_english_translate(input_string)
    else:
        return english_to_braille_translate(input_string)

if __name__ == '__main__':
    # Parse arguments
    if len(sys.argv) > 2:
        input_string = ' '.join(sys.argv[1:])
    else:
        input_string = ''
    
    # Translate input
    output_string = translate(input_string)

    # Send translated string to stdout
    print(output_string)