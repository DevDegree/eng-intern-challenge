import sys

def to_english(braille_string):
    """
    Translates a braille string (6 characters) into an english letter and returns it
    """
    return ""

def to_braille(english_char):
    """
    Translates a english char into a braille string (6 characters and returns it
    """
    return ""

def check_if_english(phrase):
    """
    Check if the phrase provided is in braille (has only O and .) or english (contains other characters)
    Return True if english, return False if braille
    """
    for c in phrase:
        if c == "O" or c == ".":
            continue
        return False
    return True

def translate(phrase):
    """
    Main function, determines if a phrase is english or braille then accordingly iterates through phrase to translate it
    Returns the translated result
    """
    # Setup strings to store result
    res = ""

    if check_if_english(phrase):
        # We have confirmed it is an english phrase, now we change each character into braille
        for c in phrase:
            res += to_braille(c)
    else:
        # We have confirmed it is a braille phrase, now we change every 6 characters into english
        cur = ""
        for c in phrase:
            # Add characters to cur until 6 characters, then convert it into english and add to res, and clear cur
            cur += c
            if len(cur) == 6:
                res += to_english(cur)
                cur = ""

    return res

if __name__ == '__main__':
    if len(sys.argv) > 1:
        translate(" ".join(sys.argv[1:]))
    else:
        print("Welcome to braille translator: enter a braille phrase or english phrase as an argument to translate")
