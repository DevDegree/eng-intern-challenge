import sys
from brailleToEnglish import *
from englishToBraille import *

# get all arguments into one string
input = ' '.join(sys.argv[1:])
isBraille = False

args = sys.argv[1:]

#parse input string first
# since only Braille can have '.' and all Braille characters have at least one '.', the '.' character identifies a Braille string
for char in input:
    if char == '.':
        isBraille = True
        break

output = ""
if isBraille:
    # every Braille character has length 6, so entire string will be divisible by 6
    num_chars = len(input) // 6
    isUpper = False
    isNumber = False
    for i in range(num_chars):
        start_char = i * 6  #start of current character
        end_char = start_char + 6 # end of current character
        
        braille_char = input[start_char: end_char]
        
        # need to check if space, if upper, if capital
        
        #if capital follows
        if braille_char == ".....O":
            isUpper = True
            continue
        
        #if space
        if braille_char == "......":
            output += " "
            isNumber = False
            continue
        
        #if number follows 
        if braille_char == ".O.OOO":
            isNumber = True
            continue
        
        if isNumber:
            output += braille_to_number[braille_char]
        else:
            if isUpper:
                output += (braille_to_english[braille_char]).upper()
                isUpper = False
            else:
                output += (braille_to_english[braille_char])

# given English text and need to translate to braille
else :
    needNumberIdentifier = True
    for char in input:
        #if number
        if char.isnumeric():
            #if need to show number follows
            if needNumberIdentifier:    
                output += ".O.OOO"
                needNumberIdentifier = False #now no longer need to show number follows until we reach space
            output += number_to_braille[char]
            continue
            
        #if space
        if char == ' ':
            needNumberIdentifier = True #now need to show "number follows" character in Braille for next number
            output += "......"
            continue
        
        #if capital letter
        if char.isupper():
            output += ".....O"
            char = char.lower() # turn into lowercase
            output += english_to_braille[char]
            continue
        
        else:
            #finally we know we just have a single lowercase letter
            output += english_to_braille[char]

print(output)
