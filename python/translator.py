import sys

# dictionaries to store eng <-> braille mapping
eng_to_braille = {
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
    " ": "......"
}

num_to_braille = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
}

braille_to_eng = {v:k for k, v in eng_to_braille.items()}
braille_to_num = {v:k for k, v in num_to_braille.items()}

def check_if_english(phrase):
    """
    Check if the phrase provided is in braille (has only O and .) or english (contains other characters)
    Return True if english, return False if braille
    """
    for c in phrase:
        if c != "O" and c != ".":
            return True
    return False

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
