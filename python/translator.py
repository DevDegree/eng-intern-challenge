import sys

CAPITAL_FOLLOWS = ".....O"
NUM_FOLLOWS = ".O.OOO"
SPACE = "......"

letter_to_br_dict = {
    'a': "O.....",
    'b': "O.O...",
    'c': "OO....",
    'd': "OO.O..",
    'e': "O..O..",
    'f': "OOO...",
    'g': "OOOO..",
    'h': "O.OO..",
    'i': ".OO...",
    'j': ".OOO..",
    'k': "O...O.",
    'l': "O.O.O.",
    'm': "OO..O.",
    'n': "OO.OO.",
    'o': "O..OO.",
    'p': "OOO.O.",
    'q': "OOOOO.",
    'r': "O.OOO.",
    's': ".OO.O.",
    't': ".OOOO.",
    'u': "O...OO",
    'v': "O.O.OO",
    'w': ".OOO.O",
    'x': "OO..OO",
    'y': "OO.OOO",
    'z': "O..OOO"
}

num_to_br_dict = {
    '1': "O.....",
    '2': "O.O...",
    '3': "OO....",
    '4': "OO.O..",
    '5': "O..O..",
    '6': "OOO...",
    '7': "OOOO..",
    '8': "O.OO..",
    '9': ".OO...",
    '0': ".OOO.."
}

br_to_letter_dict = {
    "O.....":"a",
    "O.O...":"b",
    "OO....":"c",
    "OO.O..":"d",
    "O..O..":"e",
    "OOO...":"f",
    "OOOO..":"g",
    "O.OO..":"h",
    ".OO...":"i",
    ".OOO..":"j",
    "O...O.":"k",
    "O.O.O.":"l",
    "OO..O.":"m",
    "OO.OO.":"n",
    "O..OO.":"o",
    "OOO.O.":"p",
    "OOOOO.":"q",
    "O.OOO.":"r",
    ".OO.O.":"s",
    ".OOOO.":"t",
    "O...OO":"u",
    "O.O.OO":"v",
    ".OOO.O":"w",
    "OO..OO":"x",
    "OO.OOO":"y",
    "O..OOO":"z",
}

br_to_num_dict = {
    "O.....":'1',
    "O.O...":'2',
    "OO....":'3',
    "OO.O..":'4',
    "O..O..":'5',
    "OOO...":'6',
    "OOOO..":'7',
    "O.OO..":'8',
    ".OO...":'9',
    ".OOO..":'0'
}

def translate_braille_to_letter(arg):
    text = ""
    num_counter = 0
    cap_counter = 0
    for i in range(0, len(arg), 6):
        unit = arg[i: i+6]
        if unit in br_to_num_dict and num_counter:
            text = text + br_to_num_dict[unit]
        elif unit in br_to_letter_dict:
            if cap_counter:
                text = text + br_to_letter_dict[unit].upper()
                cap_counter = 0
            else:
                text = text + br_to_letter_dict[unit]
        elif unit == CAPITAL_FOLLOWS:
            cap_counter = 1
        elif unit == NUM_FOLLOWS:
            num_counter = 1
        elif unit == SPACE:
            text = text + ' '
            if num_counter:
                num_counter = 0
    return text

def translate_letters_to_braille(args):
    br = ""
    num_counter = 0
    for elem in args:
        for i in elem:
            if i in letter_to_br_dict:
                br = br + letter_to_br_dict[i]
            elif i.isupper() and i.lower() in letter_to_br_dict:
                br = br + CAPITAL_FOLLOWS + letter_to_br_dict[i.lower()]
            elif i in num_to_br_dict:
                if num_counter == 0:
                    br = br + NUM_FOLLOWS +  num_to_br_dict[i]
                    num_counter = 1
                else:
                    br = br +  num_to_br_dict[i]              
        br = br + SPACE
        num_counter = 0

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