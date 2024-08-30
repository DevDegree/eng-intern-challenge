
import sys

def translator(s: str) -> str:
    """
    Translates a string from braille to english and vice versa.
    Args: s (str): The string to be translated.
    Returns: str: The translated string.
    """
    english_to_braille = {"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO"} 
    braile_to_english = {v: k for k, v in english_to_braille.items()}

    number_to_braille = {"1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."}
    braille_to_number = {v: k for k, v in number_to_braille.items()}

    is_capital = False
    is_number = False

    # if string is braille
    if s[0] == "O" or s[0] == ".":
        # process braille to english
        english = ""
        for i in range(0, len(s), 6):
            char = s[i:i+6]
            # if space follows
            if char == "......":
                english += " "
                is_number = False
            # if capital follows
            elif char == ".....O":
                is_capital = True
            elif char == ".O.OOO":
                is_number = True
            else:
                if is_capital:
                    english += braile_to_english[char].upper()
                    is_capital = False
                elif is_number:
                    english += braille_to_number[char]
                else:
                    english += braile_to_english[s[i:i+6]]
        return english
    else:
        # process english to braille
        braille = ""
        for i in range(len(s)):
            # if the character is a number
            if s[i].isnumeric():
                if i == 0 or i != 0 and s[i-1] == " ":
                    braille += ".O.OOO"
                braille += number_to_braille[s[i]]
            # if the character is a space
            elif s[i] == " ":
                braille += "......"
            # if the character is in uppercase
            elif s[i].isupper():
                braille += ".....O" + english_to_braille[s[i].lower()]
            else:
                braille += english_to_braille[s[i]]
        return braille

def main() -> None:
    s = ""

    # concatenate all the arguments into a single string
    for i in range(1, len(sys.argv)):
        if i != len(sys.argv) - 1:
            s += sys.argv[i] + " "
        else:
            s += sys.argv[i]

    print(translator(s))
    
if __name__ == '__main__':
    main()
