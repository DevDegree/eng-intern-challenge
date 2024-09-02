import sys

# all mappings
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO...O': 'c', 'OO.O.O': 'd', 'O.O.O.': 'e',
    'O..OO.': 'f', 'O..OOO': 'g', 'O..O.O': 'h', '.O.O.O': 'i', '.O.OOO': 'j',
    'O...O.': 'k', 'O.O..O': 'l', 'OO...O': 'm', 'OO.O.O': 'n', 'O.O.O.': 'o',
    'O..OO.': 'p', 'O..OOO': 'q', 'O..O.O': 'r', '.O.O.O': 's', '.O.OOO': 't',
    'O...O.': 'u', 'O.O..O': 'v', '.O.O.O': 'w', 'OO...O': 'x', 'OO.O.O': 'y',
    'O.O.O.': 'z', '......': ' ', # space
    # numbers
    '.....O.': '1', '.....OO': '2', '.....O.O': '3', '.....O.OO': '4', '.....O.O.': '5',
    '.....OOO': '6', '.....OOOO': '7', '.....OO.O': '8', '.....O.OOO': '9', '.....O....': '0'
}

english_to_braille = {v: k for k, v in braille_to_english.items()}

def translate_to_braille(text):
    braille = ""
    for char in text:
        if char.lower() in english_to_braille:
            braille += english_to_braille[char.lower()]
        elif char == ' ':
            braille += '......'
        else:
            braille += '' 
    return braille

def translate_to_english(braille):
    english = ""
    for i in range(0, len(braille), 6):
        char = braille[i:i+6]
        if char in braille_to_english:
            english += braille_to_english[char]
        elif char == '......':
            english += ' '
    return english

def is_braille(text):
    return 'O' in text or '.' in text

def main():
    if len(sys.argv) != 2:
        print('Error! Please use: python3 translator.py "text"')
        sys.exit(1)
    
    text = sys.argv[1]

    if is_braille(text):
        print(translate_to_english(text))
    else:
        print(translate_to_braille(text))

if __name__ == "__main__":
    main()
