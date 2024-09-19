import re  # Access: regex parsing

# High-level idea:
# 
# Braille follows this set of rules:
# - Each "character" has length 6
# - Each "character" is composed solely from "O" or "."
# - There is a defined alphabet, BUT:
#       - Some special instructions, such as "capitalize" / "number" / "decimal" exist
# 
# 
# 
# Observations:
# Problem is broken up into two steps; classifying and translating.
# 
# To classify:
# - Can probably use regex to check if strings match the "O" or "." requirements
# - Can also assert that inputString.length() % 6 == 0 to match Braille length
# 
# ===================================================================================
# 
# To translate (FROM Braille):
# - Can tokenize each Braille character
# - Can check the edge cases (capitalize, number)
#       - Handle it
# - Can reference a dictionary to replace the characters
# 
# POTENTIAL EDGE CASE: The string "OOOOOO" passes the regex and length requirement,
#                      but would still be an English string, because that character isn't in the Braille ALPHABET.
#                      => if token not in Braille dict, translate the input string from English -> Braille
# 
# 
# * To translate (FROM ENGLISH):
# - For each char, check:
#       - is number or decimal
#       - is capital
# - Apply transformation rules
# - Replace with Braille alphabet entry
# 
# ===================================================================================



CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS  = ".O.OOO"

ALPHABET = {
    "j": ".OOO..",  # Value may also be 0
    "a": "O.....",  # Value may also be 1
    "b": "O.O...",  # Value may also be 2
    "c": "OO....",  # Value may also be 3
    "d": "OO.O..",  # Value may also be 4
    "e": "O..O..",  # Value may also be 5
    "f": "OOO...",  # Value may also be 6
    "g": "OOOO..",  # Value may also be 7
    "h": "O.OO..",  # Value may also be 8
    "i": ".OO...",  # Value may also be 9
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

def english_to_braille(str: str) -> str:
    # State variable for checking if we're in numeric mode
    numeric_mode = False

    out = ""
    for c in str:
        if (c.isdigit()):

            # Toggle numeric mode and prepend with the "number follows"
            if not numeric_mode:
                numeric_mode = True
                out += NUMBER_FOLLOWS

            # Dictionary is ordered such that the "letter" entries are indexed by their numerical counterpart 
            # j = 0, a = 1, b = 2, ..., i = 9
            out += ALPHABET[list(ALPHABET)[int(c)]]
            continue
        
        # Space should disable numeric mode
        if(c == ' '):
            numeric_mode = False

        # Space should not trigger this -- should also prepend the capital letter with "capital follows"
        elif(c.capitalize() == c):
            out += CAPITAL_FOLLOWS
            c = c.lower()

        out += ALPHABET[c]

    return out
    

def braille_to_english(user_str: str) -> str:
    # Tokenize using list comprehension.
    # We've already asserted that len % 6 == 0 (evenly divisible by 6)
    tokenized = [user_str[i:i+6] for i in range(0, len(user_str), 6)]
    
    # Invert the ALPHABET dictionary to make it easier to build output string
    inv_map = {v: k for k, v in ALPHABET.items()}    

    out = ""
    consumed_cap = False
    number_mode = False

    
    # print(tokenized)
    
    for braille_char in tokenized:
        if(braille_char not in inv_map):
            # braille_char can either be:
            # NUMBER_FOLLOWS
            # CAPITAL_FOLLOWS
            # (or, not valid Braille)

            if(braille_char == NUMBER_FOLLOWS):
                number_mode = True
                # Consume this non-printed character
                continue

            if(braille_char == CAPITAL_FOLLOWS):
                consumed_cap = True
                # Consume this non-printed character
                continue


            # Catch edge cases about Braille-like inputs, but with invalid characters -- e.g. (OOOOOO)+
            return english_to_braille(user_str)
        

        # Valid Braille / is in the map.
        # Depending on capital / number mode, apply modifications
        if(consumed_cap):
            out += inv_map[braille_char].capitalize()
            consumed_cap = False
            continue

       
        # Spaces should disable number mode
        if(braille_char == "......"):
            number_mode = False

        # If in number mode, need to output numbers instead of A-J
        if(number_mode):
            out += str(list((inv_map.keys())).index(braille_char))
            continue
        
        out += inv_map[braille_char]
    
    return out

if __name__ == "__main__":
    # user_str = input()
    # print(user_str)
    if(re.fullmatch('^(\\.|O)*$', user_str) and (len(user_str) % 6 == 0)):
        # print("Potentially Braille\n")
        print("$" + braille_to_english(user_str) + "$")

    else:
        # print("Not Braille\n")
        print(english_to_braille(user_str))
