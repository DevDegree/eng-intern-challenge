import sys
# English to Braille map
ENGLISH_TO_BRAILLE = {
    'A':'O.....',
    'B':'O.O...',
    'C':'OO....',
    'D':'OO.O..',
    'E':'O..O..',
    'F':'OOO...',
    'G':'OOOO..',
    'H':'O.OO..',
    'I':'.OO...',
    'J':'.OOO..',
    'K':'O...O.',
    'L':'O.O.O.',
    'M':'OO..O.',
    'N':'OO.OO.',
    'O':'O..OO.',
    'P':'OOO.O.',
    'Q':'OOOOO.',
    'R':'O.OOO.',
    'S':'.OO.O.',
    'T':'.OOOO.',
    'U':'O...OO',
    'V':'O.O.OO',
    'W':'.OOO.O',
    'X':'OO..OO',
    'Y':'OO.OOO',
    'Z':'O..OOO',
    '1':'O.....',
    '2':'O.O...',
    '3':'OO....',
    '4':'OO.O..',
    '5':'O..O..',
    '6':'OOO...',
    '7':'OOOO..',
    '8':'O.OO..',
    '9':'.OO...',
    '0':'.OOO..',
    '.':'..OO.O',
    ',':'..O...',
    '?':'..O.OO',
    '!':'..OOO.',
    ':':'..OO..',
    ';':'..O.O.',
    '-':'....OO',
    '/':'.O..O.',
    '<':'.OO..O',
    '>':'O..OO.',
    '(':'O.O..O',
    ')':'.O.OO.',
    ' ':'......',
}

# English to Braille numbers map
ENGLISH_TO_BRAILLE_NUMS={
    '1':'O.....',
    '2':'O.O...',
    '3':'OO....',
    '4':'OO.O..',
    '5':'O..O..',
    '6':'OOO...',
    '7':'OOOO..',
    '8':'O.OO..',
    '9':'.OO...',
    '0':'.OOO..'
}

# Define other constants
CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS  = '.O.OOO'
BRAILLE_CHUNK = 6

'''
Input is English, output is Braille.
Takes a string as an argument and uses it as the input string
'''
def translate_english_to_braille(_input):
    output_str = ""
    flag_set = False
    for letter in _input:
        if(letter.isupper()):
            output_str+=CAPITAL_FOLLOWS
            # Reset the NUMBER_FOLLOWS flag to false
            flag_set = False
        elif(letter.isdigit()):
            if(not flag_set):
                # Set the the NUMBER_FOLLOWS flag to True
                flag_set = True
                output_str+=NUMBER_FOLLOWS
        # Append the current character to the output string
        output_str+=ENGLISH_TO_BRAILLE[letter.upper()]

    return output_str

'''
Input is Braille, output is English.
Takes a string as an argument and uses it as the input string
'''
def translate_braille_to_english(_input):
    pass



# Get all command-line arguments but ignoring the script name
_input = ' '.join(sys.argv[1:])
# Save the first 6 characters of the string
inputTypeCheck = _input[0:6]
# E for English, B for Braille
inputType = 'E'
outputString = ""

# Check if the first 6 characters make up a valid braille character
for alpha in ENGLISH_TO_BRAILLE:
    if(ENGLISH_TO_BRAILLE[alpha] == inputTypeCheck):
        inputType='B'
    elif(inputTypeCheck == CAPITAL_FOLLOWS or inputTypeCheck == NUMBER_FOLLOWS):
        inputType='B'
if(inputType == 'B'): # Braille to English
    outputString = translate_braille_to_english(_input)
else: # English to Braille
    outputString = translate_english_to_braille(_input)
    
print(outputString)
