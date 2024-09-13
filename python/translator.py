import sys



english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
           'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
           '.', ',', '?', '!', ':', ';', '-', '/', '<', '>', '(', ')', ' ']

capitalEnglish = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
    'U', 'V', 'W', 'X', 'Y', 'Z'
]

Braille = [
    'O.....',  
'O.O...',  
'OO....',  
'OO.O..',  
'O..O..',  
'OOO...',  
'OOOO..',  
'O.OO..',  
'.OO...',  
'.OOO..',  
'O...O.',  
'O.O.O.',  
'OO..O.',  
'OO.OO.',  
'O..OO.',  
'OOO.O.',  
'OOOOO.',  
'O.OOO.',  
'.OO.O.',  
'.OOOO.',  
'O...OO',  
'O.O.OO',  
'.OOO.O',  
'OO..OO',  
'OO.OOO',  
'O..OOO',  
'O.....',  
'O.O...',  
'OO....',  
'OO.O..',  
'O..O..',  
'OOO...',  
'OOOO..',  
'O.OO..',  
'.OO...',  
'.OOO..',  
'..OO.O',  
'..O...',  
'..O.OO',  
'..OOO.',  
'..OO..',  
'..O.O.',  
'....OO',  
'.O..O.',  
'.OO..O',  
'O..OO.',  
'O.O..O',  
'.O.OO.',  
'......'   

]

capitalBraille = '.....O'
numberBraille = '.O.OOO'
decimalBraille = '.O...O'


user_input = ' '.join(sys.argv[1:])

isEnglish = False
isBraille = False

# Determine if the input is Braille or English
testingArray = []
i = 0

while i < len(user_input):
    testingArray.append(user_input[i:i + 6])
    i += 6

if testingArray[0] in Braille or testingArray[0] == capitalBraille or testingArray[0] == numberBraille or testingArray[0] == decimalBraille:
    isBraille = True
else:
    isEnglish = True

output = ""

if isEnglish:
    i = 0
    user_input_array = list(user_input)
    
    while i < len(user_input_array):
        char = user_input_array[i]

        if char in capitalEnglish:
            index_of_char = english.index(char.lower())
            output += capitalBraille
            output += Braille[index_of_char]
            i+=1
        elif char.isdigit():
            output += numberBraille
            while i < len(user_input_array) and user_input_array[i] != ' ':
                char = user_input_array[i]
                if char == '.':
                    output += decimalBraille
                else:
                    if char in english:
                        indices = [index for index, value in enumerate(english) if value == char]

                        if indices:
                            index_of_char = indices[-1]
                            output += Braille[index_of_char]
                i += 1
        elif char == '.':
            if i + 1 < len(user_input_array) and user_input_array[i + 1].isdigit():
                output += decimalBraille
            i += 1
        else:
            if char in english:
                index_of_char = english.index(char)
                output += Braille[index_of_char]
            i += 1
    
    print(output)


if isBraille:
    i = 0
    user_input_array = []
    
    while i < len(user_input):
        user_input_array.append(user_input[i:i + 6])
        i += 6
    
    i = 0
    
    while i < len(user_input_array):
        brailleChar = user_input_array[i]

        if brailleChar == capitalBraille:
            if i + 1 < len(user_input_array):
                brailleChar = user_input_array[i + 1]
                index_of_char = Braille.index(brailleChar)
                letter = english[index_of_char]
                output += letter.upper()
                i += 2
            else:
                i += 1
        elif brailleChar == numberBraille:
            i+=1
            while i < len(user_input_array) and user_input_array[i] != '......':
                brailleChar = user_input_array[i]
                if brailleChar == decimalBraille:
                    output += '.'
                else:
                    if brailleChar in Braille:
                        indices = [index for index, value in enumerate(Braille) if value == brailleChar]

                        if indices:
                            index_of_brailleChar = indices[-1]
                            output += english[index_of_brailleChar]

                i += 1
        elif brailleChar == decimalBraille:
            output += '.'
            i += 1
        else:
            if brailleChar in Braille:
                index_of_brailleChar = Braille.index(brailleChar)
                output += english[index_of_brailleChar]
            i += 1
    
    print(output)

    

