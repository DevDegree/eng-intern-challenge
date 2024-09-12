import sys

#ASSUMPTIONS: Test Case is wrong, and braille is supposed to be read left to right rather than the right to left described in the problem description
eng_to_braille = {
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
    ")": ".O.OO.",
    " ": "......",
    "capital follows": ".....O",
    "decimal follows": ".O...O",
    "number follows": ".O.OOO"
}

braille_to_eng = {
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
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O..OO.": ">",
    "O.O..O": "(",
    ".O.OO.": ")",
    "......": " ",
    ".....O": "capital follows",
    ".O...O": "decimal follows",
    ".O.OOO": "number follows"
}

def translate_braille_to_eng(braille_input):
    braille_list = [braille_input[i:i + 6] for i in range(0, len(braille_input), 6)]
    ans = ""
    upper = False
    numeric = False

    for braille in braille_list:
        if braille_to_eng[braille] == "capital follows":
            upper = True
            continue
        elif braille_to_eng[braille] == "number follows":
            numeric = True
            continue
        elif braille_to_eng[braille] == " ":
            numeric = False
        if numeric:
            ans += str((ord(braille_to_eng[braille])) - 96) 
            #a and 1, b and 2... to 10 share the same braille, and ord(a) = 97
            #so by subtracting 96 from ord(braille to letter), it results in the number we need

        elif upper:
            ans += braille_to_eng[braille].upper()
            upper = False
        else: 
            ans += braille_to_eng[braille]
    return ans

def translate_eng_to_braille(eng_input):
    ans = ""
    numeric = False
    for letter in eng_input:
        if letter.isupper():
            ans += eng_to_braille["capital follows"]
            ans += eng_to_braille[letter.lower()]
        elif letter.isnumeric():
            if numeric == False:
                ans += eng_to_braille["number follows"]
                numeric = True
            ans += eng_to_braille[letter.lower()]
        elif letter == ".":
            ans += eng_to_braille["decimal follows"]
        elif letter == " ":
            ans += eng_to_braille[letter]
            numeric = False
        else:
            ans += eng_to_braille[letter]
    return ans



if __name__ == "__main__":
    args = " ".join(sys.argv[1:])

    is_braille = set(args).issubset({'O', '.'}) and (len(args) % 6 == 0) #braille must be only "O" and "." and length must be a multiple of 6

    if not is_braille:
        print(translate_eng_to_braille(args))
    
    elif is_braille:
        print(translate_braille_to_eng(args))


