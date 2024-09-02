import sys
from textwrap import wrap

if __name__ == "__main__":

    input_string = ' '.join(sys.argv[1:])
    pre_translate = []
    is_cap = False
    is_num = False
    res = ""

    translation_letters = {
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
        " ": "......",
        "cap": ".....O",
    }

    translation_nums = {
        "0": ".OOO..",
        "1": "O.....",
        "2": "O.O...",
        "3": "OO....",
        "4": "OO.O..",
        "5": "O..O..",
        "6": "OOO...",
        "7": "OOOO..",
        "8": "O.OO..",
        "9": ".OO...",
        "num": ".O.OOO",
    }
    
    isBraille = len(input_string) % 6 == 0 and '.' in input_string

    if isBraille:
        pre_translate = wrap(input_string, width=6)

        for ele in pre_translate:
            ele_nums = None
            ele_letters = None

            if ele in translation_nums.values():
                ele_nums = list(translation_nums.keys())[list(translation_nums.values()).index(ele)]

            if ele in translation_letters.values():
                ele_letters = list(translation_letters.keys())[list(translation_letters.values()).index(ele)]
            
            if ele_nums == "num":
                is_num = True
            elif ele_letters == "cap":
                is_cap = True
            elif is_num:
                res += ele_nums
            elif is_cap:
                res += ele_letters.upper()
                is_cap = False
            elif ele_letters:
                res += ele_letters

    else:
        pre_translate = [c for c in input_string]

        for ele in pre_translate:
            if ele.isupper():
                res += translation_letters["cap"]
                res += translation_letters[ele.lower()]
            elif ele.isnumeric():
                if not is_num:
                    is_num = True
                    res += translation_nums["num"]
                res += translation_nums[ele]
            elif ele == " ":
                is_num = False
                res += translation_letters[ele]
            else:
                res += translation_letters[ele]        

    print(res.strip())