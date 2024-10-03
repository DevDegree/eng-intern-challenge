import sys

# Braille mappings
# Dictionary mapping Braille patterns to English letters and special symbols
braille_to_eng = {
    'O.....': 'A', 'O.O...': 'B', 'OO....': 'C', 'OO.O..': 'D', 'O..O..': 'E',
    'OOO...': 'F', 'OOOO..': 'G', 'O.OO..': 'H', '.OO...': 'I', '.OOO..': 'J',
    'O...O.': 'K', 'O.O.O.': 'L', 'OO..O.': 'M', 'OO.OO.': 'N', 'O..OO.': 'O',
    'OOO.O.': 'P', 'OOOOO.': 'Q', 'O.OOO.': 'R', '.OO.O.': 'S', '.OOOO.': 'T',
    'O...OO': 'U', 'O.O.OO': 'V', '.OOO.O': 'W', 'OO..OO': 'X', 'OO.OOO': 'Y',
    'O..OOO': 'Z', '......': ' ',
    '.....O': 'CAPITAL', '.O.OOO': 'NUMBER'
}

# Reverse mapping: English to Braille
eng_to_braille = {v: k for k, v in braille_to_eng.items()}

# Mapping for numbers in Braille (uses the same patterns as A-J)
numbers = {
    'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5',
    'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '0'
}

def braille_to_text(braille):
    """
    Converts Braille string to English text.
    Handles capitalization and number mode.
    """
    result = []
    i = 0
    capital_next = False
    number_mode = False

    while i < len(braille):
        char = braille[i:i+6]
        if char == '.....O':  # Indicates Capital
            capital_next = True
        elif char == '.O.OOO':  # Indicates Number
            number_mode = True
        elif char in braille_to_eng:
            letter = braille_to_eng[char]
            if number_mode and letter in numbers:
                result.append(numbers[letter])
            else:
                if capital_next:
                    letter = letter.upper()
                    capital_next = False
                result.append(letter)
                number_mode = False
        i += 6

    return ''.join(result)

def text_to_braille(text):
    """
    Converting English text to Braille.
    Handling capitalization and numbers.
    """
    result = []
    number_mode = False

    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(eng_to_braille['NUMBER'])
                number_mode = True
            result.append(eng_to_braille[list(numbers.keys())[list(numbers.values()).index(char)]])
        else:
            if number_mode:
                number_mode = False
            if char.isupper():
                result.append(eng_to_braille['CAPITAL'])
                result.append(eng_to_braille[char.upper()])
            else:
                result.append(eng_to_braille[char.upper()])

    return ''.join(result)

def is_braille(input_string):
    """
    Check if Braille input string is valid .
    Braille should only contain '.' and 'O' and have a length multiple of 6.
    """
    return all(c in '.O' for c in input_string) and len(input_string) % 6 == 0

if __name__ == "__main__":
    # Prompt user for input
    print("Enter a string to translate (Braille or English):")
    input_string = input().strip()

    # Determine if input is Braille or English and translate accordingly
    if is_braille(input_string):
        print(braille_to_text(input_string))
    else:
        print(text_to_braille(input_string))