import sys

ENGLISH_TO_BRAILLE = {
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
    " ": "......",
    "caps": ".....O",
    "numb": ".O.OOO",
}

NUM_TO_BRAILLE = {
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

BRAILLE_TO_ENGLISH = {braille: english for english, braille in ENGLISH_TO_BRAILLE.items()}
BRAILLE_TO_NUM     = {braille: num for num, braille in NUM_TO_BRAILLE.items()}


# Get input from the user from the terminal
def get_user_input() -> str:
    if (len(sys.argv)) < 2:
        sys.exit(0)
    return " ".join(sys.argv[1:])


# Check if the string is braille
def is_string_braille(strn: str) -> bool:
    return len(strn) % 6 == 0 and set(strn).issubset(["O", "."])


# Convert a given braille string to english
def convert_braille_to_english(braille: str) -> str:
    english = ""
    caps_lock = False
    num_lock = False
    for i in range(0, len(braille), 6):
        braille_char = braille[i : i + 6]
        # Handle caps-lock
        if braille_char == ENGLISH_TO_BRAILLE["caps"]:
            caps_lock = True
        # Handle num-lock
        elif braille_char == ENGLISH_TO_BRAILLE["numb"]:
            num_lock = True
        # Handle space character
        elif braille_char == ENGLISH_TO_BRAILLE[" "]:
            english += BRAILLE_TO_ENGLISH[braille_char]
            num_lock = False
        # Handle upper-case alphabets
        elif caps_lock:
            english += BRAILLE_TO_ENGLISH[braille_char].upper()
            caps_lock = False
        # Handle numbers
        elif num_lock:
            english += BRAILLE_TO_NUM[braille_char]
        # Handle lower-case alphabets
        else:
            english += BRAILLE_TO_ENGLISH[braille_char]
    return english


# Convert a given english string to braille
def convert_english_to_braille(english: str) -> str:
    braille = ""
    num_lock = False
    for char in english:
        # Handle alphabets
        if char.isalpha():
            if char.isupper():
                braille += ENGLISH_TO_BRAILLE["caps"]
            braille += ENGLISH_TO_BRAILLE[char.lower()]
        # Handle the space character
        elif char.isspace():
            braille += ENGLISH_TO_BRAILLE[char]
            num_lock = False
        # Handle numbers
        else:
            if not num_lock:
                braille += ENGLISH_TO_BRAILLE["numb"]
                num_lock = True
            braille += NUM_TO_BRAILLE[char]
    return braille


def main():
    user_sentence = get_user_input()
    if is_string_braille(user_sentence):
        print(convert_braille_to_english(user_sentence))
    else:
        print(convert_english_to_braille(user_sentence))


if __name__ == "__main__":
    main()
