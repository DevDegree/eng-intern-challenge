braille_dict = {
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
    "..OO.O": (".", None),
    "..O...": (",", None),
    "..OOO.": ("!", None),
    "..OO..": (":", None),
    "..O.O.": (";", None),
    "....OO": ("-", None),
    ".O..O.": ("/", None),
    ".O.O.O": ("<", None),
    "O..OO.": (">", None),
    "O.O..O": ("(", None),
    ".O.OO.": (")", None),
    "......": (" ", " "),
    ".....O": ("CAPITOL_FOLLOWS", None),
    ".O...O": ("DECIMAL_FOLLOWS", None),
    ".O.OOO": ("NUMBER_FOLLOWS", None)
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
        tempChar = braille_dict.get(inputStr[i:i+6])[tuple_index] 
        
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
        print("Input char: " + inputStr[i:i+6] + "  output char: " + outputStr)
        
        
        
        
    
    #for key in braille_dict:
    #    print(braille_dict.get(key)[0])
    
    
    
    
if __name__ == '__main__': 
    inputStr = input()
    if isEnglish(inputStr):
        print("English not done yet")
    else:
        Brail_to_English(inputStr)
    
