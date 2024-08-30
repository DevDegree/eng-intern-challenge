import sys

NUM_TO_BRAILLE = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
}

ALPHA_TO_BRAILLE = {
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
    "z": "O..OOO"
}

BRAILLE_TO_NUM = {value: key for key, value in NUM_TO_BRAILLE.items()}
BRAILLE_TO_ALPHA = {value: key for key, value in ALPHA_TO_BRAILLE.items()}

CAPITAL = ".....O"
NUMBER = ".O.OOO"
SPACE = "......"

def translate(input_str: str) -> str:
    is_braille: bool = isBraille(input_str)

    if (is_braille):
        result: str = convertBrailleToEnglish(input_str)
    else:
        result: str = convertEnglishToBraille(input_str)
    
    return result

def convertBrailleToEnglish(input_str: str) -> str:
    result: str = ""
    
    l_pointer: int = 0
    while l_pointer < len(input_str):
        braille: str = input_str[l_pointer: l_pointer + 6]

        if (braille == CAPITAL) and (l_pointer + 6 < len(input_str)): # Make sure there is one more character worth of braille after the capital follows
            l_pointer += 6
            next_braille: str = input_str[l_pointer: l_pointer + 6]
            result += BRAILLE_TO_ALPHA[next_braille].upper()
        elif braille == NUMBER: # Start of a number
            while l_pointer + 6 < len(input_str) and input_str[l_pointer + 6: l_pointer + 12] in BRAILLE_TO_NUM: # Iterate until next character is not a number or is end of input_str
                l_pointer += 6
                next_braille: str = input_str[l_pointer: l_pointer + 6]
                result += BRAILLE_TO_NUM[next_braille]
        elif braille == SPACE: # Space
            result += " "
        else: # Lowercase alphabet
            result += BRAILLE_TO_ALPHA[braille]

        l_pointer += 6

    return result

def convertEnglishToBraille(input_str: str) -> str:
    result: str = ""

    l_pointer: int = 0
    while l_pointer < len(input_str):
        char = input_str[l_pointer]
        if char.isalpha(): # Char is an alphabet
            if char.isupper(): # Char is uppercased alphabet
                result += CAPITAL
            result += ALPHA_TO_BRAILLE[char.lower()]
        elif char.isnumeric(): # Start of a number
            result += NUMBER
            result += NUM_TO_BRAILLE[char]
            while l_pointer + 1 < len(input_str) and input_str[l_pointer + 1].isnumeric(): # Iterate until next character is not a number or is end of input_str
                l_pointer += 1
                result += NUM_TO_BRAILLE[input_str[l_pointer]]
        else: # Char is a space
            result += SPACE
        l_pointer += 1
        
    return result


def isBraille(input_str: str) -> bool:
    # If the input is not a multiple of 6, then it is not braille
    if len(input_str) % 6 != 0:
        return False
    
    # Iterate through the characters and if it is not . or O, it is not braille
    for char in input_str:
        if char != "." and char != "O":
            return False

    # If the input passes the above two checks, it is braille
    return True

if __name__ == "__main__":
    args = " ".join(sys.argv[1:])
    print(translate(args))