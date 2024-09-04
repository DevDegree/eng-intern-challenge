import sys

CAPITAL_FOLLOWS = ".....O"
NUM_FOLLOWS = ".O.OOO"
SPACE = "......"

letter_to_br_dict = {
    'a': "O.....",
    'b': "O.O...",
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': "O.OO..",
    'i': ".OO...",
    'j': ".OOO..",
    'k': "O...O.",
    'l': "O.O.O.",
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
    "z": "O..OOO"
}

num_to_br_dict = {
    '1': "O.....",
    '2': "O.O...",
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': "O.OO..",
    '9': ".OO...",
    '0': ".OOO.."
}

def translate_letters_to_braille(args):
    br = ""
    num_counter = 0
    for elem in args:
        for i in elem:
            if i in letter_to_br_dict:
                if num_counter == 1:
                    num_counter = 0
                br = br + letter_to_br_dict[i]
            elif i.isupper() and i.lower() in letter_to_br_dict:
                if num_counter == 1:
                    num_counter = 0
                br = br + CAPITAL_FOLLOWS + letter_to_br_dict[i.lower()]
            elif i in num_to_br_dict:
                if num_counter == 0:
                    br = br + NUM_FOLLOWS +  num_to_br_dict[i]
                    num_counter = 1
                else:
                    br = br +  num_to_br_dict[i]              
        br = br + SPACE
    # cut off the last SPACE
    br = br[:-6]
    return br

def main():
    res = ""
    if len(sys.argv) > 1:
        # decide if the inputs are braille
        if len(sys.argv) == 2 and any(letter == "." for letter in sys.argv[1]):
            res = translate_braille_to_letter(sys.argv[1])
        else:
            res = translate_letters_to_braille(sys.argv[1:])
    return res

if __name__ == "__main__":
    res = main()
    print(res)