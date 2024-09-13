import sys

# dictionary mapping for letters
braille_english_mapping = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z'
}

# dictionary mapping for numbers
braille_number_mapping = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

# reverses everything in dictionary to get english to braille, updates dictionary
braille_english_mapping.update({v: k for k, v in braille_english_mapping.items()})
braille_number_mapping.update({v: k for k, v in braille_number_mapping.items()})

capital_symbol = '.....O'
number_symbol = '.O.OOO'

def is_braille(input_str):
    # checking if all the characters contain 'O' or '.', if not then language is english
    return all(char in 'O.' for char in input_str)

# translate english to braille
def to_braille(input_str):
    result = []
    number_mode = False

    for char in input_str:
        if char.isdigit():
            # if it's the first digit we encounter (haven't printed number follows signifier yet)
            if not number_mode:
                result.append(number_symbol)
                number_mode = True
            result.append(braille_number_mapping[char])
        elif char.isalpha():
            # to go back to non-digits, print a space in braille
            if number_mode:
                result.append('......')
                number_mode = False
            if char.isupper():
                # print special capital signifier
                result.append(capital_symbol)
                result.append(braille_english_mapping[char.lower()])  # convert to lowercase for the mapping
            else:
                result.append(braille_english_mapping[char])
        elif char == ' ':
            # if number_mode:
            #     result.append('......')
            result.append('......')
            number_mode = False  # Exit number mode on space

    return ''.join(result)

# translate braille to english
def to_english(input_str):
    result = []
    i = 0
    number_mode = False
    capital_mode = False

    while i < len(input_str):
        # braille is every 6 inputs
        symbol = input_str[i:i+6]
        if symbol == '......':
            number_mode = False
            result.append(' ')
        elif symbol == capital_symbol:
            capital_mode = True
        elif symbol == number_symbol:
            number_mode = True
        # if we are in number mode, translate as a number
        elif number_mode:
            result.append(braille_number_mapping[symbol])

        # otherwise, translate as a letter
        else:
            char = braille_english_mapping[symbol]
            if capital_mode:
                result.append(char.upper())
                capital_mode = False
            else:
                result.append(char)
        i += 6

    return ''.join(result)

def main():

    input_str = ' '.join(sys.argv[1:])

    if is_braille(input_str):
        print(to_english(input_str))
    else:
        print(to_braille(input_str))

if __name__ == "__main__":
    main()

