import sys

argument = sys.argv[1]

def translator(argument):
    result = ""
    is_number_mode = False
    capitalize_next = False

    if argument[0] == "O" or argument[0] == ".":
        # Braille to English
        for i in range(0, len(argument), 6):
            braille_char = argument[i:i+6]
            eng_char = brailleToEng(braille_char)
            if eng_char == "CAPITAL":
                capitalize_next = True
            elif eng_char == "NUMBER":
                is_number_mode = True
            elif eng_char == " ":
                is_number_mode = False
                result += eng_char
            else:
                if capitalize_next:
                    result += eng_char.upper()
                    capitalize_next = False
                elif is_number_mode and eng_char.isdigit():
                    result += eng_char
                else:
                    result += eng_char.lower()
    else:
        # English to Braille
        for eng_char in argument:
            if eng_char.isupper():
                result += engToBraille("CAPITAL")
                result += engToBraille(eng_char.upper())
            elif eng_char.isdigit():
                if not is_number_mode:
                    result += engToBraille("NUMBER")
                    is_number_mode = True
                result += engToBraille(eng_char)
            else:
                if eng_char == " ":
                    is_number_mode = False
                result += engToBraille(eng_char)
    return result

def engToBraille(string):
    switcher = {
        "A": "O.....", "B": "O.O...", "C": "OO....", "D": "OO.O..", "E": "O..O..",
        "F": "OOO...", "G": "OOOO..", "H": "O.OO..", "I": ".OO...", "J": ".OOO..",
        "K": "O...O.", "L": "O.O.O.", "M": "OO..O.", "N": "OO.OO.", "O": "O..OO.",
        "P": "OOO.O.", "Q": "OOOOO.", "R": "O.OOO.", "S": ".OO.O.", "T": ".OOOO.",
        "U": "O...OO", "V": "O.O.OO", "W": ".OOO.O", "X": "OO..OO", "Y": "OO.OOO",
        "Z": "O..OOO",
        "1": ".O....", "2": ".OO...", "3": ".O.O..", "4": ".O.OO.", "5": ".O..O.",
        "6": ".OOO..", "7": ".OOOO.", "8": ".O.OOO", "9": ".OO.O.", "0": ".OO.OO",
        "CAPITAL": ".....O", "NUMBER": "...O..", " ": "......",
        ".": "....OO", ",": "...OO.", "!": "...OOO", "?": "...O.O"
    }
    return switcher.get(string, "?")

def brailleToEng(string):
    switcher = {
        "O.....": "A", "O.O...": "B", "OO....": "C", "OO.O..": "D", "O..O..": "E",
        "OOO...": "F", "OOOO..": "G", "O.OO..": "H", ".OO...": "I", ".OOO..": "J",
        "O...O.": "K", "O.O.O.": "L", "OO..O.": "M", "OO.OO.": "N", "O..OO.": "O",
        "OOO.O.": "P", "OOOOO.": "Q", "O.OOO.": "R", ".OO.O.": "S", ".OOOO.": "T",
        "O...OO": "U", "O.O.OO": "V", ".OOO.O": "W", "OO..OO": "X", "OO.OOO": "Y",
        "O..OOO": "Z",
        ".O....": "1", ".OO...": "2", ".O.O..": "3", ".O.OO.": "4", ".O..O.": "5",
        ".OOO..": "6", ".OOOO.": "7", ".O.OOO": "8", ".OO.O.": "9", ".OO.OO": "0",
        ".....O": "CAPITAL", "...O..": "NUMBER", "......": " ",
        "....OO": ".", "...OO.": ",", "...OOO": "!", "...O.O": "?"
    }
    return switcher.get(string, "?")

print(translator(argument))