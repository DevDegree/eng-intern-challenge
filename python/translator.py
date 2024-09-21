import sys

"""
This file contains a program that translates English text to Braille and vice versa.
"""

# a dictionary that maps english letters to braille
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO'
}

# a dictionary that maps numbers to braille
number_to_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# dictionaries that maps braille to english letters and numbers
braille_to_english = {v: k for k, v in english_to_braille.items()}
braille_to_number = {v: k for k, v in number_to_braille.items()}

# function to check if the input string is in braille
def is_braille(input_str):
    return all(char in 'O.' for char in input_str)

# function to convert braille to english
def convert_braille_to_english(input_str):
    output = []
    capital_follows = False
    number_follows = False

    for i in range(0, len(input_str), 6):
        symbol = input_str[i:i+6]

        if symbol == ".....O":
            capital_follows = True
            continue
        elif symbol == ".O.OOO":
            number_follows = True
            continue

        if symbol == "......":
            output.append(" ")
            number_follows = False
        elif number_follows:
            char = braille_to_number.get(symbol, '')
            output.append(char)
        else:
            char = braille_to_english.get(symbol, '')
            if capital_follows:
                output.append(char.upper())
                capital_follows = False
            else:
                output.append(char)

    return ''.join(output)

# function to convert english to braille
def convert_english_to_braille(input_str):
    output = []
    number_follows = False

    for char in input_str:
        if char.islower():
            output.append(english_to_braille[char])
            number_follows = False
        elif char.isupper():
            output.append(".....O" + english_to_braille[char.lower()])
            number_follows = False
        elif char == ' ':
            output.append("......")
            number_follows = False
        elif char.isdigit():
            if not number_follows:
                output.append(".O.OOO")
                number_follows = True
            output.append(number_to_braille[char])

    return ''.join(output)

def main():
    if len(sys.argv) < 2:
        return

    input_str = ' '.join(sys.argv[1:])
    if is_braille(input_str):
        res = convert_braille_to_english(input_str)
    else:
        res = convert_english_to_braille(input_str)
    print(res)

if __name__ == "__main__":
    main()
