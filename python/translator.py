# This is for converting braille to English

bra_eng = {
    "O....." : "a", "O.O..." : "b", "OO...." : "c", "OO.O.." : "d", "O..O.." : "e",
    "OOO..." : "f", "OOOO.." : "g", "O.OO.." : "h", ".OO..." : "i", ".OOO.." : "j",
    "O...O." : "k", "O.O.O." : "l", "OO..O." : "m", "OO.OO." : "n", "O..OO." : "o",
    "OOO.O." : "p", "OOOOO." : "q", "O.OOO." : "r", ".OO.O." : "s", ".OOOO." : "t",
    "O...OO" : "u", "O.O.OO" : "v", ".OOO.O" : "w", "OO..OO" : "x", "OO.OOO" : "y",
    "O.OOO" : "z", "......" : " "
}

#for converting english to braille

eng_bra = {
    "a" : "O.....", "b" : "O.O...", "c" : "OO....", "d" : "OO.O..", "e" : "O..O..",
   "f" :  "OOO...", "g" : "OOOO..", "h" : "O.OO..", "i" : ".OO...", "j" : ".OOO..",
    "k" : "O...O.", "l" : "O.O.O.", "m" : "OO..O.", "n" : "OO.OO.", "o" : "O..OO.",
    "p" : "OOO.O.", "q" : "OOOOO.", "r" : "O.OOO.", "s" : ".OO.O.", "t" : ".OOOO.",
    "u" : "O...OO", "v" : "O.O.OO", "w" : ".OOO.O", "x" : "OO..OO", "y" :  "OO.OOO",
    "z" : "O.OOO",  "capital" : ".....O", "number" : ".O.OOO", " " : "......"
}


#function to convert from braille to english

def bra_to_eng(bra_str):
        output = []
        is_capital = False
        is_number = False

        for i in range(0, len(bra_str), 6):
                words =  bra_str[i: i+6]

                if words == ".....O":
                        is_capital = True
                        continue
                elif words ==  ".O.OOO":
                        is_number = True
                elif words == bra_eng["......"]:
                        is_number = False
                else:
                        char = bra_eng.get(words)    
                        if char:    
                            if is_number:
                                    num_bra = {
                                    "O....." : "1",  
                                    "O.O...": "2",
                                    "OO...." : "3",
                                    "OO.O.." : "4",
                                    "O..O.." : "5",
                                    "OOO..." : "6",
                                    "OOOO.." : "7",
                                    "O.OO.." : "8",
                                    ".OO..." : "9",
                                    ".OOO.." : "0"
                                    }

                                    if words in num_bra:
                                            output.append(num_bra[words])
                            else:
                                    if is_capital:
                                        char = char.upper()
                                        is_capital = False    
                                    output.append(char)
        return "".join(output).strip() 

#converts braille to english
def eng_to_bra(eng_str):
        output = []

        for char in eng_str:
                if char.isupper():
                        output.append(eng_bra["capital"])
                        char = char.lower()
                elif char.isdigit():
                        output.append(eng_bra["number"])
                        num_eng = {
                                "1" : "O.....", "2" : "O.O...", "3" : "OO....", "4" : "OO.O..", 
                                "5" : "O..O..", "6" :  "OOO...", "7" : "OOOO..", "8" : "O.OO..", 
                                "9" : ".OO...", "0" : ".OOO.."
                        }
                        output.append(num_eng[char])

                else:
                        output.append(eng_bra.get(char, ""))
        return "".join(output).strip() 

import sys

if __name__ == '__main__':
    
    input_string = "".join(sys.argv[1:])

    if any(char in input_string for char in "O."):
        print(bra_to_eng(input_string))
    else:
        print(eng_to_bra(input_string))