import sys

braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO...O': 'd',
    'O..O..': 'e', 'OOO...': 'f', 'OOO..O': 'g', 'O.O..O': 'h',
    'O..O..': 'i', 'O...OO': 'j', 'O..O.O': 'k', 'OO.O..': 'l',
    'OO..O.': 'm', 'OO.O.O': 'n', 'O...O.': 'o', 'OOO.O.': 'p',
    'OOO..O': 'q', 'O.O.O.': 'r', 'O..OO.': 's', 'O...O.': 't',
    'O..O.O': 'u', 'OO.O.O': 'v', 'O...OO': 'w', 'O.O..O': 'x',
    'O.O.O.': 'y', 'O..OO.': 'z', '.O....': ' ',  # space
    '.O..O.': '1', '.O.O..': '2', '.OO...': '3', 
    '.OO..O': '4', '.O..O.': '5', '.OOO..': '6', 
    '.OOO.O': '7', '.O.O..': '8', '.O..O.': '9', 
    '.O...O': '0'
}

english_to_braille = {v: k for k, v in braille_to_english.items()}

def translate_braille_to_english(braille_string):
    return ''.join(braille_to_english.get(braille_string[i:i+6], '') for i in range(0, len(braille_string), 6))

def translate_english_to_braille(english_string):
    return ''.join(english_to_braille.get(char, '.') for char in english_string.lower())

def main():
    if len(sys.argv) != 2:
        print("Usage: python translator.py <string>")
        return
    
    input_string = sys.argv[1]

    # Check if input string is Braille or English
    if all(c in 'O.' for c in input_string):
        # It's Braille
        translated = translate_braille_to_english(input_string)
    else:
        # It's English
        translated = translate_english_to_braille(input_string)
    
    print(translated)

if __name__ == "__main__":
    main()

