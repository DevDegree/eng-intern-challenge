import sys

alphaDict = {
    'a': "O.....",
    'b': "O.O...",
    'c': "OO....",
    'd': "OO.O..",
    'e': "O..O..",
    'f': "OOO...",
    'g': "OOOO..",
    'h': "O.OO..",
    'i': ".OO...",
    'j': ".OOO..",
    'k': "O...O.",
    'l': "O.O.O.",
    'm': "OO..O.",
    'n': "OO.OO.",
    'o': "O..OO.",
    'p': "OOO.O.",
    'q': "OOOOO.",
    'r': "O.OOO.",
    's': ".OO.O.",
    't': ".OOOO.",
    'u': "O...OO",
    'v': "O.O.OO",
    'w': ".OOO.O",
    'x': "OO..OO",
    'y': "OO.OOO",
    'z': "O..OOO",
    ' ': "......"     
}

numDict = {
    '1': "O.....",
    '2': "O.O...",
    '3': "OO....",
    '4': "OO.O..",
    '5': "O..O..",
    '6': "OOO...",
    '7': "OOOO..",
    '8': "O.OO..",
    '9': ".OO...",
    '0': ".OOO..",
}

followsDict = {
    "cf": ".....O",
    "nf": ".O.OOO"
}


#As per instructions: braille alphabet consists of a-z, 0-9, capitalization and multiple words (spaces)



def str2bra(text):
    bra = ""
    idx = 0
    while idx < len(text):
        letter = text[idx]
        #Need to check for 'follows' braille first
        if(letter.isnumeric()):     #if letter is a number
            bra = bra + followsDict.get("nf")
            while(idx < len(text) and text[idx] != ' '):       #number until space or EOF
                bra = bra + numDict.get(text[idx])
                idx += 1
            if idx < len(text) and text[idx] == ' ':
                bra = bra + alphaDict.get(text[idx])

        elif(letter.isupper()):       #if letter is a capital
            bra = bra + followsDict.get("cf")
            letter = letter.lower()
            bra = bra + alphaDict.get(letter)

        else:
            bra = bra + alphaDict.get(letter)

        idx += 1
        


    return bra



def bra2str(bra):
    text = ""
    idx = 0

    #need to invert dictionaries
    braAlphaDict = {v: k for k, v in alphaDict.items()}
    braNumDict = {v: k for k, v in numDict.items()}
    braFollowDict = {v: k for k, v in followsDict.items()}


    while idx < len(bra):
        letter = bra[idx:idx + 6]

        if braFollowDict.get(letter) == "cf":       #if a capital follows
            idx += 6
            text = text + (braAlphaDict.get(bra[idx:idx + 6])).upper()
        
        elif braFollowDict.get(letter) == "nf":       #if a number follows
            idx += 6
            while(idx < len(bra) and bra[idx:idx + 6] != "......"):
                text = text + (braNumDict.get(bra[idx:idx + 6])).upper()
                idx += 6
            if idx < len(bra) and bra[idx:idx + 6] == "......":
                text = text + (braAlphaDict.get(bra[idx:idx + 6])).upper()



        else:
            text = text + braAlphaDict.get(letter)

        idx += 6

    return text

def main():
    inp = ""
    idx = 1
    while idx < len(sys.argv):
        if idx != 1:
            inp = inp + " " + sys.argv[idx]
        else:
            inp = inp + sys.argv[idx]
        idx += 1
    if all(char in {'O', '.'} for char in inp) and len(inp)%6 == 0: # need to convert braille to text
        print(bra2str(inp))
    else:
        print(str2bra(inp))     #converting text to braille


if __name__ == "__main__":
    main()

