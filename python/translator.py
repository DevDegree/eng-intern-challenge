import sys

#Take input line from user
user_input = ' '.join(sys.argv[1:])

# Braille Dictionary for english to braille
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',

    # Capital letter indicator
    'capital': '.....O',

    # Numbers 1-9 and 0 (1-9 correspond to a-i in Braille, 0 to j)
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',

    # Number indicator
    'number': '.O.OOO',

    # Space
    ' ': '......'
}
#braille to english for letters
dict_A = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z'
}
#braille to english for numbers
dict_B = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0'
}


# method/function for converting english to braille
def english_to_braille(english):
    #initiallize variables
    output = ['']
    number_mode = False
    #for loop to go through all characters
    for char in english:
        #check if the char is a number
        if char.isdigit():
            #if it is a number, and the char right before this was not a number, output the correct braille to indiacte the upcoming char is a number
            if number_mode == False:
                number_mode = True
                output.append(braille_dict['number'])
            #add the number to output
            output.append(braille_dict[char])
        #check if the char is then and alpha from a-z
        elif char.isalpha():
            #first check to see if it is uppercase
            if char.isupper():
                output.append(braille_dict["capital"])
                output.append(braille_dict[char.lower()])
            #otherise proceed as normal
            else:
                output.append(braille_dict[char])
        #lastly if the char is a space, then provide it as the key
        elif char == ' ':
            output.append(braille_dict[" "])
            number_mode = False
#format output properly
    return ''.join(output)

#class/function for translate from braille to english
def braille_to_english(braille):
    #intialize all variables
    output = ['']
    i=0
    number_mode = False
    capital_mode = False
    #loop to work though all of the input
    while i < len(braille):
        #simple math/spacing since braile is in clumps of 6 chars
        temp = braille[i:i+6]
        i = i+6
        #first check if we had determined the char is a a capital, then do this immedialty instead
        if capital_mode == True:
            output.append(dict_A[temp].upper())
            capital_mode = False
        #next check if it is a space
        elif temp == '......':
            output.append(" ")
            number_mode = False
        #otherise -
        else:
            #check if is showing we have numbers up coming
            if temp == '.O.OOO':
                number_mode = True
            #if we know we have numbers, and no spce has been made yet, proceed witht the numbers dictionary
            elif number_mode == True:
                output.append(dict_B[temp])
            #check if input is saying we have a capital
            elif temp == '.....O':
                number_mode = False
                capital_mode = True
                #last option is a normal lower case alpha
            else:
                output.append(dict_A[temp])


#reformat for proper output
    return ''.join(output)
#class to detect direction of translation
def detect(input_text):
    #if the input string consits of only . or O, and it is divisable by 6 we can safely conclude it is a a braille input
    if all( c in ".O" for c in user_input) and len(user_input)%6==0:
        return braille_to_english(user_input)
    else:
        return english_to_braille(user_input)

output = detect(user_input)
print(output)
