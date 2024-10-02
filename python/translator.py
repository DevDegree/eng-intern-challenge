import sys

input_string = " ".join(sys.argv[1:])

def identifyString(s):
    translation = ""
    capital = False
    number = False
    if '.' in s:
        chars = [s[i:i+6] for i in range(0, len(s), 6)]
        print(chars)
        for i in chars:
            if i == ".....O":
                capital = True
            elif i == ".O.OOO":
                number = True
            elif i == ".O...O." or i == "..OO.O":
                print("no")
                translation = translation + "."
            elif i == "..O...":
                translation = translation + ","
            elif i == "..O.OO":
                translation = translation + "?"
            elif i == "..OOO.":
                translation = translation + "!"
            elif i == "..OO..":
                translation = translation + ":"
            elif i == "..O.O.":
                translation = translation + ";"
            elif i == "....OO":
                translation = translation + "-"
            elif i == ".O..O.":
                translation = translation + "/"
            elif i == "....OO":
                translation = translation + "-"
            elif i == ".OO..O":
                translation = translation + "<"
            elif i == "O..OO.":
                translation = translation + ">"
            elif i == "O.O..O":
                translation = translation + "("
            elif i == ".O.OO.":
                translation = translation + ")"
            elif i == "......":
                translation = translation + " "
            elif i == "O.....":
                if capital == True:
                    translation = translation + "A"
                elif number == True:
                    translation =  translation + "1"
                else:
                    translation = translation + "a"
            elif i == "O.O...":
                if capital == True:
                    translation = translation + "B"
                elif number == True:
                    translation = translation + "2"
                else:
                    translation = translation + "b"
            elif i == "OO....":
                if capital == True:
                    translation = translation + "C"
                elif number == True:
                    translation = translation + "3"
                else:
                    translation = translation + "c"
            elif i == "OO.O..":
                if capital == True:
                    translation = translation + "D"
                elif number == True:
                    translation = translation + "4"
                else:
                    translation = translation + "d"
            elif i == "O.O...":
                if capital == True:
                    translation = translation + "E"
                elif number == True:
                    translation = translation + "5"
                else:
                    translation = translation + "e"
            elif i == "OOO...":
                if capital == True:
                    translation = translation + "F"
                elif number == True:
                    translation = translation + "6"
                else:
                    translation = translation + "f"
            elif i == "OOOO..":
                if capital == True:
                    translation = translation + "G"
                elif number == True:
                    translation = translation + "7"
                else:
                    translation = translation + "g"
            elif i == "O.OO..":
                if capital == True:
                    translation = translation + "H"
                elif number == True:
                    translation = translation + "8"
                else:
                    translation = translation + "h"
            elif i == ".OO...":
                if capital == True:
                    translation = translation + "I"
                elif number == True:
                    translation = translation + "9"
                else:
                    translation = translation + "i"
            elif i == ".OOO..":
                if capital == True:
                    translation = translation + "J"
                elif number == True:
                    translation = translation + "10"
                else:
                    translation = translation + "j"
            elif i == "O...O.":
                if capital == True:
                    translation = translation + "K"
                elif number == True:
                    translation = translation + "11"
                else:
                    translation = translation + "k"
            elif i == "O.O.O.":
                if capital == True:
                    translation = translation + "L"
                elif number == True:
                    translation = translation + "12"
                else:
                    translation = translation + "l"
            elif i == "OO..O.":
                if capital == True:
                    translation = translation + "M"
                elif number == True:
                    translation = translation + "13"
                else:
                    translation = translation + "m"
            elif i == "OO.OO.":
                if capital == True:
                    translation = translation + "N"
                elif number == True:
                    translation = translation + "14"
                else:
                    translation = translation + "n"
            elif i == "O..OO.":
                if capital == True:
                    translation = translation + "O"
                elif number == True:
                    translation = translation + "15"
                else:
                    translation = translation + "o"
            elif i == "OOO.O.":
                if capital == True:
                    translation = translation + "P"
                elif number == True:
                    translation = translation + "16"
                else:
                    translation = translation + "p"
            elif i == "OOOOO.":
                if capital == True:
                    translation = translation + "Q"
                elif number == True:
                    translation = translation + "17"
                else:
                    translation = translation + "q"
            elif i == "O.OOO.":
                if capital == True:
                    translation = translation + "R"
                elif number == True:
                    translation = translation + "18"
                else:
                    translation = translation + "r"
            elif i == ".OO.O.":
                if capital == True:
                    translation = translation + "S"
                elif number == True:
                    translation = translation + "19"
                else:
                    translation = translation + "s"
            elif i == ".OOOO.":
                if capital == True:
                    translation = translation + "T"
                elif number == True:
                    translation = translation + "20"
                else:
                    translation = translation + "t"
            elif i == "O...OO":
                if capital == True:
                    translation = translation + "U"
                elif number == True:
                    translation = translation + "21"
                else:
                    translation = translation + "u"
            elif i == "O.O.OO":
                if capital == True:
                    translation = translation + "v"
                elif number == True:
                    translation = translation + "22"
                else:
                    translation = translation + "v"
            elif i == ".OOO.O":
                if capital == True:
                    translation = translation + "W"
                elif number == True:
                    translation = translation + "23"
                else:
                    translation = translation + "w"
            elif i == "OO..OO":
                if capital == True:
                    translation = translation + "X"
                elif number == True:
                    translation = translation + "24"
                else:
                    translation = translation + "x"
            elif i == "OO.OOO":
                if capital == True:
                    translation = translation + "Y"
                elif number == True:
                    translation = translation + "25"
                else:
                    translation = translation + "y"
            elif i == "O..OOO":
                if capital == True:
                    translation = translation + "Z"
                elif number == True:
                    translation = translation + "26"
                else:
                    translation = translation + "z"
    else:
        numbers = "123456789"
        for i in s:
            if i == "A":
                translation = translation + ".....O" + "O....."
            elif i == "a":
                translation = translation + "O....."
            elif i == "1":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + "O....."
                else:
                    translation = translation + ".O.OOO" + "O....."
            elif i == "B":
                translation = translation + ".....O" + "O.O..."
            elif i == "b":
                translation = translation + "O.O..."
            elif i == "2":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + "O.O..."
                else:
                    translation = translation + ".O.OOO" + "O.O..."
            elif i == "C":
                translation = translation + ".....O" + "OO...."  
            elif i == "c":
                translation = translation + "OO...."
            elif i == "3":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + "OO...."
                else:
                    translation = translation + ".O.OOO" + "OO...."
            elif i == "D":
                translation = translation + ".....O" + "OO.O.."  
            elif i == "d":
                translation = translation + "OO.O.."
            elif i == "4":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + "OO.O.."
                else:
                    translation = translation + ".O.OOO" + "OO.O.."
            elif i == "E":
                translation = translation + ".....O" + "O.O..." 
            elif i == "e":
                translation = translation + "O.O..." 
            elif i == "5":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + "O.O..."
                else:
                    translation = translation + ".O.OOO" + "O.O..."   
            elif i == "F":
                translation = translation + ".....O" + "OOO..." 
            elif i == "f":
                translation = translation + "OOO..."  
            elif i == "6":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + "OOO..." 
                else:
                    translation = translation + ".O.OOO" + "OOO..."    
            elif i == "G":
                translation = translation  + ".....O" + "OOOO.."
            elif i == "g":
                translation = translation + "OOOO.."  
            elif i == "7":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + "OOOO.." 
                else:
                    translation = translation + ".O.OOO" + "OOOO.."    
            elif i == "H":
                translation = translation + ".....O" + "O.OO.."
            elif i == "h":
                translation = translation + "O.OO.." 
            elif i == "8":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + "O.OO.." 
                else:
                    translation = translation + ".O.OOO" + "O.OO.."
            elif i == "I":
                translation = translation + ".....O" + ".OO..." 
            elif i == "i":
                translation = translation + ".OO..." 
            elif i == "9":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + ".OO..." 
                else:
                    translation = translation + ".O.OOO" + ".OO..."    
            elif i == "J":
                translation = translation + ".....O" + ".OOO.." 
            elif i == "j":
                translation = translation + ".OOO.."
            elif i == "10":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + ".OOO.." 
                else:
                    translation = translation + ".O.OOO" + ".OOO.."
            elif i == "K":
                translation = translation + ".....O" + "O...O."
            elif i == "k":
                translation = translation + "O...O."  
            elif i == "11":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + "O...O." 
                else:
                    translation = translation + ".O.OOO" + "O...O."
            elif i == "L":
                translation = translation + ".....O" + "O.O.O."
            elif i == "l":
                translation = translation + "O.O.O."
            elif i == "12":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + "O.O.O." 
                else:
                    translation = translation + ".O.OOO" + "O.O.O."
            elif i == "M":
                translation = translation + ".....O" + "OO..O." 
            elif i == "m":
                translation = translation + "OO..O."
            elif i == "13":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + "OO..O." 
                else:
                    translation = translation + ".O.OOO" + "OO..O."   
            elif i == "N":
                translation = translation + ".....O" + "OO.OO."
            elif i == "n":
                translation = translation + "OO.OO."
            elif i == "14":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + "OO.OO." 
                else:
                    translation = translation + ".O.OOO" + "OO.OO."
            elif i == "O":
                translation = translation + ".....O" + "O..OO."
            elif i == "o":
                translation = translation + "O..OO."
            elif i == "15":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + "O..OO." 
                else:
                    translation = translation + ".O.OOO" + "O..OO."                   
            elif i == "P":
                translation = translation + ".....O" + "OOO.O."
            elif i == "p":
                translation = translation + "OOO.O."
            elif i == "16":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + "OOO.O." 
                else:
                    translation = translation + ".O.OOO" + "OOO.O."    
            elif i == "Q":
                translation = translation + ".....O" + "OOOOO."
            elif i == "q":
                translation = translation + "OOOOO."
            elif i == "17":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + "OOOOO." 
                else:
                    translation = translation + ".O.OOO" + "OOOOO."    
            elif i == "R":
                translation = translation + ".....O" + "O.OOO." 
            elif i == "r":
                translation = translation + "O.OOO."
            elif i == "18":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + "O.OOO." 
                else:
                    translation = translation + ".O.OOO" + "O.OOO." 
            elif i == "S":
                translation = translation + ".....O" + ".OO.O."
            elif i == "s":
                translation = translation + ".OO.O." 
            elif i == "19":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + ".OO.O." 
                else:
                    translation = translation + ".O.OOO" + ".OO.O."
            elif i == "T":
                translation = translation + ".....O" + ".OOOO."
            elif i == "t":
                translation = translation + ".OOOO."
            elif i == "20":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + ".OOOO." 
                else:
                    translation = translation + ".O.OOO" + ".OOOO."  
            elif i == "U":
                translation = translation + ".....O" + "O...OO"
            elif i == "u":
                translation = translation + "O...OO"
            elif i == "21":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + "O...OO" 
                else:
                    translation = translation + ".O.OOO" + "O...OO"
            elif i == "V":
                translation = translation + ".....O" + "O.O.OO"
            elif i == "v":
                translation = translation + "O.O.OO"
            elif i == "22":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + "O.O.OO"
                else:
                    translation = translation + ".O.OOO" + "O.O.OO"  
            elif i == "W":
                translation = translation + ".....O" + ".OOO.O" 
            elif i == "w":
                translation = translation + ".OOO.O" 
            elif i == "23":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + ".OOO.O"
                else:
                    translation = translation + ".O.OOO" + ".OOO.O" 
            elif i == "X":
                translation = translation + ".....O" + "OO..OO"
            elif i == "x":
                translation = translation + "OO..OO"
            elif i == "24":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + "OO..OO"
                else:
                    translation = translation + ".O.OOO" + "OO..OO" 
            elif i == "Y":
                translation = translation + ".....O" + "OO.OOO" 
            elif i == "y":
                translation = translation + "OO.OOO" 
            elif i == "25":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + "OO.OOO" 
                else:
                    translation = translation + ".O.OOO" + "OO.OOO"   
            elif i == "Z":
                translation = translation + ".....O" + "O..OOO"
            elif i == "z":
                translation = translation + "O..OOO"
            elif i == "26":
                if 1 in [c in prev for c in numbers]:
                    translation = translation + "O..OOO"
                else:
                    translation = translation + ".O.OOO" + "O..OOO"
            elif i == ".":
                translation = translation + "..OO.O"
            elif i == ",": 
                translation = translation + "..O..."
            elif i == "?":
                translation = translation + "..O.OO"
            elif i == "!":
                translation = translation + "..OOO."
            elif i == ":":
                translation = translation + "..OO.."
            elif i == ";":
                translation = translation + "..O.O."                
            elif i == "-":
                translation = translation + "....OO"
            elif i == "/":
                translation = translation + ".O..O."
            elif i == "<":
                translation = translation + "O..OO."
            elif i == ">":
                translation = translation + "O..OO."
            elif i == "(":
                translation = translation + "O.O..O"
            elif i == ")":
                translation = translation + ".O.OO."
            elif i == " ":
                translation = translation + "......"  
            prev = i
    print(translation)

identifyString(input_string)
