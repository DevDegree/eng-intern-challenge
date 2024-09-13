import sys

def translator(string): 

    generalDict = {
        "O....." : "a", 
        "O.O..." : "b", 
        "OO...." : "c", 
        "OO.O.." : "d", 
        "O..O.." : "e", 
        "OOO..." : "f", 
        "OOOO.." : "g", 
        "O.OO.." : "h", 
        ".OO..." : "i",  
        ".OOO.." : "j", 
        "O...O." : "k", 
        "O.O.O." : "l",
        "OO..O." : "m", 
        "OO.OO." : "n", 
        "O.OO.O" : "o", 
        "OOO.O." : "p", 
        "OOOOO." : "q", 
        "O.OOO." : "r", 
        ".OOOO." : "s",
        ".OOOOO" : "t", 
        "O...OO" : "u",
        "O.O.OO" : "v", 
        ".OOOO." : "w", 
        "OO..OO" : "x", 
        "OO.OOO" : "y", 
        "O..OOO" : "z",
        ".....O" : "capital",
        ".O.OOO" : "number",
        "..OO.O" : ".",
        "..O..." : ",",
        "..O.OO" : "?",
        "..OOO." : "!",
        "..OO.." : ":",
        "..O.O." : ";",
        "....OO" : "-",
        ".O..O." : "/",
        ".OO..O" : "<",
        "O..OO." : ">",
        "O.O..O" : "(",
        ".O.OO." : ")",
        "......" : " ",
        ".O...O" : "."
    }

    numberDict = {
        "O....." : "1", 
        "O.O..." : "2", 
        "OO...." : "3", 
        "OO.O.." : "4", 
        "O..O.." : "5", 
        "OOO..." : "6", 
        "OOOO.." : "7", 
        "O.OO.." : "8", 
        ".OO..." : "9",  
        ".OOO.." : "0" 
    }

    translated = ""

    cond = ""

    active_number = 0
    
    #Braile Conditions
    if string.find(".O") != -1 and len(string) % 6 == 0:

        # Split string into 6 symbol sets
        for index in range(0,len(string) // 6):
            braille = string[index*6:(index+1)*6]
            alpha = generalDict.get(braille)
            
            if alpha == " ":
                cond = ""

            # Conditions to set the next symbol to number or capital
            if cond != "":
                if cond == "c" and isinstance(alpha, str):
                    alpha = alpha.capitalize()
                    cond = ""

                if cond == "n":
                    alpha = numberDict.get(braille)
                    
            # sets the condition for the next symbol
            if isinstance(alpha, str) and len(alpha) > 1:
                if alpha == "capital":
                    cond = "c"

                elif alpha == "number":
                    cond = "n"
                
                alpha = ""

            elif isinstance(alpha, str) and alpha != "":
                translated += alpha

    #Alphabet Conditions
    else:
        for i in range(len(string)): 

            t_char = ""

            char = string[i]
            
            # number conditions
            if '0' <= char <= '9':
                for key, value in numberDict.items():
                    if char == value:
                        t_char =  key if active_number else ".O.OOO" + key
                        active_number = 1
                        break

            # Capital letters
            elif 'A' <= char <= 'Z':
                char = char.lower()
                for key, value in generalDict.items():
                    if char == value:
                        t_char =  ".....O" + key
                        break

            # normal letters
            else:
                for key, value in generalDict.items():
                    if char == value:
                        t_char = key
            
            if char == " ":
                active_number = 0

            if isinstance(t_char, str):
                translated += t_char

    return translated

def main():
    for arg in sys.argv[1:]:
        result = translator(arg)
        print(result)

if __name__ == "__main__":
    main()

