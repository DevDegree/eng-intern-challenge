import argparse

# translations in dictionary
braille_english = {
    'O.....': ('a', '1'), 'O.O...': ('b', '2'),
    'OO....': ('c', '3'), 'OO.O..': ('d', '4'),
    'O..O..': ('e', '5'), 'OOO...': ('f', '6'),
    'OOOO..': ('g', '7'), 'O.OO..': ('h', '8'), 
    '.OO...': ('i', '9'), '.OOO..': ('j', '0'),
    'O...O.': 'k', 'O.O.O.': 'l',
    'OO..O.': 'm', 'OO.OO.': 'n', 
    'O..OO.': 'o', 'OOO.O.': 'p',
    'OOOO.': 'q', 'O.OOO.': 'r',
    '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v',
    '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O..OOO': 'z',
    '.....O': 'capital follows', '.O...O': 'decimal follows',
    '.O.OOO': 'number follows', '......': ' ',
    '..OO.O': '.', '..O...': ',',
    '..O.OO': '?', '..OOO.': '!',
    '..OO..': ':', '..O.O.': ';',
    '....OO': '-', '.O..O.': '/',
    '.OO..O': '<', 'O..OO.': '>',
    'O.O..O': '(', '.O.OO.': ')'
}

english_braille = {
    'a': 'O.....', '1': 'O.....',
    'b': 'O.O...', '2': 'O.O...',
    'c': 'OO....', '3': 'OO....', 
    'd': 'OO.O..', '4': 'OO.O..',
    'e': 'O..O..', '5': 'O..O..', 
    'f': 'OOO...', '6': 'OOO...',
    'g': 'OOOO..', '7': 'OOOO..', 
    'h': 'O.OO..', '8': 'O.OO..', 
    'i': '.OO...', '9': '.OO...',
    'j': '.OOO..', '0': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 
    'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO',
    'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO',
    'capital follows': '.....O', 'decimal follows': '.O...O',
    'number follows': '.O.OOO', ' ': '......',
    '.': '..OO.O', ',': '..O...',
    '?': '..O.OO', '!': '..OOO.',
    ':': '..OO..', ';': '..O.O.',
    '-': '....OO', '/': '.O..O.',
    '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.'
}

def translator(input_string):
    # boolean to keep track of numbers
    global number
    number = False
    # boolean to keep track of capitalization
    global cap
    cap = False
    language = 'B'
    translated = ''

    # first, detect the language ('E' for English, 'B' for Braille)
    for letter in input_string:
        if letter not in '.O':
            language = 'E'
            break
    
    # if the language is English, translate it to Braille
    if language == 'E':
        for letter in input_string:
            # add the capital follows symbol for an upcoming capitalized letter
            if letter.isalpha() and letter.isupper(): 
                translated = translated + english_braille['capital follows']
            # if this is the start of a string of number, make sure that the number follows 
            # symbol is added and the status of "number" set to True to avoid duplicates
            # of the number follows symbol
            elif letter.isdigit() and not number:
                translated = translated + english_braille['number follows']
                number = True
            # add the decimal follows symbol if we are currently 
            # in a section of numbers and the current symbol is a decimal (period)
            elif letter == '.' and number:
                translated = translated + english_braille['decimal follows']
            # if we have reached a space, that means the string of number (if it was) ends here
            # until we have another "number follows" symbol
            elif letter.isspace():
                number = False
            # after completing any necessary actions, we insert the letter into the string
            # after translating it. Make sure that the letter is lower cased as that's how
            # the dictionary is created
            translated = translated + english_braille[letter.lower()]
    else:
        for i in range(0, len(input_string) - 1, 6): # need a step of 6
            # to obtain the 6 letter string that represent a single letter in braille
            current_braille = input_string[i:i+6]
            # translate it to english
            current_letter = braille_english[current_braille]

            # if captial follows, set "cap" to True so we capitalize the next letter
            if current_letter == 'capital follows':
                cap = True
            # if decimal follows, then the next letter won't be a decimal, so we have to
            # add a decimal manually to the translated string
            elif current_letter == 'decimal follows':
                translated = translated + '..OO.O'
            # if number follows, we set "number" to True and set it to False when we reach
            # a space
            elif current_letter == 'number follows':
                number = True
            # if number is True, then we should get the number element in the tuple, since
            # that same tuple also contain an english letter that has the same braille string
            elif number:
                translated = translated + current_letter[1]
            # if we have a space, the turn "number" to false
            elif current_letter == ' ':
                number = False
                translated = translated + current_letter
            # if cap is true, then we capitalize the current letter. THen turn cap to false
            elif cap:
                translated = translated + current_letter[0].capitalize()
                cap = False
            # otherwise, we just have a normal letter that needs translation. However, note that
            # letter a to j are in tuples, so we need to index the current_letter to 0. As for
            # those that are not in a tuple, indexing 0 will take the first letter in that string, 
            # but all strings contain only 1 letter so we still get the result we want
            else:
                translated = translated + current_letter[0]

    # once we are done translating, return the translated string
    return translated


def main():
    parser = argparse.ArgumentParser(description="A command-line app that translate between English and Braille.")
    parser.add_argument("input_string", type=str, help="The string to be translated")
    args = parser.parse_args()

    # Pass the input string to the function and print the result
    result = translator(args.input_string)
    print(f"{result}")


if __name__ == "__main__":
    main()