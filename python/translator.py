import sys


def main(input_string):
    # Check the set to see if O and . are the only characters in the input
    if set(input_string) <= set("O."):
        translation_type = "braille_to_english"
    else:
        translation_type = "english_to_braille"

    if translation_type == "braille_to_english":
        result = translate_to_english(input_string)
    else:
        result = translate_to_braille(input_string)

    print(result)


def get_braille_to_english():
    # Define the braille dictionary so I don't have to create two separate dictionaries and can inverse mappings
    braille_to_english = {
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
        "capital follows": ".....O",
        "number follows": ".O.OOO",
        "space": "......",
    }

    return braille_to_english


def translate_to_braille(english_string):

    braille_to_english = get_braille_to_english()

    result = ""
    is_digit = False

    for char in english_string:
        if char.isupper():
            result += braille_to_english["capital follows"]
            char = char.lower()

        if char.isdigit():
            if not is_digit:
                result += braille_to_english["number follows"]
                is_digit = True

            # Map numbers 1-9 to 'a'-'i' and 0 to 'j', special way to use ASCII values
            # so I don't have to create a new dictionary mapping the numbers to braille
            corresponding_letter = chr(ord("a") + int(char) - 1) if char != "0" else "j"
            result += braille_to_english[corresponding_letter]

        elif char == " ":
            result += braille_to_english["space"]
            is_digit = False
        else:
            result += braille_to_english[char]
            is_digit = False

    return result


def translate_to_english(braille_string):
    braille_dict_letters = get_braille_to_english()

    english_to_braille = {v: k for k, v in braille_dict_letters.items()}

    result = ""
    i = 0
    capital_mode = False
    number_mode = False

    while i < len(braille_string):
        current_symbol = braille_string[i : i + 6]

        if current_symbol == braille_dict_letters["capital follows"]:
            capital_mode = True
            i += 6
            continue

        if current_symbol == braille_dict_letters["number follows"]:
            number_mode = True
            i += 6
            continue

        if current_symbol == braille_dict_letters["space"]:
            result += " "
            number_mode = False
            i += 6
            continue

        if number_mode:
            # Convert Braille letter (a-j) to digit (1-9, 0) reverse of the mapping in translate_to_braille
            number_char = english_to_braille[current_symbol]
            digit = str(ord(number_char) - ord("a") + 1) if number_char != "j" else "0"
            result += digit
        else:
            if current_symbol in english_to_braille:
                translated_char = english_to_braille[current_symbol]
                result += translated_char.upper() if capital_mode else translated_char
                capital_mode = False
            else:
                result += "?"  # Handle unexpected Braille symbols for error checking

        i += 6

    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_string = " ".join(sys.argv[1:])
        main(input_string)
    else:
        print(
            "Please provide an input string. Example: python translator.py 'Hello World'"
        )
