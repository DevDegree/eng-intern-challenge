import sys

ENG_TO_BRAILLE_ALPHABET = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......',

    # to indicate capital, decimal, or number follows
    'cap': '.....O', 'dec': '.O...O', 'num': '.O.OOO', 

    ',': '.O....', ';': '.OO...', ':': '.O.O..', '.': '.O.OO.', '!': '.OO.O.',
    '?': '.OO..O', '-': '..O.O.', '/': '.O.O..', '(': '.O.O.O', ')': 'O..O.O', 
    '<': 'OO...O', '>': '..OO.O', 
}

ENG_TO_BRAILLE_DIGITS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

BRAILLE_TO_ENG_ALPHABET = { braille: eng for eng, braille in ENG_TO_BRAILLE_ALPHABET.items() }
BRAILLE_TO_ENG_DIGITS = { braille: eng for eng, braille in ENG_TO_BRAILLE_DIGITS.items() }


"""
Check if a given string contains only "O" and "." characters (braille).
Inputs:
    str: input_str
Returns:
    bool
"""
def is_braille(input_str: str) -> bool:
    for letter in input_str:
        if letter != 'O' and letter != '.':
            return False
    
    return True


"""
Translate braille to english.
Inputs:
    str: input_str
Returns:
    str: english
"""
def translate_braille_to_eng(input_str: str) -> str:
    english = ""
    cap_follows = False
    num_follows = False
    
    for i in range(0, len(input_str), 6):
        braille_char = input_str[i:i+6]

        eng_char = BRAILLE_TO_ENG_ALPHABET[braille_char]

        if eng_char == 'cap':
            cap_follows = True

        elif eng_char == 'num':
            num_follows = True
        
        elif eng_char == ' ':
            english += eng_char
            num_follows = False

        elif num_follows:
            english += BRAILLE_TO_ENG_DIGITS[braille_char]
        
        elif cap_follows:
            english += eng_char.upper()
            cap_follows = False
        
        else:
            english += eng_char

    return english


"""
Translate english to braille.
Inputs:
    str: input_str
Returns:
    str: braille
"""
def translate_eng_to_braille(input_str: str) -> str:
    braille = ""
    num_follows = False

    for eng_char in input_str:
        if eng_char.isdigit():
            if num_follows:
                braille += ENG_TO_BRAILLE_DIGITS[eng_char]
            else:
                braille += ENG_TO_BRAILLE_ALPHABET['num'] + ENG_TO_BRAILLE_DIGITS[eng_char]
                num_follows = True

        elif eng_char.isupper():
            braille += ENG_TO_BRAILLE_ALPHABET['cap'] + ENG_TO_BRAILLE_ALPHABET[eng_char.lower()]
        
        elif eng_char == ' ':
            braille += ENG_TO_BRAILLE_ALPHABET[' ']
            num_follows = False
        
        else:
            braille += ENG_TO_BRAILLE_ALPHABET[eng_char]
    
    return braille


if __name__ == "__main__":
    input_str = " ".join(sys.argv[1:])

    if is_braille(input_str):
        output_str = translate_braille_to_eng(input_str)
    else:
        output_str = translate_eng_to_braille(input_str)

    print(output_str)
