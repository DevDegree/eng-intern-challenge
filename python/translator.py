import sys

brailleNumberFollows = ".O.OOO"
brailleCapitalFollows = ".....O"
brailleSpace="......"
localIndexToASCIIOffset = 29
ASCIItoLocalIndexOffset = 29
ASCIIcaptialToSmallLetterOffset = 61
letterJOffset = 26
letterAtoIOffset = 16

brailleConvention = [".....O",".O...O",".O.OOO","......","..OOO.","","","","","","","O.O..O",".O.OO.","","","..O...","....OO","..OO.O",".O..O.",".OOO..","O.....","O.O...","OO....","OO.O..","O..O..","OOO...","OOOO..","O.OO..",".OO...","","","","","","","","O.....","O.O...","OO....","OO.O..","O..O..","OOO...","OOOO..","O.OO..",".OO....",".OOO..","O...O.","O.O.O.","OO..O.","OO.OO.","O..OO.","OOO.O.","OOOOO.","O.OOO.",".OO.O.",".OOOO.","O...OO","O.O.OO",".OOO.O","OO..OO","OO.OOO","O..OOO"]
def inputchecker(input1):           # here i am checking if it's braille or english by removing the braille only characters and seeing if it's null or not. 
    typeOfString = ""
    input1 = input1.replace('O','')
    input1 = input1.replace('.','')
    if(input1 == ""):
        typeOfString = "Braille"
    else:
        typeOfString = "English"
    return typeOfString
    

def brailleToEnglish(input):
    smallLetterFlag = True
    numberFollowsFlag = False
    inputSplit = []
    finalString = ""
    while(input):
        inputSplit.append(input[:6])
        input=input[6:]
    for singleInput in inputSplit:
        indexValue = brailleConvention.index(singleInput)
        if(indexValue == 0):
            smallLetterFlag = False
        elif(indexValue == 2):
            numberFollowsFlag = True
        elif(indexValue == 3):
            if numberFollowsFlag == True :
                finalString = finalString + " " 
                numberFollowsFlag = False
            else:
                finalString = finalString + " "
        elif(numberFollowsFlag == True and indexValue > 2):             #using chr() here to convert the int values to ASCII characters by obtaining the index by matching the indiviudal braille input.
            finalString = finalString + chr(indexValue + localIndexToASCIIOffset)
        elif(numberFollowsFlag == False and indexValue > 2):          # 2 exceptions.. if index is in 48 and 57 add + 16/26
            if((indexValue + localIndexToASCIIOffset) > 47 and (indexValue + localIndexToASCIIOffset) < 57 and smallLetterFlag == False ):   # I am checking if the ASCII values of 0 to 9 are between 47 and 57 and if it is true with small letter flag as false, I will print the braille Letters of A - J appropriately since braille for these numbers and letters are the same. 
                if((indexValue + localIndexToASCIIOffset) == 48):                                                        # 48 is the ASCII value of 0
                    finalString = finalString + chr((indexValue + localIndexToASCIIOffset) + letterJOffset)            # letterJOffset - 26 for offsetting it to ASCII for adding J corresponding to 0
                    smallLetterFlag = True
                else:
                    finalString = finalString + chr((indexValue + localIndexToASCIIOffset) + letterAtoIOffset)            # letterAtoIOffset - 16 for offsetting it to ASCII for adding A - I corresponding to 1 - 9
                    smallLetterFlag = True
            elif((indexValue + localIndexToASCIIOffset) > 36 and (indexValue + localIndexToASCIIOffset) < 61 and smallLetterFlag == True ):
                if((indexValue + localIndexToASCIIOffset) == 48):                                                           # 48 is the ASCII value of 0
                    finalString = finalString + chr((indexValue + ASCIIcaptialToSmallLetterOffset) + letterJOffset)            # letterJOffset - 26 is added as offset to get the ASCII value of letter 'j' since J and 0 has same Braille pattern
                else:
                    finalString = finalString + chr((indexValue + ASCIIcaptialToSmallLetterOffset) + letterAtoIOffset)            #  letterAtoIOffset - 16 is added as offset to get the ASCII value of letters 'a b c d e f g h i' since numbers 1 to 9 same Braille pattern
            elif(smallLetterFlag == False):
                 finalString = finalString + chr(indexValue + localIndexToASCIIOffset)   
                 smallLetterFlag = True; 
            else:
                if(smallLetterFlag == True):
                    finalString = finalString + chr(indexValue + ASCIIcaptialToSmallLetterOffset)    
                else:
                    finalString = finalString + chr(indexValue + localIndexToASCIIOffset)
    return finalString

        


def englishToBraille(input):
    numberFollowsFlag = False
    inputSplit = []
    finalString = ""
    spaceFlag = False
    inputSplit = list(input)
    for singleInput in inputSplit:
        if(singleInput.isalpha() and singleInput.isupper()):        # using ord() here to find the ASCII value of characters and doing the offsetting and getting the value as per the local braille convention index.
            finalString = finalString + brailleCapitalFollows
            finalString = finalString + brailleConvention[ord(singleInput) - ASCIItoLocalIndexOffset]
        elif(singleInput.isalpha() and singleInput.islower()):
            finalString = finalString + brailleConvention[(ord(singleInput) - 32) - ASCIItoLocalIndexOffset]     # 32 is needed to bring from e to E and reference it to the local index that I have 
        elif(singleInput.isnumeric()):
            if(numberFollowsFlag == True):
                finalString = finalString + brailleConvention[ord(singleInput) - ASCIItoLocalIndexOffset]
            else:
                numberFollowsFlag = True
                finalString = finalString + brailleNumberFollows
                finalString = finalString + brailleConvention[ord(singleInput) - ASCIItoLocalIndexOffset]
        elif(singleInput == ' '):
            if(numberFollowsFlag == True):
                finalString = finalString + brailleSpace
                numberFollowsFlag = False
            else:                
                finalString = finalString + brailleSpace
        else:
            finalString = finalString + brailleConvention[ord(singleInput) - ASCIItoLocalIndexOffset]
    return finalString


    
def driverProgram(inputs):
    finalOutputString = ""
    counter = 0
    for singleInput in inputs:          #looping the inputs and adding space as needed
        typeOfString = inputchecker(singleInput)
        outputString =""
        if(typeOfString == "Braille"):
            outputString = brailleToEnglish(singleInput)
        else:
            outputString = englishToBraille(singleInput)
        finalOutputString = finalOutputString + outputString
        if(counter != len(inputs) - 1):
            finalOutputString = finalOutputString + brailleSpace
        counter+=1
    print(finalOutputString)
if __name__ == '__main__':
    driverProgram(sys.argv[1:])         # getting inputs from cmd
    
