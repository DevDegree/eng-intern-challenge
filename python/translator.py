import sys
   
def isBraille(line):
    """
    checks if a given string is braille
    
    Parameters
    ----------
    line : string
        potential string of braille

    Returns
    -------
    boolean
        true if string is braille
    """
    for n in range(len(line)):
        if line[n] != "O" and line[n] != ".":
            return False
    return True

def fromBraille(line):
    """
    translates a given phrase from braille
    dependent on translation and translationNumbers dictionaries
    
    Parameters
    ----------
    line : string
        string of braille to be translated

    Returns
    -------
    string
        translated braille
    """
    ans = ""
    braille = list(translation.values())
    alpha = list(translation.keys())
    numbers = list(translationNumbers.keys())
    caps = False
    nums = False
    # take segments 6 at a time to translate from braille until there are no more
    while len(line) != 0:
        char = line[:6]
        if braille.index(char) == 1: # index of space character, terminate numeric case
            nums = False
            ans += " "
        elif braille.index(char) == 0: # index of capitalization marker
            caps = True
        elif braille.index(char) == 2: # index of numeric marker
            nums = True
        else:
            if nums:
                # search in nums list
                ans += numbers[braille.index(char)-3]
            elif caps:
                ans += alpha[braille.index(char)].upper()
                caps = False
            else:
                ans += alpha[braille.index(char)]
        line = line[6:]
    return ans

def toBraille(phrases):
    """
    translates a given phrase to braille
    dependent on translation and translationNumbers dictionaries
    
    Parameters
    ----------
    lines : list
        list of strings to be translated

    Returns
    -------
    string
        translated braille
    """
    ans = ""
    prevInputNumeric = False
    # iterate through input
    while len(phrases) != 0:
        # iterate through each word
        for i in range(len(phrases[0])):
            # determine if input requires special designation in braille (numeric / capital)
            if phrases[0][i].isnumeric(): # determine if input is numeric
                # if numeric, make sure that numeric marker is placed only once
                if not prevInputNumeric:
                    ans += translation["NUMBERS"]
                prevInputNumeric = True
                ans += translationNumbers[phrases[0][i]]
                continue
            elif phrases[0][i].isupper():
                ans += translation["CAPITAL"]

            ans += translation[phrases[0][i].lower()]
        phrases = phrases[1:]
        # only adds space between words if it is not the last word
        if len(phrases) != 0:
            ans += translation[" "]
        # resets numeric marker for a new word (space has been reached)
        prevInputNumeric = False
    return ans

translation = {"CAPITAL": ".....O",
               " ": "......",
               "NUMBERS": ".O.OOO",
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
               "<": ".OO..O",
               ">": "O..OO.",
               "(": "O.O..O",
               ")": ".O.OO.",
}

translationNumbers = {"1": "O.....",
                      "2": "O.O...",
                      "3": "OO....",
                      "4": "OO.O..",
                      "5": "O..O..",
                      "6": "OOO...",
                      "7": "OOOO..",
                      "8": "O.OO..",
                      "9": ".OO...",
                      "O": ".OOO..",}

# "clear" first input of sys.argv which is the name of the .py file run
sys.argv = sys.argv[1:]

# braille is in segments of 6, so any braille code would be in segments of 6
# braille is also inputted in combinations of . and O
# braille input is unseparated by any spaces
# with these 3 requirements, we can determine if input is to be translated from braille or to braille
if (len(sys.argv[0]) % 6) == 0 and isBraille(sys.argv[0]) and len(sys.argv) == 1:
    print(fromBraille(sys.argv[0]))
else:
    print(toBraille(sys.argv))