# Arya Patel
# Eng Intern Challenge Submission
# Sept 22, 2024

eng_to_braille = {
    'A': 'O.....',
    'B': 'O.O...',
    'C': 'OO....',
    'D': 'OO.O..',
    'E': 'O..O..',
    'F': 'OOO...',
    'G': 'OOOO..',
    'H': 'O.OO..',
    'I': '.OO...',
    'J': '.OOO..',
    'K': 'O...O.',
    'L': 'O.O.O.',
    'M': 'OO..O.',
    'N': 'OO.OO.',
    'O': 'O..OO.',
    'P': 'OOO.O.',
    'Q': 'OOOOO.',
    'R': 'O.OOO.',
    'S': '.OO.O.',
    'T': '.OOOO.',
    'U': 'O...OO',
    'V': 'O.O.OO',
    'W': '.OOO.O',
    'X': 'OO..OO',
    'Y': 'OO.OOO',
    'Z': 'O..OOO',
    'capital': '.....O',
    'decimal': '.O...O',
    'number': '.O.OOO',
    'space': '......',
}

eng_to_num = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

eng_to_punctuation = {
    ',': '..OO.O',
    '.': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
}

braille_to_eng = {value: key for key, value in eng_to_braille.items()}
braille_to_num = {value: key for key, value in eng_to_num.items()}
braille_to_punctuation = {value: key for key, value in eng_to_punctuation.items()}

def translate():
    str_to_translate = input()

    length = len(str_to_translate)
    idx = 0
    translation = ""

    if len(str_to_translate) == 0:
        print('')

    # Convert from English to Braille 
    elif isEnglish(str_to_translate):
        # implement

    # Convert from Braille to English
    else:
        in_number_mode = False
        while idx < length:
            start = idx
            end = idx + 6
            char = str_to_translate[start:end]

            # for a space
            if char == "......":
                translation += ' '
                idx += 6

            # for a capital letter
            elif char == ".....O":
                idx += 6
                if idx + 6 <= length:
                    char = str_to_translate[idx:idx + 6]
                    eng_char = braille_to_eng.get(char)
                    translation += eng_char.upper()  # convert to uppercase
                idx += 6

            # for a decimal follows symbol
            # assumption: the decimal follows symbol is for numbers only (ie. 123.45 would have a decimal follows symbol after the digit '3' followed by a decimal and then the rest of the numbers)
            elif char == ".O...O":
                idx += 6
                translation += '.'

            # for a number
            elif char == ".O.OOO":
                in_number_mode = True  # enter number mode
                idx += 6
                while idx + 6 <= length:
                    char = str_to_translate[idx:idx + 6]
                    if char == "......":
                        in_number_mode = False  # exit number mode
                        break
                    elif char == ".O...O":  # handle decimal points while still in number mode
                        translation += '.'
                        idx += 6
                    else:
                        num_char = braille_to_num.get(char)
                        if num_char:
                            translation += num_char
                        idx += 6

            # for regular English letters
            else:
                eng_char = braille_to_eng.get(char)
                if eng_char:
                    if in_number_mode:
                        in_number_mode = False  # exit number mode
                    translation += eng_char.lower()  # convert to lowercase
                else:
                    punctuation_char = braille_to_punctuation.get(char)
                    if punctuation_char:
                        translation += punctuation_char
                idx += 6
    
    print(translation)
    return 0

# Check if the string is English or Braille
def isEnglish(str_to_translate):
    for char in str_to_translate:
        if char == ' ':
            continue
        elif char != 'O' and char != '.':
            return True
    return False

if __name__ == "__main__":
    translate()
