"""
    translator.py
    
    Author:  Hyoungjoo (Andy) Kim, hjandykim@gmail.com

    This file contains the logic to accept command line arguments,
    determine whether the given input is English text or Braille, and 
    perform the translation to the opposite format. The program supports 
    the entire English alphabet (including capitalization), numbers (0-9), 
    and spaces. The Braille output is represented using 'O' (letter O, representing raised dots) 
    and '.' (flat dots) in a 3x2 grid format.

    Accepted Braille Format:
    - Each braille symbol is stored as a 6-character string, reading right to left,
      line by line, starting at the top left.
    - Example: 'O.....' represents the letter 'a' in braille.

    Usage:
        python translator.py Hello world
        python translator.py .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
    
    Output:
        Outputs only the Braille/English string.
        
"""

import argparse
from typing import List

# Braille dictionary
char_dict = {
    'a' : 'O.....', 'b' : 'O.O...', 'c' : 'OO....',
    'd' : 'OO.O..', 'e' : 'O..O..', 'f' : 'OOO...',
    'g' : 'OOOO..', 'h' : 'O.OO..', 'i' : '.OO...',
    'j' : '.OOO..', 'k' : 'O...O.', 'l' : 'O.O.O.',
    'm' : 'OO..O.', 'n' : 'OO.OO.', 'o' : 'O..OO.',
    'p' : 'OOO.O.', 'q' : 'OOOOO.', 'r' : 'O.OOO.',
    's' : '.OO.O.', 't' : '.OOOO.', 'u' : 'O...OO',
    'v' : 'O.O.OO', 'w' : '.OOO.O', 'x' : 'OO..OO',
    'y' : 'OO.OOO', 'z' : 'O..OOO', '`' : '..OO.O',
    ',' : '..O...', '?' : '..O.OO', '!' : '..OOO.',
    ':' : '..OO..', ';' : '..O.O.', '-' : '....OO',
    '/' : '.O..O.', '<' : '.OO..O', '(' : 'O.O..O',
    ')' : '.O.OO.', ' ' : '......'
}
braille_char_dict = { value: key for key, value in char_dict.items()}
num_dict = {
    '1' : 'O.....', '2' : 'O.O...', '3' : 'OO....',
    '4' : 'OO.O..', '5' : 'O..O..', '6' : 'OOO...',
    '7' : 'OOOO..', '8' : 'O.OO..', '9' : '.OO...',
    '0' : '.OOO..'
}
braille_num_dict = { value : key for key, value in num_dict.items()}
cases_dict = {
    'capital' : '.....O', 'decimal' : '.O...O', 'number' : '.O.OOO' 
}
def isBraille(arguments: List[str]) -> bool:
    """
    Determines if the arguement list is in Braille format

    :param arguments: list of strings passed as arguments.
    :return: bool - True if arguments are in Braille format, False otherwise
    """

    if len(arguments) > 1 or len(arguments[0]) % 6 != 0:
        return False
    for eachChar in arguments[0]:
        if eachChar != 'O' and eachChar !='.':
            return False
    return True 
def brailleToEnglish(braille: str) -> str:
    """
    Translates a Braille string to English string.

    :param braille: A string of Braille characters to translate.
    :return: string - The translated English text
    :raises: argparse.ArgumentTypeError if the Braille pattern is invalid.
            Braille pattern is invalid if it does not exist in the mapping 
            or if the assumption that when a Braille number follows symbol is read, assume all following symbols are numbers until the next space symbol.
    """
    i = 0
    nums = False
    caps = False 
    res = ''
    while i < len(braille):
        currBraille = braille[i: i+ 6]
        try:
            if currBraille == cases_dict['capital']:
                caps = True
                nums = False
            elif currBraille == cases_dict['number']:
                nums = True
            elif currBraille == cases_dict['decimal']:
                nums = True
                caps = False
                res += '.'
            elif currBraille == char_dict[' ']:
                nums = False
                caps = False
                res += ' '
            else:
                    if nums:
                        res += braille_num_dict[currBraille]
                    elif caps:
                        res += braille_char_dict[currBraille].upper()
                        caps = False
                    else:
                        res +=braille_char_dict[currBraille]
        except KeyError:
            raise argparse.ArgumentTypeError(f"Error: Invalid Braille pattern")

        i += 6
    return res 

def englishToBraille(arguments: List[str]) -> str:
    """
    Translates an English string to Braille string.

    :param arguments: List of words from parsed arguments.
    :return: string - The translated Braille text
    :raises: argparse.ArgumentTypeError if unsupported character (characters not in the provided jpg) is used in the text.
    """
    res = ''
    nums = False
    for currIndex, eachWord in enumerate(arguments):
        currBraille = ''
        for eachChar in eachWord:
            if eachChar.isdigit():
                if not nums:
                    currBraille +=cases_dict['number']
                    nums = True
                currBraille += num_dict[eachChar]
            elif eachChar.lower() in char_dict:
                if eachChar.isupper():
                    currBraille += cases_dict['capital']
                currBraille += char_dict[eachChar.lower()]
            else:
                raise argparse.ArgumentTypeError(f'Non english letter found')
        res += currBraille
        if currIndex < len(arguments) - 1:
            res += char_dict[' ']
    return res

def main():
    """
    Main function: parses arguments, translates and outputs English to Braille, and Braille to English
    """
    parser = argparse.ArgumentParser(description='Implementation of translation between English text and Braille text')
    parser.add_argument('text', nargs='+', help='The input text to translate (English or Braille).', type = str)
    args = parser.parse_args()
    braille = isBraille(args.text)
    if braille:
        print(brailleToEnglish(args.text[0]))
    else:
        print(englishToBraille(args.text))
    


if __name__ == '__main__':
    main()
