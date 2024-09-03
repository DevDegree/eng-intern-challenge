import sys
from typing import List


def translate(phrases: List[str]) -> str:

    out = ""

    c = {
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
        "capital_follows": ".....O",
        "decimal_follows": ".O...O",
        "space": "......",
        "number_follows": ".O.OOO",
        ".": "..OO.O",
    }

    isNum = False

    if len(phrases) == 1 and set(phrases[0]) == {".", "O"}:

        other = {
            "a": "1",
            "b": "2",
            "c": "3",
            "d": "4",
            "e": "5",
            "f": "6",
            "g": "7",
            "h": "8",
            "i": "9",
            "j": "0",
        }

        brail = {value: key for key, value in c.items()}
        brail["O....."] = "a"
        brail["O.O..."] = "b"
        brail["OO...."] = "c"
        brail["OO.O.."] = "d"
        brail["O..O.."] = "e"
        brail["OOO..."] = "f"
        brail["OOOO.."] = "g"
        brail["O.OO.."] = "h"
        brail[".OO..."] = "i"
        brail[".OOO.."] = "j"

        phrase = phrases[0]

        while len(phrase) > 0:
            # print(phrase[0:6])
            if phrase[0:6] == ".O.OOO":  # number_follows
                isNum = True
            elif phrase[0:6] == "......":  # space
                isNum = False
                out += " "
            elif phrase[0:6] == ".O...O":  # decimal_follows
                isNum = True
                
            elif isNum:
                if phrase[0:6] == "..OO.O":
                    out += brail[phrase[0:6]]
                else:
                    out += other[brail[phrase[0:6]]]

            elif phrase[0:6] == ".....O":  # capital_follows
                phrase = phrase[6:]
                out += brail[phrase[0:6]].upper()

            else:
                # print(other[brail[phrase[0:6]]])
                out += brail[phrase[0:6]]

            if len(phrase) > 6:
                phrase = phrase[6:]
            else:
                phrase = ""

        return out

    count = 0

    for p in phrases:
        if count > 0:
            out += c["space"]
        count += 1
        isNum = False
        phrase = list(p)
        while len(phrase) > 0:

            if phrase[0].isalpha() and phrase[0].isupper():
                isNum = False
                out += c["capital_follows"]
                out += c[phrase[0].lower()]

            elif phrase[0].isalpha():
                isNum = False
                out += c[phrase[0].lower()]

            elif isNum and phrase[0] == ".":
                out += c["decimal_follows"]
                out += c[phrase[0]]

            elif isNum:
                out += c[phrase[0]]

            elif int(phrase[0]) in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) and not isNum:
                isNum = True
                out += c["number_follows"]
                out += c[phrase[0]]

            else:
                out += c[phrase[0]]

            phrase.pop(0)
    return out


if __name__ == "__main__":
    phrases = sys.argv[1:]
    print(translate(phrases))
