import sys

# Get command line arguments
input_args = sys.argv[1:]

#
# Mappings
#
braille_to_letter = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
}

braille_to_digit = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
}

letter_to_braille = {
    'a': "O.....",
    'b': "O.O...",
    'c': "OO....",
    'd': "OO.O..",
    'e': "O..O..",
    'f': "OOO...",
    'g': "OOOO..",
    'h': "O.OO..",
    'i': ".OO...",
    'j': ".OOO..",
    'k': "O...O.",
    'l': "O.O.O.",
    'm': "OO..O.",
    'n': "OO.OO.",
    'o': "O..OO.",
    'p': "OOO.O.",
    'q': "OOOOO.",
    'r': "O.OOO.",
    's': ".OO.O.",
    't': ".OOOO.",
    'u': "O...OO",
    'v': "O.O.OO",
    'w': ".OOO.O",
    'x': "OO..OO",
    'y': "OO.OOO",
    'z': "O..OOO",
}

digit_to_braille = {
    '1': "O.....",
    '2': "O.O...",
    '3': "OO....",
    '4': "OO.O..",
    '5': "O..O..",
    '6': "OOO...",
    '7': "OOOO..",
    '8': "O.OO..",
    '9': ".OO...",
    '0': ".OOO..",
}

empty_space = "......"
capital_marker = ".....O"
number_marker = ".O.OOO"

#
# Utility functions
#

def is_valid_braille(braille_str: str) -> bool:
    # Check input uses only 'O' and '.'
    allowed_chars = set(braille_str)
    if allowed_chars != {'O', '.'}:
        return False
    # Ensure length is a multiple of 6
    return len(braille_str) % 6 == 0

def decode_braille(braille_str: str) -> str:
    braille_chunks = [braille_str[i:i+6] for i in range(0, len(braille_str), 6)]
    result = ""
    capital_flag = False
    digit_flag = False

    for braille_char in braille_chunks:
        if braille_char == empty_space:
            result += " "
            digit_flag = False
        elif braille_char == capital_marker:
            capital_flag = True
        elif braille_char == number_marker:
            digit_flag = True
        else:
            if digit_flag:
                result += braille_to_digit.get(braille_char, "")
            else:
                if capital_flag:
                    result += braille_to_letter.get(braille_char, "").upper()
                    capital_flag = False
                else:
                    result += braille_to_letter.get(braille_char, "")
    return result

def encode_english(text: str) -> str:
    encoded_result = ""
    in_digit_mode = False

    for letter in text:
        if letter == " ":
            encoded_result += empty_space
            in_digit_mode = False
        elif letter.isdigit():
            if not in_digit_mode:
                encoded_result += number_marker
                in_digit_mode = True
            encoded_result += digit_to_braille.get(letter, "")
        elif letter.isupper():
            if in_digit_mode:
                encoded_result += empty_space
                in_digit_mode = False
            encoded_result += capital_marker + letter_to_braille.get(letter.lower(), "")
        elif letter.islower():
            if in_digit_mode:
                encoded_result += empty_space
                in_digit_mode = False
            encoded_result += letter_to_braille.get(letter, "")
        else:
            return f"Invalid character encountered: {letter}"
    
    return encoded_result

#
# Main function
#

def run():
    user_input = " ".join(input_args)
    result = ""

    if is_valid_braille(user_input):
        result = decode_braille(user_input)
    else:
        result = encode_english(user_input)

    print(result)

if __name__ == "__main__":
    run()

