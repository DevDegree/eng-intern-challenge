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
    # Setup string to store result
    res = ""
    # set up flags indicating number or capital is next
    number_follows = False
    capital_follows = False

    if check_if_english(phrase):
        for c in phrase:
            # Pre-operations for each character
            if c.isupper():
                # if upper, add identifier first
                res += ".....O"
                c = c.lower()
            elif c.isnumeric():
                # if adding a number and not in a number sequence yet, add identifier before adding number
                if not number_follows:
                    res += ".O.OOO"
                    number_follows = True
                res += num_to_braille[c]
                continue
            elif c == " ":
                # if there is a space, set the numerical sequence flag to false
                number_follows = False
            # finally, add the digit
            res += eng_to_braille[c]
    else:
        # We have confirmed it is a braille phrase, now we change every 6 characters into english
        cur = ""
        for c in phrase:
            # Add characters to cur until 6 characters, then convert it into english and add to res, and clear cur
            cur += c
            if len(cur) == 6:
                if cur == ".O.OOO":
                    # if braille indicates number follows, set flag
                    number_follows = True
                elif cur == ".....O":
                    # if braille indicates capital follows, set flag
                    capital_follows = True
                elif cur == "......":
                    # if braille indicates space, remove number follows flag, and add a space
                    number_follows = False
                    res += " "
                else:
                    if number_follows:
                        # if we expect numbers, use braille to num dict
                        res += braille_to_num[cur]
                    elif capital_follows:
                        # if we expect a capital, change letter added to uppercase and remove capital flag
                        res += braille_to_eng[cur].upper()
                        capital_follows = False
                    else:
                        # otherwise, just add the letter
                        res += braille_to_eng[cur]
                cur = ""

    return res

if __name__ == '__main__':
    # join everything after calling the script with a space (as it appears visually
    if len(sys.argv) > 1:
        print(translate(" ".join(sys.argv[1:])))
    else:
        print("Welcome to braille translator: enter a braille phrase or english phrase as an argument to translate")
