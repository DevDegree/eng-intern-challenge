
alpha1 = {"a" : "O.....",
        "b" : "O.O...",
        "c" : "OO....",
        "d" : "OO.O..",
        "e" : "O..O..",
        "f" : "OOO...",
        "g" : "OOOO..",
        "h" : "O.OO..",
        "i" : ".O.O..",
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
        "(" : "O.O..O",
        ")" : ".O.OO.",
        " " : "......",
}
alpha2 = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".O.O..": "i",
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
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O.O..O": "(",
    ".O.OO.": ")",
    "......": " ",
}

numbers1 = {
    "1" : "O.....",
    "2" : "O.O...",
    "3" : "OO....",
    "4" : "OO.O..",
    "5" : "O..O..",
    "6" : "OOO...",
    "7" : "OOOO..",
    "8" : "O.OO..",
    "9" : ".OO...",
    "0" : ".OOO..",
}
numbers2 = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0'
}
def brailleToEnglish():
        sentence = ""
        cap = False
        dec = False
        num = False
        space = False
        for i in range(0,ln,6):
            
            word = user_input[i:i+6]
            if word == ".....O":
                cap = True
            elif word == ".O...O":
                dec = True
            elif word == ".O.OOO":
                num = True;
            elif word == "......":
                sentence += " "
                num = False
            else:
                if cap == True:
                    sentence += (alpha2.get(word)).upper()
                    cap = False
                elif dec == True:
                    sentence += "."
                    dec = False
                elif num == True:
                    sentence += numbers2.get(word)
                else:
                    sentence += alpha2.get(word)
        return sentence

def engnlishToBraille():
        sentence = ""
        dec = False
        num = False
        for letter in user_input:
            if letter.isupper():
                sentence += ".....O" + (alpha1.get(letter.lower()))
            elif letter == " ":
                sentence += "......"
                num = False
            elif letter.isdigit():
                if user_input[ln-1] != letter and not(num):
                    sentence += ".O.OOO" + numbers1.get(letter)
                    num = True
                else:
                    sentence += numbers1.get(letter)
            else:
                if dec == True and letter == ".":
                    sentence += ".O...O"
                    dec = False
                else:
                    sentence += alpha1.get(letter)
        return sentence

user_input = input()
ln = len(user_input)
if(ln == 0):
    print("")
else:
    if "." == user_input[0] or "O" == user_input[0]:
        result = brailleToEnglish()
    else:
        result = engnlishToBraille()
print(result)





