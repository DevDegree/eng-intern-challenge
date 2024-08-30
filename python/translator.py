import sys

letter = { 
    "a" : "O.....",
    "b" : "O.O...",
    "c" : "OO....",
    "d" : "OO.O..",
    "e" : "O..O..",
    "f" : "OOO...",
    "g" : "OOOO..",
    "h" : "O.OO..",
    "i" : ".OO...",
    "j" : ".OOO..",
    "k" : "O...O.",
    "l" : "O.O.O.",
    "m" : "OO..O.",
    "n" : "OO.OO.",
    "o" : "O..OO.",
    "p" : "OOO.O.",
    "q" : "OOOOO.",
    "r" : "O.OOO.",
    "s" : ".OO.O.",
    "t" : ".OOOO.",
    "u" : "O...OO",
    "v" : "O.O.OO",
    "w" : ".OOO.O",
    "x" : "OO..OO",
    "y" : "OO.OOO",
    "z" : "O..OOO",
    "." : "..OO.O",
    "," : "..O...",
    "?" : "..O.OO",
    "!" : "..OOO.",
    ":" : "..OO..",
    ";" : "..O.O.",
    "-" : "....OO",
    "/" : ".O..O.",
    "<" : ".OO..O",
    ">" : "O..OO.",
    "(" : "O,O,,O",
    ")" : ".O.OO.",
}

nums = {
    "1" : "O.....",
    "2" : "O.O...",
    "3" : "OO....",
    "4" : "OO.O..",
    "5" : "O..O..",
    "6" : "OOO...",
    "7" : "OOOO..",
    "8" : "O.OO..",
    "9" : ".OO...",
    "O" : ".OOO..",
}

info = {
    "capital" : ".....O",
    "decimal" : ".O...O",
    "number" : ".O.OOO",
}


def which(inputs):
    for i, word in enumerate(inputs):
        if all(char in {'.', 'O'} for char in word):
            #Then input is braille therefore will translate to English
            last = (i == len(inputs) - 1)
            translateToEnglish(word, last)
        else:
            #Then input has other characters besides . and O then it is braille and must be translated to English
            last = (i == len(inputs) - 1)
            translateToBraille(word, last)


def translateToBraille (word, last):
    Number = False
    for char in word:
        if (char.isalpha()):
            Number=False
            if (char.isupper()):
                print(info["capital"], end="")
            print(letter[char.lower()], end="")
        elif (char.isdigit()):
            if Number == False:
                print(info["number"], end="")
                print(nums[char], end="")
                Number = True
            else: print(nums[char], end="")
        elif (char == "."):
            if Number:
                print(info["decimal"], end="")
            print(letter[char], end="")
        elif (char == " "):
            print("......", end="")
            Number = False

        else:
            print(letter[char], end="")
                
    if not last:
        print("......", end="")

    return

def translateToEnglish (word, last):
    letter2 = {v: k for k, v in letter.items()}
    nums2 = {v: k for k, v in nums.items()}
    info2 = {v: k for k, v in info.items()}

    split = [word[i:i+6] for i in range(0, len(word), 6)]

    Num = False

    i = 0

    while i < (len(split)):
        if split[i] in info2:
            if info2[split[i]] == "capital":
                print(letter2[split[i+1]].upper(), end="")
                i +=1

            elif info2[split[i]] == "number":
                Num = True

            elif info2[split[i]] == "decimal":
                Num = True
                print(letter2[split[i+1]], end="")
                i+=1

        elif split[i] == "......":
            print (" ", end="")
            Num = False
        elif Num:
            print(nums2[split[i]], end="")

        else:
            print(letter2[split[i]], end="")

        i+=1            
    


if __name__ == "__main__":
    inputs = sys.argv[1:] 
    which(inputs)
