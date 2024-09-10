import sys

def main():
    arguments = sys.argv[1:]
    argument_length = len(arguments)
    for e in range(argument_length):
        sys.stdout.write(word_to_braille(arguments[e]))
        if e != argument_length-1:
            sys.stdout.write(word_to_braille(" "))
            
    return

def word_to_braille(word):
    braille = ""
    #simple
    if word.isdigit():
        braille += numeric_braille(58)
        for number in word:
            braille += numeric_braille(ord(number))
    elif word.isalpha():
        for letter in word:
            braille += alpha_braille(ord(letter))
    elif word.isspace():
        braille += space()
    #complex
    else:
        word_length = len(word)
        w_counter = 0
        first = True
        for value in word:
            w_counter += 1
            if value.isdigit():
                if first:
                    braille += numeric_braille(58)
                    first = False
                braille += numeric_braille(ord(value))
            elif value.isalpha():
                braille += alpha_braille(ord(value))
            else:
                if value == '.' and word_length != w_counter-1: # check if decimal is NOT in last position of word
                    braille += decimal()
                else:
                    braille += symbol_braille(value)

    return braille

def alpha_braille(position):
    alpha_id = ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", # A-E [0-4]
                 "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..",  # F-J [5-9]
                 "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.",  # K-O [10-14]
                 "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.",  # P-T [15-19]
                 "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO",  # U-Y [20-24]
                 "O..OOO",                                          # Z [25]
                 ".....O"]                                          # capital [26]
    if position < 91:
        return alpha_id[26] + alpha_id[position - 65]

    return alpha_id[position - 97]

def numeric_braille(position):
    numeric_id = [".OOO..", "O.....", "O.O...", "OO....", "OO.O..", # 0-4 [0-4]
                  "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", # 5-9 [5-9]
                  ".O.OOO"]                                         # number [10]

    return numeric_id[position - 48]

def symbol_braille(symbol_value):
    symbol_id = ["..OO.O", "..O...", "..O.OO", "..OOO.", "..OO..",  # . , ? ! : [0-4]
                 "..O.O.", "....OO", ".O..O.", ".OO..O", "O..OO.",  # ; - / < > [5-9]
                 "O.O..O", ".O.OO."]                                # ( ) [10-11]
    symbols = [".", ",", "?", "!", ":", ";", "-", "/", "<", ">", "(", ")"]
    for i in range(len(symbols)):
        if symbols[i] == symbol_value:
            return symbol_id[i]
    return "Symbol Error"

def space():
    return "......"

def decimal():
    return ".O...O" + "..OO.O"

if __name__== "__main__":
    main()