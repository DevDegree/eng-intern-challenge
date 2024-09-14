# Note: the technical requirements only asked for alphabet and number translations
# so I left special character translation out

braille_to_eng_dict = {
    "O.....": ("a", "1"),
    "O.O...": ("b", "2"),
    "OO....": ("c", "3"),
    "OO.O..": ("d", "4"),
    "O..O..": ("e", "5"),
    "OOO...": ("f", "6"),
    "OOOO..": ("g", "7"),
    "O.OO..": ("h", "8"),
    ".OO...": ("i", "9"),
    ".OOO..": ("j", "0"),
    "O...O.": ("k", None),
    "O.O.O.": ("l", None),
    "OO..O.": ("m", None),
    "OO.OO.": ("n", None),
    "O..OO.": ("o", None),
    "OOO.O.": ("p", None),
    "OOOOO.": ("q", None),
    "O.OOO.": ("r", None),
    ".OO.O.": ("s", None),
    ".OOOO.": ("t", None),
    "O...OO": ("u", None),
    "O.O.OO": ("v", None),
    ".OOO.O": ("w", None),
    "OO..OO": ("x", None),
    "OO.OOO": ("y", None),
    "O..OOO": ("z", None),
    "......": (" ", " "),
    ".....O": ("CAPITOL_FOLLOWS", None),
    ".O.OOO": ("NUMBER_FOLLOWS", None)
}

eng_to_braille_dict = {
    "a": "O.....",
    "1": "O.....",
    "b": "O.O...",
    "2": "O.O...",
    "c": "OO....",
    "3": "OO....",
    "d": "OO.O..",
    "4": "OO.O..",
    "e": "O..O..",
    "5": "O..O..",
    "f": "OOO...",
    "6": "OOO...",
    "g": "OOOO..",
    "7": "OOOO..",
    "h": "O.OO..",
    "8": "O.OO..",
    "i": ".OO...",
    "9": ".OO...",
    "j": ".OOO..",
    "0": ".OOO..",
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
    " ": "......",
    "CAPITOL_FOLLOWS": ".....O",
    "NUMBER_FOLLOWS": ".O.OOO"
}


# go through every letter

    # Check if there is a letter other than O or ., as soon as you see one return true otherwise false

def isEnglish(str):
    # find any val that isn't brail
    for elem in str:
        if (elem != '.' and elem != 'O'):
            return True
    return False

def Brail_to_English(inputStr):
    
    outputStr = ""
    
    if(isEnglish(inputStr)):
        return False
    
    #Inspect the input string(braille) 6 characters at a time and find the english character that is mapped to it
    i = -6
    number_follows = False
    capitol_follows = False
    tuple_index = 0
    while ((i+6) < len(inputStr)):
        i += 6
        
        if number_follows:
            tuple_index = 1 # non capitol english letter
        else:
            tuple_index = 0 # capitol english letter
            
        # logic if we find a capitol follows 
            # toUpper the char
        tempChar = braille_to_eng_dict.get(inputStr[i:i+6])[tuple_index] 
        
        if capitol_follows:
            tempChar = tempChar.upper()
            capitol_follows = False
        
        if (tempChar == "CAPITOL_FOLLOWS"):
           capitol_follows = True
           tempChar = ""
        elif (tempChar == "NUMBER_FOLLOWS"):
            number_follows = True
            tempChar = ""
        elif (tempChar == " "):
            number_follows = False
        
        outputStr += tempChar
        #print("Input char: " + inputStr[i:i+6] + "  output char: " + outputStr)
    
    print(outputStr)

def English_to_Brail(inputStr):
    outputStr = ""
    
    for char in inputStr:
        if char.isupper():
            outputStr += eng_to_braille_dict.get("CAPITOL_FOLLOWS")
        elif char.isnumeric():
            outputStr += eng_to_braille_dict.get("NUMBER_FOLLOWS")
        
        
        outputStr += eng_to_braille_dict.get(char.lower())
        #print("Input char: " + char + "  output char: " + outputStr)
        
    print(outputStr)
    
    
if __name__ == '__main__': 
    inputStr = input()
    if isEnglish(inputStr):
        English_to_Brail(inputStr)
    else:
        Brail_to_English(inputStr)
    
