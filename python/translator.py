import sys

def braille_translator(user_input: str) -> str:
    #dictionary to store the braille values for the english alphabets
    # the alphabet O represents a raised dot and . represents a blank space
    braille_dict = {
        # alphabets
        'A' : 'O.....',
        'B' : 'O.O...',
        'C' : 'OO....',
        'D' : 'OO.O..',
        'E' : 'O..O..',
        'F' : 'OOO...',
        'G' : 'OOOO..',
        'H' : 'O.OO..',
        'I' : '.OO...',
        'J' : '.OOO..',
        'K' : 'O...O.',
        'L' : 'O.O.O.',
        'M' : 'OO..O.',
        'N' : 'OO.OO.',
        'O' : 'O..OO.',
        'P' : 'OOO.O.',
        'Q' : 'OOOOO.',
        'R' : 'O.OOO.',
        'S' : '.OO.O.',
        'T' : '.OOOO.',
        'U' : 'O...OO',
        'V' : 'O.O.OO',
        'W' : '.OOO.O',
        'X' : 'OO..OO',
        'Y' : 'OO.OOO',
        'Z' : 'O..OOO',
        # numbers
        '1' : 'O.....',
        '2' : 'O.O...',
        '3' : 'OO....',
        '4' : 'OO.O..',
        '5' : 'O..O..',
        '6' : 'OOO...',
        '7' : 'OOOO..',
        '8' : 'O.OO..',
        '9' : '.OO...',
        '0' : '.OOO..',
        # special characters
        '.' : '..OO.O',
        ',' : '..O...',
        '?' : '..O.OO',
        '!' : '..OOO.',
        ':' : '..OO..',
        ';' : '..O.O.',
        '-' : '....OO',
        '/' : '.O..O.',
        '<' : '.OO..O',
        '>' : 'O..OO.',
        '(' : 'O.O..O',
        ')' : '.O.OO.',
        ' ' : '......',
        #others
        'capital' : '.....O',
        'decimal' : '.O...O',
        'number' : '.O.OOO', 
    }

    # Get the input from the user (could be English or Braille)
    # user_input = " ".join(sys.argv[1:])

    #check if the input is in english or braille
    #if the input contains . or O exclusive, it is in braille
    if all(c in ['.', 'O'] for c in user_input):
        return get_english_from_braille(user_input, braille_dict)
    else:
        return get_braille_from_english(user_input, braille_dict)


def get_english_from_braille(user_input, braille_dict):
    #result
    res = ""
    #capital flag (change it to True if the current braille character indicates the character following it is capital)
    is_capital = False
    #flag to check if the current braille character is a number
    is_number = False

    
    for i in range(0, len(user_input), 6):
        #input - braille confirmed - so we need to take 6 characters at a time
        braille = user_input[i:i+6]

        # check if the braille symbol is a capital letter
        if braille ==  braille_dict['capital']:
            is_capital = True
            continue #skip the current iteration

        #check if the braillee symbol is a number, lets skip for now
        if braille == braille_dict['number']:
            is_number = True
            continue #skip the current iteration

        #when we encounter a space, we can confirm that the number is over
        if braille == braille_dict[' ']:
            is_number = False
            res += ' '
            continue           
        
        #get the equivalent key for the braille symbol from the dictionary
        for key, value in braille_dict.items():
            #if the braille symbol exists, store its respective key(letter/no) in the result
            
            if braille == value:
                #if the braille symbol is a number, store the next letter in number
                if is_number:
                    number_map = {
                        'A' : '1', 'B' : '2', 'C' : '3', 'D' : '4', 'E' : '5', 'F' : '6', 'G' : '7', 'H' : '8', 'I' : '9', 'J' : '0'
                    }
                    #store the number in the result i.e. if A is the braille symbol, store 1 in the result
                    if key in number_map.keys():
                        res += number_map[key]
                else:    
                    #if the braille symbol is a capital letter, store the next letter in capital case else in lower case
                    #store the lower case key(character) in the result if the is_capital flag is False
                    if not(is_capital):
                        res += key.lower()
                    else:
                        res += key
                        is_capital = False
                    break
    return res


def get_braille_from_english(user_input, braille_dict):
    #result
    res = ''
    #flags
    is_number = False

    #input english confirmed - so we need to take 1 character at a time
    for i in range(0, len(user_input)):
        is_capital = False
        char = user_input[i]

        #when we encounter a space, we can confirm that the number is over
        if char == ' ':
            res += braille_dict[' ']
            is_number = False
            continue

        #deal with upper case
        if char.isupper():
            if not is_capital:
                res += braille_dict['capital'] # only add the capital flag if it has not been added
                is_capital = True
            #add the braille to the result if it exists in the dictionary
            if char in braille_dict:
                res += braille_dict[char]
            continue

        #deal with numbers
        if char.isdigit():
            if not is_number:
                res += braille_dict['number'] # only add the number flag if it has not been added
                is_number = True
            #add the braille to the result if it exists in the dictionary
            if char in braille_dict.keys():
                res += braille_dict[char]
            continue

         #deal with lower case and other characters   
        if char.upper() in braille_dict:
            if is_capital:
                res += braille_dict['capital']
                is_capital = False
            if is_number:
                res += braille_dict['number']

            res += braille_dict[char.upper()]

    return res


if __name__ == '__main__':
    # Get input from command-line arguments and process it
    user_input = " ".join(sys.argv[1:])
    print(braille_translator(user_input))

        