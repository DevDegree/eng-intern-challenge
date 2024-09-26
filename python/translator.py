from enum import Enum
import sys

# List up all Braille
class BrailleDot(Enum):
    RAISED     = 'O' # which represents the raised dot
    NOT_RAISED = '.' # which represents the not raised dot

class Braille(Enum):
    # Alphabet
    A = ((0, 1, 1, 1, 1, 1), "a")
    B = ((0, 1, 0, 1, 1, 1), "b")
    C = ((0, 0, 1, 1, 1, 1), "c")
    D = ((0, 0, 1, 0, 1, 1), "d")
    E = ((0, 1, 1, 0, 1, 1), "e")
    F = ((0, 0, 0, 1, 1, 1), "f")
    G = ((0, 0, 0, 0, 1, 1), "g")
    H = ((0, 1, 0, 0, 1, 1), "h")
    I = ((1, 0, 0, 1, 1, 1), "i")
    J = ((1, 0, 0, 0, 1, 1), "j")
    K = ((0, 1, 1, 1, 0, 1), "k")
    L = ((0, 1, 0, 1, 0, 1), "l")
    M = ((0, 0, 1, 1, 0, 1), "m")
    N = ((0, 0, 1, 0, 0, 1), "n")
    O = ((0, 1, 1, 0, 0, 1), "o")
    P = ((0, 0, 0, 1, 0, 1), "p")
    Q = ((0, 0, 0, 0, 0, 1), "q")
    R = ((0, 1, 0, 0, 0, 1), "r")
    S = ((1, 0, 0, 1, 0, 1), "s")
    T = ((1, 0, 0, 0, 0, 1), "t")
    U = ((0, 1, 1, 1, 0, 0), "u")
    V = ((0, 1, 0, 1, 0, 0), "v")
    W = ((1, 0, 0, 0, 1, 0), "w")
    X = ((0, 0, 1, 1, 0, 0), "x")
    Y = ((0, 0, 1, 0, 0, 0), "y")
    Z = ((0, 1, 1, 0, 0, 0), "z")
    
    # Numbers
    ONE   = ((0, 1, 1, 1, 1, 1), "1")
    TWO   = ((0, 1, 0, 1, 1, 1), "2")
    THREE = ((0, 0, 1, 1, 1, 1), "3")
    FOUR  = ((0, 0, 1, 0, 1, 1), "4")
    FIVE  = ((0, 1, 1, 0, 1, 1), "5")
    SIX   = ((0, 0, 0, 1, 1, 1), "6")
    SEVEN = ((0, 0, 0, 0, 1, 1), "7")
    EIGHT = ((0, 1, 0, 0, 1, 1), "8")
    NINE  = ((1, 0, 0, 1, 1, 1), "9")
    ZERO  = ((1, 0, 0, 0, 1, 1), "0")
    
    # FOLLOWS
    CAPITAL_FOLLOWS = ((1, 1, 1, 1, 1, 0), None)
    DECIMAL_FOLLOWS = ((1, 0, 1, 1, 1, 0), None)
    NUMBER_FOLLOWS  = ((1, 0, 1, 0, 0, 0), None)
    
    # Special Characters
    PERIOD        = ((1, 1, 0, 0, 1, 0), ".")
    COMMA         = ((1, 1, 0, 1, 1, 1), ",")
    QUESTION      = ((1, 1, 0, 1, 0, 0), "?")
    EXCLAMATION   = ((1, 1, 0, 0, 0, 1), "!")
    COLON         = ((1, 1, 0, 0, 1, 1), ":")
    SEMICOLON     = ((1, 1, 0, 1, 0, 1), ";")
    HYPHEN        = ((1, 1, 1, 1, 0, 0), "-")
    SLASH         = ((1, 0, 1, 1, 0, 1), "/")
    LESS_THAN     = ((1, 0, 0, 1, 1, 0), "<")
    GREATER_THAN  = ((0, 1, 1, 0, 0, 1), ">")
    BRACKET_OPEN  = ((0, 1, 0, 1, 1, 0), "(")
    BRACKET_CLOSE = ((1, 0, 1, 0, 0, 1), ")")
    SPACE         = ((1, 1, 1, 1, 1, 1), " ")
    
    def __init__(self, braille, symbol):
        self._braille = braille
        self._symbol = symbol

    @property
    def symbol(self):
        return self._symbol

# Check if the string given to it is either Braille or English
def isBraille(string):
    # If the length of the string is less than 6, it's not Braille. (i.e. "." or "A")
    if len(string) < 6:
        return False
    
    # If the string includes any alphabets, it's not Braille (i.e. "A" or "b")
    if any(char.isalpha() for char in string):
        return False
    
    # If the string includes any numbers, it's not Braille (i.e. "1" or ".2")
    if any(char.isdigit() for char in string):
        return False
    
    # If the string includes any special characters except for period, it's not Braille (i.e. "?" or ":!")
    if any(char in [',', '?', '!', ':', ';', '-', '/', '<', '>', '(', ')', ' '] for char in string):
        return False
    
    return True

# Convert the string from English to Braille (i.e. "a" -> "0.....", "a12b" -> "0......0.0000.....0.0.........0.0...")
def convertFromEnglishToBraille(string):
    result = ""
    isPrevNumber = False # Use this to check if the previous character was a number
    
    # Iterate through each character in the string
    for char in string:
        # Check which character is which in the Braille enum
        for braille in Braille:
            # If the character is found in the Braille enum
            if char.lower() == braille.symbol:
                # Check if the character is a capital letter. If so, add the CAPITAL_FOLLOWS to the result
                if char.isupper():
                    for dot in braille.CAPITAL_FOLLOWS._braille:
                        if dot == 1:
                            result += BrailleDot.NOT_RAISED.value # Add a dot
                        else:
                            result += BrailleDot.RAISED.value     # Add O
                    
                # Check if the character is a number, If so add the NUMBER_FOLLOWS to the result
                if char.isdigit():
                    # If the previous character was not a number, add the NUMBER_FOLLOWS to the result
                    if isPrevNumber == False:
                        isPrevNumber = True
                        for dot in braille.NUMBER_FOLLOWS._braille:
                            if dot == 1:
                                result += BrailleDot.NOT_RAISED.value # Add a dot
                            else:
                                result += BrailleDot.RAISED.value     # Add O
                else:
                    isPrevNumber = False
                
                # Add the Braille character to the result
                for dot in braille._braille:
                    # Check if the previous character was a number and the current character is not a number, add a space
                    if isPrevNumber == True and char.isdigit() == False:
                        for dot in braille.SPACE._braille:
                            if dot == 1:
                                result += BrailleDot.NOT_RAISED.value  # Add a dot
                            else:
                                result += BrailleDot.RAISED.value      # Add O
                    if dot == 1:
                        result += BrailleDot.NOT_RAISED.value # Add a dot
                    else:
                        result += BrailleDot.RAISED.value     # Add O
                break

    return result
    
# Convert the string from Braille to English
def convertFromBrailleToEnglish(string):
    print("not implemented yet:", string)

# Get the arguments from the command line
args = sys.argv
originalString = ""

# Concat all the arguments into one string with a space in between
if len(sys.argv) > 1:
    originalString = " ".join(args[1:])

if isBraille(originalString):
    print(convertFromBrailleToEnglish(originalString))
else:
    print(convertFromEnglishToBraille(originalString))