import collections
import sys

#Array containing the english alphabets  and special characters
ALPHABET_ARRAY = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
                  'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
                  'y', 'z', '.', ',', '?', '!', ':', ';', '-', '/', '<', '>', '(', ')']
#Array containing the numbers 0-9
NUMBER_ARRAY = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#Array containing the Braille letters for corresponding english alphabets and special characters
BRAILLE_ARRAY = [ 'O.....', 'O.O...', 'OO....', 'OO.O..', 'O..O..', 'OOO...', 'OOOO..','O.OO..','.OO...','.OOO..','O...O.','O.O.O.',
                 'OO..O.','OO.OO.','O..OO.','OOO.O.','OOOOO.','O.OOO.','.OO.O.','.OOOO.','O...OO','O.O.OO','.OOO.O','OO..OO',
                 'OO.OOO','O..OOO','..OO.O', '..O...', '..O.OO', '..OOO.', '..OO..', '..O.O.', '....OO','.O..O.','.OO..O', 'O..OO.','O.O..O', '.O.OO.']
#Array containing the Braille letters for corresponding numbers 0-9
BRAILLE_NUM_ARRAY = ['O.....', 'O.O...', 'OO....', 'OO.O..', 'O..O..', 'OOO...', 'OOOO..','O.OO..','.OO...', '.OOO..']

CAPITAL_LETTER_BRAILLE = '.....O' # Braille code for Capital Letter
DECIMAL_LETTER = '.O...O' # Braille code for Decimal char
NUMBER_FOLLOWS = '.O.OOO' # Braille code for number 
SPACE_LETTER = '......' # Braille code for space letterr


#Function to convert the english to Braille code
def convert_english_to_braille(englishText):
    result_string = [] # Final string containing Braille code
    isNumberFlag = False # Number flag 

    for tmpChar in englishText: #Loop to iterate english text
        if tmpChar.isupper(): # Checks whether the char is Capital
            result_string.append(CAPITAL_LETTER_BRAILLE) # Add Braille code for Capital letter
            result_string.append(BRAILLE_ARRAY[ALPHABET_ARRAY.index(tmpChar.lower())]) # Append the Braille code based on the index of English Alphabet array
            isNumberFlag = False 
        elif tmpChar.isdigit(): # Checks for char is numeric or not
            if not isNumberFlag: # Checks for Number flag is off
                result_string.append(NUMBER_FOLLOWS) # Append the Braille code for Numbers
                isNumberFlag = True # Set Number flag to True to continue the numbers
            result_string.append(BRAILLE_NUM_ARRAY[NUMBER_ARRAY.index(tmpChar)]) # Append the number to final string
        elif tmpChar == ' ': #Checks for space 
            result_string.append(SPACE_LETTER) # Append Braille code for space
            isNumberFlag = False # Turn off the Number flag
        else:
            result_string.append(BRAILLE_ARRAY[ALPHABET_ARRAY.index(tmpChar.lower())])
            isNumberFlag = False
        
    return ''.join(str(x) for x in result_string)

#Function to convert the Braille code to english text
def convert_braille_to_english(brailleText):
    result_string = [] # Final string containing Braille code
    isCapitalFlag = False # Capital letter flag 
    isNumberFlag = False # Number flag 
    brailleCharArray = [brailleText[i:i+6] for i in range(0, len(brailleText), 6)] #Loop to iterate Braille text to capture as a 6 character

    for tmpChar in brailleCharArray: #Loop to iterate braille text
        if tmpChar == CAPITAL_LETTER_BRAILLE: # Checks for char is capital letter or not
            isCapitalFlag = True # set Capital flag to true
            isNumberFlag = False # set Number flag to false
        elif tmpChar == NUMBER_FOLLOWS: # Checks for char is numeric or not
            isCapitalFlag = False # set Capital flag to false
            isNumberFlag = True # set Number flag to true
        elif tmpChar == SPACE_LETTER: #Checks for space 
            result_string.append(' ') #append space
            isNumberFlag = False 
        elif isNumberFlag:
            result_string.append(NUMBER_ARRAY[BRAILLE_NUM_ARRAY.index(tmpChar)]) # if number flag is true map the corresponding number for the given Braille
            isNumberFlag=True
        elif isCapitalFlag:
            result_string.append(ALPHABET_ARRAY[BRAILLE_ARRAY.index(tmpChar)].upper()) #if capital flag is true change to Upper case
            isCapitalFlag = False
        else:
            result_string.append(ALPHABET_ARRAY[BRAILLE_ARRAY.index(tmpChar)]) # else map the corresponding English letter
    return ''.join(str(x) for x in result_string) 

if __name__ == "__main__" :

    inputString = " ".join(sys.argv[1:])
    if inputString.__contains__('O.'):
        print(convert_braille_to_english(inputString))
    else:
        print(convert_english_to_braille(inputString))
        
        
    




