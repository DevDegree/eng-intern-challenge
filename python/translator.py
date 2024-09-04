import sys

#get letter, number, and special character
#from braille to character
def english_letter(input_data, cap, num):
    if (cap):
        if input_data == "O.....":
            return "A"
        elif input_data == "O.O...":
            return "B"
        elif input_data == "OO....":
            return "C"
        elif input_data == "OO.O..":
            return "D"
        elif input_data == "O..O..":
            return "E"
        elif input_data == "OOO...":
            return "F"
        elif input_data == "OOOO..":
            return "G"
        elif input_data == "O.OO..":
            return "H"
        elif input_data == ".OO...":
            return "I"
        elif input_data == ".OOO..":
            return "J"
        elif input_data == "O...O.":
            return "K"
        elif input_data == "O.O.O.":
            return "L"
        elif input_data == "OO..O.":
            return "M"
        elif input_data == "OO.OO.":
            return "N"
        elif input_data == "O..OO.":
            return "O"
        elif input_data == "OOO.O.":
            return "P"
        elif input_data == "OOOOO.":
            return "Q"
        elif input_data == "O.OOO.":
            return "R"
        elif input_data == ".OO.O.":
            return "S"
        elif input_data == ".OOOO.":
            return "T"
        elif input_data == "O...OO":
            return "U"
        elif input_data == "O.O.OO":
            return "V"
        elif input_data == ".OOO.O":
            return "W"
        elif input_data == "OO..OO":
            return "X"
        elif input_data == "OO.OOO":
            return "Y"
        else:
            return "Z"
    elif(num):
        if input_data == "O.....":
            return "1"
        elif input_data == "O.O...":
            return "2"
        elif input_data == "OO....":
            return "3"
        elif input_data == "OO.O..":
            return "4"
        elif input_data == "O..O..":
            return "5"
        elif input_data == "OOO...":
            return "6"
        elif input_data == "OOOO..":
            return "7"
        elif input_data == "O.OO..":
            return "8"
        elif input_data == ".OO...":
            return "9"
        elif input_data == "..OO.O":
            return "."
        elif input_data == ".OOO..":
            return "0"
        else:
            return " "
    else:
        if input_data == "O.....":
            return "a"
        elif input_data == "O.O...":
            return "b"
        elif input_data == "OO....":
            return "c"
        elif input_data == "OO.O..":
            return "d"
        elif input_data == "O..O..":
            return "e"
        elif input_data == "OOO...":
            return "f"
        elif input_data == "OOOO..":
            return "g"
        elif input_data == "O.OO..":
            return "h"
        elif input_data == ".OO...":
            return "i"
        elif input_data == ".OOO..":
            return "j"
        elif input_data == "O...O.":
            return "k"
        elif input_data == "O.O.O.":
            return "l"
        elif input_data == "OO..O.":
            return "m"
        elif input_data == "OO.OO.":
            return "n"
        elif input_data == "O..OO.":
            return "o"
        elif input_data == "OOO.O.":
            return "p"
        elif input_data == "OOOOO.":
            return "q"
        elif input_data == "O.OOO.":
            return "r"
        elif input_data == ".OO.O.":
            return "s"
        elif input_data == ".OOOO.":
            return "t"
        elif input_data == "O...OO":
            return "u"
        elif input_data == "O.O.OO":
            return "v"
        elif input_data == ".OOO.O":
            return "w"
        elif input_data == "OO..OO":
            return "x"
        elif input_data == "OO.OOO":
            return "y"
        elif input_data == "O..OOO":
            return "z"
        elif input_data == "..OO.O":
            return "."
        elif input_data == "..O...":
            return ","
        elif input_data == "..O.OO":
            return "?"
        elif input_data == "..OOO.":
            return "!"
        elif input_data == "..OO..":
            return ":"
        elif input_data == "..O.O.":
            return ";"
        elif input_data == "....OO":
            return "-"
        elif input_data == ".O..O.":
            return "/"
        elif input_data == ".OO..O":
            return "<"
        elif input_data == "O..OO.":
            return ">"
        elif input_data == "O.O..O":
            return "("
        elif input_data == ".O.OO.":
            return ")"
        else:
            return " "

