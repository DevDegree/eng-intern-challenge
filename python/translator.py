import sys

# TO WHOEVER IS READING THIS: I wrote this in half an hour, then debugged it for a day because the version of Python being used by the Shopify repo did not support MATCH and it did not throw an error. Smh. 

# I could just check if a string contains only .s and Os to validate it as BRAILLE, but those .s and Os could be invalid, thus causing it to be ENGLISH. The default preference is given to BRAILLE. 

braille_dict = {
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
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    'O': '.OOO..',
    'CAP': '.....O',
    'DEC': '.O...O',
    'NUM': '.O.OOO',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..O.OO',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......',
    'O.....': 'a1',
    'O.O...': 'b2',
    'OO....': 'c3',
    'OO.O..': 'd4',
    'O..O..': 'e5',
    'OOO...': 'f6',
    'OOOO..': 'g7',
    'O.OO..': 'h8',
    '.OO...': 'i9',
    '.OOO..': 'jO',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o>',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '.....O': 'CAP',
    '.O...O': 'DEC',
    '.O.OOO': 'NUM',
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '!',
    '..O.OO': '?',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    '.OO..O': '<',
    'O.O..O': '(',
    '.O.OO.': ')',
    '......': ' ',
}

def translate(s):
    isABC = False
    strBraille = ""
    strABC = ""

    counter = 0
    currWord = ""
    nextTypeBraille = ""
    nextTypeABC = ""
    for i in range(len(s)):
        counter += 1
        currWord += s[i]

        if (s[i] != '.' and s[i] != 'O'): 
            isABC = True

        if s[i].lower() in braille_dict: # abc
            if (s[i] == " "):
                nextTypeABC = ""
            elif (s[i].isnumeric()):
                if (nextTypeABC != "NUM"): 
                    strBraille += braille_dict["NUM"]
                    nextTypeABC = "NUM"
            elif (s[i] == s[i].upper()):
                strBraille += braille_dict["CAP"]

            strBraille += braille_dict[s[i].lower()]

        # works until here
        
        if (counter == 6 and not isABC): # braille
            if currWord in braille_dict:
                trans = braille_dict[currWord]

                # print(currWord + " " + trans)

                if (trans == "CAP" or trans == "NUM"):
                    nextTypeBraille = trans
                else: 
                    if (nextTypeBraille == "CAP"):
                        strABC += trans[0].upper()
                        nextTypeBraille = ""
                    elif (nextTypeBraille == "NUM"):
                        strABC += trans[1]
                    else:
                        strABC += trans[0]

                counter = 0
                currWord = ""
            else:
                isABC = True

    if (isABC):
        return strBraille
    else:
        return strABC

def main():
    if len(sys.argv) < 2:
        return

    translation_input = ' '.join(sys.argv[1:])

    print(translate(translation_input))


if __name__ == "__main__":
    main()