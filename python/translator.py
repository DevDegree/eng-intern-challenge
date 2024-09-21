import sys


isCapital = False
isNumber = False
isDecimal = False
isPeriod = False

def get_char(lang, char):
    global isCapital
    global isNumber
    global isDecimal
    global isPeriod
    upp = ""
    if lang == "eng":
        # If char is uppercase, add ".....O" before
        if char != None and char.isupper():
            upp += ".....O"
        # If it is the first occurrence of a number, isNumber becomes true
        if char != None and char in '1234567890':
            if isNumber == False:
                isNumber = True
                upp = ".O.OOO"
            # If isNumber and isDecimal are both true add ".O...O" before to show that a decimal follows
            if isNumber and isDecimal:
                isDecimal = False
                upp = ".O...O"
        if char == None or char not in '1234567890.':
            isNumber = False
            if isDecimal: # Ensures that if there is a period after a number, it will apply braille for period
                upp = "..OO.O"  
        if isNumber and char == '.':
            isDecimal = True
            return ""
        # Necessary if there is a decimal as the final input rightr after a digit ex: "Hello123."
        # An null index is placed at the end of the list for this very reason 
        if char == None: 
            return upp
        if char.upper() == 'A' or char == '1':
            return upp + "O....."
        if char.upper() == 'B' or char == '2':
            return upp + "O.O..."
        if char.upper() == 'C' or char == '3':
            return upp + "OO...."
        if char.upper() == 'D' or char == '4':
            return upp + "OO.O.."
        if char.upper() == 'E' or char == '5':
            return upp + "O..O.."
        if char.upper() == 'F' or char == '6':
            return upp + "OOO..."
        if char.upper() == 'G' or char == '7':
            return upp + "OOOO.."
        if char.upper() == 'H' or char == '8':
            return upp + "O.OO.."
        if char.upper() == 'I' or char == '9':
            return upp + ".OO..."
        if char.upper() == 'J' or char == '0':
            return upp + ".OOO.."
        if char.upper() == 'K':
            return upp + "O...O."
        if char.upper() == 'L':
            return upp + "O.O.O."
        if char.upper() == 'M':
            return upp + "OO..O."
        if char.upper() == 'N':
            return upp + "OO.OO."
        if char.upper() == 'O':
            return upp + "O..OO."
        if char.upper() == 'P':
            return upp + "OOO.O."
        if char.upper() == 'Q':
            return upp + "OOOOO."
        if char.upper() == 'R':
            return upp + "O.OOO."
        if char.upper() == 'S':
            return upp + ".OO.O."
        if char.upper() == 'T':
            return upp + ".OOOO."
        if char.upper() == 'U':
            return upp + "O...OO"
        if char.upper() == 'V':
            return upp + "O.O.OO"
        if char.upper() == 'W':
            return upp + ".OOO.O"
        if char.upper() == 'X':
            return upp + "OO..OO"
        if char.upper() == 'Y':
            return upp + "OO.OOO"
        if char.upper() == 'Z':
            return upp + "O..OOO"
        if char == '.':
            return upp + "..OO.O"
        if char == ',':
            return upp + "..O..."
        if char == '?':
            return upp + "..O.OO"
        if char == '!':
            return upp + "..OOO."
        if char == ':':
            return upp + "..OO.."
        if char == ';':
            return upp + "..O.O."
        if char == '-':
            return upp + "....OO"
        if char == '/':
            return upp + ".O..O."
        if char == '<':
            return upp + ".OO.O."
        if char == '>':
            return upp + "O..OO."
        if char == '(':
            return upp + "O.O..O"
        if char == ')':
            return upp + ".O.OO."
        if char == ' ':
            return upp + "......"

    else:
        if char == ".....O":
            isCapital = True
            return ""
        if char == "......":
            isNumber = False
            return " "
        if char == ".O.OOO":
            isNumber = True
            return ""
        if char == "O.....":
            if isNumber:
                return "1"
            else:
                if isCapital:
                    isCapital = False
                    return "A"
                else:
                    return "a"
        if char == "O.O...":
            if isNumber:
                return "2"
            else:
                if isCapital:
                    isCapital = False
                    return "B"
                else:
                    return "b"
        if char == "OO....":
            if isNumber:
                return "3"
            else:
                if isCapital:
                    isCapital = False
                    return "C"
                else:
                    return "c"
        if char == "OO.O..":
            if isNumber:
                return "4"
            else:
                if isCapital:
                    isCapital = False
                    return "D"
                else:
                    return "d"
        if char == "O..O..":
            if isNumber:
                return "5"
            else:
                if isCapital:
                    isCapital = False
                    return "E"
                else:
                    return "e"
        if char == "OOO...":
            if isNumber:
                return "6"
            else:
                if isCapital:
                    isCapital = False
                    return "F"
                else:
                    return "f"
        if char == "OOOO..":
            if isNumber:
                return "7"
            else:
                if isCapital:
                    isCapital = False
                    return "G"
                else:
                    return "g"
        if char == "O.OO..":
            if isNumber:
                return "8"
            else:
                if isCapital:
                    isCapital = False
                    return "H"
                else:
                    return "h"
        if char == ".OO...":
            if isNumber:
                return "9"
            else:
                if isCapital:
                    isCapital = False
                    return "I"
                else:
                    return "i"
        if char == ".OOO..":
            if isNumber:
                return "0"
            else:
                if isCapital:
                    isCapital = False
                    return "J"
                else:
                    return "j"
        if char == "O...O.":
            if isCapital:
                isCapital = False
                return "K"
            else:
                return "k"
        if char == "O.O.O.":
            if isCapital:
                isCapital = False
                return "L"
            else:
                return "l"
        if char == "OO..O.":
            if isCapital:
                isCapital = False
                return "M"
            else:
                return "m"
        if char == "OO.OO.":
            if isCapital:
                isCapital = False
                return "N"
            else:
                return "n"
        if char == "O..OO.":
            if isCapital:
                isCapital = False
                return "O"
            else:
                return "o"
        if char == "OOO.O.":
            if isCapital:
                isCapital = False
                return "P"
            else:
                return "p"
        if char == "OOOOO.":
            if isCapital:
                isCapital = False
                return "Q"
            else:
                return "q"
        if char == "O.OOO.":
            if isCapital:
                isCapital = False
                return "R"
            else:
                return "r"
        if char == ".OO.O.":
            if isCapital:
                isCapital = False
                return "S"
            else:
                return "s"
        if char == ".OOOO.":
            if isCapital:
                isCapital = False
                return "T"
            else:
                return "t"
        if char == "O...OO":
            if isCapital:
                isCapital = False
                return "U"
            else:
                return "u"
        if char == "O.O.OO":
            if isCapital:
                isCapital = False
                return "V"
            else:
                return "v"
        if char == ".OOO.O":
            if isCapital:
                isCapital = False
                return "W"
            else:
                return "w"
        if char == "OO..OO":
            if isCapital:
                isCapital = False
                return "X"
            else:
                return "x"
        if char == "OO.O.O":
            if isCapital:
                isCapital = False
                return "Y"
            else:
                return "y"
        if char == "O..OOO":
            if isCapital:
                isCapital = False
                return "Z"
            else:
                return "z"
        if char == "..OO.O" or char == ".O...O":
            return "."
        if char == "..O...":
            return ","
        if char == "..O.OO":
            return "?"
        if char == "..OOO.":
            return "!"
        if char == "..OO..":
            return ":"
        if char == "..O.O.":
            return ";"
        if char == "....OO":
            return "-"
        if char == ".O..O.":
            return "/"
        if char == ".OO.O.":
            return "<"
        if char == "O..OO.":
            return ">"
        if char == "O.O..O":
            return "("
        if char == ".O.OO.":
            return ")"
        if char == "......":
            return " "
    
#Translate English to Braille
def trsl_eng(txt):
    trsl = ""
    count = 0
    for item in txt:
        trsl += get_char("eng", txt[count]) 
        count += 1
    return trsl

#Translate Braille to English
def trsl_brl(txt):
    trsl = ""
    count = 0
    braille_arr = []
    for i in range(0, len(txt), 6):
        braille_arr.append(''.join(txt[i:i+6]))

    for item in braille_arr:
        trsl += get_char("brl", braille_arr[count]) 
        count += 1
    return trsl

def main():
    text = ' '.join(sys.argv[1:])
    result = ""
    lst = list(text)

    # First, check if less than 6 chars --> If true, then the text is English (saves time)
    if len(lst) < 6:
        lst.append(None)
        result += trsl_eng(lst)
        

    is_braille = False
    # Next, check if each character is a '.' or 'O'. If yes, then it is Braille
    if len(lst) >= 6:
        for item in lst:
            if item != '.' and item != 'O':
                is_braille = False
                break
            else:
                is_braille = True

    if is_braille:
        result += trsl_brl(lst)
    else:
        lst.append(None)
        result += trsl_eng(lst)

    print(result)

if __name__ == "__main__":
    main()




