import sys

english_to_braille_non_numeric = {
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
    " ": "......",
    "capital_follows": ".....O",
    "number_follows": ".O.OOO",
}

english_to_braille_numeric = {
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
}

braille_to_english_character = {v: k for k, v in english_to_braille_non_numeric.items()}
braille_to_english_number = {v: k for k, v in english_to_braille_numeric.items()}

braille_size = 6


def is_braille(string):
    # check that the string is only '.' or 'O'
    only_braille_characters = (
        string.count(".") + string.count("O") == len(string) and len(string) % 6 == 0
    )
    if not only_braille_characters:
        return False

    # check that we can parse all the braille
    can_parse = True
    for start in range(0, len(input), braille_size):
        chunk = input[start : start + braille_size]
        can_parse = (
            chunk in braille_to_english_character or chunk in braille_to_english_number
        ) and can_parse

    return can_parse


def braille_to_english(input):
    result = []

    flag = None  # can be 'capital_follows' or 'number_follows'
    for start in range(0, len(input), braille_size):
        chunk = input[start : start + braille_size]

        character = None
        if chunk in braille_to_english_character:
            character = braille_to_english_character[chunk]

        curr_char_or_num = ""  # what to add to the result
        if character == "capital_follows" or character == "number_follows":
            flag = character
        else:
            if flag == "capital_follows":
                curr_char_or_num = character.capitalize()
                flag = None
            elif flag == "number_follows" and character != " ":
                curr_char_or_num = braille_to_english_number[chunk]
            else:
                curr_char_or_num = character
                flag = None

            result.append(curr_char_or_num)

    return "".join(result)


def english_to_braille(input):
    result = []
    numeric_flag = False

    for character in input:
        braille_characters = []
        if character.isnumeric():
            if not numeric_flag:
                braille_characters.append(
                    english_to_braille_non_numeric["number_follows"]
                )
            numeric_flag = True
            braille_characters.append(english_to_braille_numeric[character])
        else:
            numeric_flag = False
            if character.isupper():
                braille_characters.append(
                    english_to_braille_non_numeric["capital_follows"]
                )
            braille_characters.append(english_to_braille_non_numeric[character.lower()])
        result += braille_characters

    return "".join(result)


input = " ".join(sys.argv[1:])

result_string = ""
if is_braille(input):
    result_string = braille_to_english(input)
else:
    result_string = english_to_braille(input)

print(result_string)
