import sys

# Dictionary for braille translation
BRAILLE_DICT = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', '0': '.O.OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....',
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

# Invert Braile dictionary for English translation
ENG_DICT = {}
for key, value in BRAILLE_DICT.items():
    ENG_DICT[value] = key

# Markers for capitals, numbers, and spaces
CAPITAL_MARKER = '.....O'
NUMBER_MARKER = '.O.OOO'
SPACE_MARKER = '......'

# Check if the phrase is in braille
def check_if_braille(text):
    for char in text:
        if char != '.' and char != 'O':
            return False
    return True

# Translate English to Braille
def eng_to_braille(text):
    # Split into individual words
    words = text.split()
    braille = ""

    for word in words:
        for char in word:
            if char.isupper():
                braille += CAPITAL_MARKER
                char = char.lower()
            elif char.isdigit():
                braille += NUMBER_MARKER
            braille += BRAILLE_DICT[char]

        # Add space marker if not the last word    
        if (word != words[-1]):
            braille += SPACE_MARKER
    return braille

# Translate Braille to English
def braille_to_eng(text):
    english = ""
    sequence = ""
    is_number = False
    is_capital = False

    for char in text:
        sequence += char

        # Once sequence reaches six characters, translate
        if (len(sequence) == 6):
            if (sequence == NUMBER_MARKER):
                is_number = True
            elif (sequence == CAPITAL_MARKER):
                is_capital = True
            elif (sequence == SPACE_MARKER):
                english += " "
                is_number = False
                is_capital = False
            else:
                if (is_number):
                    english += ENG_DICT[sequence]
                elif (is_capital):
                    is_capital = False
                    if (ENG_DICT[sequence].isdigit()):
                        # Convert the number to uppercase letter
                        english += chr(ord(ENG_DICT[sequence]) - ord('0') + ord('a') - 1).upper()
                    else:
                        # Otherwise, just convert to uppercase
                        english += ENG_DICT[sequence].upper()
                else:
                    if (ENG_DICT[sequence].isdigit()):
                        # Convert the number to lowercase letter
                        english += chr(ord(ENG_DICT[sequence]) - ord('0') + ord('a') - 1)
                    else:
                        # Otherwise, just convert to lowercase
                        english += ENG_DICT[sequence]

            # Reset sequence
            sequence = ""
    return english

if  __name__ == '__main__':
    import sys
    input_text = ' '.join(sys.argv[1:])

    if (check_if_braille(input_text)):
        print(braille_to_eng(input_text))
    else:
        print(eng_to_braille(input_text))
