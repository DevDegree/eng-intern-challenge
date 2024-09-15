# Braille Translator
import sys

E2B_MAP = { # English -> Braille Character Mapping
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
    " ": "......"
}

# NOTE: Can't move NUM2B_MAP into the same MAP as above, since when we invert/reverse 
# this we will have the same key trying to map to multiple values. 
# For example: "O....." -> ("a", "1") and this would be incorrect!

NUM2B_MAP = { # Number to Braille Mapping
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
}

B2E_MAP = {v: k for (k,v) in E2B_MAP.items()} # Reverse the E2B_MAP
B2NUM_MAP = {v: k for (k,v) in NUM2B_MAP.items()} # Reverse the NUM2B_MAP

CAPITAL = ".....O" # CAPITAL_FOLLOWS
NUMBER = ".O.OOO" # NUMBER_FOLLOWS
SPACE = "......" # SPACE CONSTANT

def braille_to_english(input_str: str) -> str:
    """
    Function to convert Braille into English
    
    Returns: String with the final translation
    """
    ans = ""
    # Break up input_str into chunks of length 6
    chunks = [input_str[i: i + 6] for i in range(0, len(input_str), 6)] 
    isCapital = isNumber = False
    
    for chunk in chunks:
        if isCapital:
            # Reset isCapital to False and add in the UPPERCASE letter to ans
            isCapital = False
            ans += B2E_MAP.get(chunk, "").upper()
        elif chunk == CAPITAL:
            # first time seeing a CAPITAL, so mark as true and move on
            isCapital = True
        elif isNumber:
            # we are in a sequence of numbers, add in the the NUMBER to ans
            ans += B2NUM_MAP.get(chunk, "")
        elif chunk == NUMBER:
            # we are going to start seeing NUMBERs now!
            isNumber = True
        elif chunk == SPACE:
            # Reset isNumber back to False and add in " " in the ans
            isNumber = False
            ans += B2E_MAP.get(chunk, "")
        else: # GENERAL CASE -> "NORMAL" LETTERS
            ans += B2E_MAP.get(chunk, "")
    
    return ans
    
    
def english_to_braille(input_str: str) -> str:
    """
    Function to convert English into Braille
    
    Returns: String with the final translation
    """
    ans = ""
    isNumber = False
    for char in input_str:
        if char.isupper(): # CAPITAL LETTER
            ans += CAPITAL
            ans += E2B_MAP.get(char.lower(), "") # Find its LOWERCASE counterpart in our map
        elif char.isnumeric(): # NUMBER
            if not isNumber:
                # If this is the first number in this sequence, we know a NUMBER_FOLLOWS
                isNumber = True
                ans += NUMBER
            ans += NUM2B_MAP.get(char, "")
        elif char.isspace(): # SPACE
            isNumber = False # After seeing a SPACE, we reset isNumber to False again
            ans += E2B_MAP.get(char, "")
        else: # REGULAR CHARACTER
            ans += E2B_MAP.get(char, "")
    
    return ans


def is_braille(input_str: str) -> bool:
    """
    Function that checks if the input string (input_str) is Braille
    based on the following rules:
        -> Need length of the input_str to be a multiple of 6, since each chunk of Braille is 6 characters long.
        -> AND Need all characters to be either "O" or "."
        -> AND Need atleast 1 "." since there is an edge case where "OOOOOO" is valid English too.
    Outputs: True -> if input_str is Braille
             False -> otherwise
    """
    return (len(input_str) % 6 == 0) and \
           (all(char in ["O","."] for char in input_str)) and \
           (any(char == "." for char in input_str))

if __name__ == "__main__":
    arguments = sys.argv
    if len(arguments) < 2:
        print("Usage: python translator.py <English or Braille>")
        
    input_str = " ".join(arguments[1:])
    
    # Braille alphabet consists of "[a-zA-Z][0-9]<space>"
    
    translate = braille_to_english if is_braille(input_str) else english_to_braille
    print(translate(input_str))
    