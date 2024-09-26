import sys

char_to_braille_mapping = {"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
                           "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
                           "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
                           "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
                           "y": "OO.OOO", "z": "O..OOO", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
                           "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
                           ".": "..OO.O", ",": ".O....", "?": "..O.OO", "!": "..OOO.", ":": "..OO..", ";": "..O.O.",
                           "-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO.",
                           " ": "......", "capital_follows": ".....O", "decimal_follows": ".O...O",
                           "number_follows": ".O.OOO", }
braille_to_char_mapping = {v: k for k, v in char_to_braille_mapping.items()}


def get_braille_char(character):
    braille_char = ""
    if 'A' <= character <= 'Z':
        braille_char += char_to_braille_mapping["capital_follows"]
        character = character.lower()
    if character in char_to_braille_mapping:
        braille_char += char_to_braille_mapping[character]
    return braille_char


def get_braille(user_input):
    res = ""
    is_number = False
    for index, char in enumerate(user_input):
        if not is_number and ('0' <= char <= '9'):
            res += char_to_braille_mapping["number_follows"]
            is_number = True
        elif is_number and char == '.':
            res += char_to_braille_mapping["decimal_follows"]
            continue
        # This takes care of the case when we start the number with a dot for example: .34
        elif not is_number and index < len(user_input) - 1 and ('0' <= user_input[index + 1] <= '9') and char == '.':
            res += char_to_braille_mapping["number_follows"] + char_to_braille_mapping["decimal_follows"]
            is_number = True
            continue
        elif is_number and not ('0' <= char <= '9'):
            is_number = False
        res += get_braille_char(char)
    return res


def get_string(user_input):
    braille_blocks = [user_input[i:i + 6] for i in range(0, len(user_input), 6)]
    res = ""
    is_number = False
    is_capital = False
    for block in braille_blocks:
        if block not in braille_to_char_mapping:
            return ""
        current_character = braille_to_char_mapping[block]
        if current_character == "number_follows":
            is_number = True
            continue
        elif current_character == "decimal_follows":
            current_character = '.'
        elif current_character == "capital_follows":
            is_capital = True
            continue
        elif current_character == " ":
            is_number = False
        # Numbers and some characters share braille symbols, so we need to check if we are currently reading a number
        # In the case where it is not, we transform the current character which will be in number form and transform it
        # to characters via their ASCII values
        elif ('0' <= current_character <= '9') and not is_number:
            if current_character == '0':
                current_character = 'j'
            else:
                current_character = chr(ord(current_character) + 48)
        # The bigger than sign ">" and the letter "o" have the same braille representation. I made the assumption that
        # the bigger than sign can only be used on a number.
        elif current_character == '>' and not is_number:
            current_character = 'o'
        if is_capital:
            current_character = current_character.upper()
            is_capital = False
        res += current_character
    return res


def transform_input(user_input):
    characters = set(user_input)
    output = ""
    if len(characters) == 2 and '.' in characters and 'O' in characters and len(user_input) % 6 == 0:
        output = get_string(user_input)
    # The output will be empty if it is not in braille form or if there is a wrong braille input given. In that case,
    # we assume the user inputer a string that needs to be transformed to braille.
    if output == "":
        output = get_braille(user_input)
    return output


if __name__ == '__main__':
    print(transform_input(' '.join(sys.argv[1:])))
