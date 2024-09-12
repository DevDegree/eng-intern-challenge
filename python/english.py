import alphabet as al


def translateEnglish(s):
    result = ""

    isNum = False
    for c in s:
        if c.isnumeric() and not isNum:
            isNum = True
            brailleChars = al.symbolsToBraille["NUMBER"] + al.symbolsToBraille[c]
        elif c == "." and isNum:
            brailleChars = al.symbolsToBraille["DECIMAL"] + al.symbolsToBraille[c]
        elif c.isupper():
            brailleChars = (
                al.symbolsToBraille["CAPITAL"] + al.symbolsToBraille[c.lower()]
            )
        else:
            assert c.isnumeric() or c == " " if isNum else True
            brailleChars = al.symbolsToBraille[c]

        if isNum and c == " ":
            isNum = False

        result += brailleChars
    return result
