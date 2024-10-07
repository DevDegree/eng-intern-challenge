#!/usr/bin/env python3

import argparse

# Parses the inputs passed in at the command line. Input is required in a string format. 
def parseInputs(): 
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str, nargs='+')
    args = parser.parse_args()
    return ' '.join(args.input)


# Checks if the given input is braille. Returns false if not. 
def is_braille(input):
    braille_chars = ['O', '.']
    for char in input:
        if(char not in braille_chars): 
            return False
    return True

# Converts the text from braille to english. 
def braille_to_eng(input):
    braille_alphabet_dict = {
        'O.....': 'a',
        'O.O...': 'b', 
        'OO....': 'c', 
        'OO.O..': 'd', 
        'O..O..': 'e', 
        'OOO...': 'f', 
        'OOOO..': 'g', 
        'O.OO..': 'h', 
        '.OO...': 'i', 
        '.OOO..': 'j', 
        'O...O.': 'k', 
        'O.O.O.': 'l',
        'OO..O.': 'm', 
        'OO.OO.': 'n', 
        'O..OO.': 'o', 
        'OOO.O.': 'p', 
        'OOOOO.': 'q', 
        'O.OOO.': 'r', 
        '.OO.O.': 's', 
        '.OOOO.': 't', 
        'O...OO': 'u', 
        'O.O.OO': 'v', 
        '.OOO.O': 'w', 
        'OO..OO': 'x', 
        'OO.OOO': 'y', 
        'O..OOO': 'z', 
        '.....O': 'capital follows', 
        '.O.OOO': 'number follows', 
        '.O...O': 'decimal follows', 
        '......': ' '
    }
    braille_num_dict = {
        'O.....': '1',
        'O.O...': '2', 
        'OO....': '3', 
        'OO.O..': '4', 
        'O..O..': '5', 
        'OOO...': '6', 
        'OOOO..': '7', 
        'O.OO..': '8', 
        '.OO...': '9', 
        '.OOO..': '0', 
        '......': ' '
    }

    translated_text = ''

    curr_index = 0
    is_num = False
    is_uppercase = False
    
    while curr_index < len(input):
        # Takes the current 6 characters that form the braille letter. 
        braille_letter = input[curr_index:curr_index + 6]
        eng_letter = ''
        # If we have said that we are working with numbers, then we will look only at the numbers
        if(is_num):
            eng_letter = braille_num_dict[braille_letter]
            # If there is a space, then we end our number mode.
            if(eng_letter == ' '):
                is_num = False
        # If it is not number mode, then we will look at the alphabet set. 
        else:
            eng_letter = braille_alphabet_dict[braille_letter]

        # Sets the capital letter mode. 
        if(eng_letter == 'capital follows'):
            is_uppercase = True
        elif(eng_letter == 'number follows'):
            is_num = True
        elif(eng_letter == 'decimal follows'):
            translated_text += '.'
        else:
            if(is_uppercase):
                translated_text += str(eng_letter).capitalize()
                is_uppercase = False
            else: 
                translated_text += str(eng_letter)

        curr_index += 6
        
    print(translated_text.strip())


# Converts the text from english to braille. 
def eng_to_braille(input):
    alphabet_dict = {
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
        ' ': '......', 
        '1': 'O.....',
        '2': 'O.O...',
        '3': 'OO....',
        '4': 'OO.O..',
        '5': 'O..O..',
        '6': 'OOO...',
        '7': 'OOOO..',
        '8': 'O.OO..',
        '9': '.OO...',
        '0': '.OOO..',
    }
    translated_text = ""
    number_mode = False
    for char in input: 
        if(char.isupper()):
            translated_text += '.....O'
            char = char.lower()
        elif(char.isdigit() and not number_mode):
            translated_text += '.O.OOO'
            number_mode = True
        if(char == ' ' and number_mode):
            number_mode = False

        brailleLetter = alphabet_dict[char]
        translated_text += brailleLetter

    print(translated_text.strip())




# main method that runs everything. 
def main():
    input = parseInputs()
    
    if(is_braille(input)):
        braille_to_eng(input)
    else:
       eng_to_braille(input)
    
main()


