import sys

BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f',
    'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r',
    '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O..OOO': 'z', 
    '......': ' ', '.....O': 'CAPITAL', '.O.OOO': 'NUMBER'
}

ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}
NUMBER_MAP = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 
              'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'}

def is_braille(text):
    return all(char in 'O.' for char in text) and len(text) % 6 == 0

def translate_to_english(braille):
    result = []
    capitalize_next = False
    number_mode = False
    i = 0
    while i < len(braille):
        char = braille[i:i+6]
        if char in BRAILLE_TO_ENGLISH:
            if BRAILLE_TO_ENGLISH[char] == 'CAPITAL':
                capitalize_next = True
            elif BRAILLE_TO_ENGLISH[char] == 'NUMBER':
                number_mode = True
            else:
                letter = BRAILLE_TO_ENGLISH[char]
                if number_mode and letter in NUMBER_MAP:
                    result.append(NUMBER_MAP[letter])
                elif letter.isalpha():
                    if capitalize_next:
                        letter = letter.upper()
                        capitalize_next = False
                    result.append(letter)
                else:
                    result.append(letter)
                    number_mode = False
        i += 6
    return ''.join(result)

def translate_to_braille(text):
    result = []
    number_mode = False
    for char in text:
        if char.isupper():
            result.append(ENGLISH_TO_BRAILLE['CAPITAL'])
            char = char.lower()
        if char.isdigit():
            if not number_mode:
                result.append(ENGLISH_TO_BRAILLE['NUMBER'])
                number_mode = True
            char = next(letter for letter, digit in NUMBER_MAP.items() if digit == char)
        elif char != ' ':
            number_mode = False
        if char.lower() in ENGLISH_TO_BRAILLE:
            result.append(ENGLISH_TO_BRAILLE[char.lower()])
    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        return
    input_text = ' '.join(sys.argv[1:])
    if is_braille(input_text):
        output = translate_to_english(input_text)
    else:
        output = translate_to_braille(input_text)
    print(output, end='')

if __name__ == "__main__":
    main()