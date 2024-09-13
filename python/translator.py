import sys

ALPHABET_DICT= {
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
}

NUM_DICT= {
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

SYMBOL_DICT= {
     ".....O": "capital",
    ".O.OOO": "number"
}

def translate_to_braille(input):
    '''
    Translates the given input to Braille.

    Args:
        input (str): The text to be translated.

    Returns:
        str: The translated text in Braille.

    '''
    braille_output_text = ""
    number_flag = False

    for char in input:
        if char.isupper():
            number_flag = False
            for key, value in SYMBOL_DICT.items():
                if value == 'capital':
                    braille_output_text += key 
            #braille_output_text += ".....O"
            char = char.lower()
            char = ALPHABET_DICT[char]
        elif not char.isupper() and not char.isdigit():
            number_flag = False
            for key, value in ALPHABET_DICT.items():
                if key == char:
                    char = ALPHABET_DICT[char]
        elif char.isdigit():
            if not number_flag:
                for key, value in SYMBOL_DICT.items():
                    if value == 'number':
                        braille_output_text += key 
                char = NUM_DICT[char]
                number_flag = True
            else:
                char = NUM_DICT[char]
        braille_output_text += char

    return braille_output_text
def translate_to_text(input):
    '''
    Translates the given input to english text.

    Args:
        input (str): The text to be translated.

    Returns:
        str: The translated text in normal text.

    '''
    eng_output_text = ""
    capital_flag = False
    number_flag = False
    letters = [input[i:i+6] for i in range(0, len(input), 6)]

    for letter in letters:
        if letter in SYMBOL_DICT:
            if SYMBOL_DICT[letter] == "capital":
                capital_flag = True
            elif SYMBOL_DICT[letter] == "number":
                number_flag = True
        else:
            if number_flag:
                if letter == "......":
                    number_flag = False
                    break
                else:
                    for key, value in NUM_DICT.items():

                        if value == letter:
                            eng_output_text += key
                            #number_flag = False
                            break
            
            else:
                for key, value in ALPHABET_DICT.items():
                    if value == letter:
                        if capital_flag:
                            eng_output_text += key.upper()
                            capital_flag = False
                        else:
                            eng_output_text += key
                        break
    
    return eng_output_text
def main():
    input_str = ' '.join(sys.argv[1:])

    # Check if input is text or braille, if all characters are either 'O' or '.' then it is braille, else text
    if all(char in 'O.' for char in input_str):
        output_text = translate_to_text(input_str)
        print(output_text)
    else:
        output_text = translate_to_braille(input_str)
        print(output_text)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input>")
        sys.exit(1)
    else:
        main()