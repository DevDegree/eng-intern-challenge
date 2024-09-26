import sys

def brailleToEnglish(phrase, translator, numberbook):
    returnValue = []
    flags = [False, False ] #ORDER: Capital flag, Number flag

    for i in range(0,len(phrase)-5, 6): # 
        if phrase[i : i+6] in translator:
            translatedLetter = translator[phrase[i : i+6]]
            
            if phrase[i : i+6] ==  "O..OO.": #since o and > are the same we will use context to differentiate 
                if len(returnValue) != 0:
                    if 'a' <= returnValue[len(returnValue)-1] <= 'z' or 'A' <= returnValue[len(returnValue)-1] <= 'Z':
                        returnValue.append("o")
                    elif len(phrase) >= 12 and ('a' <= phrase[i+6 : i+12] <= 'z' or 'A' <= phrase[i+6 : i+12] <= 'Z'):
                        returnValue.append("o")
                    else:
                        returnValue.append(">")
                else:
                    returnValue.append("o")
                
            elif flags[0]:
                flags = [False, False]
                returnValue.append(translatedLetter.upper())
                
            elif flags[1]:
                returnValue.append(numberbook[translatedLetter])
                
            elif translatedLetter == "Capital":
                 flags = [True, False]
                
            elif translatedLetter == "Number":
               
                flags[1] = not flags[1]
                
            elif translatedLetter == "Decimal":
                returnValue.append(".")
            
            else:
                flags = [False, False]
                returnValue.append(translator[phrase[i : i+6]])
       
        else:
            raise ValueError("The value does not exist!")
        
    return returnValue

def englishToBraille(phrase, translator, numberbook):

    returnValue = []
    flag = False
    for char in phrase:
        
        if flag and not char.isdigit:
            flag = False 
            
        if char.isalpha() and char == char.upper():
            returnValue.append(translator["Capital"])
            returnValue.append(translator[char.lower()])
            
        elif char.isdigit(): 
            
            if flag:
                returnValue.append(translator[numberbook[char]])
                
            else: 
                returnValue.append(translator["Number"])
                returnValue.append(translator[numberbook[char]])
                flag = True
                
        elif char == "." and phrase[phrase.index(char) +1 ].isdigit(): 
            returnValue.append(translator['Decimal'])
            
        else:
            if char in translator:
                returnValue.append(translator[char])
            else: 
                raise ValueError("The value does not exist!" )
        
        
    return "".join(returnValue)


numberBook = {
    "a" : "1",
    "b" : "2",
    "c" : "3",
    "d" : "4",
    "e" : "5",
    "f" : "6",
    "g" : "7",
    "h" : "8",
    "i" : "9",
    "j" : "0"
}
fastBook = {
    
        "O....." : "a",
        "O.O..." : "b",
        "OO...." : "c",
        "OO.O.." : "d",
        "O..O.." : "e",
        "OOO..." : "f",
        "OOOO.." : "g",
        "O.OO.." : "h",
        ".OO..." : "i",
        ".OOO.." : "j",
        "O...O." : "k",
        "O.O.O." : "l",
        "OO..O." : "m",
        "OO.OO." : "n",
        "O..OO." : "o",
        "OOO.O." : "p",
        "OOOOO." : "q",
        "O.OOO." : "r",
        ".OO.O." : "s",
        ".OOOO." : "t",
        "O...OO" : "u",
        "O.O.OO" : "v",
        ".OOO.O" : "w",
        "OO..OO" : "x",
        "OO.OOO" : "y",
        "O..OOO" : "z",
        ".....O" : "Capital",
        ".O...O" : 'Decimal',
        ".O.OOO" : "Number",
        "..OO.O" : ".",
        "..O..." : ",",
        "..O.OO" : "?",
        "..OOO." : "!",
        "..OO.." : ":",
        "..O.O." : ";",
        "....OO" : "_",
        ".O..O." : "/",
        ".OO..O" : "<", # The > has the same as code as o must be a mistake so i did not include
        "O.O..O" : "(",
        ".O.OO." : ")",
        "......" : " "
    }

arguments = sys.argv[1:]
flag = False 

translatedPhrase = []
for str in arguments:
    if ((len(str) % 6) == 0) and str[0:6] in fastBook and (str[6:12] in fastBook or len(str) <= 6):
        try:
            translatedPhrase.append("".join(brailleToEnglish(str, fastBook, numberBook)))
        except ValueError as e:
            print(e)
            exit()
        
    else:
        try:
            flag = True
            translatedPhrase.append(englishToBraille(str, {value: key for key, value in fastBook.items()}, {value: key for key, value in numberBook.items()}))
            if not str is arguments[len(arguments) -1 :][0]:
                translatedPhrase.append("......")
        except ValueError as e:
            print(e)
            exit()
        
if flag:
    print("".join(translatedPhrase))
else:
    print(translatedPhrase[0])

