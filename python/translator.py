import sys

BRAILLE_MAP = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", 
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", 
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", 
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", 
    "z": "O..OOO", " ": "......", "capital": ".....O", "number": ".O.OOO"}

NUMBER_MAP = {
    "0": ".O.OOO", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", 
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO..." 
}

ENGLISH_MAP = {v: k for k, v in BRAILLE_MAP.items()}
ENGLISH_NUM_MAP = {v: k for k, v in NUMBER_MAP.items()}

def is_braille(input_str):
    return all(char in "O." for char in input_str)

def translate_to_braille(input_str):
    translation = []
    number_flag = False
    for char in input_str:
        if char.isupper():
            number_flag = False
            translation.append(BRAILLE_MAP["capital"])
            translation.append(BRAILLE_MAP[char.lower()])
        elif char.isdigit():
            if number_flag == False:
                translation.append(BRAILLE_MAP["number"])
                number_flag = True
            translation.append(NUMBER_MAP[char])
        else:
            number_flag = False
            translation.append(BRAILLE_MAP[char])
    return ''.join(translation)

def translate_to_english(input_str):
    translation = []
    i = 0
    is_capital = False
    is_number = False
    
    while i < len(input_str):
        braille_char = input_str[i:i+6]

        if braille_char == BRAILLE_MAP["capital"]:
            is_capital = True
            i += 6
            continue
        elif braille_char == BRAILLE_MAP["number"]:
            is_number = True
            i += 6
            continue
        elif braille_char == "......":  
            is_number = False
            translation.append(" ")
            i += 6
            continue
        
        if is_capital:
            translation.append(ENGLISH_MAP[braille_char].upper())
            is_capital = False
        elif is_number:
            translation.append(ENGLISH_NUM_MAP[braille_char])
        else:
            translation.append(ENGLISH_MAP[braille_char])
        
        i += 6

    return ''.join(translation)

if len(sys.argv) > 1:
    input_str = ' '.join(sys.argv[1:])

    if is_braille(input_str):
        print(translate_to_english(input_str))
    else:
        print(translate_to_braille(input_str))
