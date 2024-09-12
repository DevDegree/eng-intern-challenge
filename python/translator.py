import sys

eng_to_braille_letters = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO'
}

num_to_braille_letters = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    'O': '.OOO..',
}

special_braille_action = {
    'capital follows': '.....O',
    'decimal follows': '.O...O',
    'number follows': '.O.OOO',
    ' ': '......'
}

special_symbol_to_braille = {
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.'
}

braille_to_eng_letters = {braille: eng for eng, braille in eng_to_braille_letters.items()}
braille_to_num = {braille: num for num, braille in num_to_braille_letters.items()}
braille_to_special_action = {braille: special_action for special_action, braille in special_braille_action.items()}
braille_to_special_symbol = {braille: special_symbol for special_symbol, braille in special_symbol_to_braille.items()}


def is_english(string):
    distinct_char = set(string)
    if len(distinct_char) == 2 and "." in distinct_char and "O" in distinct_char:
        return False
    return True


def translate_braille_to_eng(string):
    result = ""
    capitalize = False
    number = False
    decimal = False
    for i in range(0, len(string), 6):
        braille = string[i:i+6]
        if capitalize and braille in braille_to_eng_letters:
            capitalize = False
            result += braille_to_eng_letters[braille].capitalize()
        elif number and braille in braille_to_num:
            result += braille_to_num[braille]
        elif decimal:
            decimal = False
            result += "."
        else:
            if braille in braille_to_eng_letters:
                result += braille_to_eng_letters[braille]
            elif braille in braille_to_special_action:
                if braille_to_special_action[braille] == "capital follows":
                    capitalize = True
                elif braille_to_special_action[braille] == "decimal follows":
                    decimal = True
                elif braille_to_special_action[braille] == "number follows":
                    number = True
                elif braille_to_special_action[braille] == " ":
                    if number:
                        number = False
                    result += " "
            elif braille in braille_to_special_symbol:
                result += braille_to_special_symbol[braille]
    return result


def translate_eng_to_braille(string):
    braille = ""
    prev_num = False
    for char in string:
        if prev_num == True and char not in num_to_braille_letters and char != " ":
            braille += special_braille_action[" "]
            prev_num = False
        if char.lower() in eng_to_braille_letters:
            if char.isupper():
                braille += special_braille_action["capital follows"]
            braille += eng_to_braille_letters[char.lower()]
        elif char in num_to_braille_letters:
            if prev_num != True:
                braille += special_braille_action["number follows"]
            braille += num_to_braille_letters[char]
            prev_num = True
        elif char in special_symbol_to_braille:
            braille += special_symbol_to_braille[char]
        elif char == " ":
            braille += special_braille_action[" "]
            prev_num = False

    return braille


def translate(string):
    if is_english(string):
        return translate_eng_to_braille(string)
    else:
        return translate_braille_to_eng(string)


if __name__ == "__main__":
    inputs = sys.argv[1:]
    inputs_str = ' '.join(inputs)
    output = translate(inputs_str)
    print(output)

