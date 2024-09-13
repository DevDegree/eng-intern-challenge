import sys

#variables needed: translator input, translator output
arg_length = len(sys.argv)
translator_input = ''
translator_output = ''

#iterator to use, necessary for findAlpha
count = 0
#handle number
handleNumber = False
#handle uppercase
handleUppercase = False

for i in range (1, arg_length):
    translator_input += sys.argv[i]
    if (i < arg_length - 1):
        translator_input += ' '

# DATA: Two arrays mapping braille to alphabet, where index corresponds to data. For example: A = O..... (both stored index 1)
# One additional string for capital, decimal, and number follows. 
alphabet = ['A', 'B', 'C', 
            'D', 'E', 'F',
            'G', 'H', 'I',
            'J', 'K', 'L',
            'M', 'N', 'O',
            'P', 'Q', 'R',
            'S', 'T', 'U',
            'V', 'W', 'X',
            'Y', 'Z', 1,
            2, 3, 4, 
            5, 6, 7,
            8, 9, 0,
            '.', ',', '?',
            '!', ':', ';',
            '-', '/', '<',
            '>', '(', ')',
            ' ']
braille = ['O.....', 'O.O...', 'OO....',
           'OO.O..', 'O..O..', 'OOO...',
           'OOOO..', 'O.OO..', '.OO...',
           '.OOO..', 'O...O.', 'O.O.O.',
           'OO..O.', 'OO.OO.', 'O..OO.',
           'OOO.O.', 'OOOOO.', 'O.OOO.',
           '.OO.O.', '.OOOO.', 'O...OO',
           'O.O.OO', '.OOO.O', 'OO..OO',
           'OO.OOO', 'O..OOO', 'O.....',
           'O.O...', 'OO....', 'OO.O..',
           'O..O..', 'OOO...', 'OOOO..',
           'O.OO..', '.OO...', '.OOO..',
           '..OO.O', '..O...', '..O.OO',
           '..OOO.', '..OO..', '..O.O.',
           '....OO', '.O..O.', '.OO..O',
           'O..OO.', 'O.O..O', '.O.OO.',
           '......']
braille_capital = '.....O'
braille_decimal = '.O...O'
braille_number = '.O.OOO'

#function that checks if input is alphanumeric (so not braille)
def isAlphanumeric(inputString):
    # if any one of the input characters (not . or O) is contained in alphabet array then return true
    for i in range (0, len(inputString)):
        if(inputString[i].upper() in alphabet and inputString[i] != '.' and inputString[i].upper() != 'O'):
            return True

    #if nothing found then it must be braille    
    return False

#function that looks up an alphanumeric character and returns a braille
def findBraille(alphaChar):
    brailleChar = ''

    #if capital add a capital notation first
    if (alphaChar.isupper()):
        brailleChar += braille_capital

    #if number add a number notation first
    elif (alphaChar.isnumeric()):
        #if there is no numeric after index of last space, add this.
        index_space = translator_output.find('......')
        index_numeric = translator_output.find(braille_number)
        if (index_numeric <= index_space):
            brailleChar += braille_number

    #if decimal add a decimal notation first
    #this is currently ignored

    #look for the alpha character's index and then get the braille based on that (index match braille to alphanumeric)
    for i in range(0, len(alphabet)):
        if(str(alphabet[i]).lower() == alphaChar.lower()):
            brailleChar += braille[i]
            break
    #return result
    return brailleChar

#function that takes a braille character and returns its alphanumeric counterpart
def findAlpha(brailleChar):

    global handleUppercase
    global handleNumber

    alphaChar = ''

    #if uppercase, we skip to next iteration after setting handle uppercase to true
    if (brailleChar == braille_capital):
        handleUppercase = True
        return alphaChar

    #if number, we skip to next iteration after setting handle number to true
    if (brailleChar == braille_number):
        handleNumber = True
        return alphaChar

    #reset handle number to false on space
    if (brailleChar == '......'):
        handleNumber = False

    #do range 26 if handle number is true (corresponds to integers)
    if(handleNumber == True):
        for i in range(26, len(braille)):
            if(brailleChar == braille[i]):
                alphaChar += str(alphabet[i])
                break
    #otherwise we look for alpha character
    else: 
        for i in range(0, len(braille)):
            if(brailleChar == braille[i]):
                alphaChar += alphabet[i]
                break

    #if not uppercase then lowercase
    if(handleUppercase == False):
        alphaChar = alphaChar.lower()

    #reset upper case to false
    handleUppercase = False

    #return result
    return alphaChar


if(isAlphanumeric(translator_input) == True):
    #iterate over the input string, convert alpha to braille
    for i in range(0, len(translator_input)):
        translator_output += findBraille(translator_input[i])
else:
    #convert braille to alpha
    while (count < len(translator_input)):
        next_count = count + 6
        brailleChar = translator_input[count : next_count]
        translator_output += findAlpha(brailleChar)
        count = next_count #iterate over 6 to correspond with braille char length


#output to terminal
sys.stdout.write(translator_output)

#compare:
#ALPHA TO BRAILLE
#42
#.O.OOOOO.O..O.O...
#.O.OOOOO.O..O.O...
#Hello world
#.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
#.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
#BRAILLE TO ALPHA
#.....OO.....O.O...OO...........O.OOOO.....O.O...OO....
#Abc 123