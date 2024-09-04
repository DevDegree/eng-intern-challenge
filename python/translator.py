import sys

braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 
    'OO....': 'c', 'OO.O..': 'd', 
    'O..O..': 'e', 'OOO...': 'f', 
    'OOOO..': 'g', 'O.OO..': 'h', 
    '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 
    'OO..O.': 'm', 'OO.OO.': 'n', 
    'O..OO.': 'o', 'OOO.O.': 'p', 
    'OOOOO.': 'q', 'O.OOO.': 'r', 
    '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', 
    '.OOO.O': 'w', 'OO..OO': 'x', 
    'OO.OOO': 'y', 'O..OOO': 'z', 
    '......' : " "
}

braille_to_english_numbers = {
    'O.....': '1', 'O.O...': '2', 
    'OO....': '3', 'OO.O..': '4', 
    'O..O..': '5', 'OOO...': '6', 
    'OOOO..': '7', 'O.OO..': '8', 
    '.OO...': '9', '.OOO..': '0'
}

english_to_braille = {english: braille for braille, english in braille_to_english.items()}

english_to_braille_numbers = {english: braille for braille, english in braille_to_english_numbers.items()}

#Special Characters
space = "......"
capital_follows = ".....O"
number_follows = ".O.OOO"

def convertBrailleToEnglish(brailleString: str):
    numeric_value = False
    capital_letter = False
    englishString = ""

    #This divides the length of the braille string by six to get the number of output values there are
    for index in range(len(brailleString) // 6):
        #Gathers the six characters in braille that will be translated
        currentCharacter = brailleString[6*index:(6*index)+6]

        #Checks for the special case of a capital value following
        if currentCharacter == capital_follows:
            capital_letter = True
        
        #Checks for the special case that number(s) will follow
        elif currentCharacter == number_follows:
            numeric_value = True

        #If the know the next value is meant to be numeric
        elif numeric_value:
            if currentCharacter == space:
                #if it is a space then numeric values will not follow
                englishString += " "
                numeric_value = False
            else:
                #If it's not a space add the mapping from braille to english numbers
                englishString += braille_to_english_numbers[currentCharacter]
        
        else:
            newCharacter = braille_to_english[currentCharacter]

            #If the character is meant to be capitalized
            if capital_letter:
                newCharacter = newCharacter.upper()
                capital_letter = False

            englishString += newCharacter
    
    print(englishString)

def convertEnglishToBraille(englishString: str):
    numeric = False
    brailleString = ""

    for character in englishString:
        #if the character is in the alphabet
        if character.isalpha():
            #Adds uppercase character if needed
            if character.isupper():
                brailleString += capital_follows
            brailleString += english_to_braille[character.lower()]

        #If the character is a number
        elif character.isnumeric():
            #Check if we already added the numeric character ahead of it
            if not numeric:
                numeric = True
                brailleString += number_follows
            brailleString += english_to_braille_numbers[character]
        
        #Space is the only remaining character left
        else:
            numeric = False
            brailleString += space
    
    print(brailleString)

def isBraille(inputText: str):
    #All braille characters are length six so entire string must be a multiple of six
    if len(inputText) % 6 != 0:
        return False

    #Check that each character is either a period or O
    for character in inputText:
        if character not in ".O":
            return False

    #If input text passes both checks then it will be considered braille text
    return True

def main():
    if len(sys.argv) < 2:
        return
    
    inputText = ' '.join(sys.argv[1:])

    if(isBraille(inputText)):
        convertBrailleToEnglish(inputText)
    else:
        convertEnglishToBraille(inputText)

if __name__ == '__main__':
    main()