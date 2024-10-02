import sys

def get_brl_dict():
    return {
        "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
        "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
        "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
        "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
        "y": "OO.OOO", "z": "O..OOO", "capital": ".....O", "number": ".O.OOO", "space": "......"
    }

def get_rev_dict(brl_dict):
    return {value: key for key, value in brl_dict.items()}

def is_brl(input_str):
    return all(c in "O." for c in input_str)

def to_brl(text, brl_dict):
    res = []
    num_mode = False

    for c in text:
        if c.isupper():
            res.append(brl_dict["capital"])
            c = c.lower()
        
        if c.isdigit():
            if not num_mode:
                res.append(brl_dict["number"])
                num_mode = True
            res.append(brl_dict[chr(ord('a') + int(c) - 1)] if c != '0' else brl_dict['j'])
        elif c == ' ':
            res.append(brl_dict["space"])
            num_mode = False
        else:
            res.append(brl_dict[c])
            num_mode = False
    
    return ''.join(res)

def to_eng(brl, brl_dict):
    rev_dict = get_rev_dict(brl_dict)
    res, i = [], 0
    cap_mode = num_mode = False

    while i < len(brl):
        symbol = brl[i:i+6]
        
        if symbol == brl_dict["capital"]:
            cap_mode = True
        elif symbol == brl_dict["number"]:
            num_mode = True
        elif symbol == brl_dict["space"]:
            res.append(' ')
            num_mode = False
        elif num_mode:
            letter = rev_dict[symbol]
            res.append(str(ord(letter) - ord('a') + 1) if letter != 'j' else '0')
        else:
            letter = rev_dict[symbol]
            res.append(letter.upper() if cap_mode else letter)
            cap_mode = False
        
        i += 6
    
    return ''.join(res)

def main(input_str):
    brl_dict = get_brl_dict()

    if is_brl(input_str):
        print(to_eng(input_str, brl_dict))
    else:
        print(to_brl(input_str, brl_dict))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_str = " ".join(sys.argv[1:])
        main(input_str)
    else:
        print("provide input string to translate please")
