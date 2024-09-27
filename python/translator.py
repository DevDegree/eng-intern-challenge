# Initializing maps for english to braille and braille to english
BRAILLE_DICT = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', '0': '.O.OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....',
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

ENGLISH_DICT = {v: k for k, v in BRAILLE_DICT.items()}


# Initializing Markers 
CAPITAL_MARKER = '.....O'
NUMBER_MARKER = '.O.OOO'
SPACE_MARKER = '......'


# Function to convert from english text to braille
def english_to_braille(phrase):
    result = ""
    first_num = False


    for char in phrase:
        if char.isdigit():
            if not first_num:
                result+=NUMBER_MARKER
                first_num = True
            result+=BRAILLE_DICT[char]

        elif char == ' ':
            result+=SPACE_MARKER
            first_num = False

        elif char.isupper():
            result+=CAPITAL_MARKER
            result+=BRAILLE_DICT[char.lower()]
            first_num = False

        else:
            result+=BRAILLE_DICT[char]
            first_num = False

    return result

# Function to convert from braille to english 
def braille_to_english(phrase):
    result = ""
    first_num = False
    CAPITAL = False
    phrase = [phrase[i:i+6] for i in range(0, len(phrase), 6)]

    for symbol in phrase:
        if symbol == CAPITAL_MARKER:
            CAPITAL = True

        elif symbol == NUMBER_MARKER:
            first_num = True

        elif symbol == SPACE_MARKER:
            result+= ' '
            first_num = False

        else:
            char = ENGLISH_DICT[symbol]
            if first_num and char.isdigit():
                result+=char
            elif char.isdigit():
                if CAPITAL:
                    result+=chr(int(char) + 96).upper()
                    CAPITAL = False
                else:
                    result+=chr(int(char) + 96)
            else:
                result+=char


    return result


#Getting command line args
if __name__ == '__main__':
    import sys
    phrase = ' '.join(sys.argv[1:])

    # Check whether it is braille, and use that to decide which function to call
    print(braille_to_english(phrase) if all(i in 'O.' for i in phrase) else english_to_braille(phrase))