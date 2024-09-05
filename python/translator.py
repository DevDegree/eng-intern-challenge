BRAILLE_TO_CHARACTER = {
    "O.....": "a", "O.O...": "b", "OO....": "c",
    "OO.O..": "d", "O..O..": "e", "OOO...": "f",
    "OOOO..": "g", "O.OO..": "h", ".OO...": "i",
    ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
    ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u",
    "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z", "......": " ",
}

BRAILLE_TO_DIGIT = {
    "O.....": "1", "O.O...": "2", "OO....": "3",
    "OO.O..": "4", "O..O..": "5", "OOO...": "6",
    "OOOO..": "7", "O.OO..": "8", ".OO...": "9",
    ".OOO..": "0",
}

CHARACTER_TO_BRAILLE = {char: braille_char for braille_char, char in BRAILLE_TO_CHARACTER.items()}
DIGIT_TO_BRAILLE = {digit: braille_char for braille_char, digit in BRAILLE_TO_DIGIT.items()}

CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"
SPACE = CHARACTER_TO_BRAILLE[" "]

def translate_to_english(text) -> str:
    """Translates braille text to English. Returns translated text in English."""
    characters = []
    capital_follows = False
    number_follows = False

    for i in range(0, len(text), 6):
        braille_character = text[i:i+6]

        if braille_character == CAPITAL_FOLLOWS:
            capital_follows = True
        elif braille_character == NUMBER_FOLLOWS:
            number_follows = True
        elif braille_character == SPACE:
            characters.append(" ")
            number_follows = False
        elif number_follows:
            digit = BRAILLE_TO_DIGIT[braille_character]
            characters.append(digit)
        else:
            character = BRAILLE_TO_CHARACTER[braille_character]
            cased_character = character.upper() if capital_follows else character.lower()
            characters.append(cased_character)
            capital_follows = False
            
    return "".join(characters)

def translate_to_braille(text: str) -> str:
    """Translates English text to braille. Returns translated text in braille."""
    previous_character = None
    braille_characters = []

    for character in text:
        if character.isdigit():
            first_digit_of_number = not previous_character or not previous_character.isdigit()
            if first_digit_of_number:
                braille_characters.append(NUMBER_FOLLOWS)
            braille_characters.append(DIGIT_TO_BRAILLE[character])
        else:
            if character.isupper():
                braille_characters.append(CAPITAL_FOLLOWS)
            lowercased_character = character.lower()
            braille_characters.append(CHARACTER_TO_BRAILLE[lowercased_character])
        previous_character = character

    return "".join(braille_characters)