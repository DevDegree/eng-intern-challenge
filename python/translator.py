import sys, json, re

arguments = sys.argv

with open("char-b.json", "r") as file:
    charToB = json.load(file)
with open("b-char.json", "r") as file:
    bToChar = json.load(file)


def brailleToChar(fullString, ref):
    """
    Translate braille to characters
    return: string
    """
    res = ""
    switch = 0
    capital = False

    # O(n)
    for i in range(6, len(fullString) + 1, 6):
        braille = fullString[i - 6 : i]
        translation = ref[braille][switch]

        # Invalid input
        if translation == "~":
            return ""

        # Flags
        if translation == "capital":
            capital = True
            continue
        if translation == "number":
            switch = 1
            continue

        # Number edge cases
        if translation == " ":
            switch = 0
        elif translation == "decimal":
            switch = 1
            translation = "."

        if capital:
            res += translation.upper()
            capital = False
        else:
            res += translation

    return res


def charToBraille(fullString, ref):
    """
    Translate characters to braille
    return: string
    """
    res = ""
    number = False

    # O(n)
    for i in range(len(fullString)):
        char = fullString[i]

        # Invalid input
        if not ref[char.lower()]:
            return ""

        # Decimal follow edge case
        if i < len(fullString) - 1 and fullString[i + 1].isdigit() and char == ".":
            res += ref["decimal"]
        else:
            if char.isupper():
                res += ref["capital"]
                char = char.lower()
            elif char.isdigit():
                if number == False:
                    res += ref["number"]
                    number = True

            if char == " ":
                number = False
            res += ref[char]

    return res


def translate(args):
    try:
        fullString = " ".join(args[1:])

        # If string only contains O and .
        # And if string only consists 6 sets of O and .
        if bool(re.fullmatch(r"[O.]*", fullString)) and len(fullString) % 6 == 0:
            # Translate braille to characters
            return brailleToChar(fullString, bToChar)
        else:
            return charToBraille(fullString, charToB)
    except:
        # If empty or invalid argument
        return ""


def main():
    print(translate(arguments))


if __name__ == "__main__":
    main()
