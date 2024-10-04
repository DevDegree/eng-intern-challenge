
"""
Here is the braille/english alphabet translator
conditions: if a number follows symbol is read, then assume that the following symbols are numbers until there is a space
            if a capital follow symbol is read, then assume that only the immediate following symbol is capital
"""
import sys
# create a dictionary to hold corresponding english alphabets to braille
alphabetToBraille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O..OO.', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......'
}

# create a reverse dictionary for looking up braille symbols/characters for their corresponding english letters
brailleToAlphabet = {v: k for k, v in alphabetToBraille.items()}

number_follows = '.O.OOO'
capital_follows = '.....O'

# create a dictionary to hold numbers
numberToBraille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', 
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
    '0': '.OOO..'
}

# create a reverse dictionary for looking up braille symbols/characters for their corresponding digits
brailleToNumber = {v: k for k, v in numberToBraille.items()}


# Define a function for braille to english
def brailleToEnglish(str1):
    # array to store our results
    results = []

    # checks to see if we triggered a number follows or a capital follows
    capitalNext = False
    numberNext = False

    # since all braille alphabets are in sets of 6 characters, we loop in sets of 6
    for i in range(0, len(str1), +6):
        # extract the braille 'char'
        braille_char = str1[i:i+6]

        # process digits
        if braille_char in brailleToNumber and numberNext:
            results.append(brailleToNumber[braille_char])
        
        # if braille char is a letter
        elif braille_char in brailleToAlphabet:
            # check if there was a previous capital symbol and append item as capital
            if capitalNext:
                results.append(brailleToAlphabet[braille_char].upper())
                capitalNext = False
            else:
                results.append(brailleToAlphabet[braille_char])
            numberNext = False

        # check if its a capital follow symbol
        elif braille_char == capital_follows:
            capitalNext = True

        # check if its a number follow symbol
        elif braille_char == number_follows:
            numberNext = True
                
    return ''.join(results)



# Define a function for english to braille
def englishToBraille(str1):
    # array to store our results
    results = []

    # boolean to check if prev is a number so we dont need to add the number follows symbol
    currentlyAddingNumber = False
    
    # create a loop to loop over characters in the string
    for char in str1:

        # check if char is upper cased
        if char.isupper():
            results.append(capital_follows)
            # make it lowercase so that our dictionary can read it
            char = char.lower()

        # check if char is in our alphabet
        if char in alphabetToBraille:
            results.append(alphabetToBraille[char])

        # check if char is a digit
        elif char.isdigit():
            if not currentlyAddingNumber:
                results.append(number_follows)
                currentlyAddingNumber = True
            results.append(numberToBraille[char])

    return ''.join(results)


# Have a main function that will run commands for us
def main():
    str1 = ' '.join(sys.argv[1:]).strip()
    translated_string = ''
    # determine if our input str1 is from the braille alphabet or the english alphabet
    if all(c in ('O', '.') for c in str1):
        translated_string = brailleToEnglish(str1)
    else:
        translated_string = englishToBraille(str1)

    print(translated_string)

    return translated_string

if __name__ == "__main__":
    main()
    