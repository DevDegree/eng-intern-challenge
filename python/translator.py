import sys

# Braille to English map
BRAILLE_TO_ENG = {
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
    "......": " ",
    ".....O": "capital_follows",
    ".O.OOO": "number_follows",
}

BRAILLE_TO_NUMBER = {
    'O.....': '1', 
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0'
}

ENG_TO_BRAILLE = {v: k for k,v in BRAILLE_TO_ENG.items()}
NUMBER_TO_BRAILLE = {v: k for k,v in BRAILLE_TO_NUMBER.items()}

def tokenize_message(message: str) -> tuple[list[str], str]:
    '''
    Splits a message into a list of tokens and returns the language to which
    it corresponds. If the language is english, it returns the message as a
    list of characters. For braille, it returns a list of strings of len = 6.
    '''
    if len(message) % 6 != 0:
        return (list(message), "english")

    tokens: list[str] = []
    for i in range(0, len(message), 6):
        token = message[i:i+6]
        # cut tokenization early, translate as english
        if not all(ch in ("O", ".") for ch in token):
            return (list(message), "english")

        tokens.append(token)

    return (tokens, "braille")

def braille_to_english(tokens: list[str]) -> str:
    '''Translates a list of braille tokens to an english string.'''
    english_text: list[str] = []
    is_capital = False
    is_number = False

    for token in tokens:
        char = BRAILLE_TO_ENG[token]
        # special cases for modifiers
        if char == "capital_follows":
            is_capital = True
        elif char == "number_follows":
            is_number = True
        elif char == " ":
            is_number = False
            english_text.append(char)
        else:
            if is_capital:
                english_text.append(char.upper())
                is_capital = False
            elif is_number:
                english_text.append(BRAILLE_TO_NUMBER[token])
            else:
                english_text.append(char)

    return "".join(english_text)

def english_to_braille(message: list[str]) -> str:
    '''Translates a list of english characters to a braille string.'''
    braille_text: list[str] = []
    is_number = False

    for char in message:
        if char.isdigit():
            if not is_number:
                is_number = True
                braille_text.append(ENG_TO_BRAILLE['number_follows'])

            braille_text.append(NUMBER_TO_BRAILLE[char])
        elif char.isupper():
            braille_text.append(ENG_TO_BRAILLE['capital_follows'])
            braille_text.append(ENG_TO_BRAILLE[char.lower()])
        else:
            is_number = False
            braille_text.append(ENG_TO_BRAILLE[char])

    return "".join(braille_text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    input_string = ' '.join(sys.argv[1:])
    tokens, language = tokenize_message(input_string)

    if language == "braille":
        print(braille_to_english(tokens))
    else:
        print(english_to_braille(tokens))
            

