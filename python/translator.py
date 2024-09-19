import sys

ENGLISH_TO_BRAILLE = {
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
    'z': 'O..OOO',
}

NUMBER_TO_BRAILLE = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
}

UTILITIES = {
    "capital_follows": ".....O",
    "number_follows": ".O.OOO",
    "space":  "......"
}

# reverse both dictionaries for braille to english/number translations
BRAILLE_TO_ENGLISH = {braille: letter for letter, braille in ENGLISH_TO_BRAILLE.items()}
BRAILLE_TO_NUMBER = {braille: number for number, braille in NUMBER_TO_BRAILLE.items()}

def is_braille(input_string):
    # all six braille characters are either "O" or ".""
    return all(char in "O." for char in input_string)

def translate_english_to_braille (english_string):
    braille_output = []
    is_number = False

    for char in english_string:
        if char == ' ':
            braille_output.append(UTILITIES["space"])
            is_number = False
        elif char.isdigit():
            if not is_number:
                braille_output.append(UTILITIES["number_follows"])
                is_number = True
            braille_output.append(NUMBER_TO_BRAILLE[char])
        elif char.isupper():
            braille_output.append(UTILITIES["capital_follows"])
            braille_output.append(ENGLISH_TO_BRAILLE[char.lower()])
            is_number = False
        else:
            braille_output.append(ENGLISH_TO_BRAILLE[char])
            is_number = False
    
    return ''.join(braille_output)

def translate_braille_to_english(braille_string):
    english_output = []
    i = 0
    is_capital = False
    is_number = False

    while i < len(braille_string):
        braille_char = braille_string[i:i+6]

        if braille_char == UTILITIES["space"]:
            english_output.append(' ')
            is_capital = False
            is_number = False
        elif braille_char == UTILITIES["capital_follows"]:
            is_capital = True
        elif braille_char == UTILITIES["number_follows"]:
            is_number = True
        else:
            if is_number:
                number = BRAILLE_TO_NUMBER.get(braille_char, '')
                english_output.append(number)
                if (i + 6 >= len(braille_string)) or (braille_string[i + 6:i + 12] == UTILITIES["space"]):
                    is_number = False
            else:
                letter = BRAILLE_TO_ENGLISH.get(braille_char, '')
                if is_capital:
                    english_output.append(letter.upper())
                    is_capital = False
                else:
                    english_output.append(letter)
        i += 6

    return ''.join(english_output)

def run_translation(input_string):
    if is_braille(input_string):
        return translate_braille_to_english(input_string)
    else:
        return translate_english_to_braille(input_string)

def main():
    input_string = ' '.join(sys.argv[1:])
    print(run_translation(input_string))

if __name__ == "__main__":
    main()