import sys

braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", ".....O": "capitalize", ".OOO..": "0", "......": " ", ".O.OOO": "number", ".O...O": "decimal",
    "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!","..OO..": ":",
    "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".O.O.O": "<", "O.O.O.": ">",
    "O.O..O": "(", ".O.OO.": ")"

}
english_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......", "1": "O.....", "2": "O.O...", "3": "OO....",
    "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..",
    "9": ".OO...", "0": ".OOO..", ".": "..O.O.", ",": "..O...", "?": "..O.OO",
    "!": "..OOO.", ":": "..OO..", ";": "..O.O.", "-": "....OO", "/": ".O..O.",
    "<": ".O.O.O", ">": "O.O.O.", "(": "O.O..O", ")": ".O.OO.", "decimal": ".O...O"
}

def is_braille(input_string):
    return all(c in ['O', '.'] for c in input_string)

def translate_to_english(braille_string):
    result = []
    i = 0
    capitalize_next = False
    is_number = False

    while i < len(braille_string):
        braille_char = braille_string[i:i+6]
        i += 6

        if braille_char in braille_to_english:
            translation = braille_to_english[braille_char]
            if translation == "capitalize":
                capitalize_next = True
            elif braille_char == ".O.OOO":  # Number indicator
                is_number = True
            else:
                if capitalize_next:
                    result.append(translation.upper())
                    capitalize_next = False
                elif is_number:
                    if translation == "a":
                        result.append("1")
                    elif translation == "b":
                        result.append("2")
                    elif translation == "c":
                        result.append("3")
                    elif translation == "d":
                        result.append("4")
                    elif translation == "e":
                        result.append("5")
                    elif translation == "f":
                        result.append("6")
                    elif translation == "g":
                        result.append("7")
                    elif translation == "h":
                        result.append("8")
                    elif translation == "i":
                        result.append("9")
                    else:
                        is_number = False
                        result.append(translation)
                else:
                    result.append(translation)
        else:
            result.append("?")  # Unrecognized symbol

    return "".join(result)



def translate_to_braille(english_string):
    result = []
    isNum = False
    for char in english_string:
        if char.isupper():
            result.append(".....O")
            result.append(english_to_braille[char.lower()])
        elif char.isdigit() and isNum == True:
            result.append(english_to_braille[char])
        elif char.isdigit() and isNum == False:
            isNum = True
            result.append(".O.OOO")
            result.append(english_to_braille[char])
        else:
            result.append(english_to_braille.get(char))

    return "".join(result)

def main():
    input_string = " ".join(sys.argv[1:])

    if is_braille(input_string):
        print(translate_to_english(input_string))
    else:
        print(translate_to_braille(input_string))

if __name__ == "__main__":
    main()
