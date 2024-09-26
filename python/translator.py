
braille_letter = {"O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d",
                  "O..O..": "e", "OOO...": "f", "OOOO..": "g", "O.OO..": "h",
                  ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
                  "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p",
                  "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
                  "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
                  "OO.OOO": "y", "O..OOO": "z"}

braille_func = {".....O": "cap", ".O.OOO": "num", "......": "space"}

braille_num = {"O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4",
               "O..O..": "5", "OOO...": "6", "OOOO..": "7", "O.OO..": "8",
               ".OO...": "9", ".OOO..": "0"}


def translate(s: str) -> str:
    braille_count = 0
    for i in s:
        if i == 'O' or i == '.':
            braille_count += 1

    if braille_count == len(s):
        # s is a braille
        return braille_to_english(s)
    else:
        # s is English
        return english_to_braille(s)


def english_to_braille(s: str) -> str:
    braille = ""
    num = False
    for i in s:
        if i.isupper():
            braille += list(braille_func.keys())[list(braille_func.values()).index("cap")]
            braille += list(braille_letter.keys())[list(braille_letter.values()).index(i.lower())]
        elif i.isnumeric():
            if not num:
                braille += list(braille_func.keys())[list(braille_func.values()).index("num")]
                braille += list(braille_num.keys())[list(braille_num.values()).index(i)]
                num = True
            else:
                braille += list(braille_num.keys())[list(braille_num.values()).index(i)]
        elif i == " ":
            braille += list(braille_func.keys())[list(braille_func.values()).index("space")]
            num = False
        else:
            braille += list(braille_letter.keys())[list(braille_letter.values()).index(i.lower())]

    return braille


def braille_to_english(s: str) -> str:
    braille = ""
    word = ""
    count = 0

    cap = False
    num = False

    for i in s:
        if count < 6:
            braille += i
            count += 1
        else:
            if braille in braille_func:
                func = braille_func[braille]
                if func == "cap":
                    cap = True
                elif func == "num":
                    num = True
                else:
                    num = False
                    word += " "
            else:
                if cap:
                    word += braille_letter[braille].upper()
                    cap = False
                elif num:
                    word += braille_num[braille]
                else:
                    word += braille_letter[braille]

            braille = i
            count = 1

    if braille in braille_func:
        func = braille_func[braille]
        if func == "space":
            word += " "
    else:
        if cap:
            word += braille_letter[braille].upper()
        elif num:
            word += braille_num[braille]
        else:
            word += braille_letter[braille]

    return word


if __name__ == '__main__':
    inp = input()
    print(translate(inp))
