"""
Shopify Eng Intern Challenge Fall - Winter 2025

Name: Falak Rastogi
Email: falakrast1@gmail.com

Terminal / command-line application that can translate Braille to English and vice versa.
"""

# Braille dictionary to convert English to Braille
braille_dict = {

    # alphabets
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

    # numbers
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

    # additionals
    " ": "......",
    "capital_follows": ".....O",
    "number_follows": ".O.OOO"
}


# English dictionary to convert Braille to English
english_dict = {braille: eng for eng, braille in braille_dict.items()}


# .......................

ENGLISH_TO_BRAILLE = {
    # This dictionary maps English characters to their
    # corresponding Braille characters
    'A': 'O.....',
    'B': 'O.O...',
    'C': 'OO....',
    'D': 'OO.O..',
    'E': 'O..O..',
    'F': 'OOO...',
    'G': 'OOOO..',
    'H': 'O.OO..',
    'I': '.OO...',
    'J': '.OOO..',
    'K': 'O...O.',
    'L': 'O.O.O.',
    'M': 'OO..O.',
    'N': 'OO.OO.',
    'O': 'O..OO.',
    'P': 'OOO.O.',
    'Q': 'OOOOO.',
    'R': 'O.OOO.',
    'S': '.OO.O.',
    'T': '.OOOO.',
    'U': 'O...OO',
    'V': 'O.O.OO',
    'W': '.OOO.O',
    'X': 'OO..OO',
    'Y': 'OO.OOO',
    'Z': 'O..OOO',
    ' ': '......'  # Space
}

NUMBERS_TO_BRAILLE = {
    # This dictionary maps numbers to their
    # corresponding Braille characters
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
}

# Reverses dictionaries
BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}
BRAILLE_TO_NUMBERS = {v: k for k, v in NUMBERS_TO_BRAILLE.items()}



# ......................................

# Function to translate English to Braille
def translate_to_braille(text: str) -> str:
    """Translates English input text to braille and returns a string of braille characters"""

    result = []
    number_mode = False
    for char in text:
        if char.isdigit() and not number_mode:
            number_mode = True
            result.append(braille_dict["number_follows"])
        elif not char.isdigit() and number_mode:
            number_mode = False

        if char.isupper():
            result.append(braille_dict["capital_follows"])
            result.append(braille_dict[char.lower()])
        else:
            result.append(braille_dict[char.lower()])

    return "".join(result)


# Function to translate Braille to English
def translate_to_english(text: str) -> str:
    """Translates Braille input to English and returns a string of English characters"""

    result = []
    i = 0
    length = len(text)
    number_mode = False

    while i < length:
        chunk = text[i:i+6]
        if chunk == braille_dict["capital_follows"]:
            i += 6
            chunk = text[i:i+6]
            result.append(BRAILLE_TO_ENGLISH[chunk].upper())
        elif chunk == braille_dict["number_follows"]:
            number_mode = True
        elif chunk == '......':
            number_mode = False
            result.append(BRAILLE_TO_ENGLISH[chunk])
        else:
            if number_mode:
                result.append(BRAILLE_TO_NUMBERS[chunk])
            else:
                result.append(BRAILLE_TO_ENGLISH[chunk].lower())

        i += 6
    return "".join(result)

if __name__ == '__main__':
    answer1 = translate_to_braille("Abc 123")
    print(answer1)
    answer2 = translate_to_english(answer1)
    print(answer2 == "Abc 123")