import sys
char_brl = {
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
    ".": "..OO.O", 
    ",": "..O...", 
    "?": "..OOO.", 
    "!": "..OOO.", 
    ":": "..O.O.", 
    ";": "..O.O.", 
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O", 
    ">": "O..OO.", 
    "(": "O.O..O",
    ")": ".O.OO.", 
    " ": "......"
}

brl_char = {v: k for k, v in char_brl.items()}

num_brl = {
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

brl_num = {v: k for k,v in num_brl.items()}

number_follow= ".O.OOO"
capital_follow= ".....O"


def is_brl(sentence):
    for ch in sentence:
        if ch not in "O.":
            return False
    return len(sentence) % 6 == 0

def eng_to_brl(sentence):
    result = ""
    isNumber = False
    for ch in sentence:
        if ch.lower()  in char_brl and not ch.isdigit():
            isNumber = False
            if ch.isupper():
                result += capital_follow
                result += char_brl[ch.lower()]
            else:
                result += char_brl[ch]
        else:
            if not isNumber:
                isNumber = True
                result += number_follow
            result += num_brl[ch]

    return result

def brl_to_eng(sentence):
    result = ""
    is_num = False
    is_cap = False
    sentence = [sentence[i:i+6] for i in range (0,len(sentence),6)]
    for brail in sentence:
        if brail==number_follow:
            is_num= True
        if brail ==capital_follow:
            is_cap = True  
        
        if brail==" ":
            is_num = False
            result += " "
        elif not is_num:
            if is_cap:
                is_cap = False
                result += brl_char[brail].upper()
            else:
                result += brl_char[brail]
        else:
            result += brl_num[brail]
    return result

if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Error: Not sufficient arguments to translate")
    else:
        txt = " ".join(sys.argv[1:])
        if is_brl(txt):
            print(brl_to_eng(txt))
        else:
            print(eng_to_brl(txt))

