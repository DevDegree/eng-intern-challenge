import sys
#!/usr/bin/env python

#Defining English alphabet to Braille
engToBraille = {'a':'O.....', 'b':'O.O...', 'c':'OO....','d':'OO.O..','e':'O..O..','f':'OOO...','g':'OOOO..','h':'O.OO..','i':'.OO...','j':'.OOO..','k':'O...O.','l':'O.O.O.','m':'OO..O.','n':'OO.OO.','o':'O..OO.','p':'OOO.O.','q':'OOOOO.','r':'O.OOO.','s':'.OO.O.','t':'.OOOO.','u':'O...OO','v':'O.O.OO','w':'.OOO.O','x':'OO..OO','y':'OO.OOO','z':'OO..O.',' ':'......'}

#Defining Numbers to Braille
numberToBraille = {'1':'O.....','2':'O.O...','3':'OO....','4':'OO.O..','5':'O..O..','6':'OOO...','7':'OOOO..','8':'O.OO..','9':'.OO...','0':'.OOO..'}

#Defining Braille to English alphabet
brailleToEng = {'O.....':'a','O.O...':'b','OO....':'c','OO.O..':'d','O..O..':'e','OOO...':'f','OOOO..':'g','O.OO..':'h','.OO...':'i','.OOO..':'j','O...O.':'k','O.O.O.':'l','OO..O.':'m','OO.OO.':'n','O..O.':'o','OOO.O.':'p','OOOOO.':'q','O.OOO.':'r','.OO.O.':'s','.OOOO.':'t','O...OO':'u','O.O.OO':'v','.OOO.O':'w','OO..OO':'x','OO.OOO':'y','OO..O.':'z','......':' '}

#Defining Braille to Numbers
brailleToNumber = {'O.....':'1','O.O...':'2','OO....':'3','OO.O..':'4','O..O..':'5','OOO...':'6','OOOO..':'7','O.OO..':'8','.OO...':'9','.OOO..':'0'}

#Special characters for Braille
capital = '.....O'
decimal = '.O...O'
number = '.O.OOO'
space = '......'

#For English to Braille
def eng_to_braille(inputStr):
    brailleOutput = []
    numCheck = False
    for char in inputStr:
        if char.isdigit():
            if not numCheck:
                #Adds the 'number follow' braille to the output string
                brailleOutput.append(number)
                numCheck = True
            #Adds the number to the output string by referring to the dictionary
            brailleOutput.append(numberToBraille[char])
        elif char.isalpha(): #Checks if character is from the alphabet
            if char.isupper(): #Checks if character is uppercase
                brailleOutput.append(capital) #Adds the 'capital follows' braille to the output string
                #Convers the character to lowercase and refers to the dictionary for the braille
                char = char.lower()
            brailleOutput.append(engToBraille[char])
            numCheck = False
        elif char == ' ': #Checks for space
            brailleOutput.append(space) #Adds 'space follows' braille to the output string
            numCheck = False
    return ''.join(brailleOutput)

#For Braille to English
def braille_to_eng(inputStr):
    englishOutput = []
    numCheck = False
    capitalizeChar = False

    #Splits braille input into 6 character blocks
    brailleBlocks = []
    for i in range(0, len(inputStr), 6):
        brailleBlocks.append(inputStr[i:i+6])

    for char in brailleBlocks:
        #Special Braille Character Handling
        if char == number: #Checks if next character is a number
            numCheck = True

        elif char == capital: #Checks for capital character
            capitalizeChar = True

        elif char == space:
            englishOutput.append(' ') #Adds a space if it sees the braille for a space
            numCheck = False
            capitalizeChar = False

        #Regular Character Handling
        else:
            if numCheck:
                toAdd = brailleToNumber.get(char, '?')
                englishOutput.append(toAdd) #Adds number

            elif capitalizeChar:
                toAdd = brailleToEng.get(char, '?')
                englishOutput.append(toAdd.upper()) #Adds capital character
                capitalizeChar = False

            else:
                toAdd = brailleToEng.get(char, '?')
                englishOutput.append(toAdd) #Adds character

    return ''.join(englishOutput)

def checkLanguage(inputStr):
    counter = 0
    for char in inputStr:
        if (char == 'O') or (char == '.'):
            counter += 1
        else:
            return False
    return counter % 6 == 0 #Checks if counter iis divisble by six since braille is in 6 character blocks 

def translate(inputStr):
    if checkLanguage(inputStr):
        return braille_to_eng(inputStr)
    else: 
        return eng_to_braille(inputStr)

if __name__ == "__main__":
    inputStr = sys.argv[1].strip()  #Removes any spaces in the front or back of the string
    result = translate(inputStr)
    print(result)