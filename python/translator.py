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

brailleToEnglishNumbers = {
    ".OOO..": "0", "O.....": "1", "..OO..": "2", "OO....": "3", "OO.O..": "4", 
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
            #if it isn't, that means there aren't any and break out of loop
            else:
                isBraille = False
                break
    
    #choosing which function to run depending on whether the input text is braille or not
    if isBraille:
        return translateBrailleToEnglish(text)
    else:
        return translateEnglishToBraille(text)