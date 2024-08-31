#!/usr/bin/env python3

# Ajlal Paracha Aug 31 2024 for Shopify Intern Challenge Winter 2025 submission.
# To run on my ubuntu machine, this file is a UNIX converted file of translator.py

import sys

# all dict stores capital letters for letter references!
braille_dict = {
    "A": "O.....",
    "B": "O.O...",
    "C": "OO....",
    "D": "OO.O..",
    "E": "O..O..",
    "F": "OOO...",
    "G": "OOOO..",
    "H": "O.OO..",
    "I": ".OO...",
    "J": ".OOO..",
    "K": "O...O.",
    "L": "O.O.O.",
    "M": "OO..O.",
    "N": "OO.OO.",
    "O": "O..OO.",
    "P": "OOO.O.",
    "Q": "OOOOO.",
    "R": "O.OOO.",
    "S": ".OO.O.",
    "T": ".OOOO.",
    "U": "O...OO",
    "V": "O.O.OO",
    "W": ".OOO.O",
    "X": "OO..OO",
    "Y": "OO.OOO",
    "Z": "O..OOO",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
    "capital": ".....O",
    "number": ".O.OOO",
    "space": "......"
}

english_dict = {v: k for k, v in braille_dict.items() if not k.isdigit()}
number_dict = {v: k for k, v in braille_dict.items() if k.isdigit()}

def english_to_braille(s: str) -> str:
    """Converts english string to braille string

    Args:
        s (str): english string of only alphabet, numbers, and space keys and all numbers are followed by a space

    Returns:
        str: braille translation
    """
    res = []
    in_number = False
    for ch in s: 
        if in_number:
            if ch == " ":
                in_number = False
                res.append(braille_dict["space"])
            
            else:
                res.append(braille_dict[ch])
            
        else:
            if ch == " ":
                res.append(braille_dict["space"])
                
            elif ch.isdigit():
                res.append(braille_dict["number"])
                res.append(braille_dict[ch])
                in_number = True
            
            else:
                if ch.isupper():
                    res.append(braille_dict["capital"])
                
                res.append(braille_dict[ch.upper()])
                     
    return "".join(res)

def braille_to_english(s: str) -> str:
    """Converts braille string to english string

    Args:
        s (str): braille string of only alphabet, digit, space, and capital/number follow keys

    Returns:
        str: english translation
    """
    res = []
    in_number = False
    in_capital = False
    
    s_arr = [s[i:i+6] for i in range(0, len(s), 6)]
    for ch in s_arr:
        if in_number: 
            # check if ch is a space (out of number)
            if english_dict[ch] == "space":
                in_number = False
                res.append(" ")
            
            else:
                res.append(number_dict[ch])
            
        else:
            # if going into number
            if english_dict[ch] == "number":
                in_number = True
            
            elif english_dict[ch] == "capital":
                in_capital = True
            
            elif english_dict[ch] == "space":
                res.append(" ")
            
            else: 
                # we store in all the dicts the capital letters so need to go lower accordingly
                # do not need to check for non-alphabetic symbols (like ! and <) as per specs
                res.append(english_dict[ch] if in_capital else english_dict[ch].lower())
                in_capital = False

       
    return "".join(res)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: translator.py <string>")
        sys.exit(1)
    
    if len(sys.argv) == 2:
        s = sys.argv[1]
        output = braille_to_english(s) if s.count(".") > 0 else english_to_braille(s)
        print(output)
    
    # if more than one argument, like in the unit test
    else: 
        # combine all the inputs to one space seperated string
        join_char = english_dict["space"] if sys.argv[1].count(".") > 0 else " "
        s = join_char.join([sys.argv[i] for i in range(1, len(sys.argv))])

        output = braille_to_english(s) if s.count(".") > 0 else english_to_braille(s)
        print(output)