import sys

englishLettersDict={"a":"O.....","b":"O.O...","c":"OO....","d":"OO.O..","e":"O..O..","f":"OOO...","g":"OOOO..","h":"O.OO..","i":".OO...","j":".OOO..","k":"O...O.","l":"O.O.O.",
                    "m":"OO..O.","n":"OO.OO.","o":"O..OO.","p":"OOO.O.","q":"OOOOO.","r":"O.OOO.","s":".OO.O.","t":".OOOO.","u":"O...OO","v":"O.O.OO","w":".OOO.O","x":"OO..OO",
                    "y":"OO.OOO","z":"O..OOO", ".":"..OO.O",",":"..O...","?":"..O.OO","!":"..OOO.",":":"..OO..",";":"..O.O.","-":"....OO","/":".O..O.","<":".OO..O",">":"O..OO.",
                    "(":"O.O..O",")":".O.OO."}

numbersDict={"1":"O.....","2":"O.O...","3":"OO....","4":"OO.O..","5":"O..O..","6":"OOO...","7":"OOOO..","8":"O.OO..","9":".OO...","0":".OOO.."}

brailleDict = {}

num =0

#use the english to braille dictionary to construct the braille to english dictionary
for key in englishLettersDict:
    num+=1
    number = num
    if num>9:           #since numbers have the same braille symbol as letters, increment this count so numbers 0-9 can be grouped with the first 10 letters
        number = 0
    if num>10:
        number =-1
    
    if englishLettersDict[key] not in brailleDict:   #noticed in braille.jpg that O and > have the same braille symbol. Not sure if this was a mistake or not so decided to not include ">" in this dictionary
        brailleDict[englishLettersDict[key]] = (key,number)


brailleDict["......"] = (" ",-1)



def englishTranslate(argument):
    
    braille = argument[0]
    ind =0
    ch=""
    output =""
    numPres=False
    capital=False

    while ind<len(braille):
        ch += braille[ind]
        if len(ch)==6:
            if ch ==".....O":   #if capital letter set true to make the next letter capital
                capital = True
            
            elif ch ==".O.OOO":  #if number next braille character, set condition true for proceeding characters
                numPres = True
            
            elif ch not in brailleDict and ch!=".O...O":  # if current braille character is not valid, then switch to english->braille translation since the string is invalid braille
                brailleTranslate(argument)
                return
            else:
                if numPres and ch ==".O...O":      # if decimal follows character, add the the decimal point
                    output+="."   
                else:             
                    lett,num = brailleDict[ch]
                    if numPres and num!=-1:
                        output+=str(num)
                    elif lett.isalpha():
                        if capital:
                            output+=lett.upper()
                            capital=False
                        else:
                            output+=lett
                    else:
                        if lett ==" ":
                            numPres=False
                        output+=lett   

            ch=""
        ind +=1

    print(output)

def brailleTranslate(argument):

    output = ""

    for word in argument:
        numberPres=False
        for ch in word:
            if ch in numbersDict or (numberPres and ch=="."):
                if not numberPres:
                    output+=".O.OOO"
                    numberPres=True
                if numberPres and ch==".":
                    output+=".O...O"
                else:
                    output+=numbersDict[ch]
            else:
                if ch.isalpha():                      
                    if ch!=ch.lower():
                        output+=".....O"
                        output+=englishLettersDict[ch.lower()]
                    else:
                        output+=englishLettersDict[ch]
                else:
                    output+=englishLettersDict[ch]
        
        output+="......"    # the arguments passed will not include the spaces as string characters. Since the words are split into an array, add the space character after processing each word
    
    output = output[:-6]  #removes the last space character added after the last word processed

    print(output)


if __name__ == "__main__":


    if len(sys.argv) > 1:
        argument = []
        wordCnt = len(sys.argv)
        for i in range(1,wordCnt):
            argument.append(sys.argv[i])
        
        if len(argument)==1 and (len(argument[0])%6 ==0):
            englishTranslate(argument)
        else:
            brailleTranslate(argument)

