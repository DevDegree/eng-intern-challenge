# english to braille, braille to english translator

# imports
import sys

def conversion_dicts():
    """
    Returns an obj containing dicts for converting alpha, num, symbols, and special chars to braille.
    """
    # '.' = flat, 'O' = raised
    alpha_to_braille = {
        "a" : "O.....",
        "b" : "O.O...",
        "c" : "OO....",
        "d" : "OO.O..",
        "e" : "O..O..",
        "f" : "OOO...",
        "g" : "OOOO..",
        "h" : "O.OO..",
        "i" : ".OO...",
        "j" : ".OOO..",
        "k" : "O...O.",
        "l" : "O.O.O.",
        "m" : "OO..O.",
        "n" : "OO.OO.",
        "o" : "O..OO.",
        "p" : "OOO.O.",
        "q" : "OOOOO.",
        "r" : "O.OOO.",
        "s" : ".OO.O.",
        "t" : ".OOOO.",
        "u" : "O...OO",
        "v" : "O.O.OO",
        "w" : ".OOO.O",
        "x" : "OO..OO",
        "y" : "OO.OOO",
        "z" : "O..OOO",
        " " : "......",
    }
    
    num_to_braille = {
        "1" : "O.....",
        "2" : "O.O...",
        "3" : "OO....",
        "4" : "OO.O..",
        "5" : "O..O..",
        "6" : "OOO...",
        "7" : "OOOO..",
        "8" : "O.OO..",
        "9" : ".OO...",
        "0" : ".OOO.."
    }
    
    symbols_to_braille = {
        "." : "..OO.O",
        "," : "..O...",
        "?" : "..O.OO",
        "!" : "..OOO.",
        ":" : "..OO..",
        ";" : "..O.O.",
        '-' : "....OO",
        "/" : ".O..O.",
        "<" : ".OO..O",
        ">" : "O..OO.",
        "(" : "O.O..O",
        ")" : ".O.OO."
    }
    
    special_to_braille = {
        "capital" : ".....O",
        "decimal" : ".O...O",
        "number"  : ".O.OOO"
    }

    return {
        "alpha" : alpha_to_braille,
        "num" : num_to_braille,
        "symbols" : symbols_to_braille,
        "special" : special_to_braille
    }


def english_to_braille(input_str, dicts_obj):
    """
    Converts an English string to Braille.

    Args:
        input_str (str): English string to convert to Braille
        dicts_obj (dict): object containing dictionaries for converting alpha, num, symbols, and special chars to braille
            dicts_obj = {
                "alpha" : { "a" : "O.....", ... },
                "num" : { "1" : "O.....", ... },
                "symbols" : { "." : "..OO.O", ... },
                "special" : { "capital" : ".....O", ... }
            }

    Returns:
        str: Braille representation of the input string
    """
    # extract dicts from conversion_dicts object
    alpha_to_braille = dicts_obj["alpha"]
    num_to_braille = dicts_obj["num"]
    symbols_to_braille = dicts_obj["symbols"]
    special_to_braille = dicts_obj["special"]

    braille_output = []
    is_number = False  # flag to check if in number mode

    for char in input_str:
        if char.isalpha():
            # add capital indicator if char is uppercase
            if char.isupper():
                braille_output.append(special_to_braille["capital"])
                char = char.lower()
            
            # append braille conversion of letter
            braille_output.append(alpha_to_braille[char])

        elif char.isdigit():
            # switch to number mode if not already in it
            if not is_number:
                braille_output.append(special_to_braille["number"])
                is_number = True
            
            # append braille conversion of number
            braille_output.append(num_to_braille[char])

        elif char in symbols_to_braille:
            # append braille conversion of symbol
            braille_output.append(symbols_to_braille[char])

        elif char == ' ':
            # append space and reset number mode
            braille_output.append(alpha_to_braille[' '])
            is_number = False  # Reset number mode when a space is encountered

    # join and return all braille cells into a single string
    return ''.join(braille_output)


