import sys


braille_to_english_letters = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd',
    'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h',
    '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p',
    'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.OOOO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O..OOO': 'z'
}
braille_to_english_numbers = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8',
    '.OO...': '9', '.OOO..': '0'
}

# reverse the dictionaries to get the english to braille mappings
english_to_braille_letters = {v: k for k, v in braille_to_english_letters.items()}
english_to_braille_numbers = {v: k for k, v in braille_to_english_numbers.items()}


def isBraille(string):
    # check if the string is a valid braille string
    return all(c in '.O' for c in string)


def brailleToEnglish(string):
    output = []
    number_mode = False
    capital_follows = False

    for i in range(0, len(string), 6):
        braille = string[i:i + 6]

        if braille == '.....O': # Capital follows
            capital_follows = True
            continue
        if braille == '.O.OOO': # Number mode
            number_mode = True
            continue
        if braille == '......': # Space
            number_mode = False
            output.append(' ')
            continue

        if number_mode:
            output.append(braille_to_english_numbers[braille])
        else:
            char = braille_to_english_letters[braille]
            if capital_follows:
                char = char.upper()
                capital_follows = False
            output.append(char)

    return ''.join(output)


def englishToBraille(string):
    output = []
    number_mode = False

    for char in string:
        if char == ' ':
            output.append('......')
            number_mode = False # space ends number mode
            continue

        if char.isupper():
            output.append('.....O') # capital follows symbol
            char = char.lower()
        elif not number_mode and char.isdigit():
            output.append('.O.OOO') # number mode started symbol
            number_mode = True

        if number_mode:
            output.append(english_to_braille_numbers[char])
        else:
            output.append(english_to_braille_letters[char])

    return ''.join(output)


def main():
    input_string = ' '.join(sys.argv[1:])

    if isBraille(input_string):
        output = brailleToEnglish(input_string)
    else:
        output = englishToBraille(input_string)
    
    print(output)


if __name__ == '__main__':
    main()
