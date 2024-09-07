
import sys
import re

'''
first solution that comes to mind:
initialize result string

check if input braille or english (if characters in argument not in ['0', '.']
input = braille:
    create dict for braille to english
    create list with each braille letter seperated
    
    loop through list
        treat special cases (capital follows, decimal follows, number follows)
        append english letter to result

input = english:
    create dict for english to braille
    create list with each character seperated

    loop through list
        treat special cases (capital follows, decimal follows, number follows)
        append braille letter to result

return result
'''

def translate_input(args):
    #print(args)
    input = args[0]
    #print(input)
    result = ""
    # input = braille
    if not input.isalnum():
        pass

    else:
        #print('helloooo')
        # create dict for braille to english
        braille_to_english = {
            'a': "O.....",
            'b': "O.O...",
            'c': "OO....",
            'd': "OO.O..",
            'e': "O..O..",
            'f': "OOO...",
            'g': "OOOO..",
            'h': "O.OO..",
            'i': ".OO...",
            'j': ".OOO..",
            'k': "O...O.",
            'l': "O.O.O.",
            'm': "OO..O.",
            'n': "OO.OO.",
            'o': "O..OO.",
            'p': "OOO.O.",
            'q': "OOOOO.",
            'r': "O.OOO.",
            's': ".OO.O.",
            't': ".OOOO.",
            'u': "O...OO",
            'v': "O.O.OO",
            'w': ".OOO.O",
            'x': "OO..OO",
            'y': "OO.OOO",
            'z': "O..OOO",
            
            '1': "O.....",
            '2': "O.O...",
            '3': "OO....",
            '4': "OO.O..",
            '5': "O..O..",
            '6': "OOO...",
            '7': "OOOO..",
            '8': "O.OO..",
            '9': ".OO...",
            '0': ".OOO..",
            
            ',': "..O...",
            ';': "..O.O.",
            ':': "..OO..",
            '.': "..OO.O",
            '!': "..OOO.",
            '?': "..O.OO",
            '(': ".OO.OO",
            ')': ".OO.OO",
            '-': "..O..O",
            '/': ".O.OO.",
            '<': ".O.OO.",
            '>': ".O.OO.",
            
            'capital': ".....O",
            'number': ".OO.OO",
            'decimal': ".OO...",
            ' ': "......"
        }

        for letter in input:
            
            if letter.isupper():
                result += braille_to_english['capital']
                letter = letter.lower()

            char = braille_to_english[letter]

            #if char in ['captial', 'number', 'decimal']
            result += char

    return result

if __name__ == "__main__":
    args = sys.argv[1:]
    output = translate_input(args)
    print(output)