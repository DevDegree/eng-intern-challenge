
'''
Braille Translator: An application that translate Braille to English and English to Braille

How to run:
  python3 translator.py <input>
Examples:
  python3 translator.py "Hello world"


Author: Abdullah Yusuf
'''


import sys

# Braille to english dictionary
braille_dict = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", ".....O": "capital", ".O.OOO": "number", "......": " "
}

# english to Braille dictionary
english_dict = {v: k for k, v in braille_dict.items()}

# Number mappings
char_to_number = {
    "a": '1', "b": '2', "c": '3', "d": '4', "e": '5',
    "f": '6', "g": '7', "h": '8', "i": '9', "j": '0'
}
number_to_char = {v: k for k, v in char_to_number.items()}

#  Braille to English
def braille_to_english(braille_str):
    result = ""
    capitalize = False
    is_number = False

    for i in range(0, len(braille_str), 6):
        braille_char = braille_str[i:i+6]
        if braille_char == ".....O":
            capitalize = True
        elif braille_char == ".O.OOO":
            is_number = True
        elif braille_char in braille_dict:
            letter = braille_dict[braille_char]
            if letter == " ":
                is_number = False
            elif is_number:
                letter = char_to_number[letter]
            elif capitalize:
                letter = letter.upper()
                capitalize = False
            result += letter
        else:
            return f"Invalid input:"

    return result

#  English to Braille
def english_to_braille(english_str):
    result = ""
    is_number = False

    for char in english_str:
        if char == " ":
            is_number = False
            result += english_dict[" "]
        elif char.isdigit():
            if not is_number:
                result += english_dict["number"]
                is_number = True
            result += english_dict[number_to_char[char]]
        elif char.isalpha():
            if char.isupper():
                result += english_dict["capital"]
            result += english_dict[char.lower()]
        else:
            return "Invalid input:"

    return result

# Translate 
def translate(input_str):
    if '.' in input_str:  # Input is Braille
        return braille_to_english(input_str)
    else:  # Input is English
        return english_to_braille(input_str)

# Main function 
def main():
    if len(sys.argv) == 1:  # No input provided
        print("No input was given. Use: python3 translator.py <input>")
        return

    input_str = " ".join(sys.argv[1:])

    # Detect and translate input, then print output
    output_str = translate(input_str)
    print(output_str)

if __name__ == "__main__":
    main()

