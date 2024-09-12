import sys

# dictionaries for translating
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 
    'O..OOO': 'z', '......': ' ', 
    '.....O': 'capital', '.O.OOO': 'number', # '.O...O': 'decimal'
}

braille_to_int = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

'''
braille_to_punctuation = {
    '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!',
    '..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/', 
    'O.O..O': '(', '.O.OO.': ')', '.OO..O': '<', 'O..OO.': '>', 
}
'''

# reverse dictionaries
int_to_braille = {v: k for k, v in braille_to_int.items()}
english_to_braille = {v: k for k, v in braille_to_english.items()}

def translate(string):
    # check if braille or stirng
    if len(string) % 6 == 0 and set(string) <= set("O."):
        return translate_braille(string)
    else:
        return translate_english(string)
    
def translate_braille(string):

    # split string into array of 6 characters
    braille = [string[i:i+6] for i in range(0, len(string), 6)]

    # translate to english
    english = []

    # keep track of capital and number cases
    is_capital = False
    is_number = False
    for b in braille:
        # make sure it is in dictionary
        if b in braille_to_english:
            translated = braille_to_english[b]
            if is_capital:
                translated = translated.upper()
                is_capital = False
            elif is_number:
                # assume number until next space
                translated = braille_to_int[b]
            elif translated == ' ':
                is_number = False
            elif translated == 'capital':
                is_capital = True
                continue
            elif translated == 'number':
                is_number = True
                continue
            english.append(translated)

    return "".join(english)

def translate_english(string):
    # translate string to braille
    braille = []

    is_number = False
    for c in string:
        # check if capital
        if c.isupper():
            braille.append(english_to_braille['capital'])
            c = c.lower()

        # check if space to remove number flag
        if c == ' ':
                is_number = False

        # check if number
        if c.isdigit() and not is_number:
            braille.append(english_to_braille['number'])
            braille.append(int_to_braille[c])
            is_number = True
        elif c.isdigit() and is_number:
            braille.append(int_to_braille[c])
        else:            
            # standard character case
            braille.append(english_to_braille[c])

    return "".join(braille)

if __name__ == '__main__':
    # check for input
    if len(sys.argv) < 2:
        print("Invalid input. Provide an input to translate.")
        sys.exit()
    
    input_string = " ".join(sys.argv[1:])
    translated_string = translate(input_string)
    print(translated_string)

