
# Name: Keta Khatri
# Email: ketak78@gmail.com

import sys
"""
eng_to_braille and braille_to_eng are dicts that store conversions from and to english and braille

braille_to_num and num_to_brialle are dicts that store conversions from and to braille and numbers

all dicts are used for the two translator functions


"""
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
    " ": "......",
    "capital": ".....O",
    "number": ".O.OOO"
}

braille_to_eng = {c: e for e, c in eng_to_braille.items()}

num_to_braille = {
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

braille_to_num = {c: e for e, c in num_to_braille.items()}


def isBraille(text):
    """
    isBraille takes in a string and returns a boolean value

    Iterates through the string and if the characters are not braille (O,.), it returns False
    Otherwise Return True

    O(n) time complexity 

    """
    for t in text:
        if t not in ['O', '.']:
            return False
    return True


def brailleTranslator(text):
    """
    brailleTranslator takes in a string and returns string

    splits the string into 6 for the 2 x 3 grid
    Iterates through the list matching conditions by accessing the values from the dict

    O(n) time complexity 

    """
    letters = [text[i:i+6] for i in range(0, len(text), 6)]
    res = []
    capital = False
    number = False

    for l in letters:
        if not number:
            currLetter = braille_to_eng[l]

        if currLetter == "capital":
            capital = True
        elif currLetter == "number":
            number = True
        elif currLetter == " ":
            res.append(currLetter)
            number == False
        elif capital:
            res.append(currLetter.lower())
            capital = False
        elif number:
            res.append(braille_to_num[l])
        else:
            res.append(currLetter)

    return ''.join(res)


def englishTranslator(text):
    """
    englishTranslator takes in a string and returns string

    splits the string into 6 for the 2 x 3 grid
    Iterates through the list matching conditions by accessing the values from the dict

    O(n) time complexity 

    """
    res = []
    number = False

    for l in text:
        if l.isalpha():
            if l.islower():
                res.append(eng_to_braille[l])
            else:
                res.append(".....O")
                res.append(eng_to_braille[l.lower()])
        elif l.isdigit():
            if not number:
                res.append(".O.OOO")
                number = True
            res.append(num_to_braille[l])
        elif l.isspace():
            res.append(eng_to_braille[l])
            number = False
        else:
            res.append(eng_to_braille[l])
    return ''.join(res)


if __name__ == '__main__':

    text = ' '.join(sys.argv[1:])
    text = ".O.OOOOO.O..O.O..."

    if isBraille(text):
        print(brailleTranslator(text))
    else:
        print(englishTranslator(text))
