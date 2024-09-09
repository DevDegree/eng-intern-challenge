import sys

Braille_To_English = {
    'O.....' : 'a', 'O.O...' : 'b', 'OO....' : 'c', 'OO.O..' : 'd',
    'O..O..' : 'e', 'OOO...' : 'f', 'OOOO..' : 'g', 'O.OO..' : 'h',
    '.OO...' : 'i', '.OOO..' : 'j', 'O...O.' : 'k', 'O.O.O.' : 'l',
    'OO..O.' : 'm', 'OO.OO.' : 'n', 'O..OO.' : 'o', 'OOO.O.' : 'p',
    'OOOOO.' : 'q', 'O.OOO.' : 'r', '.OO.O.' : 's', '.OOOO.' : 't',
    'O...OO' : 'u', 'O.O.OO' : 'v', '.OOO.O' : 'w', 'OO..OO' : 'x',
    'OO.OOO' : 'y', 'O..OOO' : 'z', '......' : ' '
}

Braille_Digit = {
    '.OOO..' : '0', 'O.....' : '1', 'O.O...' : '2', 'OO....' : '3', 'OO.O..' : '4',
    'O..O..' : '5', 'OOO...' : '6', 'OOOO..' : '7', 'O.OO..' : '8', '.OO...' : '9'
}

Braille_Uppercase = '.....O'
Braille_Number = '.O.OOO'

English_To_Braille = {v : k for k, v in Braille_To_English.items()}
English_Digit = {v : k for k, v in Braille_Digit.items()}


# Determines whether word is Braille or not.
# True if it is in Braille and false otherwise

def isBraille(word):
    for i in word: 
        if i != 'O' and i != '.':
            return False
    return True


# Returns the the string that is English version  
# of word which was originally in Braille

def brailleToEnglish(word):
    result = []
    isCapital = False
    isNumber = False
    index = 0

    while index < len(word):
        # Slice every 6 characters
        currLetter = word[index:index + 6]
        
        if currLetter == Braille_Uppercase:
            isCapital = True
        elif currLetter == Braille_Number:
            isNumber = True
        else:
            if isCapital:
                result.append(Braille_To_English[currLetter].capitalize())
                isCapital = False

            elif isNumber:
                if Braille_To_English[currLetter] == ' ':
                    result.append(' ')
                    isNumber = False
                else:
                    result.append(Braille_Digit[currLetter])
            
            else:
                result.append(Braille_To_English[currLetter])
        index += 6
    
    return ''.join(result)


# Returns the the string that is Braille version  
# of word which was originally in English

def englishToBraille(word):
    result = []
    isNumber = False
    index = 0

    while index < len(word):

        if word[index].isupper() and word[index].isalpha():
            result.append(Braille_Uppercase)
            result.append(English_To_Braille[word[index].lower()])

        elif word[index].isdigit():
            if isNumber == False:
                isNumber = True
                result.append(Braille_Number)
            result.append(English_Digit[word[index]])

        else:
            if word[index] == ' ' and isNumber == True:
                isNumber = False
            result.append(English_To_Braille[word[index]])

        index += 1
    return ''.join(result)


if __name__ == "__main__":
    input_word = ' '.join(sys.argv[1:])
    if isBraille(input_word):
        print(brailleToEnglish(input_word))
    else:
        print(englishToBraille(input_word))

