import sys

# Braille to English mapping
BRAILLE_ALPHA = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", 
}

# Numbers mapping
BRAILLE_NUM = {
    "0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", 
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
}

# Symbols mapping
BRAILLE_SYMBOLS = {
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",
    ";": "..O.O.", "-": "....OO", "/": ".O..O.", "(": "O.O..O", ")": ".O.OO.",
}

# Special signals
CAPITAL = ".....O"
NUMBER = ".O.OOO"
SPACE = "......"

# Reverse dictionaries for English to Braille
ALPHA_TO_BRAILLE = {v: k for k, v in BRAILLE_ALPHA.items()}
NUM_TO_BRAILLE = {v: k for k, v in BRAILLE_NUM.items()}
SYMBOL_TO_BRAILLE = {v: k for k, v in BRAILLE_SYMBOLS.items()}

# Detect if the input is in Braille format
def is_braille(input_string):
    return all(c in "O." for c in input_string) and len(input_string) % 6 == 0

# Function to convert Braille to English
def braille_to_english(braille_input):
    output = []
    is_capital = False
    is_numeric = False
    characters = [braille_input[i:i+6] for i in range(0, len(braille_input), 6)]

    for char in characters:
        if char == CAPITAL:
            is_capital = True
        elif char == NUMBER:
            is_numeric = True
        elif char == SPACE:
            output.append(" ")
        elif is_numeric:
            output.append(NUM_TO_BRAILLE.get(char, ""))
            is_numeric = False
        else:
            letter = ALPHA_TO_BRAILLE.get(char, "")
            if is_capital:
                letter = letter.upper()
                is_capital = False
            output.append(letter)

    return ''.join(output)

# Function to convert English to Braille
def english_to_braille(english_input):
    output = []
    
    for char in english_input:
        if char.isupper():
            output.append(CAPITAL)
            char = char.lower()
        if char.isdigit():
            output.append(NUMBER)
            output.append(BRAILLE_NUM[char])
        elif char == " ":
            output.append(SPACE)
        elif char in BRAILLE_ALPHA:
            output.append(BRAILLE_ALPHA[char])
        elif char in BRAILLE_SYMBOLS:
            output.append(BRAILLE_SYMBOLS[char])

    return ''.join(output)

# Main function to handle input and output
def main():
    if len(sys.argv) < 2:
        print("Usage: python braille_translator.py <text>")
        return

    input_text = " ".join(sys.argv[1:])
    
    if is_braille(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))

if __name__ == "__main__":
    main()