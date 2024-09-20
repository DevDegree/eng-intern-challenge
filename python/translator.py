import argparse

braille_dict = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "_": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......",
    "uppercase": ".....O",
    "decimal": ".O...O",
    "number": ".O.OOO"
}


def check_braille(input_string):
    """
    Checks if string is in braille format or not

    input_string (str): input string
    """
    return input_string.count("O") + input_string.count(".") == len(input_string)


def braille_to_english(input_string):
    """
    Translates Braille string to English

    input_string (str): input string in English to be translated
    """

    braille_symbols = [input_string[i:i+6] for i in range(0, len(input_string), 6)]
    output_string = ""

    uppercase_letter = False
    number = False

    for symbol in braille_symbols:
        if symbol == braille_dict['uppercase']:
            uppercase_letter = True
        elif symbol == braille_dict['number']:
            number = True
        elif symbol in braille_dict.values():
            char_match = [letter for letter, value in braille_dict.items() if value == symbol]
            character = str()
            if number:
                if len(char_match) == 2:
                    character = char_match[1]  # Make sure the symbol after the number is valid
                else:
                    character = char_match[0]  # Use a letter if no valid number symbol found
            else:
                character = char_match[0]

            if uppercase_letter:
                character = character.upper()
                uppercase_letter = False

            if character == " ":
                number = False

            output_string += character
        else:
            raise ValueError(f"The symbol {symbol} does not exist in Braille")

    return output_string


def english_to_braille(input_string):
    """
    Translates English string to Braille

    input_string (str): input string in Braille to be translated
    """

    output_string = ""
    number = False
    for character in input_string:
        if character.isupper():
            output_string += braille_dict['uppercase']
            character = character.lower()

        if character.isnumeric():
            if not number:
                output_string += braille_dict['number']
                number = True
        elif character == " ":  # prevents an additional space being added after a number
            if number:
                number = False
        elif character.isalpha():
            if number:
                output_string += braille_dict[' ']  # add space between number and next letter
                number = False

        if character in braille_dict:
            output_string += braille_dict[character]
        else:
            raise KeyError(f"The character {character} does not exist in braille")

    return output_string


def main():
    parser = argparse.ArgumentParser(description="Convert between Braille and English.")
    parser.add_argument("text", nargs="+", help="The input text to convert (Braille or English).")

    # Parse command-line arguments
    args = parser.parse_args()

    # If no argument is provided, prompt the user for input
    if not args.text:
        input_text = input("Please enter text to convert (Braille or English): ")
    else:
        input_text = " ".join(args.text)
        
    # Detect whether input is in Braille or English
    if check_braille(input_text):
        output = braille_to_english(input_text)
        print(output)
    else:
        output = english_to_braille(input_text)
        print(output)


if __name__ == "__main__":
    main()
