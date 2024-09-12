import sys

# Braille translation table
BRAILLE_ALPHABET = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OOO...', 'e': 'O.O...',
    'f': 'OOOO..', 'g': 'OOOOO.', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OOO.O.', 'o': 'O.O.O.',
    'p': 'OOOOO.', 'q': 'OOOOOO', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OOO.OO',
    'z': 'O.O.OO', ' ': '......', '0': '.....O', '1': 'O.....', '2': 'O.O...', 
    '3': 'OO....', '4': 'OOO...', '5': 'O.O...', '6': 'OOOO..', '7': 'OOOOO.',
    '8': 'O.OO..', '9': '.OO...'
}

# Flipping the dictionary for Braille to English translation
BRAILLE_TO_ENGLISH = {v: k for k, v in BRAILLE_ALPHABET.items()}

def english_to_braille(text):
    return ''.join(BRAILLE_ALPHABET.get(char.lower(), '......') for char in text)

def braille_to_english(braille):
    return ''.join(BRAILLE_TO_ENGLISH.get(braille[i:i+6], '?') for i in range(0, len(braille), 6))

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <mode> <text>")
        print("Mode should be 'english' or 'braille'")
        sys.exit(1)

    mode = sys.argv[1]
    input_text = ' '.join(sys.argv[2:])

    if mode == 'english':
        print(english_to_braille(input_text))
    elif mode == 'braille':
        print(braille_to_english(input_text))
    else:
        print("Invalid mode. Use 'english' or 'braille'.")

if __name__ == "__main__":
    main()
