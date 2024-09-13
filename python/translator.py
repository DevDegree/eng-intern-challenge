import sys

#dictionary that holds English characters as key and the braille equivalent as the value
englishToBraille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', '0': '.OOO..', '1': 'O.....', '2': 'O.O...', 
    '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', 
    '8': 'O.OO..', '9': '.OO...', "number follows": ".O.OOO","uppercase follows": ".....O"
}

#vice-versa of the above dictionary
brailleToEnglish = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "......": " ", ".O.OOO": "number follows", ".....O": "uppercase follows"
}

#the numbers version of the above dictionary
brailleToEnglishNumbers = {
    ".OOO..": "0", "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", 
    "O..O..": "5", "OOO...": "6", "..OO.O": "7", "OOOO..": "8", ".OO...": "9"
}

def translateEnglishToBraille(text):
    #final answer that will be combined together at the end using join
    translated = []
    #toggle variable to check if the "number follows" has been already put
    numberMode = False

    #looping though each character in the English phrase
    for i in text:
        #if the character is a digit
        if i.isdigit():
            #if the number isn't coming in
            if not numberMode:
                #add the "number follows" braille symbol to the list
                translated.append(englishToBraille["number follows"])
                 #indicate that it isn't a number
                numberMode = True
            #add the corresponding number to the list
            translated.append(englishToBraille[i])
        #if the number is a letter from the alphabet
        elif i.isalpha():
            #checking for uppercase letter to add proper braille sign to string
            if i.isupper():
                #add the "capital letter follows" braille symbol to the list
                translated.append(englishToBraille["uppercase follows"])
            #convert to lowercase since the dictionary only accounts for lowercase letters
            lowercase = i.lower()
            #add corresponding letter to the list
            translated.append(englishToBraille[lowercase])
            #indicate that it isn't a number
            numberMode = False
        #for all other symnols
        else:
            #add corresponding letter to the list
            translated.append(englishToBraille[i])
             #indicate that it isn't a number
            numberMode = False

    #join the elements in the list together to form the answer
    return "".join(translated)

def translateBrailleToEnglish(text):
    #split the braille text into groups of 6 for interpretation
    brailleCharacters = [text[i:i+6] for i in range(0, len(text), 6)]
    #holds list of characters which composes final answer
    translated = []
    #checks for uppercase letters
    isUpperCase = False
    #boolean to check if the previous braille character was the "number follows" symbol
    numberFollowsBefore = False
    
    #checking every braille character
    for i in brailleCharacters:
        #if there is a number that follows before
        if numberFollowsBefore:
            #we assume that if there is a space, the numberFollowsBefore toggle will be false
            if i == "......": 
                translated.append(" ")
                numberFollowsBefore = False
            else:
                #if not we just append i
                translated.append(brailleToEnglishNumbers[i])
            continue
        #if a number doesn't follow before
        else:
            #if it's a number, then we set the toggle variable to true
            if brailleToEnglish[i] == "number follows":
                numberFollowsBefore = True
                continue
            #if it's an uppercase, pass but set the isUpperCase to true
            elif brailleToEnglish[i] == "uppercase follows":
                isUpperCase = True
                numberFollowsBefore = False
                continue
            #if we encounter a space
            elif brailleToEnglish[i] == " ":
                translated.append(brailleToEnglish["......"])
                numberFollowsBefore = False
                continue
            #else, it's a normal letter
            else:
                #if it's an uppercase, then return the translation answer in uppercase
                if isUpperCase:
                    translated.append(brailleToEnglish[i].upper())
                    isUpperCase = False
                    numberFollowsBefore = False
                #if it isn't uppercase, return the letter with no uppercase
                else:
                    translated.append(brailleToEnglish[i])
                    numberFollowsBefore = False
    
    #join the elements in the list together to form the answer
    return "".join(translated)

#method to figure out which translation method to use
def translate(text):
    
    #variable to hold the braille status of the input text
    isBraille = False
    
    #if the length of the input isn't a multiple of 6 then it automatically isn't braille
    if len(text) % 6 != 0:
        isBraille = False
    else:
        #for every letter in text
        for i in text:
            #if it is . or O, then we assume that input is braille
            if i == "." or i == "O":
                isBraille = True
            #if we come across a character that isn't . or O, break out of loop
            else:
                isBraille = False
                break
    
    #choosing which function to run and return the answer depending on whether the input text is braille or not
    if isBraille:
        return translateBrailleToEnglish(text)
    else:
        return translateEnglishToBraille(text)

#function to run file from the command line
def main():
    #get the command-line arguments (excluding the script name)
    args = sys.argv[1:]
    #join the arguments to form the input text
    input_text = ' '.join(args)
    #call the translate function and print the result
    print(translate(input_text))

if __name__ == "__main__":
    main()