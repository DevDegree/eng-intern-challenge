import sys

# Mapping from braille to English alphabet
BRAILLE_TO_ENGLISH_MAP = {
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
    ".....O": "capital",
    ".O.OOO": "number"
}

# Mapping from braille to numbers
BRAILLE_TO_NUMBER_MAP = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0"
}

# Reverse mappings for English to braille
ENGLISH_TO_BRAILLE_MAP = {value: key for key, value in BRAILLE_TO_ENGLISH_MAP.items()}
NUMBER_TO_BRAILLE_MAP = {value: key for key, value in BRAILLE_TO_NUMBER_MAP.items()}

def convert_braille_to_english(braille_text):
    english_text = ""
    # Split braille text into 6-character tokens
    tokens = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]
    is_capital = False
    is_number = False

    for token in tokens:
        if BRAILLE_TO_ENGLISH_MAP[token] == "capital":
            is_capital = True
            continue
        elif BRAILLE_TO_ENGLISH_MAP[token] == "number":
            is_number = True
            continue
        elif BRAILLE_TO_ENGLISH_MAP[token] == " ":
            is_number = False

        if is_number:
            english_text += BRAILLE_TO_NUMBER_MAP[token]
        elif is_capital:
            english_text += BRAILLE_TO_ENGLISH_MAP[token].upper()
            is_capital = False
        else:
            english_text += BRAILLE_TO_ENGLISH_MAP[token]

    return english_text

def convert_english_to_braille(english_text):
    braille_text = ""
    is_number = False

    for char in english_text:
        if char == " ":
            is_number = False
            braille_text += ENGLISH_TO_BRAILLE_MAP[" "]
        elif char.isdigit():
            # Add number symbol if the previous character was not a number
            if not is_number:
                is_number = True
                braille_text += ENGLISH_TO_BRAILLE_MAP["number"]
            braille_text += NUMBER_TO_BRAILLE_MAP[char]
        elif char.isupper():
            braille_text += ENGLISH_TO_BRAILLE_MAP["capital"] + ENGLISH_TO_BRAILLE_MAP[char.lower()]
        else:
            braille_text += ENGLISH_TO_BRAILLE_MAP[char]
    
    return braille_text

def is_braille_text(text):
    # Check if the text contains only 'O' and '.' characters and its length is a multiple of 6
    return all(char in "O." for char in text) and len(text) % 6 == 0

if __name__ == "__main__":
    input_text = ' '.join(sys.argv[1:])
    if is_braille_text(input_text):
        print(convert_braille_to_english(input_text))
    else:
        print(convert_english_to_braille(input_text))

