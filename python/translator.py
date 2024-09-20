import sys

eng2Braille = {
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

braille2Eng = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    "......": " "
}

capitalFollows = ".....O"
numberFollows =  ".O.OOO"

def englishToBraille():
    number = False 
    brailleText = []
    for word in sys.argv[1:]:
        for char in word:
            if char.isdigit():
                if not number: 
                    #only insert the numberFollows symbol once per word
                    brailleText.append(numberFollows)
                    number = True
                if char == '0':
                    #ASCII math doesn't apply to 0
                    brailleText.append(eng2Braille['j'])
                else:
                    #Find letter by adding number to a and subtracting 1 (since 1 is a)
                    brailleText.append(eng2Braille[chr(ord('a')+int(char)-1)])
            else:
                if char.isupper():
                    #capitalFollows is required for every capital letter
                    brailleText.append(capitalFollows)
                brailleText.append(eng2Braille[char.lower()])  
        brailleText.append(eng2Braille[" "])
        number = False 

    #remove trailing space symbol
    print(''.join(brailleText[:-1]))

def brailleToEnglish():
    englishText = []
    index = 0
    number = False
    capital = False
    brailleText = sys.argv[1]
    while index <  len(brailleText):
        word = brailleText[index:index+6]
        if word == capitalFollows:
            capital = True
        elif word == numberFollows:
            number = True
        elif capital:
            englishText.append(braille2Eng[word].upper())
            #reset capital flag after every capital letter
            capital = False
        elif word == eng2Braille[" "]:
            #reset number flag after every space symbol
            number = False
            englishText.append(braille2Eng[word])
        elif number:
            if word == ".OOO..":
                #ASCII math doesn't apply to 0
                englishText.append("0")
            else:
                #Find number by subtracting letter from a and adding 1 (since a is 1)
                englishText.append(str(ord(braille2Eng[word])-ord('a')+1))
        else:
            englishText.append(braille2Eng[word])

        #read 6 characters at a time
        index+=6
    print(''.join(englishText))
       

def main():
  if len(sys.argv) <= 1:
    return
  if (sys.argv[1].isalnum()):
    #if the first argument is alphanumeric, assume it's an english text
    englishToBraille()
  else:
    #otherwise assume it's braille
    brailleToEnglish()

if __name__ == '__main__':
    main()


