import argparse

# Dictionary mapping Braille characters to English
braille_dict = {
    "CHARS": {
        "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f",
        "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
        "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
        ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
        "OO.OOO": "y",  "O..OOO": "z"
    },
    "NUMS": {
        ".OOOOO": "0", "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
        "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9"
    },
    "SIGNS": {
        "......": " ", "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
        "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O..OO.": ">", "O.O..O": "(",
        ".O.OO.": ")", 
        ".....O": "^", 
        ".O...O": "%",  
        ".O.OOO": "#" 
    }
}

# Create reverse mapping for converting English to Braille
english_to_braille_map = {
    "CHARS": {v: k for k, v in braille_dict["CHARS"].items()},
    "NUMS": {v: k for k, v in braille_dict["NUMS"].items()},
    "SIGNS": {v: k for k, v in braille_dict["SIGNS"].items()}
}

def is_braille_input(text):
    """
    Check if input is Braille based on format and length.
    """
    return len(text) % 6 == 0 and all(text[i:i+6] in braille_dict["CHARS"] or
                                       text[i:i+6] in braille_dict["NUMS"] or
                                       text[i:i+6] in braille_dict["SIGNS"]
                                       for i in range(0, len(text), 6))

def braille_to_english(braille_code):
    """
    Convert Braille code to English text.
    """
    english_text = ""
    uppercase = False
    in_number_mode = False

    for i in range(0, len(braille_code), 6):
        symbol = braille_code[i:i+6]

        if symbol == english_to_braille_map["SIGNS"]["^"]:
            uppercase = True
            continue
        elif symbol == english_to_braille_map["SIGNS"]["#"]:
            in_number_mode = True
            continue

        if in_number_mode and symbol in braille_dict["NUMS"]:
            english_text += braille_dict["NUMS"][symbol]
        elif uppercase and symbol in braille_dict["CHARS"]:
            english_text += braille_dict["CHARS"][symbol].upper()
            uppercase = False
        elif symbol in braille_dict["CHARS"]:
            english_text += braille_dict["CHARS"][symbol]
        elif symbol == english_to_braille_map["SIGNS"][" "]:
            english_text += " "
            in_number_mode = False
        else:
            english_text += braille_dict["SIGNS"].get(symbol, '')

    return english_text

def english_to_braille(text_list):
    """
    Convert a list of English text strings to Braille.
    """
    braille_result = ""
    number_mode = False

    for text in text_list:
        for char in text:
            if char.isdigit() and not number_mode:
                braille_result += english_to_braille_map["SIGNS"]['#']
                number_mode = True

            if char.isdigit():
                braille_result += english_to_braille_map["NUMS"][char]
            elif char == ' ':
                braille_result += english_to_braille_map["SIGNS"][' ']
                number_mode = False
            elif char.isalpha():
                if char.isupper():
                    braille_result += english_to_braille_map["SIGNS"]['^']
                braille_result += english_to_braille_map["CHARS"][char.lower()]
            else:
                braille_result += english_to_braille_map["SIGNS"].get(char, '')

    return braille_result



def main():
    # Set up argument parsing for multiple inputs
    arg_parser = argparse.ArgumentParser(description="Convert between English text and Braille")
    arg_parser.add_argument('inputs', nargs='+', help='Provide one or more inputs')
    parsed_args = arg_parser.parse_args().inputs
    combined_input = "".join(parsed_args)
    braille_check = is_braille_input(combined_input)

    if braille_check:
        output = braille_to_english(combined_input)
    else:
        output = english_to_braille(parsed_args)
    
    print(output)

if __name__ == "__main__":
    main()
