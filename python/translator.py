import sys

mapping = {
    "a": "O.....", "O.....": "a", "b": "O.O...", "O.O...": "b",
    "c": "OO....", "OO....": "c", "d": "OO.O..", "OO.O..": "d",
    "e": "O..O..", "O..O..": "e", "f": "OOO...", "OOO...": "f",
    "g": "OOOO..", "OOOO..": "g", "h": "O.OO..", "O.OO..": "h",
    "i": ".OO...", ".OO...": "i", "j": ".OOO..", ".OOO..": "j",
    "k": "O...O.", "O...O.": "k", "l": "O.O.O.", "O.O.O.": "l",
    "m": "OO..O.", "OO..O.": "m", "n": "OO.OO.", "OO.OO.": "n",
    "o": "O..OO.", "O..OO.": "o", "p": "OOO.O.", "OOO.O.": "p",
    "q": "OOOOO.", "OOOOO.": "q", "r": "O.OOO.", "O.OOO.": "r",
    "s": ".OO.O.", ".OO.O.": "s", "t": ".OOOO.", ".OOOO.": "t",
    "u": "O...OO", "O...OO": "u", "v": "O.O.OO", "O.O.OO": "v",
    "w": ".OOO.O", ".OOO.O": "w", "x": "OO..OO", "OO..OO": "x",
    "y": "OO.OOO", "OO.OOO": "y", "z": "O..OOO", "O..OOO": "z",
    " ": "......", "......": " ", "capital": ".....O", ".....O": "capital",
    "number": ".O.OOO", ".O.OOO": "number"
}

numbers = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",  "5": "O..O..", 
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
}

def translate(word):
    output = ""
    i = 0
    is_number = False

    while i < len(word):
        if word[i] != '.' and word[i] != 'O':
            char = word[i]
            if char.isupper():
                output += mapping["capital"]
                char = char.lower()
            if char.isdigit():
                if not is_number:
                    output += mapping["number"]
                    is_number = True
                output += numbers[char]
            else:
                is_number = False
                output += mapping[char]
            i += 1
        else:
            chunk = word[i:i+6]
            if chunk == mapping["capital"]:
                i += 6
                chunk = word[i:i+6]
                output += mapping[chunk].upper()
            elif chunk == mapping["number"]:
                is_number = True
            elif is_number:
                output += numbers[chunk]
            else:
                is_number = False
                output += mapping[chunk]
            i += 6

    return output

if __name__ == "__main__":
    s = ' '.join(sys.argv[1:])
    print(translate(s))
