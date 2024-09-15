import sys

# Braille to English mapping
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f", "OOOO..": "g",
    "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n",
    "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u",
    "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z",
    ".....O": "capital_follows", 
    ".O.OOO": "number_follows", 
    "......": "space",
}

# English to Braille mapping
english_to_braille = {v: k for k, v in braille_to_english.items() if v.islower()}

# Helper functions for numbers
def letter_to_number(letter):
    number_mapping = {
        'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
        'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
    }
    return number_mapping.get(letter, '')

def number_to_letter(number):
    letter_mapping = {
        '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
        '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'
    }
    return letter_mapping.get(number, '')

def translate_to_english(braille_string):
    result = []
    is_capital = False
    is_number = False

    for i in range(0, len(braille_string), 6):
        symbol = braille_string[i:i+6]

        if symbol == ".....O":
            is_capital = True
        elif symbol == ".O.OOO":
            is_number = True
        elif symbol == "......":
            result.append(' ')
            is_number = False
        else:
            char = braille_to_english.get(symbol, "")

            if is_number:
                char = letter_to_number(char)
                result.append(char)
              
            elif is_capital:
                result.append(char.upper())
                is_capital = False
            else:
                result.append(char)
    
    return ''.join(result)

def translate_to_braille(english_string):
    result = []
    in_number_sequence = False
    
    for char in english_string:
        if char.isdigit():
            if not in_number_sequence:
                result.append(".O.OOO")
                in_number_sequence = True
            char = number_to_letter(char)
        else:
            in_number_sequence = False

        if char.isupper():
            result.append(".....O")
            char = char.lower()

        braille_char = english_to_braille.get(char, "")
        if braille_char:
            result.append(braille_char)
        elif char == ' ':
            result.append("......")
    
    return ''.join(result)

if __name__ == "__main__":
    input_string = ' '.join(sys.argv[1:])

    # Check if input is Braille
    if all(c in "O." for c in input_string) and len(input_string) % 6 == 0:
        print(translate_to_english(input_string))
    else:
        print(translate_to_braille(input_string))

