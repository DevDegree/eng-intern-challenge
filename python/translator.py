import sys

CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"
SPACE_FOLLOWS = "......"

# Letters to Braille Mapping
LETTERS_TO_BRAILLE = {
    "a": "O.....",    "b": "O.O...",    "c": "OO....",    "d": "OO.O..",
    "e": "O..O..",    "f": "OOO...",    "g": "OOOO..",    "h": "O.OO..",
    "i": ".OO...",    "j": ".OOO..",    "k": "O...O.",    "l": "O.O.O.",
    "m": "OO..O.",    "n": "OO.OO.",    "o": "O..OO.",    "p": "OOO.O.",
    "q": "OOOOO.",    "r": "O.OOO.",    "s": ".OO.O.",    "t": ".OOOO.",
    "u": "O...OO",    "v": "O.O.OO",    "w": ".OOO.O",    "x": "OO..OO",
    "y": "OO.OOO",    "z": "O..OOO",    " ": "......"
}

# Number to Braille Mapping
NUMBERS_TO_BRAILLE = {
    "1": "O.....",    "2": "O.O...",    "3": "OO....",    "4": "OO.O..",
    "5": "O..O..",    "6": "OOO...",    "7": "OOOO..",    "8": "O.OO..",
    "9": ".OO...",    "0": ".OOO..",
}

BRAILLE_TO_ENG = {v: k for k, v in LETTERS_TO_BRAILLE.items()}
BRAILLE_TO_NUM = {v: k for k, v in NUMBERS_TO_BRAILLE.items()}

def translate_braille(braille_text):
    # Converts a Braille string to English text.
    result = []
    capital_mode, number_mode = False, False

    # Chunk the input into blocks of 6 characters
    braille_chunks = [braille_text[i:i + 6] for i in range(0, len(braille_text), 6)]

    for chunk in braille_chunks:
        if chunk == CAPITAL_FOLLOWS:
            capital_mode = True
            continue
        if chunk == NUMBER_FOLLOWS:
            number_mode = True
            continue
        if chunk == SPACE_FOLLOWS:
            result.append(" ")
            number_mode = False
            continue

        if number_mode:
            result.append(BRAILLE_TO_NUM.get(chunk, ""))
        else:
            letter = BRAILLE_TO_ENG.get(chunk, "")
            if capital_mode:
                result.append(letter.upper())
                capital_mode = False
            else:
                result.append(letter)

    return ''.join(result)

def translate_english(english_text):

    # Converts an English string to Braille text.
    result = []
    number_mode = False

    for char in english_text:
        if char.isupper():
            result.append(CAPITAL_FOLLOWS)
            result.append(LETTERS_TO_BRAILLE.get(char.lower(), ""))
        elif char.isdigit():
            if not number_mode:
                result.append(NUMBER_FOLLOWS)
                number_mode = True
            result.append(NUMBERS_TO_BRAILLE.get(char, ""))
        elif char == " ":
            result.append(SPACE_FOLLOWS)
            number_mode = False
        else:
            result.append(LETTERS_TO_BRAILLE.get(char, ""))
    
    return ''.join(result)

def identify_braille(input_text):

    # Checks if the input string is Braille.
    if len(input_text) % 6 != 0:
        return False
    return all(c in "O." for c in input_text) and "." in input_text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide input text to translate (English or Braille).")
        sys.exit(1)

    user_input = " ".join(sys.argv[1:])

    if identify_braille(user_input):
        print(translate_braille(user_input))
    else:
        print(translate_english(user_input))