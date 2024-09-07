import sys
import re

def is_english(str):
    braille =  r'^([O.]{6}\s?)+$'
    if re.match(braille,str):
        return False
    return True

braille_to_english_map_numbers = {
     "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0", "......": " "
}
braille_to_english_map = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z", "......": " ",  "..OO.O": ".",  "..O...": ",",  "..O.OO": "?",  "..OOO.": "!",  "..OO..": ":",  "..O.O.": ";",  "....OO": "-",  
    ".O..O.": "/", "O.O..O": "(",  ".O.OO.": ")",   ".....O": "capital follows",  ".O.OOO": "number follows"  
}

english_to_braille_map = {v:k for k,v in braille_to_english_map.items()}
english_to_braille_map_numbers = {v:k for k,v in braille_to_english_map_numbers.items()}

def convert_to_english(arr):
    english_array = []
    prev = 0
    ht = braille_to_english_map
    for i in range(0, len(arr), 6):
        braille_chunk = arr[i:i+6]
        english_chunk = ht[braille_chunk]
        if english_chunk == " ":
            ht = braille_to_english_map
        if prev == "capital follows":
            english_array.pop()
            english_array.append(english_chunk.capitalize())
        elif prev == "number follows":
            english_array.pop()
            ht = braille_to_english_map_numbers
            english_array.append(braille_to_english_map_numbers[braille_chunk])
        else:
            english_array.append(english_chunk)
        prev = english_chunk
        
    return ''.join(english_array)

def convert_to_braille(arr):
    ht = english_to_braille_map
    braille_array = []
    for i in range(0, len(arr), 1):
        english_chunk = arr[i]
        if english_chunk == " ":
            ht = english_to_braille_map
        if english_chunk.isupper():
            braille_chunk = ht["capital follows"]
            braille_chunk = braille_chunk + (ht[english_chunk.lower()])
        elif english_chunk.isnumeric():
            if arr[i-1] == " ":
                braille_chunk = ht["number follows"] # This happens just the first time
            else:
                braille_chunk = ""
            ht = english_to_braille_map_numbers
            braille_chunk = braille_chunk + (ht[english_chunk])
        else:
            braille_chunk = ht[english_chunk]
        braille_array.append(braille_chunk)
        
    return ''.join(braille_array)
    
if __name__=="__main__":
    string_array = sys.argv[1:]
    string_array = ' '.join(string_array)
    if(is_english(string_array)):
        print(convert_to_braille(string_array))
    else:
        print(convert_to_english(string_array))