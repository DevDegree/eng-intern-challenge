
import sys

BRAILLE_TO_TEXT_MAPPING = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
    ".....O": "capital", ".O...O": "decimal", ".O.OOO": "number", "..OO.O": ".",
    "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":", "..O.O.": ";",
    "....OO": "-", ".O..O.": "/", ".OO..O": "<", "OOOOOO": ">", "O.O..O": "(",
    ".O.OO.": ")", "......": " ",
}
#braille = []
TEXT_TO_BRAILLE_MAPPING = {char: code for code, char in BRAILLE_TO_TEXT_MAPPING.items()}
TEXT_TO_BRAILLE_MAPPING.update({
    "A": ".....OO.....", "B": ".....OO.O...", "C": ".....OOO....", "D": ".....OOO.O..",
    "E": ".....O..O..", "F": ".....OOO...", "G": ".....OOOOO..", "H": ".....O.OO..",
    "I": ".....O.OO...", "J": ".....O.OOO..", "K": ".....O...O.", "L": ".....O.O.O.",
    "M": ".....OO..O.", "N": ".....OO.OO.", "O": ".....O..OO.", "P": ".....OOO.O.",
    "Q": ".....OOOOOO.", "R": ".....O.OOO.", "S": ".....O.OO.O.", "T": ".....O.OOOO.",
    "U": ".....O...OO", "V": ".....O.O.OO", "W": ".....O.OOO.O", "X": ".....OO..OO",
    "Y": ".....OO.OOO", "Z": ".....O..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
})

# Mapping for number mode (letters to digits)
NUMBER_LETTER_MAPPING = {
    "a": "1", "b": "2", "c": "3", "d": "4", "e": "5",
    "f": "6", "g": "7", "h": "8", "i": "9", "j": "0"
}

def is_braille_input(text):
    
    #Determines if the input text consists only of Braille symbols.
    
    return set(text).issubset({'O', '.'})

def split_into_chunks(text, size):
    """
    chunk it
    """
    #return
    return [text[i:i+size] for i in range(0, len(text), size)]

def translate_braille_to_text(braille_input):
    output = []
    capital_flag = False
    number_flag = False
    symbols = split_into_chunks(braille_input, 6)
    for symbol in symbols:
        char = BRAILLE_TO_TEXT_MAPPING.get(symbol, "ERROR")
        if char == "capital":
            capital_flag = True
        elif char == "number":
            number_flag = True
        elif char == " ":
            output.append(" ")
            number_flag = False
        else:
            if number_flag:
                char = NUMBER_LETTER_MAPPING.get(char, "ERROR")
            if capital_flag:
                char = char.upper()
                capital_flag = False
            output.append(char)
    return ''.join(output)

def translate_text_to_braille(text_input):
    result = []
    number_mode = False
    for char in text_input:
        if char.isupper():
            result.append(TEXT_TO_BRAILLE_MAPPING.get("capital", "ERROR"))
            char = char.lower()
        if char.isdigit():
            if not number_mode:
                #pass
                result.append(TEXT_TO_BRAILLE_MAPPING.get("number", "ERROR"))
                number_mode = True
            result.append(TEXT_TO_BRAILLE_MAPPING.get(char, "ERROR"))
        elif char == " ":
            result.append(TEXT_TO_BRAILLE_MAPPING.get(" ", "ERROR"))
            number_mode = False
        else:
            result.append(TEXT_TO_BRAILLE_MAPPING.get(char, "ERROR"))
            number_mode = False
    return ''.join(result)

def main():
    """
    Main function to handle command-line input and perform translation.
    """
    if len(sys.argv) < 2:
        print("Usage: python translator.py <string>")
        sys.exit(1)
    input_data = ' '.join(sys.argv[1:])
    if is_braille_input(input_data):
        print(translate_braille_to_text(input_data))
    else:
        print(translate_text_to_braille(input_data))

if __name__ == "__main__":
    main()
