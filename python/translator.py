import sys
SPACE = "......"
CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"

ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.','u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', 
    ' ': '......'
}
BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f', 
    'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l', 
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', 
    '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 
    'OO.OOO': 'y', 'O..OOO': 'z', '......': ' '
}

BRAILLE_TO_NUMBER = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 'OOO...': '6', 
    'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0', 

}

def isBraille(input: str) -> bool: #Check if input is braille or not
    for char in input: 
        if char != '.' and char != 'O': #Braille can only be 'O' or '.'
            return False
    if len(input) % 6 != 0:
        return False #If the input is not divisble by 6, it is not Braille
    return True
    
def translate(input: str) -> str: #Main translation function
    if isBraille(input):
        return brailleToEnglish(input)
    else: 
        return englishToBraille(input) #Call english to braille function

def englishToBraille(input:str) -> str:
    translatedResult = ""
    numberSeen = False 
    for char in input:
        if char.isupper(): #If character is uppercase
            translatedResult = translatedResult + CAPITAL_FOLLOWS + ENGLISH_TO_BRAILLE[char.lower()] #Add capital follows braille and the lowercase letter 
        elif char.isdigit(): #If character is a digit
            if numberSeen == False: #If number_follows has not been added
                translatedResult += NUMBER_FOLLOWS
                numberSeen = True #Track that number_follows has already been added 
            translatedResult += ENGLISH_TO_BRAILLE[char] #Add number in braille
        else:
            translatedResult += ENGLISH_TO_BRAILLE[char]
            if char == ' ':
                numberSeen = False #Reset number_follows if a space is seen
    return translatedResult

def brailleToEnglish(input:str) -> str:
    translatedResult = ""
    numberFollows = False
    capitalFollows = False

    for i in range(0, len(input), 6): #Iterate through the entire input, stopping 6 digits away from the end
        currentBraille = input[i:i+6] #The current Braille character (6 digits)
        if currentBraille == CAPITAL_FOLLOWS:
            capitalFollows = True
        elif currentBraille == NUMBER_FOLLOWS: 
            numberFollows = True
        else:
            if capitalFollows:
                translatedResult += BRAILLE_TO_ENGLISH[currentBraille].upper() #Add uppercase English letter
                capitalFollows = False
            if numberFollows:
                translatedResult += BRAILLE_TO_NUMBER[currentBraille]
            else:
                translatedResult += BRAILLE_TO_ENGLISH[currentBraille]
            if BRAILLE_TO_ENGLISH[currentBraille] == ' ':
                numberFollows = False  # Reset number flag after space
    return translatedResult


if __name__ == "__main__":
    input = ' '.join(sys.argv[1:])
    print(translate(input)) #Print translated result