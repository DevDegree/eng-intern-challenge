import sys

# Braille patterns
BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '.....O': 'capital', '.O.OOO': 'number', '......': ' '
}

ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}
ENGLISH_TO_BRAILLE.update({
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
})


def is_braille(text):
    return all(c in 'O.' for c in text) and len(text) % 6 == 0

def english_to_braille(text):
    result = []
    number_mode = False  # Track whether the last character was a digit
    for char in text:
        if char.isupper():
            result.append(ENGLISH_TO_BRAILLE['capital'])  # Capital letter indicator
            result.append(ENGLISH_TO_BRAILLE[char.lower()])
            number_mode = False  # Exiting number mode after a capital letter
        elif char.isdigit():
            if not number_mode:
                result.append(ENGLISH_TO_BRAILLE['number'])  # Number indicator
                number_mode = True
            result.append(ENGLISH_TO_BRAILLE[char])
        else:
            if number_mode and char == ' ':
                # No explicit action needed to exit number mode; just a conceptual switch
                number_mode = False
            elif number_mode:
                # If transitioning from numbers to letters, reset number mode
                number_mode = False
            result.append(ENGLISH_TO_BRAILLE.get(char, '......'))  # Default for unknown characters
    return ''.join(result)

def braille_to_english(braille):
    result = []
    i = 0
    capitalize_next = False
    number_mode = False
    while i < len(braille):
        chunk = braille[i:i+6]
        if chunk == ENGLISH_TO_BRAILLE['capital']:
            capitalize_next = True
        elif chunk == ENGLISH_TO_BRAILLE['number']:
            number_mode = True
        elif chunk in BRAILLE_TO_ENGLISH:
            char = BRAILLE_TO_ENGLISH[chunk]
            if number_mode:
                if char == ' ':
                    number_mode = False
                else:
                    char = str(ord(char) - ord('a') + 1)  # Adjusted to correctly map a-j to 1-10
            if capitalize_next:
                char = char.upper()
                capitalize_next = False
            result.append(char)
        elif chunk == '......':  # Space encountered
            number_mode = False  # Exit number mode when a space is encountered
            result.append(' ')
        i += 6
    return ''.join(result)

def translate(text):
    if is_braille(text):
        return braille_to_english(text)
    else:
        return english_to_braille(text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text_to_translate>")
        sys.exit(1)

    input_text = ' '.join(sys.argv[1:])
    result = translate(input_text)
    print(result, end='')