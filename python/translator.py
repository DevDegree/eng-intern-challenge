from enum import Enum

# List up all Braille
class BrailleDot(Enum):
    RAISED = '0' # which represents the raised dot
    NOT_RAISED = '1' # which represents the not raised dot 

class Braille(Enum):
    # Alphabet
    A = (0, 1, 1, 1, 1, 1)
    B = (0, 1, 0, 1, 1, 1)
    C = (0, 0, 1, 1, 1, 1)
    D = (0, 0, 1, 0, 1, 1)
    E = (0, 1, 1, 0, 1, 1)
    F = (0, 0, 0, 1, 1, 1)
    G = (0, 0, 0, 0, 1, 1)
    H = (0, 1, 0, 0, 1, 1)
    I = (1, 0, 0, 1, 1, 1)
    J = (1, 0, 0, 0, 1, 1)
    K = (0, 1, 1, 1, 0, 1)
    L = (0, 1, 0, 1, 0, 1)
    M = (0, 0, 1, 1, 0, 1)
    N = (0, 0, 1, 0, 0, 1)
    O = (0, 1, 1, 0, 0, 1)
    P = (0, 0, 0, 1, 0, 1)
    Q = (0, 0, 0, 0, 0, 1)
    R = (0, 1, 0, 0, 0, 1)
    S = (1, 0, 0, 1, 0, 1)
    T = (1, 0, 0, 0, 0, 1)
    U = (0, 1, 1, 1, 0, 0)
    V = (0, 1, 0, 1, 0, 0)
    W = (1, 0, 0, 0, 1, 0)
    X = (0, 0, 1, 1, 0, 0)
    Y = (0, 0, 1, 0, 0, 0)
    Z = (0, 1, 1, 0, 0, 0)
    
    # Numbers
    ONE   = (0, 1, 1, 1, 1, 1)
    TWO   = (0, 1, 0, 1, 1, 1)
    THREE = (0, 0, 1, 1, 1, 1)
    FOUR  = (0, 0, 1, 0, 1, 1)
    FIVE  = (0, 1, 1, 0, 1, 1)
    SIX   = (0, 0, 0, 1, 1, 1)
    SEVEN = (0, 0, 0, 0, 1, 1)
    EIGHT = (0, 1, 0, 0, 1, 1)
    NINE  = (1, 0, 0, 1, 1, 1)
    ZERO  = (1, 0, 0, 0, 1, 1)
    
    # FOLLOWS
    CAPITAL_FOLLOWS = (1, 1, 1, 1, 1, 0)
    DECIMAL_FOLLOWS = (1, 0, 1, 1, 1, 0)
    NUMBER_FOLLOWS  = (1, 0, 1, 0, 0, 0)
    
    # Special Characters
    PERIOD        = (1, 1, 0, 0, 1, 0)
    COMMA         = (1, 1, 0, 1, 1, 1)
    QUESTION      = (1, 1, 0, 1, 0, 0)
    EXCLAMATION   = (1, 1, 0, 0, 0, 1)
    COLON         = (1, 1, 0, 0, 1, 1)
    SEMICOLON     = (1, 1, 0, 1, 0, 1)
    HYPHEN        = (1, 1, 1, 1, 0, 0)
    SLASH         = (1, 0, 1, 1, 0, 1)
    LESS_THAN     = (1, 0, 0, 1, 1, 0)
    GREATER_THAN  = (0, 1, 1, 0, 0, 1)
    BRACKET_OPEN  = (0, 1, 0, 1, 1, 0)
    BRACKET_CLOSE = (1, 0, 1, 0, 0, 1)
    SPACE         = (1, 1, 1, 1, 1, 1)

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

# Convert the string from English to Braille

# Convert the string from Braille to English