import sys
import re

CAPITAL_FOLLOWS = ".....O"
NUMBERS_FOLLOW = ".O.OOO"
ALPHABET_BRAILLE_MAP = {
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
    " ": "......"
}
NUMBERS_BRAILLE_MAP = {
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
}
BRAILE_ALPHABET_MAP = {value: key for key, value in ALPHABET_BRAILLE_MAP.items()}
BRAILE_NUMBERS_MAP = {value: key for key, value in NUMBERS_BRAILLE_MAP.items()}

def braille_to_english(braille):
    english = ""
    capitalize = False
    numbers = False
    for i in range(0, len(braille), 6):
        braille_code = braille[i:i+6]
        # Continue (likely end) the loop if there are any index errors
        if not braille_code:
            continue
        # Continue onto next character and flag capitalization
        if braille_code == CAPITAL_FOLLOWS:
            capitalize = True
            continue
        # Continue onto next character and flag numbers
        if braille_code == NUMBERS_FOLLOW:
            numbers = True
            continue
        # Unflag numbers
        if braille_code == ALPHABET_BRAILLE_MAP[" "]:
            numbers = False
        if numbers:
            english += BRAILE_NUMBERS_MAP[braille_code]
        else:
            english += BRAILE_ALPHABET_MAP[braille_code].upper() if capitalize else BRAILE_ALPHABET_MAP[braille_code]
        capitalize = False
    return english

def english_to_braille(english):
    braille = ""
    numbers = False
    for character in english:
        if character.isnumeric():
            # Add NUMBERS_FOLLOW braille code if numbers are to be added
            if not numbers:
                braille += NUMBERS_FOLLOW
                numbers = True
            braille += NUMBERS_BRAILLE_MAP[character]
        else:
            if character.isupper():
                braille += CAPITAL_FOLLOWS
            #Reset flag for numbers once space is reached
            if character == " ":
                numbers = False
            braille += ALPHABET_BRAILLE_MAP[character.lower()]
    return braille

# Main function
def main():
    user_input = " ".join(sys.argv[1:])
    if not user_input:
        return
    is_braille = bool(re.match(r"^(O|\.)+$", user_input))
    if is_braille:
        print(braille_to_english(user_input))
    else:
        print(english_to_braille(user_input))

main()