import sys

'''
------------------
GLOBAL VAR SETUP
------------------
'''
# translation table for English to Braile directly from alphabet posted on github
ENGLISH_TO_BRAILE = {
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
    '.': '..OO.O',
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

# Create the braile to english dict by reversing the english to braile dict and not including numbers
BRAILE_TO_ENGLISH = {braile : english for english,braile in ENGLISH_TO_BRAILE.items() if not english.isdigit()}

# Create the braile to english digit dict in a similar way as above
BRAILE_TO_ENGLISH_DIGIT = {braile : english for english,braile in ENGLISH_TO_BRAILE.items() if english.isdigit()}



# function to check if input is braile
def isBraille(unknownString):
    return all(char == '.' or char == 'O' for char in unknownString)
    
    
# function to change english into braile
def englishToBraile(englishString):
    result = ''
    
    for i,char in enumerate(englishString):
        
        # check if character is a letter
        if char.isalpha():
            
            # if its a letter, first check if its a capital
            if char.isupper():
                
                # if its a capital, add the capital comes next to the string and then the character
                result += '.....O'
            
            # then append the proper alphabet character to the result
            result += ENGLISH_TO_BRAILE[char.lower()]

        # seperate case if current character is a digit
        elif char.isdigit():
            
            # first append digit identifier only if its the first digit
            if i == 0 or not englishString[i-1].isdigit():
                result += '.O.OOO'
            
            # then append digit
            result += ENGLISH_TO_BRAILE[char]
            
        # otherwise simply append to result
        else:
            result += ENGLISH_TO_BRAILE[char]
          
    # return result  
    return result


def braileToEnglish(braileString):
    string = ''
    
    while braileString:
        current = braileString[:6]
        
        # check if a capital follows
        if current == '.....O':
            
            # delete the 6 that notify of a capital
            braileString = braileString[6:]
            
            # find the next 6 and translate
            current = braileString[:6]
            string += BRAILE_TO_ENGLISH[current].upper()
        
        # check if a number follows
        elif current == '.O.OOO':
            
            # delete current
            braileString = braileString[6:]
            
            # get next digit
            current = braileString[:6]
            
            # while current is not a space
            while current != '......' and current != '':

                # use alternative dict to add number
                string += BRAILE_TO_ENGLISH_DIGIT[current]
                
                # delete added number
                braileString = braileString[6:]
                
                # get new current
                current = braileString[:6]
        else:
            # just do it normally
            string += BRAILE_TO_ENGLISH[current]
        
        braileString = braileString[6:]
    
    # return the resulting English string
    return string


# main function
def main():
    if len(sys.argv) != 2:
        print('Not the correct amount of arguments')
        return
    
    string = sys.argv[1]
    
    if isBraille(string):
        print(braileToEnglish(string))
    else:
        print(englishToBraile(string))


# run the main loop
if __name__ == '__main__':
    main()
