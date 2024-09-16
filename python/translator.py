import sys

english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 'cap': '.....O', 'num': '.O.OOO',
}

# Numbers are represented by the letters 'a' to 'j' preceded by the number sign
numbers_map = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
               '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'}

# Update the mapping for numbers
for digit, letter in numbers_map.items():
    english_to_braille[digit] = english_to_braille[letter]

# Reverse mapping from Braille to English
braille_to_english = {v: k for k, v in english_to_braille.items()}
braille_to_english[english_to_braille['cap']] = 'cap'
braille_to_english[english_to_braille['num']] = 'num'

def is_braille(input_string):
    """
    Determine if the input string is Braille.
    """
    input_string = input_string.strip()
    input_string_no_spaces = input_string.replace(' ', '')
    return all(c in ('O', '.') for c in input_string_no_spaces)

def translate_braille_to_english(input_string):
    """
    Translate Braille to English.
    """
    # Remove spaces and split into cells of 6 characters
    braille_cells = input_string.replace(' ', '')
    cells = [braille_cells[i:i+6] for i in range(0, len(braille_cells), 6)]
    output = ''
    capital_flag = False
    number_flag = False

    for cell in cells:
        if cell == english_to_braille['cap']:
            capital_flag = True
            continue
        elif cell == english_to_braille['num']:
            number_flag = True
            continue
        elif cell == english_to_braille[' ']:
            output += ' '
            number_flag = False  # Reset number flag after space
            continue
        else:
            char = braille_to_english.get(cell, '')
            if not char:
                continue  # Skip invalid Braille cells
            if char == 'cap':
                capital_flag = True
                continue
            if char == 'num':
                number_flag = True
                continue
            if number_flag:
                # Map letters 'a'-'j' to digits '1'-'0'
                for digit, letter in numbers_map.items():
                    if letter == char:
                        output += digit
                        break
            else:
                if capital_flag:
                    output += char.upper()
                    capital_flag = False
                else:
                    output += char
    return output

def translate_english_to_braille(input_string):
    """
    Translate English to Braille.
    """
    output = ''
    number_flag = False
    for char in input_string:
        if char == ' ':
            output += english_to_braille[' ']
            number_flag = False  # Reset number flag after space
        elif char.isupper():
            output += english_to_braille['cap']
            output += english_to_braille[char.lower()]
            number_flag = False
        elif char.isdigit():
            if not number_flag:
                output += english_to_braille['num']
                number_flag = True
            output += english_to_braille[char]
        else:
            output += english_to_braille.get(char, '')
            number_flag = False
    return output

def main():
    if len(sys.argv) < 2:
        print("Please provide input text.")
        sys.exit(1)
    input_string = ' '.join(sys.argv[1:])
    if is_braille(input_string):
        output = translate_braille_to_english(input_string)
    else:
        output = translate_english_to_braille(input_string)
    print(output)

if __name__ == '__main__':
    main()