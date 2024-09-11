import sys
# mapping of braille to english
BRAILLE_TO_ENGLISH = {
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

# mapping of braille to number
BRAILLE_TO_NUMBER = {
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

# reverses BRAILLE_TO_ENGLISH
ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}

# reverses BRAILLE_TO_NUMBER
NUMBER_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_NUMBER.items()}

def braille_to_english(braile):
    output = ""
    # split the braile into 6 character tokens
    tokens = [braile[i:i+6] for i in range(0, len(braile), 6)]
    capital = False
    number = False
    for token in tokens:
        if BRAILLE_TO_ENGLISH[token] == "capital":
            capital = True
            continue
        elif BRAILLE_TO_ENGLISH[token] == "number":
            number = True
            continue
        elif BRAILLE_TO_ENGLISH[token] == " ":
            number = False
        
        if number:
            output += BRAILLE_TO_NUMBER[token]
        elif capital:
            output += BRAILLE_TO_ENGLISH[token].upper()
            capital = False
        else:
            output += BRAILLE_TO_ENGLISH[token]
    
    return output

def english_to_braille(english):
    output = ""
    number = False
    for char in english:
        if char == " ":
            number = False
            output += ENGLISH_TO_BRAILLE[" "]
        elif char.isnumeric():
            # if the previous character was not a number, add the number symbol
            if not number:
                number = True
                output += ENGLISH_TO_BRAILLE["number"]
            output += NUMBER_TO_BRAILLE[char]
        elif char.isupper():
            output += ENGLISH_TO_BRAILLE["capital"] + ENGLISH_TO_BRAILLE[char.lower()]
        else:
            output += ENGLISH_TO_BRAILLE[char]
    return output

def is_braille(text):
    # checks if there are only O and . in the text and the length is a multiple of 6
    return all([c in "O." for c in text]) and len(text) % 6 == 0

if __name__ == "__main__":
    text = ' '.join(sys.argv[1:])
    if is_braille(text):
        print(braille_to_english(text))
    else:
        print(english_to_braille(text))