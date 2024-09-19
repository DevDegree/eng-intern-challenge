

#!/usr/bin/env python3
# Braille mappings for alphabets and numbers
BRAILLE_ALPHABET = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OOO...', 'e': 'O..O..', 'f': 'O.OO..', 'g': 'OOOO..',
    'h': 'O..OO.', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......', ',': '..O...'
}

BRAILLE_NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

CAPITAL_INDICATOR = '.....O'
NUMBER_INDICATOR = '.O.OOO'  # Correctly updated "numbers follows" indicator

def english_to_braille(text):
    result = ''
    is_number_context = False
    for char in text:
        if char.isdigit():
            if not is_number_context:
                result += NUMBER_INDICATOR  # Indicate the start of a number sequence
                is_number_context = True
            result += BRAILLE_NUMBERS[char]
        else:
            is_number_context = False
            if char == ' ':
                result += BRAILLE_ALPHABET[char]
            elif char.isupper():
                result += CAPITAL_INDICATOR + BRAILLE_ALPHABET[char.lower()]
            else:
                result += BRAILLE_ALPHABET[char]
    return result
#hardest part was figuring out edge case for a capital letter following a lower case letter (xYz)
def braille_to_english(braille):
    result = ''
    i = 0
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == CAPITAL_INDICATOR:
            i += 6
            # Ensure there are enough characters left to process the capital letter
            if i + 6 <= len(braille):
                next_symbol = braille[i:i+6]
                char = [k for k, v in BRAILLE_ALPHABET.items() if v == next_symbol]
                if char:
                    result += char[0].upper()
            i += 6  # Move past the current symbol after processing
        elif symbol == NUMBER_INDICATOR:
            i += 6
            while i < len(braille) and braille[i:i+6] != '......':
                char = [k for k, v in BRAILLE_NUMBERS.items() if v == braille[i:i+6]]
                if char:
                    result += char[0]
                i += 6
            continue
        else:
            char = [k for k, v in BRAILLE_ALPHABET.items() if v == symbol]
            if char:
                result += char[0]
            i += 6  # Move past the current symbol

    return result.strip()

def translate(input_text):
    if all(c in '.O' for c in input_text):  # Check if the input is in Braille
        return braille_to_english(input_text)
    else:
        return english_to_braille(input_text)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])
        print(translate(input_text))
    else:
        print("Please provide the text to translate as an argument.")

