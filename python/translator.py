import sys

# numbers reuse letter codes in this setup,
# so let's keep them separate

ENGLISH_TO_BRAILLE = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    'capital': '.....O',
    'decimal': '.O...O',
    'number': '.O.OOO',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    'space': '......'
}

NUMBER_TO_BRAILLE = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

# Create reverse dictionaries for Braille to English
BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items() if k not in ['capital', 'decimal', 'number']}
BRAILLE_TO_NUMBER = {v: k for k, v in NUMBER_TO_BRAILLE.items()}
SPECIAL_BRAILLE = {
    'capital': ENGLISH_TO_BRAILLE['capital'],
    'number': ENGLISH_TO_BRAILLE['number'],
    'space': ENGLISH_TO_BRAILLE['space']
}

def english_to_braille(text):

    # iterate over english string, checking if set to use numbers
    braille = []
    number_mode = False

    for i, char in enumerate(text):

        # check if special tokens need to be added

        if char == ' ':
            braille.append(ENGLISH_TO_BRAILLE['space'])
            number_mode = False
            continue # or use elifs

        if char.isupper():
            braille.append(ENGLISH_TO_BRAILLE['capital'])
            char = char.lower()

        if char.isdigit():
            if not number_mode:
                braille.append(ENGLISH_TO_BRAILLE['number'])
                number_mode = True
            braille.append(NUMBER_TO_BRAILLE[char])
        else:
            if number_mode:
                number_mode = False
            if char in ENGLISH_TO_BRAILLE:
                braille.append(ENGLISH_TO_BRAILLE[char])
            else:
                print('Error character:',char)
    
    return ''.join(braille)

def braille_to_english(braille_str):

    # each braille symbol is 6 characters, so start by splitting the list
    braille_symbols = [braille_str[i:i+6] for i in range(0, len(braille_str), 6)]

    # need a capitalized mode as well
    english = []
    capitalize_next = False
    number_mode = False

    for symbol in braille_symbols:
        if symbol == SPECIAL_BRAILLE['space']:
            english.append(' ')
            number_mode = False
            continue

        if symbol == SPECIAL_BRAILLE['capital']:
            capitalize_next = True
            continue

        if symbol == SPECIAL_BRAILLE['number']:
            number_mode = True
            continue

        if number_mode:
            if symbol in BRAILLE_TO_NUMBER:
                english.append(BRAILLE_TO_NUMBER[symbol])
            else:
                # If symbol is not a number, exit number mode. A little more lenient than just spaces
                # can tests expect an error instead?
                number_mode = False

                if symbol in BRAILLE_TO_ENGLISH:
                    char = BRAILLE_TO_ENGLISH[symbol]
                    if capitalize_next:
                        char = char.upper()
                        capitalize_next = False
                    english.append(char)
                else:
                    print('Error Braille symbol:',symbol)
        else:
            if symbol in BRAILLE_TO_ENGLISH:
                char = BRAILLE_TO_ENGLISH[symbol]
                if capitalize_next:
                    char = char.upper()
                    capitalize_next = False
                english.append(char)
            else:
                print('Error Braille symbol:',symbol)

    return ''.join(english)

def main():
    
    # trick to allow spaces in the input text
    input_text = ' '.join(sys.argv[1:])

    if all(c in ['O', '.'] for c in input_text): # is braille (or weird English...)
        output = braille_to_english(input_text)
    else:
        output = english_to_braille(input_text)
    
    print(output)

if __name__ == "__main__":
    main()
