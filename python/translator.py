import sys

englishToBraille = {
    "capital follows": ".....O",
    "number follows": ".O.OOO",
    " ": "......",
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
}

numberToBraille = {
    "0": ".OOO..",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
}

brailleToNumber = { value: key for key, value in numberToBraille.items() }
brailleToEnglish = { value: key for key, value in englishToBraille.items() }

# translate from braille to english
def translateEnglish(inputString):
    output = ""
    capitalFollow = False
    numberFollow = False

    words = [inputString[i : i + 6] for i in range(0, len(inputString), 6)]

    for word in words:
        if brailleToEnglish[word] == "capital follows":
            capitalFollow = True
        elif brailleToEnglish[word] == "number follows":
            numberFollow = True  
        elif brailleToEnglish[word] == " ":
            output += " "
            numberFollow = False
            capitalFollow = False
        else:
            if numberFollow:
                output += brailleToNumber[word]
            elif capitalFollow:
                output += brailleToEnglish[word].upper()
                capitalFollow = False
            else:
                output += brailleToEnglish[word]
            
    return output

# translate from english to braille
def translateBraille(inputString):
    output = ""
    numberFollow = False

    for character in inputString:
        if character.isdigit():
            if not numberFollow:
                output += englishToBraille["number follows"]
                numberFollow = True
                
            output += numberToBraille[character]
        else: 
            if character == " ":
                output += englishToBraille[" "]
                numberFollow = False
            else:               
                if character.isupper(): 
                    output += englishToBraille["capital follows"]
                output += englishToBraille[character.lower()]    
                                
    return output

def main(args):
    if len("".join(args).replace(".", "").replace("O", "")) == 0:
        output = translateEnglish("".join(args))
    else:
        output = translateBraille(" ".join(args))

    return output

if __name__ == "__main__":
    args = sys.argv[1:]
    if args:
        output = main(args)
    else:   
        output = main("");
    print(output)
