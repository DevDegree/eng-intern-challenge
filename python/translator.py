import sys


def main(input_string):
    braille_dict = get_braille_dict()

    # Check if the input string is in English or Braille by checking for number of characters in sets
    if set(input_string) <= set("O."):
        print(translate_to_english(input_string, braille_dict))
    else:
        print(translate_to_braille(input_string, braille_dict))


def get_braille_dict():
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
        "capital follows": ".....O",
        "number follows": ".O.OOO",
        "space": "......",
    }

    return braille_dict


def translate_to_braille(english_string, braille_dict):
    result = []
    is_digit = False
    for char in english_string:
        if char.isupper():
            result.append(braille_dict["capital follows"])
            char = char.lower()

        if char.isdigit():
            if not is_digit:
                result.append(braille_dict["number follows"])
                is_digit = True

            # Map numbers to Braille using letters (1-9 -> a-i, 0 -> j) to use the ASCII values and some math
            # to map the digits without using a separate dictionary
            corresponding_letter = chr(ord("a") + int(char) - 1) if char != "0" else "j"
            result.append(braille_dict[corresponding_letter])
        elif char == " ":
            result.append(braille_dict["space"])
            is_digit = False
        else:
            result.append(braille_dict.get(char, "?"))
            is_digit = False
    return "".join(result)


def translate_to_english(braille_string, braille_dict):
    # Reverse the dictionary to get the English character for the Braille representation
    english_dict = {v: k for k, v in braille_dict.items()}
    result = []
    i = 0
    capital_mode = is_digit = False

    while i < len(braille_string):
        symbol = braille_string[i : i + 6]
        if symbol == braille_dict["capital follows"]:
            capital_mode = True
        elif symbol == braille_dict["number follows"]:
            is_digit = True
        elif symbol == braille_dict["space"]:
            result.append(" ")
            is_digit = False
        elif is_digit:
            letter = english_dict.get(symbol, "?")
            digit = str(ord(letter) - ord("a") + 1) if letter != "j" else "0"
            result.append(digit)
        else:
            letter = english_dict.get(symbol, "?")
            result.append(letter.upper() if capital_mode else letter)
            capital_mode = False
        i += 6

    return "".join(result)


# This is the main entry point for the script to execute words to translate
if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_string = " ".join(sys.argv[1:])
        main(input_string)
    else:
        print(
            "Please provide an input string. Example: python translator.py 'Hello World'"
        )

""
