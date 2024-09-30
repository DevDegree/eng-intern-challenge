
import sys
b_to_eng_map = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    ".OOO.O": "k", "0.0.0.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "000.0.": "p", "00000.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z",
    "......": " "
}
eng_to_b_map = {v: k for k, v in b_to_eng_map.items()}

def alphabet_to_int(char):
    return str(ord(char) - ord('a') + 1)

def int_to_alphabet(num):
    # Convert numbers 1 to 26 into 'a' to 'z'
    return chr(num + ord('a') - 1)

def is_braille(text):
    return all(char in "O." for char in text)

def braille_to_eng(text): 
    # store by 6 character string
    braille = [text[i:i+6] for i in range(0, len(text), 6)]
    # print(len(braille[i]) for i in range(len(braille)))
    i=0
    res_str=[]
    while i<len(braille):
        # if the following characters is/are numeric
        if braille[i] ==".O.OOO":
            i+=1
            # assum the chacter is numeric until space is read
            while i<len(braille) and braille[i] != "000000":
                eng=alphabet_to_int(b_to_eng_map[braille[i]])
                res_str.append(eng)
                i+=1
        # if the next character is capital
        elif braille[i]==".....O":
            i+=1
            eng=b_to_eng_map[braille[i]].upper()
            res_str.append(eng)
            i+=1
        else:
            eng=b_to_eng_map[braille[i]]
            res_str.append(eng)
            i+=1
    return "".join(res_str) 
def eng_to_braille(text):
    res_str=[]
    i=0
    while i<len(text):
        
        if text[i].isnumeric():
            res_str.append(".O.OOO")
            res_str.append(eng_to_b_map[int_to_alphabet(int(text[i]))])
            i+=1
            while i<len(text) and text[i] != " " :
                res_str.append(eng_to_b_map[int_to_alphabet(int(text[i]))])
                i += 1
        elif text[i].isupper():
            res_str.append(".....O")
            res_str.append(eng_to_b_map[text[i].lower()])
            i += 1
        else:
            res_str.append(eng_to_b_map[text[i]])
            i += 1

    return "".join(res_str)

def main():
    if len(sys.argv) < 1:
        
        return
    text = " ".join(sys.argv[1:])
    if is_braille(text):
        print(braille_to_eng(text)) 
    else:
        print(eng_to_braille(text)) 

                 

if __name__ == "__main__":
    main()