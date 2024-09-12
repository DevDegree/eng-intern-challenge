import sys
from braille import translateBraille
from english import translateEnglish


def isBraille(s):
    for c in s:
        if c not in [".", "O"]:
            return False

    return True


def translate(s):
    if isBraille(s):
        return translateBraille(s)
    else:
        return translateEnglish(s)


def main():
    s = " ".join(sys.argv[1:])
    print(translate(s))


if __name__ == "__main__":
    main()
