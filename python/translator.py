import sys

class TwoWayDict:
    
    def __init__(self):
        self.key_to_val = {}
        self.val_to_key = {}

    #  A function to add values and keys into the dictionary
    def add(self, key, val):
        self.key_to_val[key] = val
        self.val_to_key[val] = key

    # A function to get the value using the key
    def get_val(self, key):
        return self.key_to_val.get(key)
    
    # A function to get the key using the value
    def get_key(self, val):
        return self.val_to_key.get(val)
    

mydict = TwoWayDict()

def str_to_int(ch):
    if ord(ch) >= ord('a') and ord(ch) < ord('j'):
        return str(ord(ch) - ord('a') + 1)
    return ch

def int_to_str(num):
    return chr(ord('a') + int(num) - 1)

def buildDict(dict):
    dict.add("a", "O.....")
    dict.add("b", "O.O...")
    dict.add("c", "OO....")
    dict.add("d", "OO.O..")
    dict.add("e", "O..O..")
    dict.add("f", "OOO...")
    dict.add("g", "OOOO..")
    dict.add("h", "O.OO..")
    dict.add("i", ".OO...")
    dict.add("j", ".OOO..")
    dict.add("k", "O...O.")
    dict.add("l", "O.O.O.")
    dict.add("m", "OO..O.")
    dict.add("n", "OO.OO.")
    dict.add("o", "O..OO.")
    dict.add("p", "OOO.O.")
    dict.add("q", "OOOOO.")
    dict.add("r", "O.OOO.")
    dict.add("s", ".OO.O.")
    dict.add("t", ".OOOO.")
    dict.add("u", "O...OO")
    dict.add("v", "O.O.OO")
    dict.add("w", ".OOO.O")
    dict.add("x", "OO..OO")
    dict.add("y", "OO.OOO")
    dict.add("z", "O..OOO")
    dict.add("cap", ".....O")
    dict.add("dec", ".O...O")
    dict.add("num", ".O.OOO")
    dict.add(".", "..OO.O")
    dict.add(",", "..O...")
    dict.add("?", "..O.OO")
    dict.add("!", "..OOO.")
    dict.add(":", "..OO..")
    dict.add(";", "..O.O.")
    dict.add("-", "....OO")
    dict.add("/", ".O..O.")
    dict.add("<", ".OO..O")
    #dict.add(">", "O..OO.") same as the letter o?
    dict.add("(", "O.O..O")
    dict.add(")", ".O.OO.")
    dict.add(" ", "......")

def is_braille(str) -> bool:
    for ch in str:
        if ch != '.' and ch != 'O':
            return False
    return True

def capital(ch) -> bool:
    return ord(ch) >= ord('A') and ord(ch) <= ord('Z')

def number(ch) -> bool:
    return ord(ch) >= ord('0') and ord(ch) <= ord('9')

def convert_eng(str):
    braille = []
    num = False
    for ch in str:
        if capital(ch):
            braille.append(mydict.get_val("cap")) 
            ch = ch.lower()
        elif number(ch) and not num:
            braille.append(mydict.get_val("num"))
            num = True
    
        if ch == " ":
            num = False

        if num:
            braille.append(mydict.get_val(int_to_str(ch)))
        else:
            braille.append(mydict.get_val(ch)) 


    # print(braille)

    braille_str = ''.join(braille)
    return braille_str

def convert_braille(str):
    eng = []
    cap = False
    num = False
    for i in range(0, len(str), 6):
        cur_braille = ""
        for j in range(i, i+6):
            cur_braille += str[j]

        conversion_result = mydict.get_key(cur_braille)
        if conversion_result == "num":
            num = True
            continue
        elif conversion_result == "cap":
            cap = True
            continue
        elif conversion_result == " ":
            num = False

        if num:
            num_ch = str_to_int(conversion_result)
            eng.append(num_ch)
        elif cap:
            caps = conversion_result.upper()
            eng.append(caps)
        else:
            eng.append(conversion_result)

        cap = False

    eng_str = ''.join(eng)
    return eng_str

def main():
    buildDict(mydict)
    args = sys.argv
    n = len(args)
    for i in range(1, n):
        str = sys.argv[i]
        if is_braille(str):
            print(convert_braille(str), end="")
        else:
            print(convert_eng(str), end="")
        if i != n - 1:
            print(mydict.get_val(" "), end="") # manually print spaces as braille
    return 

if __name__ == '__main__':
    main()

