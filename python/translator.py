import sys

# Mapping of english to braille
ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..',
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', '.': '..OO.O', ',': '..O...',
    '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O',
    '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.', ' ': '......', 'cap': '.....O', 'dec': '.O...O', 'num': '.O.OOO'
}

# Mapping of numbers to braille
NUMBERS_TO_BRAILLE = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Mapping of braille to English
BRAILLE_TO_ENGLISH = {br: en for en, br in ENGLISH_TO_BRAILLE.items()}


# Mapping of braille to numbers
BRAILLE_TO_NUMBERS = {br: num for num, br in NUMBERS_TO_BRAILLE.items()}


def translate_braille_to_english(braille: str) -> str:
    """
    Params:
        - braille: str -> a string of braille characters

    Returns:
        - english_text: str -> a string of the inputted braille characters translated to english

    """
    english_text = ''
    is_num = False
    is_cap = False
    i = 0

    while i < len(braille):
        char = braille[i: i+6]
        translated = BRAILLE_TO_ENGLISH[char]

        if translated == 'cap':
            is_cap = True
        elif translated == 'num':
            is_num = True
        else:
            if is_cap:
                english_text += char.upper()
                is_cap = False
            elif is_num:
                english_text += NUMBERS_TO_BRAILLE[char]
            else:
                english_text += translated
                if translated == ' ':
                    is_num = False
        
        i = i + 6
    
    return english_text


def translate_english_to_braille(english: str) -> str:
    """
    Params:
        - english: str -> a string of english characters
    
    Returns:
        - braille_text: str -> a string of the inputted english text translated to braille
    """
    braille_text = ''
    is_num = False

    for char in english:
        if char.isupper():
            braille_text += ENGLISH_TO_BRAILLE['cap']
            braille_text += ENGLISH_TO_BRAILLE[char.lower()]
        elif char in NUMBERS_TO_BRAILLE:
            if not is_num:
                braille_text += ENGLISH_TO_BRAILLE['num']
                is_num = True
            braille_text += NUMBERS_TO_BRAILLE[char]
        else:
            if char == ' ':
                is_num = False
            braille_text += ENGLISH_TO_BRAILLE[char]
    
    return braille_text


def verify_braille(text: str) -> bool:
    """
    Params:
        - text: str -> a string of characters

    Returns true if the text is braille, false if the text is english
    """
    return len(text) % 6 == 0 and all(char == 'O' or char == '.' for char in text)


def main():
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
    else: 
        print('Improper usage')
    
    if verify_braille(text):
        print(translate_braille_to_english(text))
    else:
        print(translate_english_to_braille(text))


if __name__ == "__main__":
    main()
