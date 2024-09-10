import sys

letter_Braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...","g": "OOOO..", 
    "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.","m": "OO..O.", "n": "OO.OO.", 
    "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", 
    "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO"
}

number_Braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..",
    "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

number_Follows = ".O.OOO"
capital_Follows = ".....O"
space = "......"

"""
Checks if input string is a valid Braille representation.

    Args:
    string (str): The input string to be checked.

    Returns:
    bool: True if the string is valid Braille, False otherwise indicating String is English.
"""
def brailleChecker(string str) -> bool:
    # Checks if length of string is a multiple of 6.
    if len(str) % 6 != 0:
        return False
    
    # Checks if string contains only '.' (flat dot) and 'O' (raised dot) characters.
    if not all(char in '.O' for char in str):
        return False

    # Set of all valid braille values
    valid_braille = set(letter_Braille.values()) and set(number_Braille.values())
    valid_braille.add(number_Follows)
    valid_braille.add(capital_Follows)
    valid_braille.add(space)

    # Check for every 6 characters they're a valid braille
    return all(string[i:i+6] in valid_braille for i in range(0, len(string), 6))
    
