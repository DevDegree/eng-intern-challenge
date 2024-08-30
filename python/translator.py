import sys

NUMBER_PREFIX =".O.OOO"

# Braille to English dictionary 
braille_to_english = {
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
    ".....O": "capital",  # Capital follows
    ".O.OOO": "number",        # Number follows 
    NUMBER_PREFIX + "O.....": "1",        # 1 
    NUMBER_PREFIX + "O.O...": "2",        # 2
    NUMBER_PREFIX + "OO....": "3",        # 3
    NUMBER_PREFIX + "OO.O..": "4",        # 4
    NUMBER_PREFIX + "O..O..": "5",        # 5
    NUMBER_PREFIX + "OOO...": "6",        # 6
    NUMBER_PREFIX + "OOOO..": "7",        # 7
    NUMBER_PREFIX + "O.OO..": "8",        # 8
    NUMBER_PREFIX + ".OO...": "9",        # 9
    NUMBER_PREFIX + ".OOO..": "0",        # 0
    "..OO.O": ".",        # Period
    "..O...": ",",        # Comma
    "..O.OO": "?",        # Question mark
    "..OOO.": "!",        # Exclamation mark
    "..OO..": ":",        # Colon
    "..O.O.": ";",        # Semicolon
    "....OO": "-",        # Hyphen
    ".O..O.": "/",        # Slash
    ".OO..O": "<",        # Less than
    "O..OO.": ">",        # Greater than
    "O.O..O": "(",        # Left parenthesis
    ".O.OO.": ")",        # Right parenthesis
    "......": " ",        # Space
}

# English to Braille dictionary
english_to_braille = {
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
    ".": "..OO.O",        # Period
    ",": "..O...",        # Comma
    "?": "..O.OO",        # Question mark
    "!": "..OOO.",        # Exclamation mark
    ":": "..OO..",        # Colon
    ";": "..O.O.",        # Semicolon
    "-": "....OO",        # Hyphen
    "/": ".O..O.",        # Slash
    "<": ".OO..O",        # Less than
    ">": "O..OO.",        # Greater than
    "(": "O.O..O",        # Left parenthesis
    ")": ".O.OO.",        # Right parenthesis
    " ": "......",        # Space
}

def is_braille(input_string):
    return all(c in "O." for c in input_string)

def isCapital(input_char): 
    return input_char.isupper()

def isNumber(input_char): 
    return input_char.isnumeric()

def translate_to_braille(english_text):
    result = []
    while english_text:
        braille_key = english_text[:1]
        english_text = english_text[1:]

        if isCapital(braille_key):
            capital_follows = ".....O"
            result.append(capital_follows)
            toLowerCase = braille_key.lower()
            result.append(english_to_braille[toLowerCase])

        elif isNumber(braille_key):
            number_follows = ".O.OOO"
            result.append(number_follows)
            result.append(english_to_braille[braille_key])
            while english_text and english_text[:1] != " ":
                braille_key = english_text[:1]
                english_text = english_text[1:]
                result.append(english_to_braille[braille_key])
        else:
            result.append(english_to_braille[braille_key])

    return ''.join(result)

def translate_to_english(braille_text):
    result = []
    while braille_text:
        english_key = braille_text[:6]
        braille_text = braille_text[6:]

        # Capital follows
        if english_key == ".....O":
            english_key = braille_text[:6]
            braille_text = braille_text[6:]

            capitalized_val = braille_to_english[english_key].upper()
            result.append(capitalized_val)
        # Number Follows
        elif english_key == ".O.OOO":
            while braille_text and braille_text[:6] != "......":
                english_key = braille_text[:6]
                braille_text = braille_text[6:]
                result.append(braille_to_english[NUMBER_PREFIX + english_key])

        # Handle "O" vs ">" ambiguity
        elif english_key == "O..OO.":
            # Assuming "O" is more common in text.
            if result and result[-1].isalnum():  
                if result and result[-1].isupper():  
                    result.append("O")  # Capital 'O'
                else:
                    result.append("o")  # Lowercase 'o'
            else:
                result.append(">")  # Assume ">" in non-alphanumeric context

        # Regular Character
        else:
            result.append(braille_to_english[english_key])

    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)

    input_string = " ".join(sys.argv[1:])

    if is_braille(input_string):
        print(translate_to_english(input_string))
    else:
        print(translate_to_braille(input_string))


if __name__ == "__main__":
    main()