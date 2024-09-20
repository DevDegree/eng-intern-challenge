

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
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "_": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......",
    "uppercase": ".....O",
    "decimal": ".O...O",
    "number": ".O.OOO"
}


def check_braille(input_string):
    """
    Checks if string is in braille format or not

    input_string (str): input string
    """
    return input_string.count("O") + input_string.count(".") == len(input)


def braille_to_english(input_string):
    """
    Translates Braille string to English

    input_string (str): input string in English to be translated
    """

    braille_symbols = [input_string[i:i+6] for i in range(0, len(input_string), 6)]
    output_string = ""

    uppercase_letter = False
    number = False

    for symbol in braille_symbols:
        if symbol == braille_dict['uppercase']:
            uppercase_letter = True
        elif symbol == braille_dict['number']:
            number = True
        elif symbol in braille_dict.values():
            char_match = [letter for letter, value in braille_dict.items() if value == symbol]
            character = str()
            if number:
                if len(char_match) == 2:
                    character = char_match[1]  # Make sure the symbol after the number is valid
                else:
                    character = char_match[0]  # Use a letter if no valid number symbol found
            else:
                character = char_match[0]

            if uppercase_letter:
                character = character.upper()
                uppercase_letter = False

            if character == " ":
                number = False

            output_string += character
        else:
            raise ValueError(f"The symbol {symbol} does not exist in Braille")

    return output_string   

        
def english_to_braille(input_string):
    """
    Translates English string to Braille

    input_string (str): input string in Braille to be translated
    """

    
