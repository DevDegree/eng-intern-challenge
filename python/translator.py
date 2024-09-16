import sys

CONTROL_CHARACTERS = {
    "NUMBER_FOLLOWS": ".O.OOO",
    "CAPITAL_FOLLOWS": ".....O",
    "DECIMAL_FOLLOWS": ".O...O",

    ".O.OOO": "NUMBER_FOLLOWS",
    ".....O": "CAPITAL_FOLLOWS",
    ".O...O": "DECIMAL_FOLLOWS",
}

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
    ".0000.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
}

BRAILLE_TO_SYMBOLS = {
    "..OO.O": "." ,
    "..O...": ",",
    "..O.OO": "?",
    "..O.OO": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O..OO.": ">",
    "O.O..O": "(",
    ".0.00.": ")",
    "......": " ",
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8" ,
    ".OO...": "9",
    ".OOO..": "0",
    "......": " ",
}

ENGLISH_TO_BRAILLE  = {}


def english_to_braille(text: str) -> str:
    """
    Translate from English to Braille
    :param str text: The text being translated from English to Braille
    :return: The translated Braille text as a 6 character string reading left to right, line by line, starting at the top left
    """
    ret = ""
    numeric = False

    for character in text:
        if character.isupper():
            ret += CONTROL_CHARACTERS["CAPITAL_FOLLOWS"]
            character = character.lower()

        if character.isnumeric() and not numeric:
            numeric = True
            ret += CONTROL_CHARACTERS["NUMBER_FOLLOWS"]

        if character == " ":
            numeric = False

        ret += ENGLISH_TO_BRAILLE[character]
    return ret


def braille_to_english(braille: str) -> str:
    """
    Translate from Braille to English
    :param str text: The text being translated from Braille to English
    :return: The translated English text
    """
    braille = [braille[i:i+6] for i in range(0, len(braille), 6)]
    ret = ""
    numeric = False
    capital = False
    for character in braille:

        # Process control characters first and mark the respective flag
        if character in CONTROL_CHARACTERS:
            if CONTROL_CHARACTERS[character] == "CAPITAL_FOLLOWS":
                capital = True
            if CONTROL_CHARACTERS[character] == "NUMBER_FOLLOWS":
                numeric = True
        else:
            if character == "......":
                # Reset the numeric flag if it is a space
                numeric = False
                ret += BRAILLE_TO_SYMBOLS[character]
            
            elif numeric:
                ret += BRAILLE_TO_SYMBOLS[character]
            elif capital:
                ret += BRAILLE_TO_ENGLISH[character].upper()
                capital = False
                
            else:
                ret += BRAILLE_TO_ENGLISH[character]
            
    return ret


def translate(text: str) -> str:
    """
    Detect whether text is Braille or English and translate to the other
    :param str text: The text being translated
    :return: The translated English or Braille text
    """
    if set(text) <= set(".O"):
        # Since text only consists of "O" and ".", it's braille and translate to English
        return braille_to_english(text)
    else:
        # Otherwise translate to Braille
        return english_to_braille(text)

if __name__ == "__main__":
    if len(sys.argv) > 1:

        # Inverse dictionary generated at runtime to keep readability as only one dictionary needs to be maintained
        for key, value in BRAILLE_TO_ENGLISH.items() | BRAILLE_TO_SYMBOLS.items():
            ENGLISH_TO_BRAILLE[value] = key

        text = " ".join(sys.argv[1:])
        print(translate(text))