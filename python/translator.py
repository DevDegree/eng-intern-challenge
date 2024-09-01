#!/usr/bin/env python3
import sys
import re

# Dictionary to store alphabet
alphabet = {
    'a': 'O.....','b': 'O.O...','c': 'OO....','d': 'OO.O..','e': 'O..O..','f': 'OOO...','g': 'OOOO..','h': 'O.OO..','i': '.OO...','j': '.OOO..',
    'k': 'O...O.','l': 'O.O.O.','m': 'OO..O.','n': 'OO.OO.','o': 'O..OO.','p': 'OOO.O.','q': 'OOOOO.','r': 'O.OOO.','s': '.OO.O.','t': '.OOOO.',
    'u': 'O...OO','v': 'O.O.OO','w': '.OOO.O','x': 'OO..OO','y': 'OO.OOO','z': 'O..OOO',' ': '......','capital': '.....O','number': '.O.OOO',
    }
# Dictionary to store numbers
numbers = {
    '1': 'O.....','2': 'O.O...','3': 'OO....','4': 'OO.O..','5': 'O..O..','6': 'OOO...','7': 'OOOO..','8': 'O.OO..','9': '.OO...','0': '.OOO..'
    }
# Dictionary for braille alphabet
braille_alphabet = {
    'O.....':'a','O.O...':'b','OO....':'c','OO.O..':'d','O..O..':'e','OOO...':'f','OOOO..':'g','O.OO..':'h','.OO...':'i','.OOO..':'j',
    'O...O.':'k','O.O.O.':'l','OO..O.':'m','OO.OO.':'n','O..OO.':'o','OOO.O.':'p','OOOOO.':'q','O.OOO.':'r','.OO.O.':'s','.OOOO.':'t',
    'O...OO':'u','O.O.OO':'v','.OOO.O':'w','OO..OO':'x','OO.OOO':'y','O..OOO':'z','......':' ','.....O':'capital','.O.OOO':'number'
    }
# Dictionary for braille numbers
braille_numbers = {
    'O.....':'1','O.O...':'2','OO....':'3','OO.O..':'4','O..O..':'5','OOO...':'6','OOOO..':'7','O.OO..':'8','.OO...':'9','.OOO..':'0'
    }

# User input is in English
def english_to_braille(user_input):
    '''Takes string in english and transforms it into braille and prints it to the terminal'''

    response = ''
    # Numeric Flag to indicate if number
    number_value = False

    for i in user_input:
        # Letter
        if i.isalpha():
            # Capital Letter
            if i.isupper():
                response += alphabet.get('capital')
                i = i.lower()
                response += alphabet.get(i)
            # Simple letter
            else:
                response += alphabet.get(i)
        # Number
        elif i.isnumeric():
            if number_value == 0:
                response += alphabet.get('number')
                number_value = True
            # Get number from numbers dictionary
            response += numbers.get(i)
        # Command or space
        else:
            if number_value == True:
                number_value = False
            response += alphabet.get(i)
    number_value = 0  
    print(response) 
        
# User input is in Braille
def braille_to_english(user_input):
    '''Takes string in braille and transforms it into english and prints it to the terminal'''

    response = ''
    x = len(user_input)

    # Edge case: Check if user input is valid braille text: multiple of six
    if (x % 6) != 0:
        response = 'Invalid input'
        print(response)
    else:
        # Flags to indicate if captial or number
        capital = False
        number = False

        # Edge case: Check if braille text ends with capital or number, therefore it is invalid
        if braille_alphabet.get(user_input[-6:]).__eq__('capital') or braille_alphabet.get(user_input[-6:]).__eq__('number'):
            response = 'Invalid input'
            print(response)
        else:
            #For loop jumps every 6 as every 6 characters in braille represent 1 character
            for i in range(0, len(user_input), 6):
                letter = user_input[i:i+6]

                # Flag capital
                if braille_alphabet.get(letter).__eq__('capital'):
                    capital = True
                # Flag number
                elif braille_alphabet.get(letter).__eq__('number'):
                    number = True
                # If space, flag number to be false
                elif braille_alphabet.get(letter).__eq__(' '):
                    response += braille_alphabet.get(letter)
                    number = False
                else:
                    # Capital letter
                    if capital == True:
                        response += braille_alphabet.get(letter).upper()
                        capital = False
                    # Number
                    elif number == True:
                        response += braille_numbers.get(letter)
                    # simple letter
                    else:
                        number = False
                        response += braille_alphabet.get(letter)
            print(response)


def main(arg1):
    user_input = arg1
    # Check if string is alphanumeric or if it has space then turn it from english to braille
    if user_input.isalnum() or ' ' in user_input:
        english_to_braille(user_input)
    # Check if string has only "O." then turn it from braille to english
    elif re.match('^[O.]*$', user_input):
        braille_to_english(user_input)
    # Edge case: if input is invalid
    else:
        print("Invalid input")
    
if __name__ == '__main__':
    # Take every arugment after the file name and turn into string
    arg1 = sys.argv[1:]
    arg1 = ' '.join(arg1)
    # Edge case: if the input is empty: user hasn't inputted anything
    if not arg1:
        print("Invalid input")
    else:
        main(arg1)