import sys

# Braille mappings
BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ',
    '.....O': 'capital follows', '.O.OOO': 'number follows'
}

ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}
NUMBERS = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
           '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'}
CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'
SPACE = '......'


def braille_to_english(braille):
    result = []
    i = 0
    capitalize_next = False
    number_mode = False

    while i < len(braille):
        char = braille[i:i+6]
        if char == CAPITAL_FOLLOWS:
            capitalize_next = True
        elif char == NUMBER_FOLLOWS:
            number_mode = True
        elif char in BRAILLE_TO_ENGLISH:
            if number_mode:
                if char == SPACE:
                    result.append(' ')
                    number_mode = False
                else:
                    for num, letter in NUMBERS.items():
                        if BRAILLE_TO_ENGLISH[char] == letter:
                            result.append(num)
                            break
            else:
                letter = BRAILLE_TO_ENGLISH[char]
                if capitalize_next and letter != ' ':
                    letter = letter.upper()
                    capitalize_next = False
                result.append(letter)
        i += 6

    return ''.join(result)


def english_to_braille(text):
    result = []
    number_mode = False

    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(ENGLISH_TO_BRAILLE['number follows'])
                number_mode = True
            result.append(ENGLISH_TO_BRAILLE[NUMBERS[char]])
        else:
            if number_mode and char != ' ':
                number_mode = False
            if char.isupper():
                result.append(ENGLISH_TO_BRAILLE['capital follows'])
                result.append(ENGLISH_TO_BRAILLE[char.lower()])
            else:
                result.append(ENGLISH_TO_BRAILLE[char.lower()])
            if char == ' ':
                number_mode = False

    return ''.join(result)


def translate(input_string):
    if all(c in 'O.' for c in input_string):
        return braille_to_english(input_string)
    else:
        return english_to_braille(input_string)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
    else:
        input_string = ' '.join(sys.argv[1:])
        print(translate(input_string))
