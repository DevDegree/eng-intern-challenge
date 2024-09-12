import sys

braille_letters_to_english = {"O.....": "a", "O.O...": "b", "OO....": "c",
                              "OO.O..": "d", "O..O..": "e", "OOO...": "f",
                              "OOOO..": "g", "O.OO..": "h", ".OO...": "i",
                              ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
                              "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
                              "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
                              ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u",
                              "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
                              "OO.OOO": "y", "O..OOO": "z"}

braille_numbers_to_english = {"O.....": "1", "O.O...": "2", "OO....": "3",
                              "OO.O..": "4", "O..O..": "5", "OOO...": "6",
                              "OOOO..": "7", "O.OO..": "8", ".OO...": "9",
                              ".OOO..": "0"}

english_letters_to_braille = {"a": "O.....", "b": "O.O...", "c": "OO....",
                              "d": "OO.O..", "e": "O..O..", "f": "OOO...",
                              "g": "OOOO..", "h": "O.OO..", "i": ".OO...",
                              "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
                              "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
                              "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
                              "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO",
                              "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
                              "y": "OO.OOO", "z": "O..OOO"}

english_numbers_to_braille = {"1": "O.....", "2": "O.O...", "3": "OO....",
                              "4": "OO.O..", "5": "O..O..", "6": "OOO...",
                              "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
                              "0": ".OOO.."}

def isBraille(string: str) -> bool:
    for char in string:
        if char != 'O' and char != '.':
            return False
    return True

def convertToEnglish(string: str) -> str:
    capital_follows = False
    number_follows = False
    english = ""
    for i in range(0, len(string)-5, 6):
        symbol = string[i:i+6]
        if symbol == ".....O":
            capital_follows = True
            continue
        elif symbol == ".O.OOO":
            number_follows = True
            continue
        elif symbol == "......":
            english += " "
            number_follows = False
        elif number_follows:
            english += braille_numbers_to_english[symbol]
        elif capital_follows:
            english += chr(ord(braille_letters_to_english[symbol]) - 32)
        else:
            english += braille_letters_to_english[symbol]
        capital_follows = False
    return english

def convertToBraille(string: str) -> str:
    braille = ""
    flag = False
    for letter in string:
        if flag or letter in english_numbers_to_braille:
            if not flag:
                braille += ".O.OOO"
                flag = True
            braille += english_numbers_to_braille[letter]
        elif 65 <= ord(letter) <= 90:
            braille += ".....O"
            braille += english_letters_to_braille[chr(ord(letter) + 32)]
        else:
            braille += english_letters_to_braille[letter]
    return braille

inputlang = sys.argv[1:]
result = ""
length = len(inputlang)

if length > 1:
    for i in range(length):
        result += convertToBraille(inputlang[i])
        if i != length - 1:
            result += "......"
elif isBraille(inputlang[0]):
    result = convertToEnglish(inputlang[0])
else:
    result = convertToBraille(inputlang[0])
print(result)