# Import Basic Libraries
import sys

# Reading in the argument
if len(sys.argv) == 1:
    print('No argument passed')
    exit(0)

text = ' '.join(sys.argv[1:])

# Braille Dictionaries
# As per instructions I will only include letter values a-z, ability to capitalize, number 0-9, and " "

alphabet = {'a':'O.....', 'b':'O.O...', 'c':'OO....',
            'd':'OO.O..', 'e':'O..O..', 'f':'OOO...',
            'g':'OOOO..', 'h':'O.OO..', 'i':'.OO...',
            'j':'.OOO..', 'k':'O...O.', 'l':'O.O.O.',
            'm':'OO..O.', 'n':'OO.OO.', 'o':'O..OO.',
            'p':'OOO.O.', 'q':'OOOOO.', 'r':'O.OOO.',
            's':'.OO.O.', 't':'.OOOO.', 'u':'O...OO',
            'v':'O.O.OO', 'w':'.OOO.O', 'x':'OO..OO',
            'y':'OO.OOO', 'z':'O..OOO'}

numeric = {"1": "O.....",
            "2": "O.O...",
            "3": "OO....",
            "4": "OO.O..",
            "5": "O..O..",
            "6": "OOO...",
            "7": "OOOO..",
            "8": "O.OO..",
            "9": ".OO...",
            "0": ".OOO.."}

inverse_alphabet = {value: key for key, value in alphabet.items()}

inverse_numeric = {value: key for key, value in numeric.items()}


# Translator UDFs

# AlphaNumeric to Braille
## Alphabet to Braille
def AlphaToBraille(value):
    char = value.lower()
    return alphabet.get(char, 'invalid')

## Numeric to Braille
def NumericToBraille(value):
    return numeric.get(value, 'invalid')


# Braille to AlphaNumeric
## Braille to Alphabet
def BrailleToAlpha(value):
    return inverse_alphabet.get(value, 'invalid')

## Braille to Numeric
def BrailleToNumeric(value):
    return inverse_numeric.get(value, 'invalid')


# Braille to Alphanumeric #######problem with numeric inputs, braille to numeric doesnt show

def BrailleToAlphanumeric(input):

    initiated_string = ''
    capitalize = False
    numeric = False 

    for i in range(0, len(input), 6):
        chunk = input[i:i+6]

        if chunk == "......": # Space 
            character_value = " "
            numeric = False
        
        elif numeric:
            character_value = BrailleToNumeric(chunk)

        elif chunk == ".O.OOO": # Number Follows
            numeric = True
            continue

        elif chunk == ".....O": # Capital Follows
            capitalize = True
            continue
        
        else:
            character_value = BrailleToAlpha(chunk)
        
        if capitalize:
            character_value = character_value.upper()
            capitalize = False 

        initiated_string += character_value

    return initiated_string

# Alphanumeric to Braille


def AlphanumericToBraille(input):

    initiated_string = ''
    numeric = False

    for i in input:

        if i == ' ':
            character_value = '......'
            numeric = False

        elif i.isupper():
            capital_indicator = '.....O' 
            small_caps = AlphaToBraille(i.lower())
            character_value = capital_indicator + small_caps

        elif i.isdigit():
            numeric_indicator = '.O.OOO'
            numeric_value = NumericToBraille(i)
            if not numeric:
                character_value = numeric_indicator + numeric_value
                numeric = True
            else:
                character_value = numeric_value

        else:
            character_value = AlphaToBraille(i)

        initiated_string += character_value

    return initiated_string
    
# The Final Translator Function, Determining if its Braille or Alhpanumeric 
def BrailleTranslator(string_value):

    if any(char not in '.O' for char in string_value):
        translated = AlphanumericToBraille(string_value)

    else:
        translated = BrailleToAlphanumeric(string_value)

    return translated


print(BrailleTranslator(text))
