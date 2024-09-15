from typing import List

def brailleTokenizer(braille_string:str) -> List[str]:
    tokens = [braille_string[i:i + 6] for i in range(0, len(braille_string), 6)]
    return tokens

braille_dict_letter = {
    "O.....": 'a',
    "O.O...": 'b',
    "OO....": 'c',
    "OO.O..": 'd',
    "O..O..": 'e',
    "OOO...": 'f',
    "OOOO..": 'g',
    "O.OO..": 'h',
    ".OO...": 'i',
    ".OOO..": 'j',
    "O...O.": 'k',
    "O.O.O.": 'l',
    "OO..O.": 'm',
    "OO.OO.": 'n',
    "O..OO.": 'o',
    "OOO.O.": 'p',
    "OOOOO.": 'q',
    "O.OOO.": 'r',
    ".OO.O.": 's',
    ".OOOO.": 't',
    "O...OO": 'u',
    "O.O.OO": 'v',
    ".OOO.O": 'w',
    "OO..OO": 'x',
    "OO.OOO": 'y',
    "O..OOO": 'z', 
}

braille_dict_number = {
    "O.....": '1',
    "O.O...": '2',
    "OO....": '3',
    "OO.O..": '4',
    "O..O..": '5',
    "OOO...": '6',
    "OOOO..": '7',
    "O.OO..": '8',
    ".OO...": '9',
    ".OOO..": '0',
}

braille_space = "......"
braille_capital = ".....O"
braille_number = ".O.OOO"

def brailleTranslator(braille_string: str) -> str:
    braille_tokens = brailleTokenizer(braille_string)
    output_string = ""
    captial_flag = False
    number_flag = False
    for token in braille_tokens:
        if token == braille_capital:
            captial_flag = True
        elif token == braille_number:
            number_flag = True
        elif token == braille_space:
            number_flag = False
            output_string += " "
        elif number_flag:
            output_string += braille_dict_number[token]
        elif captial_flag:
            output_string += braille_dict_letter[token].upper()
            captial_flag = False
        else:
            output_string += braille_dict_letter[token]
    return output_string