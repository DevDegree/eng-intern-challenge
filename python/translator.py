import sys

letter_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...","g": "OOOO..", 
    "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.","m": "OO..O.", "n": "OO.OO.", 
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
    Checks if input string is a valid Braille representation.

        Args:
        string (string): The input string to be checked.

        Returns:
        bool: True if the string is valid Braille, False otherwise indicating String is English.
    """
    # Checks if length of string is a multiple of 6.
    if len(string) % 6 != 0:
        return False
    
    # Checks if string contains only '.' (flat dot) and 'O' (raised dot) characters.
    if not all(char in '.O' for char in string):
        return False

    # Set of all valid braille values
    valid_braille = set(letter_braille.values()) and set(number_braille.values())
    valid_braille.add(number_follows)
    valid_braille.add(capital_follows)
    valid_braille.add(space)

    # Check for every 6 characters they're a valid braille
    return all(string[i:i+6] in valid_braille for i in range(0, len(string), 6))

def englishtoBraille(string: str) -> str:
    """
    Converts inputted string from english to braille value

        Args:
        string (string): The input string to convert

        Returns:
        string: The translated braille string
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
    Converts inputted string from braille to english value

        Args:
        string (string): The input string to convert

        Returns:
        string: The translated english string
    """
    english_string = ""
    i = 0
    is_caps= False
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
        elif is_digit:
            for key, value in number_braille.items():
                if value == braille_character:
                    english_string += key
                    break
        else:
            for key, value in letter_braille.items():
                if value == braille_character:
                    char = key
                    english_string += char.upper() if is_capital else char
                    is_capital = False
                    break

        i += 6

    return english_string

def main():
    input_str = input_string = " ".join(sys.argv[1:])
    if brailleChecker(input_string):
        print(brailletoEnglish(input_string))
    else:
        print(englishtoBraille(input_string))

if __name__ == "__main__":
    main()
    