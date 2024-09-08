
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
    result = ""

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
        'number': ".O.OOO",
        ' ': "......"
    }

    for i in range(len(args)):
        # check if input is braille or english
        if set(args[i]).issubset({'O', '.', ' '}):
            # is braille
            pass

        else:
            # is english
            isNumber = False
            for letter in args[i]:
                # handle capital case
                if letter.isupper():
                    result += braille_to_english['capital']
                    letter = letter.lower()
                # handle numbers
                elif letter.isnumeric() and not isNumber:
                    isNumber = True
                    result += braille_to_english['number']
                result += braille_to_english[letter]
            # add space after element if its not the last one
            if i != len(args)-1:
                result += braille_to_english[' ']

    return result

if __name__ == "__main__":
    args = sys.argv[1:]
    output = translate_input(args)
    print(output)