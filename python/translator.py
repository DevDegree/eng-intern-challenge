import sys
import os



#define Braille characters


#Braille dictionary for the correct conversion of normal text to braille 
# braille = {
#     'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
#     'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
#     'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
#     's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
#     'y': 'OO.OOO', 'z': 'O..OOO', 'capital_follows': '.....O', 'decimal_follows': '.O...O', 
#     'number_follows': '.O.OOO', '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
#     ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
#     'space': '......', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
#     '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
# }


#Braille dictionary for the conversion that is given in the test case
braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', 'capital_follows': '.....O', 'decimal_follows': '.O...O', 
    'number_follows': '.O.OOO', '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
    'space': '......', '0': 'O.....', '1': 'O.O...', '2': 'OO....', '3': 'OO.O..', '4': 'O..O..',
    '5': 'OOO...', '6': 'OOOO..', '7': 'O.OO..', '8': '.OO...', '9': '.OOO..'
}


#function to identify if its braille or normal text
def is_braille(text):
    #check if text is 'o' or '.' or ' '
    for char in text:
        if char not in ['O', '.', ' ']:
            return False
    return True


#function to translate normal text to braille
def translate_to_braille(text):
    #initialize empty string

    # print("Input: ", text)
    result = ''
    is_upper = False
    is_number = False
    is_decimal = False
    is_space = False
    #loop through text
    for char in text:
        
        #check if char is uppercase
        if char.isupper():

            if not is_upper:
                #add capital_follows to result
                result += braille['capital_follows']
            #add lowercase char to result
            result += braille[char.lower()]

            is_upper = True

        #check if char is number
        elif char.isdigit():

            if not is_number:
                #add number_follows to result
                result += braille['number_follows']
                is_number = True
            #add char to result
            result += braille[char]
            is_upper = False
            is_decimal = False


        #check if char is decimal
        elif char == '.':
            if not is_decimal:
                #add decimal_follows to result
                result += braille['decimal_follows']
                is_decimal = True
            #add char to result
            result += braille[char]
            is_upper = False
            is_number = False


        #check if char is space
        elif char == ' ':
            #add space to result
            result += braille['space']
        #if char is not space
        else:
            #add char to result
            result += braille[char]
        # print(char)
        # print(result)
    # print(f"Braille text: {result}")
    return result



    

#function to translate braille to normal text
def translate_from_braille(text):
    result = ''
    is_upper = False
    is_number = False
    is_decimal = False

    # Loop through text in chunks of 6 characters (Braille cells)
    for i in range(0, len(text), 6):
        # Get the current Braille character
        char = text[i:i+6]

        #check if char is capital_follows
        if char == braille['capital_follows']:
            is_upper = True
            
            #set is_number to False
            is_number = False
            #set is_decimal to False
            is_decimal = False
        #check if char is number_follows
        elif char == braille['number_follows']:
            is_number = True
            is_upper = False
            is_decimal = False

        #check if char is decimal_follows
        elif char == braille['decimal_follows']:
            is_decimal = True
            is_upper = False
            is_number = False
        #check if char is space
        elif char == braille['space']:
            result += ' '
            is_upper = False
            is_number = False
            is_decimal = False
        #if char is not space
        else:
            # Loop through the Braille dictionary to find the matching character
            for key, value in braille.items():
                if value == char:
                    #check if is_upper is True
                    if is_upper:
                        #add uppercase char to result
                        result += key.upper()
                        is_upper = False
                    #check if is_number is True
                    elif is_number:
                        #convert 'a-j' to '0-9'
                        if 'a' <= key <= 'j':
                            key = str(ord(key) - ord('a'))

                        #add number to result
                        result += key
                    #check if is_decimal is True
                    elif is_decimal:
                        #add decimal to result
                        result += key
                    #if is_upper, is_number and is_decimal is False
                    else:
                        #add char to result
                        result += key
                    break
    return result
        






def translate(text):

    #check if text is braille
    if is_braille(text):
        #if text is braille, translate it to normal text
        return translate_from_braille(text)
    else:
        #if text is not braille, translate it to braille
        return translate_to_braille(text)
    
def main():

   

    if len(sys.argv) < 2:
        sys.exit(1)

    text = ' '.join(sys.argv[1:])

    result = translate(text)
    print(result)




if __name__ == '__main__':
    main()