def braille_to_english(input_str, dicts_obj):
    """
    Converts a Braille string to English.

    Args:
        input_str (str): Braille string to convert to English
        dicts_obj (dict): object containing dictionaries for converting alpha, num, symbols, and special chars to braille
            dicts_obj = {
                "alpha" : { "a" : "O.....", ... },
                "num" : { "1" : "O.....", ... },
                "symbols" : { "." : "..OO.O", ... },
                "special" : { "capital" : ".....O", ... }
            }

    Returns:
        str: English representation of the input string
    """
    # extract dictionaries from conversion_dicts object
    alpha_to_braille = dicts_obj["alpha"]
    num_to_braille = dicts_obj["num"]
    symbols_to_braille = dicts_obj["symbols"]
    special_to_braille = dicts_obj["special"]

    # create reverse dictionaries for quick lookup
    braille_to_alpha = {v: k for k, v in alpha_to_braille.items()}
    braille_to_num = {v: k for k, v in num_to_braille.items()}
    braille_to_symbols = {v: k for k, v in symbols_to_braille.items()}
    braille_to_special = {v: k for k, v in special_to_braille.items()}

    english_output = []
    is_capital = False
    is_number = False

    # split the input string into braille cells of 6 characters each
    braille_cells = [input_str[i:i+6] for i in range(0, len(input_str), 6)]

    for cell in braille_cells:
        if cell in braille_to_special:
            # handle special cases for capital and number indicators
            special_case = braille_to_special[cell]
            if special_case == "capital":
                is_capital = True
            elif special_case == "number":
                is_number = True  # set number mode

        elif is_number and cell in braille_to_num:
            # convert braille numbers
            english_output.append(braille_to_num[cell])

        elif cell in braille_to_alpha:
            # convert braille letters
            char = braille_to_alpha[cell]
            if is_capital:
                char = char.upper()  # apply cap
                is_capital = False  # reset cap flag after use
            english_output.append(char)

        elif cell in braille_to_symbols:
            # convert braille symbols
            english_output.append(braille_to_symbols[cell])

        elif cell == alpha_to_braille[' ']:  # handle spaces
            english_output.append(' ')
            is_number = False  # reset number mode upon space

    return ''.join(english_output)



def detect_type(input_str, dicts_obj):
    """
    Detects the type of input string.
        - Split str into braille cells (6 chars) and check if chars are '.' or 'O', and lens are 6
    
    Args:
        input_str (str): input string to detect type of
        dicts_obj (dict): object containing dictionaries for converting alpha, num, symbols, and special chars to braille
            dicts_obj = {
                "alpha" : { "a" : "O.....", ... },
                "num" : { "1" : "O.....", ... },
                "symbols" : { "." : "..OO.O", ... },
                "special" : { "capital" : ".....O", ... }
            }
    
    Returns:
        str: "braille", "english", or "invalid_type"
    """
    # extract dictionaries from conversion_dicts object
    alpha_to_braille = dicts_obj["alpha"]
    num_to_braille = dicts_obj["num"]
    symbols_to_braille = dicts_obj["symbols"]
    special_to_braille = dicts_obj["special"]
    
    # combine all braille values from the dictionaries for validation
    valid_braille = set(alpha_to_braille.values()) | set(num_to_braille.values()) | set(symbols_to_braille.values()) | set(special_to_braille.values())
    
    # turn input string into braille cells (6 chars each)
    braille_cells = [input_str[i:i+6] for i in range(0, len(input_str), 6)]

    # check if the input matches braille patterns
    is_braille = all(cell in valid_braille for cell in braille_cells)

    # combine all english keys from the dictionaries for validation
    valid_english = set(alpha_to_braille.keys()) | set(num_to_braille.keys()) | set(symbols_to_braille.keys())
    
    # check if the input matches english patterns
    is_english = all(char in valid_english for char in input_str)

    if is_braille:
        return "braille"
    else:
        return "english"


def __main__():
    conversion_dicts_obj = conversion_dicts()
    input_str = " ".join(sys.argv[1:])
    input_type = detect_type(input_str, conversion_dicts_obj)

    if input_type == "english":
        output = english_to_braille(input_str, conversion_dicts_obj)
    elif input_type == "braille":
        output = braille_to_english(input_str, conversion_dicts_obj)
    else:
        output = "Conversion Error"

    print(output)

if __name__ == "__main__":
    __main__()