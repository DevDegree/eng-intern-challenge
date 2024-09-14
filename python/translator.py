import sys

# Detection function: detect input's language: English or Braille and call related function to translate and print the translation
def detectLanguage(inputString):
    """_summary_

    Args:
        inputString (_type_): _description_
    """
    # set init values
    translate = ''
    english = False
    # extra case: if the input has only O --> it can not be a Braille input (we don't have OOOOOO in Braille)
    if len(inputString) == 0:
        translate = ''
    elif inputString == 'O'*len(inputString):
        translate = translateToBraille(inputString)
    else:   
        # loop on all characters of input
        for char in inputString:
            if char != '.' and char != 'O':
                translate = translateToBraille(inputString)
                english = True
                break        
        if english == False:
            translate = translateToEnglish(inputString)
    print(translate)
#---------------------------------------------------------

# translate Braille to English function               
def translateToEnglish(brailleInput):
    """_summary_

    Args:
        brailleInput (_type_): _description_

    Returns:
        _type_: _description_
    """
    #step1 break the input into chunk of 6 character each
    brailleChars = []
    for i in range(0, len(brailleInput), 6):
        bChar = brailleInput[i:i+6]
        brailleChars.append(bChar)
    # set init values
    englishTranslation = ''
    bChar = 0
    itsNumber = False
    # loop on all braille characters(each has 6 characters) to translate
    while bChar < len(brailleChars):
        # check number follows : turn itsNumber to True --> next characters before space are number
        if brailleChars[bChar] == '.O.OOO':
            itsNumber = True
        #check space: add space and reset itsNumber to false next one is not a number
        elif brailleChars[bChar] == '......':
            itsNumber = False
            englishTranslation += ' '
        #check capital follows: so next character  is capital letter: add next one in capital version
        elif brailleChars[bChar] == '.....O' :
            bChar += 1
            capitalChar = brailleToEnglishAlphabetDictionary[brailleChars[bChar]].upper()
            englishTranslation += capitalChar
        #  if itsNumber is false --> find alphabet from alphabet dictionary and add it's translation
        elif itsNumber == False and brailleChars[bChar] in brailleToEnglishAlphabetDictionary:
            englishTranslation += brailleToEnglishAlphabetDictionary[brailleChars[bChar]]
        # if it's number is True --> find number from number dictionary and add it's translation
        elif itsNumber == True and brailleChars[bChar] in brailleToEnglishNumberDictionary:
            englishTranslation += brailleToEnglishNumberDictionary[brailleChars[bChar]]
        bChar += 1
    #print(englishTranslation)
    return englishTranslation
#--------------------------------------------------------------    

# translate English to Braille function
def translateToBraille(englishInput):
    """_summary_

    Args:
        englishInput (_type_): _description_

    Returns:
        _type_: _description_
    """
    # set init values
    capitalAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # is for checking capital
    brailleTranslation = ''
    itsNumber = False
    #loop on englishInput to translate each character
    for char in englishInput:
        #check number: if it's first number we need to change itsNumber to True and add number follows
        if char in englishToBrailleNumberDictionary:
            if itsNumber == False:
                itsNumber = True
                brailleTranslation += '.O.OOO'
            brailleTranslation += englishToBrailleNumberDictionary[char]
        # check space: first reset itsNumber to false space meaning can be end of numbers Then add space
        elif char == ' ':
            itsNumber = False
            brailleTranslation += '......'
        # check if it's capital and add capital follow and lower case of the letter
        elif char in capitalAlphabet:
            brailleTranslation += '.....O'
            lowerChar = char.lower()
            brailleTranslation += englishToBrailleAlphabetDictionary[lowerChar]
        # check lowercase letters and add translation
        elif char in englishToBrailleAlphabetDictionary:
            brailleTranslation += englishToBrailleAlphabetDictionary[char]
    #print(brailleTranslation)
    return brailleTranslation
    
#--------------------------------------------------------------

#Braille To English Dictionaries:
#1. Braille To English Number Dictionary:
brailleToEnglishNumberDictionary = {
    "O.....":'1',
    "O.O...":'2',
    "OO....":'3',
    "OO.O..":'4',
    "O..O..":'5',
    "OOO...":'6',
    "OOOO..":'7',
    "O.OO..":'8',
    ".OO...":'9',
    ".OOO..":'0'
                        }
#2. Braille To English Alphabet Dictionary:
brailleToEnglishAlphabetDictionary = {
    "O.....":'a',
    "O.O...":'b',
    "OO....":'c',
    "OO.O..":'d',
    "O..O..":'e',
    "OOO...":'f',
    "OOOO..":'g',
    "O.OO..":'h',
    ".OO...":'i',
    ".OOO..":'j',
    "O...O.":'k',
    "O.O.O.":'l',
    "OO..O.":'m',
    "OO.OO.":'n',
    "O..OO.":'o',
    "OOO.O.":'p',
    "OOOOO.":'q',
    "O.OOO.":'r',
    ".OO.O.":'s',
    ".OOOO.":'t',
    "O...OO":'u',
    "O.O.OO":'v',
    ".OOO.O":'w',
    "OO..OO":'x',
    "OO.OOO":'y',
    "O..OOO":'z'
                              }
#---------------------------------------------------------------

#English To Braille Dictionaries:
#1. English To Braille Number Dictionary:
englishToBrailleNumberDictionary = {
    '1':"O.....",
    '2':"O.O...",
    '3':"OO....",
    '4':"OO.O..",
    '5':"O..O..",
    '6':"OOO...",
    '7':"OOOO..",
    '8':"O.OO..",
    '9':".OO...",
    '0':".OOO.."
                         }
#2. English To Braille Alphabet Dictionary:
englishToBrailleAlphabetDictionary = {
    'a':"O.....",
    'b':"O.O...",
    'c':"OO....",
    'd':"OO.O..",
    'e':"O..O..",
    'f':"OOO...",
    'g':"OOOO..",
    'h':"O.OO..",
    'i':".OO...",
    'j':".OOO..",
    'k':"O...O.",
    'l':"O.O.O.",
    'm':"OO..O.",
    'n':"OO.OO.",
    'o':"O..OO.",
    'p':"OOO.O.",
    'q':"OOOOO.",
    'r':"O.OOO.",
    's':".OO.O.",
    't':".OOOO.",
    'u':"O...OO",
    'v':"O.O.OO",
    'w':".OOO.O",
    'x':"OO..OO",
    'y':"OO.OOO",
    'z':"O..OOO"
                              }
#-------------------------------------------------------------

# take an input and call detect function with correct version of input

resultString = ''
if __name__ == "__main__":
    #command line arguments that is list
    inputStrings = sys.argv[1:]
    # change input list to one string
    if len(inputStrings)>1:
        i = 0
        resultString = resultString + inputStrings[i]
        i += 1
        while i < len(inputStrings):
            resultString = resultString + ' ' + inputStrings[i]
            i += 1
    elif len(inputStrings) == 1:
        resultString = inputStrings[0] 
    else:
        resultString = '' 
# call detect function that will 1.detect language then 2.call translate function and then 3.print the result      
detectLanguage(resultString)