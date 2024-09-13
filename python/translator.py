import sys


def main(input_string):
    # Check the set to see if O and . are the only characters in the input
    if set(input_string) <= set("O."):
        translation_type = "braille_to_english"
    else:
        translation_type = "english_to_braille"

    if translation_type == "braille_to_english":
        # result = translate_to_english(input_string)
        result = ""
    else:
        result = translate_to_braille(input_string)

    print(result)


def translate_to_braille(english_string):
    braille_dict_letters = {
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

    result = ""
    is_digit = False

    for char in english_string:
        if char.isupper():
            result += braille_dict_letters["capital follows"]
            char = char.lower()

        if char.isdigit():
            if not is_digit:
                result += braille_dict_letters["number follows"]
                is_digit = True

            # Map numbers 1-9 to 'a'-'i' and 0 to 'j', special way to use ASCII values
            # so I don't have to create a new dictionary mapping the numbers to braille
            corresponding_letter = chr(ord("a") + int(char) - 1) if char != "0" else "j"
            result += braille_dict_letters[corresponding_letter]

        elif char == " ":
            result += braille_dict_letters["space"]
            is_digit = False
        else:
            result += braille_dict_letters[char]
            is_digit = False

    return result


# 3. Function: translate_to_english(braille_string)
#    Initialize braille_dict with Braille to English mappings = {}
#    result = ""
#    i = 0
#    capital_mode = False
#    number_mode = False

# Loop to substring braille_string in chunks of 6

#    While i < length of braille_string:
#       current_symbol = braille_string[i:i+6]

#     Follow logical order of checking for capital, number, space, and then the character itself

#       If current_symbol == braille_dict["capital follows"]:
#          capital_mode = True
#          i += 6
#          continue

#       If current_symbol == braille_dict["number follows"]:
#          number_mode = True
#          i += 6
#          continue

#       If current_symbol == braille_dict["space"]:
#          result += " "
#          number_mode = False
#          i += 6
#          continue

#       If capital_mode:
#          result += braille_dict[current_symbol].upper()
#          capital_mode = False
#       Else If number_mode:
#          result += braille_dict[current_symbol]  # Assuming it's a number
#       Else:
#          result += braille_dict[current_symbol]

#       i += 6

#    Return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_string = " ".join(sys.argv[1:])
        main(input_string)
    else:
        print(
            "Please provide an input string. Example: python translator.py 'Hello World'"
        )
