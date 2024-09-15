def englishTokenizer(english_string:str) -> list[str]:
    tokens = [char for char in english_string]
    return tokens

english_dict_letter = {
    'a': "O.....",
    'b': "O.O...",
    'c': "OO....",
    'd': "OO.O..",
    'e': "O..O..",
    'f': "OOO...",
    'g': "OOOO..",
    'h': "O.OO..",
    'i': ".OO...",
    'j': ".OOO..",
    'k': "O...O.",
    'l': "O.O.O.",
    'm': "OO..O.",
    'n': "OO.OO.",
    'o': "O..OO.",
    'p': "OOO.O.",
    'q': "OOOOO.",
    'r': "O.OOO.",
    's': ".OO.O.",
    't': ".OOOO.",
    'u': "O...OO",
    'v': "O.O.OO",
    'w': ".OOO.O",
    'x': "OO..OO",
    'y': "OO.OOO",
    'z': "O..OOO",
}

english_dict_number = {
    '1': "O.....",
    '2': "O.O...",
    '3': "OO....",
    '4': "OO.O..",
    '5': "O..O..",
    '6': "OOO...",
    '7': "OOOO..",
    '8': "O.OO..",
    '9': ".OO...",
    '0': ".OOO..",
}

braille_space = "......"
braille_capital = ".....O"
braille_number = ".O.OOO"



def englishTranslator(english_string: str) -> str:
    english_tokens = englishTokenizer(english_string)
    output_string = ""
    number_flag = False
    for token in english_tokens:
        if token in english_dict_letter:
            output_string += english_dict_letter[token]
        elif token.isupper():
            output_string += braille_capital
            output_string += english_dict_letter[token.lower()]
        elif token in english_dict_number:
            if not number_flag:
                number_flag = True
                output_string += braille_number
            output_string += english_dict_number[token]
        elif token == " ":
            output_string += braille_space
            number_flag = False

    return output_string