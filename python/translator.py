import sys
# Constants
BRAILLE_TO_LETTER = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y','O..OOO': 'z',
    ' ': '......'
}

BRAILLE_TO_NUMBER = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3',
    'OO.O..': '4', 'O..O..': '5', 'OOO...': '6',
    'OOOO..': '7', 'O.OO..': '8', '.OO...': '9',
    '.OOO..': '0'
}

LETTER_TO_BRAILLE = {letter: braille for braille, letter in BRAILLE_TO_LETTER.items()}
NUMBER_TO_BRAILLE = {letter: braille for braille, letter in BRAILLE_TO_NUMBER.items()}

NUMBER_INDICATOR = '.O.OOO'
CAPITAL_INDICATOR = '.....O'
SPACE_INDICATOR =  '......'

def main():
    input = " ".join(sys.argv[1:])
    if all(character in ['.', 'O'] for character in input):
        print(braille_to_text(input))
    else:
        print(text_to_braille(input))

def braille_to_text(braille):
    is_capital = False
    is_number = False
    length = len(braille) - 6
    i = 0
    answer = ""
    special_values = [NUMBER_INDICATOR, CAPITAL_INDICATOR, SPACE_INDICATOR]
    while i <= length:
        sequence = braille[i:i+6]
        if sequence in special_values:
            if sequence == NUMBER_INDICATOR:
                is_number = True
            elif sequence == CAPITAL_INDICATOR:
                is_capital = True
            else: # it's a space.
                if is_number:
                    is_number = False
                answer += " "
        else:
            if is_capital:
                answer += BRAILLE_TO_LETTER[sequence].upper()
                is_capital = False
            elif is_number:
                answer += BRAILLE_TO_NUMBER[sequence]
            else:
                answer += BRAILLE_TO_LETTER[sequence]
        i += 6
    return answer


def text_to_braille(text):
    answer = ""
    is_number = False
    digits = [str(digit) for digit in range(1, 10)]
    for character in text:
        # Check if letter is capitalized.
        if character == " ":
            answer += SPACE_INDICATOR
            is_number = False
        elif is_number:
            answer += NUMBER_TO_BRAILLE[character]
        elif character.isupper():
            answer += (CAPITAL_INDICATOR + LETTER_TO_BRAILLE[character.lower()])
        elif character in digits:
            is_number = True
            answer += (NUMBER_INDICATOR + NUMBER_TO_BRAILLE[character])
        else:
            answer += LETTER_TO_BRAILLE[character]
    return answer


if __name__ == "__main__":
    main()
