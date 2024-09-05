#importing sys to handle input passed via tester
import sys

#setting default state of funtion bools
isCap = False
isNum = False
isBraille = True
prevNum = False

#Dictionaries to hold the braille and UTF-8 versions of chars and nums
brailleAlphabet ={
    "O.....":"a",
    "O.O...":"b",
    "OO....":"c",
    "OO.O..":"d",
    "O..O..":"e",
    "OOO...":"f",
    "OOOO..":"g",
    "O.OO..":"h",
    ".OO...":"i",
    ".OOO..":"j",
    "O...O.":"k",
    "O.O.O.":"l",
    "OO..O.":"m",
    "OO.OO.":"n",
    "O..OO.":"o",
    "OOO.O.":"p",
    "O.OOO.":"r",
    ".OO.O.":"s",
    ".OOOO.":"t",
    "O...OO":"u",
    "O.O.OO":"v",
    ".OOO.O":"w",
    "OO..OO":"x",
    "OO.OOO":"y",
    "O..OOO":"z",
    ".....O":"cap",
    ".O.OOO":"num",
    "......":" "
}

brailleNum = {
    "O.....":"1",
    "O.O...":"2",
    "OO....":"3",
    "OO.O..":"4",
    "O..O..":"5",
    "OOO...":"6",
    "OOOO..":"7",
    "O.OO..":"8",
    ".OO...":"9",
    ".OOO..":"0"
}

#getting input list from tester and combining into one string
inp = ' '.join(sys.argv[1:])

#checking if any non "O" or "." chars exist in string, indicating
#input isn't braille
for i in range(len(inp)):
    if inp[i] != "O" and inp[i]!=".":
        isBraille = False
        break

finalStr = ""

def brailleToAlphanum(isCap,isNum):
    finalStr = ""
    #progress through braille string
    pos = 0

    #Each char or function (capital, number) is made up of 6 braille dots, so the number
    #of chars/functions needed to be translated is the length of the braille input divided by 6
    for i in range(len(inp)//6):
        curChar = ""

        #Grabbing braille input in groups of 6 to be processed
        for i in range(6):
            curChar+=(inp[pos])
            pos+=1

        #Searches braille to aplha dictionary to find and convert char, if
        #a function is found instead (capital, number), it sets the
        #associated boolean to true
        if brailleAlphabet[curChar] == "cap":
            isCap=True
        elif brailleAlphabet[curChar] == " ":
                #space also sets isNum to false, since once it is true, it will
                #remain so until it finds a space
                finalStr+=" "
                isNum = False
        elif brailleAlphabet[curChar] == "num":
            isNum=True

        #If input is not a function, and instead is a num or letter,
        #the program will first check how to treat the input by checking
        #the function booleans
        else:
            #if it is a number, it checks the braille to num dictionary
            #instead of the braille to aplha one
            if isNum:
                finalStr+=brailleNum[curChar]
            
            #if it is capitalized, it capitalizes the char, and then
            #sets the capital check to off
            elif isCap:
                finalStr+=brailleAlphabet[curChar].capitalize()
                isCap=False
            
            #if neither funtion is triggered, it just adds the char to
            #the string as expected,
            else:
                finalStr+=brailleAlphabet[curChar]
    return finalStr

def alphanumToBraille(prevNum):
    finalStr = ""
    #looping through every char in input
    for i in range(len(inp)):
        #checking if current char is a number or not in order to
        #determine which dictionary to search
        if inp[i].isnumeric():
            #if the previous char wasn't a number it adds
            #the braille needed to signify that numbers have started
            if not prevNum:
                    finalStr+=".O.OOO"
            #searching through dictionary until we find a value
            #that matches the current char, and adding the associated
            #braille key to the string
            for braille,num in brailleNum.items():
                if num == inp[i]:
                    finalStr+=braille
                #after adding the number in braille, it sets the check
                #the prev char was a number to true
                prevNum = True
        else:
            #searching through alpha dictionary
            for braille,char in brailleAlphabet.items():
                #checks char in lowercase so it can be found in the dictionary
                if char == inp[i].lower():
                    #checks if the char was a capital to begin with,
                    #and if so, adds the capital braille
                    if not inp[i].islower() and not inp[i] == " ":
                        finalStr+=".....O"
                    finalStr+=braille
                    #just added a space or letter, so the prev char was no longer
                    # a number
                    prevNum = False
    return finalStr

#Runs the associated function based on whether the program
#determined the input was braille or not
if isBraille:
    finalStr = brailleToAlphanum(isCap,isNum)
else:
    finalStr = alphanumToBraille(prevNum)

#prints the output without the new line char 
print(finalStr, end="")