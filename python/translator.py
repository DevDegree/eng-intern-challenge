import sys

#get english to braille dictionary
english_to_braille_letter_conv = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    " ": "......",
}

english_to_braille_number_conv = {
    "0": ".OOO..",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
}

#get braille to english dictionary
braille_to_english_letter_conv = {}
braille_to_english_number_conv = {}

for key, value in english_to_braille_letter_conv.items():
    braille_to_english_letter_conv[value] = key

for key, value in english_to_braille_number_conv.items():
    braille_to_english_number_conv[value] = key

capitalNext = ".....O"
numberNext = ".O.OOO"

# check whether it is braille using bool
def isBraille(input):
    for letter in input:
        if letter not in 'O.':
            return False
    return True

#translates to english
def translateBraille(string):

    englishString = ""
    charsInString = len(string)
    i = 0 #index for translation

    #error checking
    if(charsInString%6 != 0):
        return "error: braille string is not written correctly"

    # each group of 6
    while i < charsInString:
        #check braille dict for first group
        group = string[i: i+6]

        #if capital indicator
        if(group == capitalNext):
            i += 6
            group = string[i: i+6]
            englishString = englishString + (braille_to_english_letter_conv.get(group, '')).upper()
        #if its a number indicator
        elif(group == numberNext):
            i += 6
            while (i < charsInString): 
                group = string[i: i+6]

                if (braille_to_english_letter_conv.get(group, '') == " "):
                    englishString += " "
                    break

                englishString += braille_to_english_number_conv.get(group, '')
                i += 6
        #just regular lowercase or whitespace
        else:
            englishString += braille_to_english_letter_conv.get(group, '')

        #go to next group of characters
        i += 6

    return englishString

#translates to braille
def translateEnglish(string):
    brailleString = ""
    isNumeric = False

    for char in string:
        #if char is a capital letter, need to add capital next symbol
        if (char.isupper()):
            brailleString += (capitalNext + english_to_braille_letter_conv.get(char.lower(), ''))
        #if char is a number, need to add number next symbol
        elif (char.isnumeric()):
            if(isNumeric is False):
                brailleString += numberNext
            isNumeric = True #so that number next indicator is only occuring once with every collection of numbers
            brailleString += english_to_braille_number_conv.get(char, '')
        #if char is lowercase letter or whitespace
        else:
            isNumeric = False #since this would be where a whitespace would enter
            brailleString += english_to_braille_letter_conv.get(char, '')


    return brailleString


def main():
    inputString = ' '.join(sys.argv[1:]) #to account for whitespaces in string provided
    brailleCheck = isBraille(inputString)
    translatedString = translateBraille(inputString) if brailleCheck else translateEnglish(inputString)
    print(translatedString)
    return

if __name__ == "__main__":
    main()