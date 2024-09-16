import sys

# This function returns True if the input is in Braille, False otherwise
def isBraille(t_str:str):
    for i in range(len(t_str)):
        if t_str[i].isalnum() and t_str[i] != "O":
            return False
    return True

# Dictionary mapping English characters to their Braille equivalent
eng_dct = {"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f":"OOO...", "g":"OOOO..", "h":"O.OO..", "i":".OO...", "j":".OOO..", "k": "O...O.", "l":"O.O.O.", "m":"OO..O.",
           "n":"OO.OO.", "o":"O..OO.", "p":"OOO.O.", "q":"OOOOO.", "r":"O.OOO.", "s":".OOOO.", "t":".OOOO.", "u":"O...OO", "v":"O.O.OO", "w":".OOO.O", "x":"OO..OO", "y":"OO.OOO", "z":"O..OOO",
           "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6":"OOO...", "7":"OOOO..", "8":"O.OO..", "9":".OO...", "0":".OOO..",
           "cf":".....O", "df":".O...O", "nf":".O.OOO", " ":"......"}
        #    ,".":"..OO.O", ",":"..O...", "?":"..O.OO", "!":"..OOO.", ":":"..OO..", ";":"..OO..", "-":"....OO", "/":".O..O.", "<":".OO..O", ">": "O..OO.", "(":"O.O..O", ")":".O.OO."}

# Dictionary with Braille characters to their English equivalent
braille_dct = {
 'O.....': 'a','O.O...': 'b','OO....': 'c','OO.O..': 'd','O..O..': 'e','OOO...': 'f','OOOO..': 'g','O.OO..': 'h','.OO...': 'i','.OOO..': 'j', "O...O.":'k', 'O.O.O.': 'l','OO..O.': 'm','OO.OO.': 'n','O..OO.': 'o','OOO.O.': 'p','OOOOO.': 'q','O.OOO.': 'r','.OOOO.': 't','O...OO': 'u','O.O.OO': 'v',
 '.OOO.O': 'w','OO..OO': 'x','OO.OOO': 'y','O..OOO': 'z','.....O': 'cf','.O...O': 'df','.O.OOO': 'nf', '......': ' '
#  '..OO.O': '.',  '..O...': ',',  '..O.OO': '?',  '..OOO.': '!',  '..OO..': ';',  '....OO': '-',  '.O..O.': '/',  '.OO..O': '<',  'O.O..O': '(',  '.O.OO.': ')',
}

# This functions takes a string of English characters as input and outputs the Braille equivalent
def translateToBraille(t_str:str):
    result = ""
    isNum = False   #flag representing whether a number follows
    for i in range(len(t_str)):
        # if the current character is a space, the sequence of numbers ends
        if t_str[i] == " ":
            isNum = False

        # if the current character is a capital letter
        elif t_str[i].isupper():
            result += eng_dct["cf"]

        # checking if the number follows character has been inserted into the result string
        elif not isNum and t_str[i].isnumeric():
            result += eng_dct["nf"]
            isNum = True
        
        result += eng_dct[t_str[i].lower()]
    return result

# This functions takes a string of Braille characters as input and outputs the English equivalent
def translateToEnglish(t_str):
    result = ""
    isCap = False    #flag representing whether a capital follows
    isNum = False    #flag representing whether a number follows


    for i in range(0, len(t_str), 6):
        start_idx = i
        end_idx = i+6

        curr = t_str[start_idx:end_idx]

        # checking if the current character is a capital follows character
        if curr == eng_dct["cf"]:
            isCap = True
            isNum = False
        else:
            # checking if the current character is a number follows character
            if curr == eng_dct["nf"]:
                isNum = True
            else:
                # inserting a capital letter into the result string if the previous character was a capital follows character
                if isCap:
                    result += braille_dct[curr].upper()
                    isCap = False

                # inserting a number into the result string if the sequence of numbers hasn't been broken
                elif isNum:
                    if curr != eng_dct[" "]:
                        num = str(ord(braille_dct[curr])-96)
                        result += num
                    else:
                        result += braille_dct[curr]
                        isNum = False
                else:
                    result += braille_dct[curr]
                    isCap = False
    return result        
        

# This function translates the given string from Braille to English or English to Braille where required
def translate(t_str:str):
    if isBraille(t_str):
        return translateToEnglish(t_str)
    else:
        return translateToBraille(t_str)
   
    
def main():
    t_str = " ".join(sys.argv[1:])
    print(translate(t_str), end='')

if __name__ == "__main__":
    main()
