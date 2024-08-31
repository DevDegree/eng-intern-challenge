import sys

englishToBraille = {
 'a': 'O.....',
 'b': 'O.O...',
 'c': 'OO....',
 'd': 'OO.O..',
 'e': 'O..O..',
 'f': 'OOO...',
 'g': 'OOOO..',
 'h': 'O.OO..',
 'i': '.OO...',
 'j': '.OOO..',
 'k': 'O...O.',
 'l': 'O.O.O.',
 'm': 'OO..O.',
 'n': 'OO.OO.',
 'o': 'O..OO.',
 'p': 'OOO.O.',
 'q': 'OOOOO.',
 'r': 'O.OOO.',
 's': '.OO.O.',
 't': '.OOOO.',
 'u': 'O...OO',
 'v': 'O.O.OO',
 'w': '.OOO.O',
 'x': 'OO..OO',
 'y': 'OO.OOO',
 'z': 'O..OOO',
 'A': '.....OO.....',
 'B': '.....OO.O...',
 'C': '.....OOO....',
 'D': '.....OOO.O..',
 'E': '.....OO..O..',
 'F': '.....OOOO...',
 'G': '.....OOOOO..',
 'H': '.....OO.OO..',
 'I': '.....O.OO...',
 'J': '.....O.OOO..',
 'K': '.....OO...O.',
 'L': '.....OO.O.O.',
 'M': '.....OOO..O.',
 'N': '.....OOO.OO.',
 'O': '.....OO..OO.',
 'P': '.....OOOO.O.',
 'Q': '.....OOOOOO.',
 'R': '.....OO.OOO.',
 'S': '.....O.OO.O.',
 'T': '.....O.OOOO.',
 'U': '.....OO...OO',
 'V': '.....OO.O.OO',
 'W': '.....O.OOO.O',
 'X': '.....OOO..OO',
 'Y': '.....OOO.OOO',
 'Z': '.....OO..OOO',
 '1': 'O.....',
 '2': 'O.O...',
 '3': 'OO....',
 '4': 'OO.O..',
 '5': 'O..O..',
 '6': 'OOO...',
 '7': 'OOOO..',
 '8': 'O.OO..',
 '9': '.OO...',
 '0': '.OOO..'
}

brailleToEnglishAlpha = {
    "O....." : 'a',
    "O.O..." : 'b',
    "OO...." : 'c',
    "OO.O.." : 'd',
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
    ".....O" : "cap",
    ".O.OOO" : "num",
    "......" : " "
}

brailleToEnglishNum = {
    "O....." : '1',
    "O.O..." : '2',
    "OO...." : '3',
    "OO.O.." : '4',
    "O..O.." : "5",
    "OOO..." : "6",
    "OOOO.." : "7",
    "O.OO.." : "8",
    ".OO..." : "9",
    ".OOO.." : "0",
    ".....O" : "cap",
    ".O.OOO" : "num",
    "......" : " "
}

def convertEnglish(cur_char):
    return englishToBraille[cur_char]

def readEnglish(input):
    is_alpha = True
    is_first = True
    output = ""
    for word in input:
        if (is_first):
            is_first = False
            continue
        for char in word:
            if char.isdigit() and is_alpha:
                output += ".O.OOO"
                is_alpha = False
            output += convertEnglish(char)
        is_alpha = True
        output += "......"
    output = output[:-6]
    print(output, sep="")


def convertBraille(cur_char, is_alpha, is_caps):
    ret = ""
    if (is_alpha):
        ret = brailleToEnglishAlpha[cur_char]
    else:
        ret = brailleToEnglishNum[cur_char]
    
    if (ret == "cap" or ret == "num"):
        return ret
    else:
        if (is_caps):
            print(ret.upper(), end= '')
        else:
            print(ret, end= '')
        return ret

def readBraille(input):
    is_alpha = True
    is_caps = False
    braille = input[1]
    char_count = 0
    cur_char = ""
    for c in braille:
        char_count += 1
        cur_char += c

        if (char_count == 6):
            english_char = convertBraille(cur_char, is_alpha, is_caps)
            is_caps = False

            if (english_char == "cap"):
                is_caps = True
            elif (english_char == "num"):
                is_alpha = False
            elif (english_char == " "):
                is_alpha = True
            
            char_count = 0
            cur_char = ""
    print()

def main():
    input = sys.argv
    if (len(input) == 1):
        return ""
    elif (len(input) > 2):
        return readEnglish(input)
    if ("." in input[1]):
        readBraille(input)
    else:
        readEnglish(input)

if (__name__ == "__main__"):
    main()