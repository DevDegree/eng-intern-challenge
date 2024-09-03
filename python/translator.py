import sys
import re

#Capture command line arguments
args = sys.argv[1:] 

#Dictionaries with corresponding braile and numbers
braile = {
    'a': 'O.....','b': 'O.O...','c': 'OO....','d': 'OO.O..','e': 'O..O..','f': 'OOO...','g': 'OOOO..','h': 'O.OO..','i': '.OO...','j': '.OOO..',
    'k': 'O...O.','l': 'O.O.O.','m': 'OO..O.','n': 'OO.OO.','o': 'O..OO.','p': 'OOO.O.','q': 'OOOOO.','r': 'O.OOO.','s': '.OO.O.','t': '.OOOO.',
    'u': 'O...OO','v': 'O.O.OO','w': '.OOO.O','x': 'OO..OO','y': 'OO.OOO','z': 'O..OOO',
    '.': '..OO.O',',': '..O...','?': '..O.OO','!': '..OO.O',':': '..OO..',';': '..O.O.','-': '....OO','/': '.O..O.','<': '.OO..O','>': 'O..OO.',
    '(': 'O.O..O',')': '.O.OO.',' ': '......'
}
numbers = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 'OOO...':'6', 'OOOO..':'7', 'O.OO..':'8', '.OO...': '9', '.OOO..' : '0'
}

#The inverse dictionary of the braile and number dictionaries
# braile -> english 
braile_inv = {val : key for key, val in braile.items()}
# number -> braile
numbers_inv = {val: key for key, val in numbers.items()}

def main(args):
    arg = ""

    # Check if our arguments is a single string or an array of arguments
    if type(args) is str:
        arg = args
    else:
        for word in args:
            arg += word
            arg += ' '
        arg = arg.strip()

    if not check_braile(arg):
        print(parse_english(arg))
    else:
        print (parse_braile(arg))

def check_braile(string):
    braileset = set('O.')
    stringset = set(string)

    if len(string) % 6 != 0:
        return False
    
    if stringset == braileset:
        return True
    else:
        return False

def parse_braile(input):
    # Constants representing the characters for capital_next & num_follows
    num_follows = '.O.OOO'
    capital_next = '.....O'
    space = '......'
    # Make sure our braile string is valid
    if len(input) % 6 != 0:
        print("Length of string: ",len(input))
        print("Error: Braile is not inputted correctly. (Invald Length; should be a multiple of 6)")


    # Breakup braile string into substrings of length 6, representing characters
    # Uses a regular expression
    chars = re.findall(r'.{6}', input) 

    #Booleans tracking whether we are writing numbers or a capitalized letter
    number = False
    cap = False

    # The string we will return
    ret = ""

    # Looping through each character in the braile string (of length 6)
    for char in chars:
        #If the character is a space turn off 'number mode' and append a space
        if char == space:
            number = False
            ret += ' '
        #Enable numbers if we have the num_follows char
        elif char == num_follows:
            number = True
        #Make the next letter capitalized
        elif char == capital_next:
            cap = True
        else:
            if not number:
                if cap:
                    # Capitalize only one characther then toggle the boolean
                    ret += braile_inv[char].capitalize()
                    cap = False
                else:
                    ret += braile_inv[char]
            else:
                ret += numbers[char]
    return ret

def parse_english(word):
    # The string we will return
    ret = ""    

    # Constants representing the characters for capital_next & num_follows
    capital_next = '.....O'
    num_follows = '.O.OOO'

    # Boolean used to track whether we are adding numbers to our return string
    number = False

    for letter in word:
        # Check whether the current letter is capitalized
        if letter.isupper():
            # If it is a letter following a number, remember to add a space
            if number:
                number = False
                ret += braile[' ']

            # Add the capital_follows symbol to our braile, then append the letter
            ret += capital_next
            ret += braile[letter.lower()]
        elif letter.isnumeric():
            # If the letter is a number, then add the num_follows character
            if number:
                ret += numbers_inv[letter]
            else:
                number = True
                ret += num_follows
                ret += numbers_inv[letter]            
        else:
            # If it is a letter following a number, remember to add a space unless it is already one
            if number and letter == ' ':
                number = False
            elif number:
                number = False
                ret += braile[' ']

            ret += braile[letter]

    return ret

if __name__ == "__main__":
    main(args)