
import sys



smallerK = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","cap","dec","num",".",",","?","!",":",";","-","/","<","(",")"," "]
smallerV = ["O.....","O.O...","OO....","OO.O..","O..O..","OOO...","OOOO..","O.OO..",".OO...",".OOO..","O...O.","O.O.O.","OO..O.","OO.OO.","O..OO.","OOO.O.","OOOOO.","O.OOO.",".OO.O.",".OOOO.","O...OO","O.O.OO",".OOO.O","OO..OO","OO.OOO","O..OOO",".....O",".O...O",".O.OOO","..OO.O","..O...","..O.OO","..OOO.","..OO..","..O.O.","....OO",".O..O.",".OO..O","O.O..O",".O.OO.","......"]
smallerN = ["1","2","3","4","5","6","7","8","9","0","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","cap","dec","num",".",",","?","!",":",";","-","/","<","(",")"," "]
compare = smallerK
arguments = []
braille = []
sentence = ""
isBraille = 1
stringToPrint = ""

for i in range(1,len(sys.argv)):
    arguments.append(sys.argv[i])
    
    sentence+= sys.argv[i]

for letter in sentence:
    if (letter != "." and letter !="O"):
        isBraille = 0

if(isBraille == 0):
    sentence = ""
    for i in range(1,len(sys.argv)):
        arguments.append(sys.argv[i])
        if (i>1):
            sentence+= " "
        sentence+= sys.argv[i]

if (isBraille == 1 and len(sentence)%6 == 0):
    alert = 0
    cap = 0
    dec = 2
    

    for i in range(0,len(sentence),6):
        divider = sentence[i:i+6]
        
        for j in range(0,len(smallerV)):
            if (alert == 0 ):
                if (smallerV[j] == divider):
                    if (len(compare[j]) > 1):
                            
                        if (compare[j] == 'cap'):
                              
                            cap = 1
                            
                                
                            
                                
                        else:
                            compare = smallerN
                            if (compare[j] == 'dec'):
                                dec = 0
                            else:
                                dec = 1
                        

                    else:
                            
                        if (compare[j] == " "):
                            alert = 0
                            cap = 0
                            compare = smallerK
                            dec = 2
                        if (compare[j] == "."):
                            if(dec < 1):
                                dec += 1
                            elif(dec == 1):
                                compare = smallerK
                                dec = 2
                            
                        if (cap == 1):
                                if (j>25 or compare == smallerN):
                                    
                                    cap = 0
                                else:
                                    stringToPrint += compare[j].upper()
                                    cap = 0
                        
                        elif (dec<2 and j>9 and j<26 ):
                            
                            stringToPrint += compare[j]
                        else:
                            stringToPrint += compare[j]
else:
    isNumber = 0
    isDecimal = 0
    pointPresent = 0
    currentNumber = ""
    checker = ".O.OOO"
    
    index =0
    pointJustDone = 0

    for letter in sentence:
        index += 1
        if (letter == "."):
            if (isDecimal == 1):
                stringToPrint += checker+currentNumber+smallerV[smallerN.index(letter)]
                isNumber = 0
                isDecimal = 0
                pointJustDone = 0
                currentNumber =""
                checker = ".O.OOO"

            elif(isNumber == 1):
                pointJustDone = 1
                currentNumber += smallerV[smallerN.index(letter)]
            else:
                stringToPrint += smallerV[smallerN.index(letter)]
        
        elif (letter.isdigit()):
            isNumber = 1
            if(pointJustDone == 0):
                currentNumber += smallerV[smallerN.index(letter)]
            elif(pointJustDone == 1):
                isDecimal =1
                checker = ".O...O"
                currentNumber += smallerV[smallerN.index(letter)]
            if(len(sentence) == index):
                stringToPrint += checker + currentNumber

            pointJustDone = 0

        else:
            if (currentNumber != ""):
                stringToPrint += checker+currentNumber
                currentNumber = ""
                isNumber = 0
                isDecimal = 0
                pointJustDone = 0

                checker = ".O.OOO"
            if(letter != letter.lower()):
                stringToPrint += ".....O"
            stringToPrint += smallerV[smallerK.index(letter.lower())]
            pointJustDone = 0

print(stringToPrint, end="")


            




        
    

            


        


       
        
        


                        
        
                



        
        



    