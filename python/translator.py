import sys

# Define Braille mappings as per the challenge (O = raised dot, . = flat)
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '.O.OOO': '1', '..O...': '2', 'O.OOOO': '3', 'O...O.': '4',
    '......': ' '  # Space
    # add more mappings for punctuation here as needed
}

# Generate the reverse mapping from English to Braille
english_to_braille = {v: k for k, v in braille_to_english.items()}

def translate_to_braille(text):
    braille_translation = ''
    for char in text.lower():
        if char in english_to_braille:
            braille_translation += english_to_braille[char]
        else:
            braille_translation += ' '  # Space for unknown characters
    return braille_translation

def translate_to_english(braille):
    english_translation = ''
    braille_chars = [braille[i:i+6] for i in range(0, len(braille), 6)]
    for char in braille_chars:
        if char in braille_to_english:
            english_translation += braille_to_english[char]
        else:
            english_translation += ' '  # Space for unknown characters
    return english_translation

def main():
    # Read input from command-line arguments
    input_text = ' '.join(sys.argv[1:])

    # Detect if the input is Braille (length of 6 characters per symbol and made up of O and .)
    if all(c in 'O.' for c in input_text) and len(input_text) % 6 == 0:
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))

if __name__ == "__main__":
    main()
