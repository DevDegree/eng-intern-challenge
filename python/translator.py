'''
Isabella Nguyen

How to run: py translator.py <braille or english>
'''

import sys

letter_to_braille = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': "OO.OO.", 't': "OOOO.O",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
    'z': "O..OOO"
}

number_to_braille = {
    '1': "O.....", '2': "O.O...", '3': "OO....",
    '4': "OO.O..", '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..",
    '9': ".OO...", '0': ".OOO.."
}

braille_to_letter = {v: k for k, v in letter_to_braille.items()}

braille_to_number = {v: k for k, v in number_to_braille.items()}

capital_follows = ".....O"
number_follows = ".O.OOO"    
space = "......"

def english_to_braille_translator(input_str):
    braille = ""
    letters_currently = True
    
    for letter in input_str:
        if letter in letter_to_braille:
            braille += letter_to_braille[letter]

        elif letter.lower() in letter_to_braille:
            braille += capital_follows
            braille += letter_to_braille[letter.lower()]

        elif letter in number_to_braille:
            if letters_currently:
                braille += number_follows
                letters_currently = False
            braille += number_to_braille[letter]

        elif letter == ' ':
            braille += space
            letters_currently = True

    return braille

def braille_to_english_translator(input_str):
    english = ""
    capital = False
    number = False

    braille_letters = [(input_str[i:i+6]) for i in range(0, len(input_str), 6)]
    
    for letter in braille_letters:
        if letter == capital_follows:
            capital = True

        elif letter == number_follows:
            number = True

        elif (not number) and (letter in braille_to_letter):
            if capital:
                english += braille_to_letter[letter].upper()
                capital = False
            else:
                english += braille_to_letter[letter]

        elif (number) and (letter in braille_to_number):
            english += braille_to_number[letter]

        elif letter == "......":
            english += ' '
            number = False
    
    return english

def is_braille(input_str):
    # Going off the assumption that there are no symbols used, as in the instructions
    return '.' in input_str

def main():
    input_str = ' '.join(sys.argv[1:])

    if is_braille(input_str):
        print(braille_to_english_translator(input_str))
    else:
        print(english_to_braille_translator(input_str))

if __name__ == "__main__":
    main()
