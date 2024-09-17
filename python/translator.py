import sys
from rosetta import (
    alphabet, 
    braille_to_alphabet, 
    numerals, 
    braille_to_numerals, 
    specials, 
    braille_to_specials, 
    capital_follows, 
    number_follows
)

def braille_to_english(text: str) -> str:
    """
    Translates a given Braille text into its English equivalent.
    Since the Braille text "O..OO." maps to two different symbols, "o" and ">", we 
    assume that we must intepret it as the ">" symbol when there is a preceding 
    unpaired "<" symbol, otherwise interpret it as the "o" symbol.

    :param str text: The input Braille text
    :return str: The translated English text
    """ 

    output = ""
    in_number_mode = False
    in_capital_mode = False
    has_unpaired_open_angle_bracket = False

    # Iterate through the text in substrings of length 6 (the length of a Braille symbol)
    for character in [text[i:i + 6] for i in range(0, len(text), 6)]:
        if character == capital_follows:
            in_capital_mode = True
        elif character == number_follows:
            in_number_mode = True
        elif character in braille_to_specials.keys() and not character == "O..OO.":
            in_number_mode = False
            if character == ".OO..O":
                has_unpaired_open_angle_bracket = True
            output += braille_to_specials[character]
        elif in_number_mode:
            output += braille_to_numerals[character]
        else:
            in_number_mode = False
            if character == "O..OO." and has_unpaired_open_angle_bracket:
                has_unpaired_open_angle_bracket = False
                output += ">"
            else:
                alpha = braille_to_alphabet[character]
                if in_capital_mode:
                    in_capital_mode = False
                    alpha = alpha.upper()
                output += alpha

    return output

def english_to_braille(text: str) -> str:
    """
    Translates a given English text into its Braille equivalent.

    :param str text: The input English text
    :return str: The translated Braille text
    """ 

    output = ""
    in_number_mode = False

    for character in text:
        if character.isdigit():
            if not in_number_mode:
                in_number_mode = True
                output += number_follows
            output += numerals[character]
        else:
            in_number_mode = False
            if character in specials.keys():
                output += specials[character]
            else:
                if character.isupper():
                    output += capital_follows
                output += alphabet[character.lower()]

    return output

def is_braille(text: str) -> bool:
    """
    Determines if a given text is Braille text or not.
    Assumes that any text with only "O", ".", or " " must be Braille text, and
    that all Braille text has a length that is a multiple of 6.

    :param str text: The input text
    :return bool: Whether the input text is Braille text or not
    """ 

    for character in text:
        if not character == "O" and not character == "." and not character == " ":
            return False

    return len(text) % 6 == 0

def main() -> None:
    args = sys.argv[1:]
    if not args: return

    text = " ".join(args)
    if is_braille(text):
        print(braille_to_english(text))
    else:
        print(english_to_braille(text))

if __name__ == "__main__":
    main()
