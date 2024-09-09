import sys

braille_dict = {
    "O....." : ["a", "1"],
    "O.O..." : ["b", "2"],
    "OO...." : ["c", "3"],
    "OO.O.." : ["d", "4"],
    "O..O.." : ["e", "5"],
    "OOO..." : ["f", "6"],
    "OOOO.." : ["g", "7"],
    "O.OO.." : ["h", "8"],
    ".OO..." : ["i", "9"],
    ".OOO.." : ["j", "0"],
    "O...O." : "k",
    "O.O.O." : "l",
    "OO..O." : "m",
    "OO.OO." : "n",
    "O..OO." : "o",
    "OOO.O." : "p",
    "OOOOO." : "q",
    "O.OOO." : "r",
    ".OO.O." : "s",
    ".OOOO." : "t",
    "O...OO" : "u",
    "O.O.OO" : "v",
    ".OOO.O" : "w",
    "OO..OO" : "x",
    "OO.OOO" : "y",
    "O..OOO" : "z",
    "..OO.O" : ".",
    "..O..." : ",",
    "..O.OO" : "?",
    "..OOO." : "!",
    "..OO.." : ":", 
    "....OO" : "-",  
    ".O..O." : "/", 
    ".OO..O" : "<",
    "O.O..O" : "(",
    ".O.OO." : ")",
    "......" : " ",   
    ".....O" : "CF",
    ".O.OOO" : "NF"
}


english_dict = {
   "a" : "O.....",
   "b" :  "O.O...",
   "c" : "OO....",
   "d" : "OO.O..",
   "e" : "O..O..",
   "f" : "OOO...",
   "g" : "OOOO..",
   "h" : "O.OO..",
   "i" : ".OO...",
   "j" : ".OOO..",
   "k" : "O...O.",
   "l" : "O.O.O.",
   "m" : "OO..O.",
   "n" : "OO.OO.",
   "o" : "O..OO.",
   "p" : "OOO.O.",
   "q" : "OOOOO.",
   "r" : "O.OOO.",
   "s" : ".OO.O.",
   "t" : ".OOOO.",
   "u" : "O...OO",
   "v" : "O.O.OO",
   "w" : ".OOO.O",
   "x" : "OO..OO",
   "y" : "OO.OOO",
   "z" : "O..OOO",
   "1" : "O.....",
   "2" :  "O.O...",
   "3" : "OO....",
   "4" : "OO.O..",
   "5" : "O..O..",
   "6" : "OOO...",
   "7" : "OOOO..",
   "8" : "O.OO..",
   "9" : ".OO...",
   "0" : ".OOO..",
   "." : "..OO.O",
   "," : "..O...",
   "?" : "..O.OO",
   "!" : "..OOO.",
   ":" : "..OO..",
   "-" : "....OO",
   "/" : ".O..O.",
   "<" : ".OO..O",
   "(" : "O.O..O",
   ")" : ".O.OO.",
   " " : "......",
   "CF" : ".....O",
   "NF" : ".O.OOO"
}


def translate(input_args): 
    if is_english(input_args):
        translated_string = "".join(english_to_braille(input_args)) 
    else:
        translated_string = "".join(braille_to_english(input_args))

    print(translated_string)
    return translated_string


def is_english(input_args):
    if len(input_args) % 6 != 0 or any(char not in ['O', '.'] for char in input_args):
        return True 
    else:
        return False 


def english_to_braille(string):
    translated_string = []
    chars_to_translate = list(string)
    is_in_number_sequence = False

    for _, char in enumerate(chars_to_translate):
        if char.isupper():
            translated_string.append(english_dict["CF"])
            char = char.lower()
        elif char.isdigit() and not is_in_number_sequence:
            translated_string.append(english_dict["NF"])
            is_in_number_sequence = True
        if not char.isdigit():
            is_in_number_sequence = False

        translated_string.append(english_dict[char])

    return translated_string


def braille_to_english(string):
    translated_string = []
    chars_to_translate = [string[i : i + 6] for i in range(0, len(string), 6)]
    print(chars_to_translate)
    i = 0
    numbers = False

    while i < len(chars_to_translate):
        if chars_to_translate[i] == ".....O":
            if numbers == False:
                translated_string.append(braille_dict[chars_to_translate[i + 1]][0].upper())
                i = i + 1
        elif chars_to_translate[i] == ".O.OOO":
            numbers = True
        elif chars_to_translate[i] == "......":
            numbers = False
            translated_string.append(braille_dict[chars_to_translate[i]])
        else:
            if isinstance(braille_dict[chars_to_translate[i]], list):
                if numbers == True:
                    translated_string.append(braille_dict[chars_to_translate[i]][1])
                else:
                    translated_string.append(braille_dict[chars_to_translate[i]][0])
            else:
                translated_string.append(braille_dict[chars_to_translate[i]])

        i += 1

    return translated_string


def main():
    input_args = ' '.join(sys.argv[1:])
    translate(input_args)


if __name__ == "__main__":
    main()
