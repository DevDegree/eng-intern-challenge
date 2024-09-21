def translateToEnglish(s) :
    #dico for translation
    tradlower = {
        "O....."  : "a" ,
        "O.O..."  : "b" ,
        "OO...."  : "c" ,
        "OO.O.."  : "d" ,
        "O..O.."  : "e" ,
        "OOO..."  : "f" ,
        "OOOO.."  : "g" ,
        "O.OO.."  : "h" ,
        ".OO..."  : "i" ,
        ".OOO.."  : "j" ,
        "O...O."  : "k" ,
        "O.O.O."  : "l" ,
        "OO..O."  : "m" ,
        "OO.OO."  : "n" ,
        "O..OO."  : "o" ,
        "OOO.O."  : "p" ,
        "OOOOO."  : "q" ,
        "O.OOO."  : "r" ,
        ".OO.O."  : "s" ,
        ".OOOO."  : "t" ,
        "O...OO"  : "u" ,
        "O.O.OO"  : "v" ,
        ".OOO.O"  : "w" ,
        "OO..OO"  : "x" ,
        "OO.OOO"  : "y" ,
        "O..OOO"  : "z" ,

        "......" : " "

    }

    tradupper = {
        "O....."  : "A" ,
        "O.O..."  : "B" ,
        "OO...."  : "C" ,
        "OO.O.."  : "D" ,
        "O..O.."  : "E" ,
        "OOO..."  : "F" ,
        "OOOO.."  : "G" ,
        "O.OO.."  : "H" ,
        ".OO..."  : "I" ,
        ".OOO.."  : "J" ,
        "O...O."  : "K" ,
        "O.O.O."  : "L" ,
        "OO..O."  : "M" ,
        "OO.OO."  : "N" ,
        "O..OO."  : "O" ,
        "OOO.O."  : "P" ,
        "OOOOO."  : "Q" ,
        "O.OOO."  : "R" ,
        ".OO.O."  : "S" ,
        ".OOOO."  : "T" ,
        "O...OO"  : "U" ,
        "O.O.OO"  : "V" ,
        ".OOO.O"  : "W" ,
        "OO..OO"  : "X" ,
        "OO.OOO"  : "Y" ,
        "O..OOO"  : "Z" 
    }

    traddecimal = {
        "O....." : "1" ,
        "O.O..." : "2" ,
        "OO...." : "3" ,
        "OO.O.." : "4" ,
        "O..O.." : "5" ,
        "OOO..." : "6" ,
        "OOOO.." : "7" ,
        "O.OO.." : "8" ,
        ".OO..." : "9" ,
        ".OOO.." : "0" 
    }


    # 0- lowercases&spaces 1- decimal/number 2- uppercases
    state = 0


    ans = []


    i = 0

    while i < len(s) :
        char = s[i:i+6]

        if state == 0 : # default  - lowercases and spaces

            if char == ".....O" : #uppercase follow
                state = 2

            elif char == ".O.OOO" : # number follow
                state = 1

            else : 
                ans.append(tradlower[char])

        elif state == 1 : # decimal/number

            if char == "......" :
                state = 0
                ans.append(tradlower[char])
            else :
                ans.append(traddecimal[char])

        else : # uppercases
            state = 0
            ans.append(tradupper[char])

        i += 6

    return  "".join(ans)# merge string and return, would have concatonated but this method is faster 


def translatetoBraille(s) :

    trad ={
        "a" : "O.....",
        "b" : "O.O...",
        "c" : "OO....",
        "d" : "OO.O..",
        "e" : "O..O..",
        "f" : "OOO...",
        "g" : "OOOO..",
        "h" : "O.OO..",
        "i" : ".OO...",
        "j" : ".OOO..",
        "k" : "O...O.",
        "l" : "O.O.O.",
        "m" : "OO..O.",
        "n" : "OO.OO.",
        "o" : "O..OO.",
        "p" : "OOO.O.",
        "q" : "OOOOO.",
        "r" : "O.OOO.",
        "s" : ".OO.O.",
        "t" : ".OOOO.",
        "u" : "O...OO",
        "v" : "O.O.OO",
        "w" : ".OOO.O",
        "x" : "OO..OO",
        "y" : "OO.OOO",
        "z" : "O..OOO",

        #preceded with capitals follow symbol
        "A" : ".....OO.....",
        "B" : ".....OO.O...",
        "C" : ".....OOO....",
        "D" : ".....OOO.O..",
        "E" : ".....OO..O..",
        "F" : ".....OOOO...",
        "G" : ".....OOOOO..",
        "H" : ".....OO.OO..",
        "I" : ".....O.OO...",
        "J" : ".....O.OOO..",
        "K" : ".....OO...O.",
        "L" : ".....OO.O.O.",
        "M" : ".....OOO..O.",
        "N" : ".....OOO.OO.",
        "O" : ".....OO..OO.",
        "P" : ".....OOOO.O.",
        "Q" : ".....OOOOOO.",
        "R" : ".....OO.OOO.",
        "S" : ".....O.OO.O.",
        "T" : ".....O.OOOO.",
        "U" : ".....OO...OO",
        "V" : ".....OO.O.OO",
        "W" : ".....O.OOO.O",
        "X" : ".....OOO..OO",
        "Y" : ".....OOO.OOO",
        "Z" : ".....OO..OOO",


        "1" : "O.....",
        "2" : "O.O...",
        "3" : "OO....",
        "4" : "OO.O..",
        "5" : "O..O..",
        "6" : "OOO...",
        "7" : "OOOO..",
        "8" : "O.OO..",
        "9" : ".OO...",
        "0" : ".OOO..",

        " " : "......"

    }

    ans = []


    i = 0
    while i < len(s) :

        if s[i] in ["0", "1" , "2" , "3" , "4" , "5" , "6" , "7" ,"8", "9"] :
            p = i

            while i < len(s) and s[i] in ["0", "1" , "2" , "3" , "4" , "5" , "6" , "7" ,"8", "9"] :
                i += 1

            ans.append(".O.OOO") #number follows
            while  p < i  :
                ans.append(trad[s[p]])
                p += 1
            #no need to manually add space after only if they are actually present

        else :
            ans.append(trad[s[i]])
            i += 1

    return "".join(ans)




#main program

import sys


# if multiple word - it's english since braille has it's own spacing character
if len(sys.argv) > 2 :
    tmp = []
    i = 1

    while i < len(sys.argv) :
        tmp.append(sys.argv[i])

        if i + 1  < len(sys.argv) :
            tmp.append(" ")

        i +=1


    print(translatetoBraille("".join(tmp)))


# only one word and it's not braille 
elif len(sys.argv[1]) % 6 != 0 : 
    print(translatetoBraille(sys.argv[1]))


else :

    #assuming that if we started writing in braille we won't swtich to English afterwards
    i = 0

    while i < len(sys.argv[1]) and i < 6 :

        if sys.argv[1][i] not in ["O", "."] :
            print(translatetoBraille(sys.argv[1]))
            break 

        i += 1

    else :
        print(translateToEnglish(sys.argv[1]))

