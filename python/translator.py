
# Braille mappings (O for raised, . for unraised)
BRAILLE_ALPHABET = {
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
    " ": "......",  # Space character
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", 
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

# Reverse mapping from Braille to English
ENGLISH_ALPHABET = {value: key for key, value in BRAILLE_ALPHABET.items()}

# Special symbols
CAPITAL_PREFIX = ".....O"  # Capital letter indicator
NUMBER_PREFIX = ".O.OOO"   # Number indicator

# Detect if input is English or Braille
def detect_input_type(input_str):
    return 'braille' if all(c in 'O.' for c in input_str) else 'english'

# Translate English to Braille
def english_to_braille(text):
    result = ''
    for char in text:
        if char.isupper():
            result += CAPITAL_PREFIX + BRAILLE_ALPHABET[char.lower()]
        elif char.isdigit():
            result += NUMBER_PREFIX + BRAILLE_ALPHABET[char]
        else:
            result += BRAILLE_ALPHABET.get(char, '')
    return result

# Translate Braille to English
def braille_to_english(braille):
    result = ''
    i = 0
    while i < len(braille):
        braille_char = braille[i:i + 6]
        if braille_char == CAPITAL_PREFIX:
            i += 6
            braille_char = braille[i:i + 6]
            result += ENGLISH_ALPHABET[braille_char].upper()
        elif braille_char == NUMBER_PREFIX:
            i += 6
            braille_char = braille[i:i + 6]
            result += ENGLISH_ALPHABET[braille_char]
        else:
            result += ENGLISH_ALPHABET.get(braille_char, '')
        i += 6
    return result

# Main function to translate based on the input type
def translator(input_str):
    input_type = detect_input_type(input_str)
    if input_type == 'english':
        print(english_to_braille(input_str))
    else:
        print(braille_to_english(input_str))

# Example usage
if __name__ == "__main__":
    import sys
    input_str = " ".join(sys.argv[1:])
    translator(input_str)
