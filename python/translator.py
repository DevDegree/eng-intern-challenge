
import sys
import re # import regex

# dictionary to store braille to alphabet
br_to_en_alph = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "......": " ", 
    
    ".....O": "capital_follows", 
    ".O.OOO": "number_follows"
}
# dictionary to store english alphabet to braille
en_to_br_alph = {v:k for k,v in br_to_en_alph.items()}

# dictionary to store braille numbers to english numbers
br_to_en_num = {
    "O....." : "1", "O.O..." : "2", "OO...." : "3",
    "OO.O.." : "4", "O..O.." : "5", "OOO..." : "6",
    "OOOO.." : "7", "O.OO.." : "8", ".OO..." : "9",
    ".OOO.." : "0"
}
# dictionary to store english numbers to braille numbers
en_to_br_num = {v:k for k,v in br_to_en_num.items()}

# regex pattern
pattern=re.compile(r"[A-Za-z0-9]+")

# function to split braille cell into 6 characters
def braille_cell_split(str):
    return [str[i:i+6] for i in range(0, len(str), 6)]

# function to translate braille to english
def braille_to_english(str):
    translation = ""
    # split braille cell into 6 characters
    braille_str = braille_cell_split(str)
    # default dictionary to map from
    selected_dict = br_to_en_alph
    cell = 0

    while cell < len(braille_str):
        # if number_follows, change dictionary to numbers
        if br_to_en_alph[braille_str[cell]] == "number_follows":
            selected_dict = br_to_en_num
            cell += 1
        # if capital_follows, add uppercase to translation and uppercase the value of next cell mapped
        if br_to_en_alph[braille_str[cell]] == "capital_follows":
            translation += br_to_en_alph[braille_str[cell+1]].upper()
            cell += 2
        # if not uppercase, map from selected dictionary + add to translation
        translation += selected_dict[braille_str[cell]]
        cell += 1
    return translation

# function to translate english to braille
def english_to_braille(str):
    translation = ""
    selected_dict = en_to_br_alph
    translated_char = ""

    if str.isdigit():
        selected_dict = en_to_br_num
        translation += en_to_br_alph["number_follows"]
    # for each character in str
    for c in str:
        #print(c)
        # if the character is uppercase
        if selected_dict == en_to_br_alph and c.isupper():
            # add capital_follows to translation and map 
            translated_char = en_to_br_alph["capital_follows"] + en_to_br_alph[c.lower()]
        else:
            # map from selected dictionary
            translated_char = selected_dict[c]
        translation += translated_char
    return translation

def main():
    # accesses the command line arguments and stores them into a list
    args = sys.argv[1:]
    result = ""
    # for each argument, check against regx to see which translator to use
    for i, arg in enumerate(args):
        if re.fullmatch(pattern,arg):
            result += english_to_braille(arg)
            # check if arg is not the last element in the list and add space after it
            if i < len(args) - 1:
                result += en_to_br_alph[" "]
        # else use braille to english
        else:
            result += braille_to_english(arg)

    print(result)

# entry point for the script
if __name__ == "__main__":
    main()