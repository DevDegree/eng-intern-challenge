import sys

letter_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..", 
    "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", 
    "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", 
    "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO"
}

number_braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..",
    "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

number_follows = ".O.OOO"
capital_follows = ".....O"
space = "......"

def brailleChecker(string: str) -> bool:
    """
    Checks if the input string is a valid Braille representation.
    Args:
    string (str): The input string to be checked.
    Returns:
    bool: True if the string is valid Braille, False otherwise indicating String is English.
    """
    if len(string) % 6 != 0:
        return False

    if not all(char in '.O' for char in string):
        return False

    valid_braille = set(letter_braille.values()) | set(number_braille.values()) | {number_follows, capital_follows, space}

    return all(string[i:i+6] in valid_braille for i in range(0, len(string), 6))

def englishtoBraille(string: str) -> str:
    """
    Converts an English string to Braille.
    Args:
    string (str): The input string to convert.
    Returns:
    str: The translated Braille string.
    """
    braille_string = ""
    is_digit = False

    for character in string:
        if character.isdigit():
            if not is_digit:
                braille_string += number_follows
                is_digit = True
            braille_string += number_braille[character]
        elif character.isalpha():
            if is_digit:
                is_digit = False
            if character.isupper():
                braille_string += capital_follows
            braille_string += letter_braille[character.lower()]
        elif character.isspace():
            braille_string += space
            is_digit = False

    return braille_string

def brailletoEnglish(string: str) -> str:
    """
    Converts a Braille string to English.
    Args:
    string (str): The input string to convert.
    Returns:
    str: The translated English string.
    """
    english_string = ""
    i = 0
    is_capital = False
    is_digit = False

    while i < len(string):
        braille_character = string[i:i+6]

        if braille_character == capital_follows:
            is_capital = True
        elif braille_character == number_follows:
            is_digit = True
        elif braille_character == space:
            english_string += " "
            is_digit = False
        else:
            if is_digit:
                english_string += next((key for key, value in number_braille.items() if value == braille_character), '?')
                is_digit = False
            else:
                char = next((key for key, value in letter_braille.items() if value == braille_character), '?')
                english_string += char.upper() if is_capital else char
                is_capital = False

        i += 6

    return english_string

def main():
    input_str = " ".join(sys.argv[1:])
    if brailleChecker(input_str):
        print(brailletoEnglish(input_str))
    else:
        print(englishtoBraille(input_str))

if __name__ == "__main__":
    main()