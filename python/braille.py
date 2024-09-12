import alphabet as al


def translateChar(c, mod=None):
    if mod is None:
        return al.brailleToEnglish[c]
    if mod == "CAPITAL":
        return al.brailleToEnglish[c].upper()
    if mod == "NUMBER":
        return al.brailleToNumbers[c]
    raise Exception("Unknown modifier")


def translateBraille(s):
    assert len(s) % 6 == 0, "Not a valid Braille string"

    idx = 0
    mod = None
    result = ""
    while idx < len(s):
        brailleChar = s[idx : idx + 6]
        englishChar = translateChar(brailleChar, mod)

        if englishChar in ["CAPITAL", "NUMBER"]:
            assert mod is None, "Cannot have two modifiers in a row"
            mod = englishChar
        else:
            if mod == "CAPITAL" or englishChar == " ":
                mod = None
            result += englishChar

        idx += 6

    return result
