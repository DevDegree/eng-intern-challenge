"""
This Python script provides a tool for translating between English text and Braille. The translated text will be printed to the console.
The script will automatically detect the input format (Braille or English) and translate accordingly. 
Detection is done through initial assumption of input string as Braille and translate into English. 
If the translation is not possible then the script assumes it is English to be translated into Braille.
"""

import sys
from typing import List
from typing import Dict


CAP_SEQUENCE = ".....O"

NUMERIC_SEQUENCE = ".O.OOO"

SPACE_SEQUENCE =  "......"

TO_BRAILLE_ALPHA = {
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
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": SPACE_SEQUENCE
}

TO_BRAILLE_NUMERIC = {
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
    ".": ".O...O",
    "<": ".OO..O",
    ">": "O..OO.",
}

def reverseMap(map: Dict[str, str]) -> Dict[str, str]:
    """
    Creates a new dictionary by reverse-mapping the input dictionary's keys to values and vice versa. 

    Parameters:
        map (Dict[str, str]): The dictionary to be reversed.

    Returns:
        Dict[str, str]: The dictionary which gets reversed.
    """
    rtn = {}
    for key, value in map.items():
        rtn[value] = key
    return rtn

TO_ENGLISH_ALPHA = reverseMap(TO_BRAILLE_ALPHA)

TO_ENGLISH_NUMERIC = reverseMap(TO_BRAILLE_NUMERIC)

def fastConcat(l : List[str]) -> str: 
    """
    Efficiently concatinate a list of strings. 
    Optimization to fast concat strings: https://stackoverflow.com/questions/1316887/what-is-the-most-efficient-string-concatenation-method-in-python

    Parameters:
        l (List[str): The list of strings to be concatinated.

    Returns:
        str: The concatinated string.
    """
    return ''.join(l)
 
def translateToEnglish(brailleString: str) -> (bool, str):
    """
    Translates a Braille string into an English string.
    
    Braille - each character is read as a series of O (the letter O) or . (a period); 6-character string read from left to right, line by line, starting at the top left. 
    When a Braille capital follows symbol is read, only the next symbol is capitalized.
    When a Braille number follows symbol is read, all following symbols are translated into numbers until the next space symbol.

    Parameters:
        brailleString (str): The Braille string to be translated.

    Returns:
        (bool, str): (Successful translation?, The translated English string).
    """
    rtn = []
    isNumeric = False
    isUpper = False
    i = 0

   
    while i < len(brailleString):
        # Read input string 6 characters at a time.
        character = brailleString[i:i+6]
        i += 6 

        # Determine if string is alphabetical or numeric; if is alphabetical, determine if it is upper or lower case.
        if character == CAP_SEQUENCE:
            isUpper = True
            continue
        if character == NUMERIC_SEQUENCE:
            isNumeric = True
            continue
        if character == SPACE_SEQUENCE:
            # assume alphabetic input if a space is read
            isNumeric = False
        
        # if character has valid mapping, in its respective dictionaries, append to rtn; else, return unsuccessful translation (False, "")
        if isNumeric:
            if character in TO_ENGLISH_NUMERIC:
                rtn.append(TO_ENGLISH_NUMERIC[character])
            else:
                return (False, "")
        else:
            if character in TO_ENGLISH_ALPHA:
                letterToAppend = TO_ENGLISH_ALPHA[character]
                if isUpper:
                    # reset isUpper if last character was capitalized
                    isUpper = False
                    letterToAppend = letterToAppend.upper()
                rtn.append(letterToAppend)
            else:
                return (False, "")

    return (True, fastConcat(rtn))


def translateToBraille(englishWord: str) -> str:
    """
    Translates an English string into a Braille string.

    Key error is raised if input string contains an unsupported character. 
    Assume all English strings with numbers are followed by a space symbol once numeric sequence completes, otherise, a key error is thrown. 

    Parameters:
        englishWord: str: The English string to be translated.

    Returns:
        str: The translated Braille string.
    """
    rtn = []
    isNum = False

    for l in englishWord:
        if l.isupper():
            rtn.append(CAP_SEQUENCE)
            l = l.lower()
        elif l.isnumeric():
            if not isNum:
                rtn.append(NUMERIC_SEQUENCE)
            isNum = True 
        
        # Assume all numeric sequences are followed by a " " (space).
        if l == " ":
            isNum = False

        if isNum:
            rtn.append(TO_BRAILLE_NUMERIC[l])
        else:
            rtn.append(TO_BRAILLE_ALPHA[l])
    return fastConcat(rtn)

def translate(phrase: str) -> str:
    """
    Automatically detect if string is English or Braille and translate it to its counterpart.

    Parameters:
        phrase (str): The string to be translated.

    Returns:
        str: The translated string.
    """

    # Assume braille and if it fails fall back to translating from english.
    successful, english = translateToEnglish(phrase)
    return english if successful else translateToBraille(phrase)
    

if __name__ == "__main__":
    # Concatinate multiple arguments into one, seperated by " " (space).
    input = ' '.join(sys.argv[1:])
    print(translate(input))
    
