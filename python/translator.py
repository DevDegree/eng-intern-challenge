
BRAILLE_DICT = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

CAPITAL_MARKER = '.....O'  

REVERSE_BRAILLE_DICT = {v: k for k, v in BRAILLE_DICT.items()}


def english_to_braille(text):
    braille = ""
    for char in text:
        if char.isupper():  
            braille += CAPITAL_MARKER
            char = char.lower()
        braille += BRAILLE_DICT.get(char, '......') 
    return braille


def braille_to_english(braille_text):
    english = ""
    i = 0
    while i < len(braille_text):
        braille_char = braille_text[i:i+6]
        if braille_char == CAPITAL_MARKER:
            i += 6
            braille_char = braille_text[i:i+6]
            english += REVERSE_BRAILLE_DICT.get(braille_char, ' ').upper()
        else:
            english += REVERSE_BRAILLE_DICT.get(braille_char, ' ')
        i += 6
    return english

if __name__ == "__main__":
    import sys
    input_text = " ".join(sys.argv[1:])
    
    if all(c in 'O.' for c in input_text):
        print(braille_to_english(input_text))  
    else:
        print(english_to_braille(input_text)) 

