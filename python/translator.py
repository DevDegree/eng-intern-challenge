import sys

# Hash for english to braille conversion
english_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    # I included special chars even if it wasn't explicitly stated in the requirement
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",
    "-": "....OO", "/": ".O..O.", "<": ".OO..O", "(": "O.O..O", ")": ".O.OO.",

    # The following is for cap, num, dec, and space chars
    "cap": ".....O", 
    "num": ".O.OOO",
    "dec": ".O...O", 
    " ": "......"
}
# Hash for braille to char conversion
braille_char = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
    # I included special chars even if it wasn't explicitly stated in the requirement
    "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
    "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O.O..O": "(",
    ".O.OO.": ")",
    ".....O": "cap",
    ".O.OOO": "num", 
    "......": " "  
}

# Hash for braille to num conversion
braille_num = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
    ".O.OOO": "num", 
    ".O...O": ".",
    "......": " "    
}



def is_Braille_to_English(inputText):
    """
    This function detirmines if the given text is braille or english, thus to what the text needs to be translated to.
    Returns True if it's Braille, otherwise False.
    """
    if len(inputText) % 6 != 0:
        return False
    
    for i in inputText:
        if i != "." and i != "O":
            return False
        
    return True

def Braille_to_English(text):
    """
    This function converts the braille text to english. 
    It iterates over every char of text, building a cur string every 6 char and building the english translation based on those 6 chars
    Assumes valid braille input.
    """
    cur, english = "", ""
    # Checks to detirmine the state of next translation values, if it is being translated to num or letter or is a capital
    isNum, isChar, isCap = False, True, False
    
    for i in text:
        cur += i
        if len(cur) == 6:
            # used the get(cur, "") in case the key val did not exist, could have also used a check to raise error
            # But decided with get to make code less error prone
            toAdd = braille_char.get(cur, "") if isChar else braille_num.get(cur, "")
            
            if toAdd == "cap":
                isCap = True
            elif toAdd == "num":
                isNum, isChar = True, False
            elif isNum and toAdd == " ":
                isNum, isChar = False, True
                english += toAdd
            else:
                english += toAdd.upper() if isCap else toAdd
                isCap = False
            
            cur = ""
    
    return english


def English_to_Braille(text):
    """
    This function converts the english text to braille. 
    It iterates over every char of text, where it is checked if the char is a letter or a number, based on which it builds the braille string
    Assumes valid english input
    """
    
    braille = ""
    isNum = False
    for char in text:
        if char.isupper():
            braille += english_braille.get("cap", "INVALID")
            braille += english_braille.get(char.lower(), "INVALID")
        elif char.isdigit():
            if not isNum:
                braille += english_braille.get("num", "INVALID")
                isNum = True
            braille += english_braille.get(char, "INVALID")
        elif char == " ":
            braille += english_braille.get(char, "INVALID")
            isNum = False
        # To account for the decimal point in a number
        elif char == "." and isNum:
            braille += english_braille.get("dec", "INVALID")
        else:
            braille += english_braille.get(char, "INVALID")
    
    if "INVALID" in braille:
        raise ValueError(f"Invalid character found in input text: {text}")
    
    return braille

                


def main():
    try:
        input_text = " ".join(sys.argv[1:])
        if not input_text:
            raise ValueError("No input provided.")
        
        if is_Braille_to_English(input_text):
            result = Braille_to_English(input_text)
        else:
            result = English_to_Braille(input_text)
        
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()