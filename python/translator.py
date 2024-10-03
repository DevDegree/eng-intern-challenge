from sys import argv

modifiers_dict = {
    "upper": ".....O",
    "decimal": ".O...O",
    "number": ".O.OOO",
    "space": "......",
}

char_dict = {
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
}

input_str = "".join(argv[1:])
# checks if the input str only contains 1s and 0s
if len(set(input_str)) <= 2:
    # split the string by 6 characters each
    input_list = [input_str[i : i + 6] for i in range(0, len(input_str), 6)]
    capital = False
    number = False

    translation = ""
    for braille in input_list:
        if braille in modifiers_dict.values():
            if braille == modifiers_dict["upper"]:
                capital = True
            elif braille == modifiers_dict["number"]:
                number = True
            elif braille == modifiers_dict["space"]:
                translation += " "
                number = False  # reset number flag after space
            continue

        for char, braille_code in char_dict.items():
            if braille == braille_code:
                if number and char.isnumeric():
                    translation += char
                elif number and not char.isnumeric():
                    continue
                elif capital:
                    translation += char.upper()
                    capital = False
                else:
                    translation += char
                break
        else:
            translation += "?"  # unknown character placeholder

    print(translation)
else:
    translation = ""
    isNumber = False

    for i, word in enumerate(argv[1:]):
        if i > 0:
            translation += modifiers_dict["space"]

        isNumber = False
        for char in word:
            if char.isupper():
                translation += modifiers_dict["upper"]
            elif char.islower():
                pass
            elif char.isnumeric() and not isNumber:
                isNumber = True
                translation += modifiers_dict["number"]
            elif char == ".":
                translation += modifiers_dict["decimal"]

            translation += char_dict.get(char.lower(), "")

    print(translation, end="")