#brute force checking number and alphabet
# convert letter into braille        
def braille_letter(input_data, digit):
    if(digit):
        if input_data == "1":
            return "O....."
        elif input_data == "2":
            return "O.O..."
        elif input_data == "3":
            return "OO...."
        elif input_data == "4":
            return "OO.O.."
        elif input_data == "5":
            return "O..O.."
        elif input_data == "6":
            return "OOO...."
        elif input_data == "7":
            return "OOOO.."
        elif input_data == "8":
            return "O.OO.."
        elif input_data == "9":
            return ".OO..."
        elif input_data == ".":
            return "..OO.O"
        elif input_data == "0":
            return ".OOO.."
        else:
            return "......"
    else:
        if input_data == "a":
            return "O....."
        elif input_data == "b":
            return "O.O..."
        elif input_data == "c":
            return "OO...."
        elif input_data == "d":
            return "OO.O.."
        elif input_data == "e":
            return "O..O.."
        elif input_data == "f":
            return "OOO...."
        elif input_data == "g":
            return "OOOO.."
        elif input_data == "h":
            return "O.OO.."
        elif input_data == "i":
            return ".OO..."
        elif input_data == "j":
            return ".OOO.."
        elif input_data == "k":
            return "O...O."
        elif input_data == "l":
            return "O.O.O."
        elif input_data == "m":
            return "OO..O."
        elif input_data == "n":
            return "OO.OO."
        elif input_data == "o":
            return "O..OO."
        elif input_data == "p":
            return "OOO.O."
        elif input_data == "q":
            return "OOOOO."
        elif input_data == "r":
            return "O.OOO."
        elif input_data == "s":
            return ".OO.O."
        elif input_data == "t":
            return ".OOOO."
        elif input_data == "u":
            return "O...OO"
        elif input_data == "v":
            return "O.O.OO"
        elif input_data == "w":
            return ".OOO.O"
        elif input_data == "x":
            return "OO..OO"
        elif input_data == "y":
            return "OO.OOO"
        elif input_data == "z":
            return "O..OOO"
        elif input_data == ".":
            return "..OO.O"
        elif input_data == ",":
            return "..O..."
        elif input_data == "?":
            return "..O.OO"
        elif input_data == "!":
            return "..OOO."
        elif input_data == ":":
            return "..OO.."
        elif input_data == ";":
            return "..O.O."
        elif input_data == "-":
            return "....OO"
        elif input_data == "/":
            return ".O..O."
        elif input_data == "<":
            return ".OO..O"
        elif input_data == ">":
            return "O..OO."
        elif input_data == "(":
            return "O.O..O"
        elif input_data == ")":
            return ".O.OO."
        else:
            return "......"

#check if English or Braille 
#check first two character (OO or O. or .O)
#if first is (.) we know is Braille else check
def check_if_braille(input_data):
    characters = input_data
    if characters[0] == ".":
        return True
    if characters[0] == "O":
        if characters[1] == "O":
            return True
        elif characters[1] == ".":
            return True

    return False


#check if capitalize or num or nothing
#return 0 if CAP, return 1 if num, return 2 if non
def check_if_capital(input_data):
    captial = ".....O"
    num = ".O.OOO"
    if input_data == captial:
        return 0
    elif input_data == num:
        return 1
    else:
        return 2


#convert Braille to English 
#get the length of characters tp get how many characters there are
def convert_to_English(input_data):
    cap = False
    num = False

    #variable for storing letter
    english = ""

    #variable for amount of letter and check if cap
    letter = len(input_data) // 6
    for i in range(0,letter):
        value = check_if_capital(input_data[i*6:(i+1)*6])
        if value == 0:
            cap = True
            continue
        if value == 1:
            num = True
            continue
        else:
            character = (english_letter(input_data[(i)*6:(i+1)*6], cap, num))
            english = english + character
            cap = False
            if character == " ":
                num = False
    print(english)
    return 

#get input_data and check if Capitalize or number 
def convert_to_Braille(input_data):
    braille = ""
    for i, character in enumerate(input_data):
        if(character.isupper()):
            braille = braille + ".....O"
        elif(character.isdigit()):
            if(not input_data[i-1].isdigit() or  i == 0  ):
                braille = braille + ".O.OOO"
            braille = braille + braille_letter(character, True)
            continue
        braille = braille + braille_letter(character.lower(), False)
    print(braille)

if __name__ == "__main__":
    input_data = sys.argv[1:]
    input_string = " ".join(input_data)
    characters = input_string.strip()
    if(check_if_braille(characters)):
        convert_to_English(characters)
    else:
        convert_to_Braille(characters)
