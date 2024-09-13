import sys

# braille to english mapping
ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 
    'c': 'OO....', 'd': 'OO.O..', 
    'e': 'O..O..', 'f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 
    'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 
    'o': 'O..OO.', 'p': 'OOO.O.', 
    'q': 'OOOOO.', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 
    'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', 
    'capital_follows': '.....O', 
    'number_follows': '.O.OOO', 
    ' ': '......'
}

NUMBER_TO_BRAILLE = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}


# reverse mapping from english to braille
BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}
BRAILLE_TO_NUMBER = {v: k for k, v in NUMBER_TO_BRAILLE.items()}

# check if input is braille by looking at characters
def is_braille(text):
    for char in text:
        if char not in "O.":
            return False
    return len(text) % 6 == 0

# convert from braille to english
def braille_to_english(text):
    result = []
    is_number_mode = False
    is_capital_mode = False
    size = 6

    for i in range(0, len(text), size):
        segment = text[i:i + size]

        if segment == ENGLISH_TO_BRAILLE['capital_follows']:
            is_capital_mode = True
            continue
        elif segment == ENGLISH_TO_BRAILLE['number_follows']:
            is_number_mode = True
            continue
        elif segment == ENGLISH_TO_BRAILLE[' ']:
            result.append(' ')
            is_number_mode = False  # Reset number mode after space
            continue

        if is_number_mode:
            char = BRAILLE_TO_NUMBER.get(segment, '?')
        else:
            char = BRAILLE_TO_ENGLISH.get(segment, '?')

        if is_capital_mode:
            char = char.upper()
            is_capital_mode = False

        result.append(char)

    return ''.join(result)

# convert english to braille
def english_to_braille(text):
    result = []
    is_number_mode = False

    for char in text:
        if char.isdigit():
            if not is_number_mode:
                result.append(ENGLISH_TO_BRAILLE['number_follows'])
                is_number_mode = True
            result.append(NUMBER_TO_BRAILLE[char])
            continue

        if char.isupper():
            result.append(ENGLISH_TO_BRAILLE['capital_follows'])
            char = char.lower()

        is_number_mode = False 
        result.append(ENGLISH_TO_BRAILLE.get(char, '......')) 

    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        print("Error: Not sufficient arguments to translate")
        return

    text = ' '.join(sys.argv[1:])

    if is_braille(text):
        print(braille_to_english(text))
    else:
        print(english_to_braille(text))

if __name__ == "__main__":
    main()
