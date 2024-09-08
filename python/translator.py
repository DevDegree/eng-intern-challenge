
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

    # create dict for english to braille
    english_to_braille = {
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

    #create dict for braille to english
    braille_to_english = {
        "O.....": 'a',
        "O.O...": 'b',
        "OO....": 'c',
        "OO.O..": 'd',
        "O..O..": 'e',
        "OOO...": 'f',
        "OOOO..": 'g',
        "O.OO..": 'h',
        ".OO...": 'i',
        ".OOO..": 'j',
        "O...O.": 'k',
        "O.O.O.": 'l',
        "OO..O.": 'm',
        "OO.OO.": 'n',
        "O..OO.": 'o',
        "OOO.O.": 'p',
        "OOOOO.": 'q',
        "O.OOO.": 'r',
        ".OO.O.": 's',
        ".OOOO.": 't',
        "O...OO": 'u',
        "O.O.OO": 'v',
        ".OOO.O": 'w',
        "OO..OO": 'x',
        "OO.OOO": 'y',
        "O..OOO": 'z',
        
        "..O...": ',',
        "..O.O.": ';',
        "..OO..": ':',
        "..OO.O": '.',
        "..OOO.": '!',
        "..O.OO": '?',
        ".OO.OO": '(',
        ".OO.OO": ')',
        "..O..O": '-',
        ".O.OO.": '/',
        ".O.OO.": '<',
        ".O.OO.": '>',
        
        ".....O": 'capital',
        ".O.OOO": 'number',
        "......": ' '
    }

    braille_to_number = {
        "O.....": '1',
        "O.O...": '2',
        "OO....": '3',
        "OO.O..": '4',
        "O..O..": '5',
        "OOO...": '6',
        "OOOO..": '7',
        "O.OO..": '8',
        ".OO...": '9',
        ".OOO..": '0',
    }


    for i in range(len(args)):
        # check if input is braille or english
        if set(args[i]).issubset({'O', '.', ' '}):
            # is braille
            isNumber = False
            isCapital = False
            for j in range(0, len(args[i]), 6):
                braille_char = args[i][j:j+6]
                char = braille_to_english[braille_char]
                # handle capital
                if isCapital:
                    char = char.upper()
                    isCapital = False
                
                elif char == 'capital':
                    isCapital = True
                    continue
                
                elif isNumber and char == ' ':
                    isNumber = False

                elif isNumber:
                    char = braille_to_number[braille_char]

                elif char == 'number':
                    isNumber = True
                    continue
                
                result += char
            isNumber = False
            isCapital = False
        else:
            # is english
            isNumber = False
            for letter in args[i]:
                # handle capital case
                if letter.isupper():
                    result += english_to_braille['capital']
                    letter = letter.lower()
                # handle numbers
                elif letter.isnumeric() and not isNumber:
                    isNumber = True
                    result += english_to_braille['number']
                result += english_to_braille[letter]
            # add space after element if its not the last one
            if i != len(args)-1:
                result += english_to_braille[' ']

    return result

if __name__ == "__main__":
    args = sys.argv[1:]
    output = translate_input(args)
    print(output)