import sys

# Define Braille to English mappings
braille_to_english = {
    "O.....": "A", "O.O...": "B", "OO....": "C", "OO.O..": "D", "O..O..": "E", 
    "OOO...": "F", "OOOO..": "G", "O.OO..": "H", ".OO...": "I", ".OOO..": "J", 
    "O...O.": "K", "O.O.O.": "L", "OO..O.": "M", "OO.OO.": "N", "O..OO.": "O", 
    "OOO.O.": "P", "OOOOO.": "Q", "O.OOO.": "R", ".OO.O.": "S", ".OOOO.": "T", 
    "O...OO": "U", "O.O.OO": "V", ".OOO.O": "W", "OO..OO": "X", "OO.OOO": "Y", 
    "O..OOO": "Z", "......": " ", "O.OO.O": "#", ".....O": "1", "....OO": "2",
    "....OOO": "3", "....OO..": "4", "....OO...": "5"  
}

# Create the inverse dictionary for English to Braille
english_to_braille = {v: k for k, v in braille_to_english.items()}

def is_braille(input_string):
    return all(char in "O. " for char in input_string)

def translate_braille_to_english(braille_string):
    output = []
    is_capital = False
    is_number = False

    braille_chars = [braille_string[i:i+6] for i in range(0, len(braille_string), 6)]
    for braille_char in braille_chars:
        if braille_char == "O.....":
            is_capital = True
            continue
        elif braille_char == "O.OO.O":
            is_number = True
            continue

        if braille_char in braille_to_english:
            char = braille_to_english[braille_char]
            if is_capital and char.isalpha():
                char = char.upper()
                is_capital = False
            if is_number and char.isdigit():
                char = char
                is_number = False
            output.append(char)
        else:
            output.append('?')
    return ''.join(output)

def translate_english_to_braille(english_string):
    output = []
    for char in english_string:
        if char.isdigit():
            output.append("O.OO.O")  # Number sign
            output.append(english_to_braille[char])
        elif char.isupper():
            output.append("O.....")  # Capital sign
            output.append(english_to_braille[char.upper()])
        else:
            output.append(english_to_braille[char.lower()])
    return ' '.join(output)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <string to translate>")
        sys.exit(1)

    input_str = ' '.join(sys.argv[1:])
    if is_braille(input_str):
        print(translate_braille_to_english(input_str))
    else:
        print(translate_english_to_braille(input_str))