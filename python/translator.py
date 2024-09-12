engToBraille = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    " ": "......"
    
}
numToBraille = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
}
brailleToEng = {value:keys for keys,value in engToBraille.items()}
brailleToNum = {value:keys for keys,value in numToBraille.items()}
def translatebrailletoeng(btext):
    numbersign = ".O.OOO"
    numberfollows = False
    capitalFollows = False
    start = 0 
   
    res = ''
    while start < len(btext) :
        end = start +6
        b = btext[start:end]
        if b == numbersign  and not numberfollows:
            numberfollows = True
            start += 6
            continue
        if b == ".....O":
            capitalFollows = True 
        else:
            if numberfollows == True:
                if b == "......":
                    numberfollows = False
                else:
                    res   += brailleToNum[b]
            if capitalFollows == True :
                res += brailleToEng[b].upper()
                capitalFollows = False
            else:
                if not numberfollows and not capitalFollows:
                    res += brailleToEng[b]
        start += 6
       
    return res
    
def translateEngToBraille(etext):
    numberfollows = False
    Capitalfollows = False
    res =""
    for c in etext:
        if c.isnumeric() and not numberfollows:
            numberfollows = True
            res+=".O.OOO"+ numToBraille[c]
        elif numberfollows ==True:
            if c.isnumeric():
                res+= numToBraille[c]
            if c == " ":
                numberfollows = False
                res+= "......"
                continue
        elif c.isupper():
            res+=".....O" + engToBraille[c.lower()]
        elif c.islower():
            res+=engToBraille[c]
        elif c == " " and not numberfollows:
            res+= engToBraille[c]
        
    return res
def checkifenglish(text):
    for c in text:
        if c!="O" and c!= ".":
            return True 
            
import sys



if __name__ == "__main__":
    if len(sys.argv) >= 1:
        text = " ".join(sys.argv[1:])

        
        if checkifenglish(text):
            print(translateEngToBraille(text))
        else:
            print(translatebrailletoeng(text))
    

