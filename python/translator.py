
import sys


ENG_TO_BRAILLE = {
    "a": "O.....", "b": "O.O...", "c": "OO....",
    "d": "OO.O..", "e": "O..O..", "f": "OOO...",
    "g": "OOOO..", "h": "O.OO..", "i": ".OO...",
    "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
    "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO",
    "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO", " ": "......"
}


CAPITAL = ".....O"
NUMBER = ".O.OOO"


def char_to_num(char: str) -> str:
    # converts char to it's number equivalent
    # where a = 1, b = 2, etc.
    # and returns it as a string
    if char == 'j':
        # special case where j = 0
        return 0
    return str(ord(char)-96)


def num_to_char(num: str) -> str:
    # converts num to it's char equivalent
    # where 1 = a, 2 = b, etc.
    # convert to int first
    num = int(num)
    if num == 0:
        # special case where 0 = j
        return 'j'
    return chr(num+96)


# returns True if string is braille and False if not
def check_braille(string: str) -> bool:
    for char in string:
        # returns False if the character is not "O" and "."
        if char != "O" and char != ".":
            return False
    return True


def braille_to_english(string: str) -> str:
    output = ""
    CAPITAL_FOLLOWS = False
    NUMBER_FOLLOWS = False

    # invert dictionary
    braille_dict = {v: k for k, v in ENG_TO_BRAILLE.items()}

    # goes through string in increments of 6 chars
    for i in range(0, len(string), 6):
        # get 6 char braille string
        braille = string[i:i+6]

        # capital/number check
        if braille == CAPITAL:
            CAPITAL_FOLLOWS = True
            # go to next braille character
            continue
        elif braille == NUMBER:
            NUMBER_FOLLOWS = True
            # go to next braille character
            continue

        # if space
        if braille == "......" and braille in braille_dict:
            output += braille_dict[braille]
            # reset number follows
            NUMBER_FOLLOWS = False
        # if capital letter
        elif CAPITAL_FOLLOWS and braille in braille_dict:
            output += braille_dict[braille].upper()
            # reset capital follows
            CAPITAL_FOLLOWS = False
        # if number
        elif NUMBER_FOLLOWS and braille in braille_dict:
            output += char_to_num(braille_dict[braille])
        # if lowercase
        elif braille in braille_dict:
            output += braille_dict[braille]
        # invalid character
        else:
            raise ValueError

    return output



def english_to_braille(string: str) -> str:
    output = ""
    NUM_ON = False
    
    for char in string:
        # if space
        if char == " " and char in ENG_TO_BRAILLE:
            output += ENG_TO_BRAILLE[char]
            # reset number follows symbol checker
            NUM_ON = False
        # if lowercase
        elif char.isalpha() and char in ENG_TO_BRAILLE:
            output += ENG_TO_BRAILLE[char]
        # if capital
        elif char.isalpha() and char.lower() in ENG_TO_BRAILLE:
            output += CAPITAL + ENG_TO_BRAILLE[char.lower()]
        # if number
        elif char.isdigit() and num_to_char(char) in ENG_TO_BRAILLE:
            # check if number follows symbol already exists
            if not NUM_ON:
                output += NUMBER
                NUM_ON = True
            output += ENG_TO_BRAILLE[num_to_char(char)]
        # invalid character
        else:
            raise ValueError

    return output


def main():
    if len(sys.argv) < 2:
        sys.exit("Please proivde a string to translate")

    # convert arguments into a single string
    string = " ".join(sys.argv[1:])

    try:
        # if braille
        if check_braille(string):
            print(braille_to_english(string))
        # if english
        else:
            print(english_to_braille(string))
    except:
        sys.exit("An exception occured")


if __name__ == "__main__":
    main()