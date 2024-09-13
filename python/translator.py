import sys

# helper constants for mapping english letters to braille and vice versa
BRAILLE_MAP = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..', 'capital': '.....O', 'number': '.O.OOO', 'space': '......',
    '.': '.O..OO', ',': '.O....', '?': '.OO.O.', '!': '.O.OO.', ':': '.OOO..',
    ';': '.O.O..', '-': '....OO', '/': '..O.O.', '<': '..OO..', '>': '..OO.O',
    '(': '...OOO', ')': '...OOO',
}

REVERSE_BRAILLE_MAP = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '.O..OO': '.', '.O....': ',', '.OO.O.': '?', '.O.OO.': '!',
    '.OOO..': ':', '.O.O..': ';', '....OO': '-', '..O.O.': '/', '..OO..': '<',
    '..OO.O': '>', '...OOO': '('
}

BRAILLE_TO_NUMBER = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

def detect_language(input_string):
    if all(c in 'O. ' for c in input_string.strip()):
        return "braille"
    else:
        return "english"
    
def translate_to_braille(input_string):
    result = []
    is_number = False

    for c in input_string:
        if not c.isdigit():
            is_number = False

        if c == " ":
            result.append(BRAILLE_MAP['space'])
            continue

        if c.isupper():
            result.append(BRAILLE_MAP['capital'])
            c = c.lower()
        elif c.isdigit() and not is_number:
            result.append(BRAILLE_MAP['number'])
            is_number = True

        if c in BRAILLE_MAP:
            result.append(BRAILLE_MAP[c])
        else:
            raise ValueError(f"Unsupported character '{c}' found in input")
        
    return "".join(result)

def translate_to_english(input_string):
    if len(input_string) % 6 != 0:
        raise ValueError(f"Braille input length {len(input_string)} is invalid.")
    
    words = [input_string[i:i+6] for i in range(0, len(input_string), 6)]

    result = []
    is_capital = False
    is_number = False

    for word in words:
        if word == BRAILLE_MAP['capital']:
            is_capital = True
            continue

        if word == BRAILLE_MAP['number']:
            is_number = True
            continue

        if word == BRAILLE_MAP['space']:
            result.append(' ')
            is_number = False # reset assuming previous symbol is a number
            continue

        if word in REVERSE_BRAILLE_MAP:
            if is_number and word in BRAILLE_TO_NUMBER:
                c = BRAILLE_TO_NUMBER[word]
            else:
                c = REVERSE_BRAILLE_MAP[word]

            if is_capital:
                c = c.upper()
                is_capital = False

            result.append(c)
        else:
            raise ValueError(f"Braille pattern '{word}' not recognized.")
    
    return "".join(result)


def translate(input_string):
    if not input_string.strip():
        raise ValueError("Input cannot be empty")
    
    language = detect_language(input_string)

    translated_output = ""

    if language == "english":
        translated_output = translate_to_braille(input_string)
    else:
        translated_output = translate_to_english(input_string)

    return translated_output

def main():
    input_args = sys.argv[1:]
    input_string = ' '.join(input_args)

    try:
       result = translate(input_string)
       print(result)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()