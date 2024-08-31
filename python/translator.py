
# translator.py
import sys
from braille_dict import (BRAILLE_LETTERS, BRAILLE_CAPITAL_PREFIX, BRAILLE_NUMBER_PREFIX,
                          BRAILLE_SPACE, BRAILLE_NUMBERS, ENGLISH_LETTERS, ENGLISH_NUMBERS)

def translate_to_braille(text):
    braille = []
    number_mode = False

    for char in text:
        if char.isdigit():
            if not number_mode:
                braille.append(BRAILLE_NUMBER_PREFIX)
                number_mode = True
            braille.append(BRAILLE_NUMBERS[char])
        elif char.isalpha():
            if number_mode:
                number_mode = False
            if char.isupper():
                braille.append(BRAILLE_CAPITAL_PREFIX)
                char = char.lower()
            braille.append(BRAILLE_LETTERS[char])
        elif char == ' ':
            braille.append(BRAILLE_SPACE)
            number_mode = False
        else:
            raise ValueError(f"Unsupported character: {char}")
    
    return ''.join(braille)

def translate_to_english(braille):
    english = []
    i = 0
    length = len(braille)
    capital_mode = False
    number_mode = False

    while i < length:
        symbol = braille[i:i+6]
        i += 6

        if symbol == BRAILLE_CAPITAL_PREFIX:
            capital_mode = True
        elif symbol == BRAILLE_NUMBER_PREFIX:
            number_mode = True
        elif symbol == BRAILLE_SPACE:
            english.append(' ')
            capital_mode = False
            number_mode = False
        else:
            if number_mode:
                english.append(ENGLISH_NUMBERS[symbol])
            else:
                letter = ENGLISH_LETTERS[symbol]
                if capital_mode:
                    letter = letter.upper()
                    capital_mode = False
                english.append(letter)
    
    return ''.join(english)


def detect_mode(text):
    # Check if the text could be Braille (only contains 'O' and '.' and is a multiple of 6 characters)
    if all(c in 'O.' for c in text) and len(text) % 6 == 0:
        return 'braille'
    else:
        return 'english'

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)

    text = ' '.join(sys.argv[1:])
    mode = detect_mode(text)

    if mode == 'english':
        print(translate_to_braille(text))
    elif mode == 'braille':
        print(translate_to_english(text))
    else:
        print("Unsupported mode detected.")
        sys.exit(1)

if __name__ == "__main__":
    main()

