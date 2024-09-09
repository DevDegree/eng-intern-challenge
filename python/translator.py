import sys

# --- Constants ---
ALPHA_TO_BRAILLE = {
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
}

NUMBER_TO_BRAILLE = {
    "0": ".OOO..",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
}

BRAILLE_TO_ENGLISH = {v: k for k, v in ALPHA_TO_BRAILLE.items()}
BRAILLE_TO_NUMBER = {v: k for k, v in NUMBER_TO_BRAILLE.items()}

CAPITAL_TO_BRAILLE = ".....O"
NUMBER_FOLLOWS_TO_BRAILLE = ".O.OOO"
SPACE = "......"

# --- Helper Functions ---
def is_english(input_string: str) -> bool:
    """
    Returns True if the input string is in English, False otherwise.
    Takes advantage of the fact that English input strings would contain only letters and numbers, so any periods would indicate a Braille string.
    """
    return "." not in input_string

def english_to_braille(input_string: str) -> str:
    """
    Converts an English string to a Braille string.
    """
    braille_string = ""
    is_number = False

    for char in input_string:
        if char.isalpha():
            if char.isupper():
                braille_string += CAPITAL_TO_BRAILLE
            braille_string += ALPHA_TO_BRAILLE[char.lower()]
        elif char.isdigit():
            if not is_number:
                is_number = True
                braille_string += NUMBER_FOLLOWS_TO_BRAILLE
            braille_string += NUMBER_TO_BRAILLE[char]
        elif char == " ":
            braille_string += SPACE
            is_number = False
    return braille_string

def braille_to_english(input_string: str) -> str:
    """
    Converts a Braille string to an English string.
    """
    grouped_input = [input_string[i:i+6] for i in range(0, len(input_string), 6)]
    english_string = ""
    is_capital = False
    is_number = False
    for braille in grouped_input:
        if braille == CAPITAL_TO_BRAILLE:
            is_capital = True
        elif braille == NUMBER_FOLLOWS_TO_BRAILLE:
            is_number = True
        elif braille == SPACE:
            english_string += " "
            is_number = False
        elif is_number:
            english_string += BRAILLE_TO_NUMBER[braille]
        elif is_capital:
            english_string += BRAILLE_TO_ENGLISH[braille].upper()
            is_capital = False
        else:
            english_string += BRAILLE_TO_ENGLISH[braille]
    
    return english_string

# --- App ---

def main():
    assert len(sys.argv) >= 2
    args = sys.argv[1:]
    string = ' '.join(args)
    
    if is_english(string):
        print(english_to_braille(string))
    else:
        print(braille_to_english(string))

if __name__ == "__main__":
    main()