import sys

ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}
NUMBERS_TO_BRAILLE = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}
BRAILLE_SPECIAL = {
    'capital_follows': '.....O', 'number_follows': '.O.OOO',
}
BRAILLE_TO_ENGLISH = {eng: braille for braille, eng in ENGLISH_TO_BRAILLE.items()}
BRAILLE_TO_NUMBERS = {num: braille for braille, num in NUMBERS_TO_BRAILLE.items()}

def is_braille(string: str) -> bool:
    if(len(string) % 6 != 0): return False
    for c in string:
        if(c not in ".O"):
            return False
    return True

def english_to_braille(english: str) -> str:
    final = []
    is_number = False
    for c in english:
        if c.isdigit():
            if not is_number:
                final.append(BRAILLE_SPECIAL['number_follows'])
                is_number = True
            final += NUMBERS_TO_BRAILLE[c]
        else:
            if c.isupper():
                final.append(BRAILLE_SPECIAL['capital_follows'])

            final.append(ENGLISH_TO_BRAILLE[c.lower()])
            is_number = False
    
    return "".join(final)

def braille_to_english(braille: str) -> str:
    final = []
    is_number = False
    is_captial = False

    for i in range(0, len(braille), 6):
        char = braille[i:i+6]
        if(char == BRAILLE_SPECIAL['capital_follows']): is_captial = True
        elif(char == BRAILLE_SPECIAL['number_follows']): is_number = True
        else:
            if is_number:
                if(char == ENGLISH_TO_BRAILLE[' ']):
                    is_number = False
                    final.append(" ")
                else:
                    final.append(BRAILLE_TO_NUMBERS[char])
            else:
                if(is_captial): final.append(ENGLISH_TO_BRAILLE[char].upper())
                else: final.append(ENGLISH_TO_BRAILLE[char])
                is_captial = False

    return "".join(final)

def main():
    args = sys.argv[1:]
    to_translate = " ".join(args)
    
    if is_braille(to_translate): print(braille_to_english(to_translate))
    else: print(english_to_braille(to_translate))