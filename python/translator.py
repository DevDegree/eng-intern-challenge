import sys

#create a dictionary with the braille characters
brailleDict ={
    "a":"O.....",
    "b":"O.O...",
    "c":"OO....",
    "d":"OO.O..",
    "e":"O..O..",
    "f":"OOO...",
    "g":"OOOO..",
    "h":"O.OO..",
    "i":".OO...",
    "j":".OOO..",
    "k":"O...O.",
    "l":"O.O.O.",
    "m":"OO..O.",
    "n":"OO.OO.",
    "o":"O..OO.",
    "p":"OOO.O.",
    "q":"OOOOO.",
    "r":"O.OOO.",
    "s":".OO.O.",
    "t":".OOOO.",
    "u":"O...OO",
    "v":"O.O.OO",
    "w":".OOO.O",
    "x":"OO..OO",
    "y":"OO.OOO",
    "z":"O..OOO",
    "capital":".....O",
    "decimal":".O...O",
    "number":".O.OOO",
    ".":"..OO.O",
    ",":"..O...",
    "?":"..O.OO",
    "!":"..OOO.",
    ":":"..OO..",
    ";":"..O.O.",
    "-":"....OO",
    "/":".O..O.",
    "<":".OO..O",
    ">":"O..OO.",
    "(":"O.O..O",
    ")":".O.OO.",
    " ":"......"
}

#assumption: when a decimal number is to be translated, the decimal follows character in braille is used to represent the .

def isBraille(sentence):
    #check if the input string is english
    if (len(sentence)<6):
        return False
    #check if the first 6 characters are in the braille alphabet
    return (sentence[:6] in brailleDict.values())


#translate from braille to english
def brailleTranslate(sentence):
    i=0
    translated=""
    cap=False
    num=False
    dec=False
    while i<=(len(sentence)-6):
        char=list(brailleDict.keys())[list(brailleDict.values()).index(sentence[i:i+6])]
        i+=6
        
        if (cap):
            #if cap is true it means that a capital character has been encountered right before
            char=chr(ord(char)-32)
            cap=False
            translated+=char

        elif (num):
            if (char=='j'):
                char='0'
            elif (char==' '):
                #no longer a number follwoing this character so we reset our boolean
                num=False
                dec =False
            elif (char=="decimal"):
                char="."
            else:
                char= chr(ord(char)-48)
            translated+=char

        elif (char == "capital"):
            cap=True
        elif (char=="number"):
            num=True
        else:
            translated+=char
    print (translated)

#translate from english to braille
def englishTranslate(sentence):
    translated=""
    num=False

    for i in range(len(sentence)):
        char=sentence[i:i+1]
        if (num):
            if (char==" "):
                num=False
            elif (char=="0"):
                char="j"
            #assumption: when a decimal number is to be translated, the decimal follows character in braille is used to represent the .
            #check if the . is in between 2 number indicating that it is a decimal point
            elif (char=="." and i+1<len(sentence)and ord(sentence[i+1])>=48 and ord(sentence[i+1])<=57):
                char="decimal"
            else:
                char=chr(ord(char)+48)
        elif (ord(char)>=65 and ord(char)<91):
            translated+=brailleDict.get("capital")
            char=char.lower()
        elif (ord(char)>=48  and ord(char)<58 and not num):
            #check if the char is the first digit of a number
            translated+=brailleDict.get("number")
            num=True
            if (char=="0"):
                char="j"
            else:
                #convert it to its corresponding alphabet before adding the braille translation
                char=chr(ord(char)+48)
        translated+=brailleDict.get(char)
    print (translated)

s=sys.argv[1:]
if (len(s)>0):
    sentence=s[0]
    for i in s[1:]:
        sentence+=" "+i

    if (isBraille(sentence)):
        brailleTranslate(sentence)
    else:
        englishTranslate(sentence)

