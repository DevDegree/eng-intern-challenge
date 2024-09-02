import sys

# Braille to English mapping
BRAILLE_TO_ENGLISH_SPECIAL = {
    ".....O": "capital",
    ".O...O": "decimal",
    ".O.OOO": "number",
    "......": " "
}

BRAILLE_TO_ENGLISH_NUMBER = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
    "......": " "
}

BRAILLE_TO_ENGLISH_DECIMAL = {
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O..OO.": ">",
    "O.O..O": "(",
    ".O.OO.": ")",
    "......": " "
}

BRAILLE_TO_ENGLISH_LETTER = {
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
    "......": " "
}

ENGLISH_TO_BRAILLE_SPECIAL = {
    'capital': '.....O', 
    'decimal': '.O...O', 
    'number': '.O.OOO', 
    ' ': '......'
}

ENGLISH_TO_BRAILLE_NUMBER = {
    '1': 'O.....', 
    '2': 'O.O...', 
    '3': 'OO....', 
    '4': 'OO.O..', 
    '5': 'O..O..', 
    '6': 'OOO...', 
    '7': 'OOOO..', 
    '8': 'O.OO..', 
    '9': '.OO...', 
    '0': '.OOO..', 
    ' ': '......'
}


ENGLISH_TO_BRAILLE_DECIMAL = {
    '.': '..OO.O', 
    ',': '..O...', 
    '?': '..O.OO', 
    '!': '..OOO.', 
    ':': '..OO..', 
    ';': '..O.O.', 
    '-': '....OO', 
    '/': '.O..O.', 
    '<': '.OO..O', 
    '>': 'O..OO.', 
    '(': 'O.O..O', 
    ')': '.O.OO.', 
    ' ': '......'
}


ENGLISH_TO_BRAILLE_LETTER = {
    'a': 'O.....', 
    'b': 'O.O...', 
    'c': 'OO....', 
    'd': 'OO.O..', 
    'e': 'O..O..', 
    'f': 'OOO...', 
    'g': 'OOOO..', 
    'h': 'O.OO..', 
    'i': '.OO...', 
    'j': '.OOO..', 
    'k': 'O...O.', 
    'l': 'O.O.O.', 
    'm': 'OO..O.', 
    'n': 'OO.OO.', 
    'o': 'O..OO.', 
    'p': 'OOO.O.', 
    'q': 'OOOOO.', 
    'r': 'O.OOO.', 
    's': '.OO.O.', 
    't': '.OOOO.', 
    'u': 'O...OO', 
    'v': 'O.O.OO', 
    'w': '.OOO.O', 
    'x': 'OO..OO', 
    'y': 'OO.OOO', 
    'z': 'O..OOO', 
    ' ': '......'
}


def is_braille(text):
    """
    Checks if a given text consists solely of Braille characters.

    Parameters:
    text (str): The text to check, which should be a string of Braille characters.

    Returns:
    bool: True if all characters in the text are Braille dots ('.') or Braille 'O' characters; False otherwise.
    """
    return all(char in "O." for char in text)


def translate_braille_to_english(braille):
    """
    Translates a string of Braille characters into English text.

    Parameters:
    braille (str): A string of Braille characters to be translated.

    Returns:
    str: The translated English text from the provided Braille string.
    """
    output = []
    is_number = False
    is_capital = False
    is_decimal = False

    i = 0

    while i < len(braille):
        symbol = braille[i:i + 6]
        if symbol == ENGLISH_TO_BRAILLE_SPECIAL['capital']:
            is_number = False
            is_capital = True
            is_decimal = False
            i += 6
            continue
        elif symbol == ENGLISH_TO_BRAILLE_SPECIAL['number']:
            is_number = True
            is_capital = False
            is_decimal = False
            i += 6
            continue
        elif symbol == ENGLISH_TO_BRAILLE_SPECIAL['decimal']:
            is_decimal = True
            is_number = False
            is_capital = False
            i += 6
            continue

        if is_capital:
            char = BRAILLE_TO_ENGLISH_LETTER[symbol]
            char = char.upper()
            is_capital = False
        elif is_number:
            char = BRAILLE_TO_ENGLISH_NUMBER[symbol]
            char = str(char)
        elif is_decimal:
            char = BRAILLE_TO_ENGLISH_DECIMAL[symbol]
            char = str(char)
        else:
            char = BRAILLE_TO_ENGLISH_LETTER[symbol]

        output.append(char)
        i += 6
    output.append(" ")

    return "".join(output).strip()


def translate_english_to_braille(english):
    """
    Translates an English text string into Braille characters.

    Parameters:
    english (str): The English text to be translated.

    Returns:
    str: The translated Braille string from the provided English text.
    """
    output = []
    is_number = False
    is_capital = False
    is_decimal = False

    for char in english:
        if char.isalpha():
            if char.isupper():
                if not is_capital:
                    output.append(ENGLISH_TO_BRAILLE_SPECIAL["capital"])
                    is_capital = True
                    char = char.lower()
                    output.append(ENGLISH_TO_BRAILLE_LETTER[char])
                else:
                    char = char.lower()
                    output.append(ENGLISH_TO_BRAILLE_LETTER[char])
            else:
                is_capital = False
                char = char.lower()
                output.append(ENGLISH_TO_BRAILLE_LETTER[char])

        if not char.isalpha() and not char.isdigit():
            if char == " ":
                output.append(ENGLISH_TO_BRAILLE_SPECIAL[" "])
            elif not is_decimal:
                output.append(ENGLISH_TO_BRAILLE_SPECIAL["decimal"])
                is_decimal = True
                output.append(ENGLISH_TO_BRAILLE_DECIMAL[char])
            else:
                output.append(ENGLISH_TO_BRAILLE_DECIMAL[char])    
        else:
            is_decimal = False

        if char.isdigit():
            if not is_number:
                output.append(ENGLISH_TO_BRAILLE_SPECIAL["number"])
                is_number = True
                output.append(ENGLISH_TO_BRAILLE_NUMBER[char])
            else:
                output.append(ENGLISH_TO_BRAILLE_NUMBER[char])    
        else:
            is_number = False

    return "".join(output)

def main():
    if len(sys.argv) != 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)

    text = sys.argv[1]

    if is_braille(text):
        translated_text = translate_braille_to_english(text)
    else:
        translated_text = translate_english_to_braille(text)

    print(translated_text)

if __name__ == "__main__":
    main()
