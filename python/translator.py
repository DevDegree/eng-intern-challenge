# English to Braille dictionary
ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    'A': '.....OO.....', 'B': '.....OO.O...', 'C': '.....OOO....', 'D': '.....OOO.O..', 
    'E': '.....O..O..', 'F': '.....OOO...', 'G': '.....OOOO..', 'H': '.....O.OO..', 
    'I': '.....O..O..', 'J': '.....O.OOO..', ' ': '......', # Braille for space
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Braille to English dictionary
BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}

# Function to convert English text to Braille
def to_braille(text):
    return ''.join(ENGLISH_TO_BRAILLE[char] for char in text if char in ENGLISH_TO_BRAILLE)

# Function to convert Braille text to English
def to_english(braille):
    braille_chars = [braille[i:i+6] for i in range(0, len(braille), 6)]
    return ''.join(BRAILLE_TO_ENGLISH.get(char, '') for char in braille_chars)

# Main logic to determine input type and convert
if __name__ == "__main__":
    import sys
    input_text = sys.argv[1] if len(sys.argv) > 1 else ""
    output = ""

    if input_text:
        if input_text.startswith('O') or input_text.startswith('.'):
            # Assuming it is Braille
            output = to_english(input_text)
        else:
            # Assuming it is English
            output = to_braille(input_text)

    print(output)

