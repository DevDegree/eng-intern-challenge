import sys

#English to Braille Conversion Dictionary
ENG_TO_BRAILLE = {
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
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO."
}

#Number to Braille Conversion Dictionary
NUM_TO_BRAILLE = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
}

#Braille Special Keys
CAPITAL_NEXT = ".....O"
NUMBER_NEXT = ".O.OOO"


#Create Braille to English Dictionary 
BRAILLE_TO_ENG = {value: key for key, value in ENG_TO_BRAILLE.items()}

#Create Braille to English Dictionary 
BRAILLE_TO_NUM = {value: key for key, value in NUM_TO_BRAILLE.items()}


def convert_to_english(sbraille: str) -> str:
    #tokenize the braille string
    length = len(sbraille)
    symbolarr = [sbraille[i:i+6] for i in range(0,length,6)]

    #set flags
    numberNext = False
    capitalNext = False

    #output string of english
    english_out = ""

    for symbol in symbolarr:

        #special cases
        if symbol == CAPITAL_NEXT:
            capitalNext = True
            numberNext = False
            continue
        elif symbol == NUMBER_NEXT:
            numberNext = True
            capitalNext = False
            continue
        elif " " == BRAILLE_TO_ENG[symbol]:
            numberNext = False
            capitalNext = False

        if capitalNext:
            english_out += BRAILLE_TO_ENG[symbol].upper()
            capitalNext = False
        elif numberNext:
            english_out += BRAILLE_TO_NUM[symbol]
        else:
            english_out += BRAILLE_TO_ENG[symbol]


    return english_out

def convert_to_braille(senglish: str) -> str:

    #output string of braille
    braille_out = ""

    #set flags
    currNumber = False

    for char in senglish:
        if char == " ":
            braille_out += ENG_TO_BRAILLE[char]
            currNumber = False
        elif char.isupper():
            braille_out += CAPITAL_NEXT
            braille_out += ENG_TO_BRAILLE[char.lower()]
            currNumber = False
        elif char.isdigit():
            if currNumber:
                braille_out += NUM_TO_BRAILLE[char]
            else:
                braille_out += NUMBER_NEXT
                braille_out += NUM_TO_BRAILLE[char]
                currNumber = True
        else:
            braille_out += ENG_TO_BRAILLE[char]

    return braille_out



if __name__ == "__main__":
    #retrieve input string
    inputstr = " ".join(sys.argv[1:])
  
    #check if it is braille or english
    if (all(char in "O." for char in inputstr)):
        output = convert_to_english(inputstr)
    else:
        output = convert_to_braille(inputstr)
    
    #write output to terminal 
    sys.stdout.write(output)

