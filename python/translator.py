import sys

arguments = sys.argv[1:]
wholeText = " ".join(arguments)

engBrailleLetters = {
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
    "cap": ".....O",
    "number": ".O.OOO",
    " ": "......"}

engBrailleNumbers = {
    0: ".OOO..",
    1: "O.....",
    2: "O.O...",
    3: "OO....",
    4: "OO.O..",
    5: "O..O..",
    6: "OOO...",
    7: "OOOO..",
    8: "O.OO..",
    9: ".OO..."}

def checkBraille(text):
    brailleText = set("O.")
    isBraille = all(char in brailleText for char in text)
    
    return isBraille

def translate(text):
    output = ""
    listLetters = []
    capTrue = False
    numTrue = False
    
    if checkBraille(text):
        for i in range(0, len(text), 6):
            listLetters.append(text[i:i+6])
        
        for letter in listLetters:
            if letter == engBrailleLetters["number"]:
                numTrue = True
                continue
            
            elif numTrue:
                if letter != engBrailleLetters[" "]:
                    for key, value in engBrailleNumbers.items():
                        if letter == value:
                            output += str(key)
                            continue
                else:
                    numTrue = False
                    output += " "
                    
            elif letter == engBrailleLetters["cap"]:
                capTrue = True
                continue

            else:
                for key, value in engBrailleLetters.items():
                    if letter == value:
                        if capTrue:
                            output += key.upper()
                            capTrue = False
                            continue
                        else:
                            output += key
                            continue
        return output
    
    elif not checkBraille(text):
        mots = text.split(" ")

        for mot in mots:
            for char in mot:
                try:
                    char = int(char)
                    if char == int(mot[0]):
                        output += engBrailleLetters["number"]
                    output += engBrailleNumbers[char]
                    continue
                except:
                    pass
                
                if char.isupper():
                    output += engBrailleLetters["cap"]
                output += engBrailleLetters[char.lower()]
            if mot != mots[-1]:
                output += engBrailleLetters[" "]
        
        return output

print(translate(wholeText))