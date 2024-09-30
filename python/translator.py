import sys

braille_to_alphabet = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    ".....O": "capital",
    ".O.OOO": "number",
    "......": " ",
}

braille_numbers = {
    "a": "1",
    "b": "2",
    "c": "3",
    "d": "4",
    "e": "5",
    "f": "6",
    "g": "7",
    "h": "8",
    "i": "9",
    "j": "0"
}

alphanumeric_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    " ": "......"
}

braille_capital_sign = ".....O"
braille_number_sign = ".O.OOO"

def is_braille(input):
    """
    Checks if the given input string is a valid Braille pattern.
    
    :param input: A string representing potential Braille characters.
    :return: True if the input is a valid Braille pattern, False otherwise.
    """
    if len(input) % 6 != 0:
        return False
    return all(char in ('O', '.') for char in input)

def translate_braille_to_alphabet(input):
    """
    Translates a Braille string into its corresponding alphabetic representation.
    
    :param input: A string of Braille characters.
    :return: A translated string in the alphabet.
    """
    is_capital = False
    is_number = False
    result = []

    for i in range(0, len(input), 6):
        braille_string = input[i:i+6]

        if braille_string in braille_to_alphabet:
            character = braille_to_alphabet[braille_string]

            if character == "capital":
                is_capital = True
                continue
            
            if character == "number":
                is_number = True
                continue

            if character == " ":
                is_number = False

            if is_number:
                result.append(braille_numbers[character])
            elif is_capital:
                result.append(character.upper())
            else:
                result.append(character)

            is_capital = False
        
        else:
            result.append("?")
    
    return ''.join(result)

def translate_alphabet_to_braille(input):
    """
    Translates an alphabetic string into its corresponding Braille representation.
    
    :param input: A string of alphabetic characters.
    :return: A translated string in Braille.
    """
    result = []
    is_number = False

    for char in input:
        
        if char.isdigit():
            if not is_number:
                result.append(braille_number_sign)
                is_number = True
            result.append(alphanumeric_to_braille[char])

        elif char.isalpha():
            if char.isupper():
                result.append(braille_capital_sign)
                result.append(alphanumeric_to_braille[char.lower()])
            else:
                result.append(alphanumeric_to_braille[char])
        else:
            if is_number:
                is_number = False
            result.append(alphanumeric_to_braille.get(char, "......"))
    
    return ''.join(result)

def main():
    """
    The main function to determine the type of input (Braille or alphabet) and translate accordingly.
    """
    # Check for Braille or alphabet
    is_alpha = False
    n = len(sys.argv)
    if n > 2:
        is_alpha = True
    else:
        is_alpha = not is_braille(sys.argv[1])

    if is_alpha:
        input_string = " ".join(sys.argv[1:])
        print(translate_alphabet_to_braille(input_string))
    else:
        print(translate_braille_to_alphabet(sys.argv[1]))

if __name__ == "__main__":
    main()









