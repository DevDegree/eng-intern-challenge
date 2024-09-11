
import sys

# Mappings
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO'
}

englishNumbers_to_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', 
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', 
    '9': '.OO...', '0': '.OOO..'
}

englishSymbols_to_braille = {
    ' ': '......', '.': '..OO.O', "'": '..O...', '?': '..O.OO',
    '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO', 
    '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', 
    ')': '.O.OO.'
}


braille_to_english = {v: k for k, v in english_to_braille.items()}
brailleNumbers_to_english = {v: k for k, v in englishNumbers_to_braille.items()}
brailleSymbols_to_english = {v: k for k, v in englishSymbols_to_braille.items()}


capital_follows = '.....O'
decimal_follows = '.O...O'
number_follows = '.O.OOO'
braille_characters = ['O', '.']


def is_braille(input_string):
    return all(char in braille_characters for char in input_string)


def english_to_braille_translator(english_string):
    braille_translation = []
    number_mode = False 

    for char in english_string:
        if char.isupper():
            braille_translation.append(capital_follows)
            char = char.lower()
        if char in english_to_braille: 
            braille_translation.append(english_to_braille[char]) 
        elif char in englishSymbols_to_braille:
            if char == ' ': number_mode = False
            braille_translation.append(englishSymbols_to_braille[char])        
        elif char in englishNumbers_to_braille:
            braille_translation.append(number_follows) if number_mode == False else None
            number_mode = True
            braille_translation.append(englishNumbers_to_braille[char])

    return ''.join(braille_translation)


def braille_to_english_translator(braille_string):
    english_translation = []
    character_chunks = [braille_string[i:i+6] for i in range(0, len(braille_string), 6)]
    number_mode = False
    decimal_mode = False
    capitalize = False
    space_character = englishSymbols_to_braille[' ']
    dot_character = englishSymbols_to_braille['.']

    for chunk in character_chunks:
        space_is_read = chunk == space_character

        if chunk == capital_follows:
            capitalize = True
            continue
        elif chunk == number_follows: 
            number_mode = True
            continue
        elif chunk == decimal_follows: 
            decimal_mode = True
            continue
        elif space_is_read:
            # reset number and decimal mode
            number_mode = False
            decimal_mode = False
        
        if number_mode:
            english_translation.append(brailleNumbers_to_english[chunk])
        elif decimal_mode:
            if chunk in brailleNumbers_to_english:
                english_translation.append(brailleNumbers_to_english[chunk])

            # decimal number has two integer parts seperated by a dot
            elif chunk == dot_character:
                english_translation.append(brailleSymbols_to_english[dot_character])

        elif chunk in braille_to_english or chunk in brailleSymbols_to_english:
            setInWhichLetterIsFound = braille_to_english if chunk in braille_to_english else brailleSymbols_to_english
            letter = setInWhichLetterIsFound[chunk].upper() if capitalize else setInWhichLetterIsFound[chunk]
            capitalize = False
            english_translation.append(letter)

    return ''.join(english_translation)
              

def main():
    if len(sys.argv) < 2:
        print("Error: No input string provided!")
        sys.exit(1)
    
    for input_string in sys.argv[1:]:
        if is_braille(input_string):
            print(braille_to_english_translator(input_string))
        else:
            print(english_to_braille_translator(input_string))



# ------------- MAIN EXECUTION -------------
main()