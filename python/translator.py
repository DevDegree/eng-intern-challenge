import sys

eng_to_braille_dict = {
    #Letters
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", 
    #Numbers
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    #Structure
    "capital_next": ".....O", "decimal_next": ".O...O", "number_next": ".O.OOO",
    #Punctuation
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..", 
    ";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "O..OO.",
    "(": "O.O..O", ")": ".O.OO.", "space": "......",
}

braille_to_letter_dict = {
    # Letters
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
    
    # Structure (decimal_next, capital_next, number_next)
    ".O...O": ".", ".....O": "capital_next", ".O.OOO": "number_next",
    # Punctuation
    "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":", 
    "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O..OO.": ">",
    "O.O..O": "(", ".O.OO.": ")", "......": " ",
}

braille_to_num_dict = {
    # Numbers
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
}

def convert_to_braille(terminal_args):
    braille_output = ""
    for arg_idx in range(len(terminal_args)):
        raw_user_input = terminal_args[arg_idx + 1]
        num_start = 0
        for idx, ele in enumerate(raw_user_input):
            if num_start == 0:
                if ele.isnumeric():
                    braille_output += eng_to_braille_dict["number_next"]
                    num_start = 1
                elif ele.isupper():
                    braille_output += eng_to_braille_dict["capital_next"]
            elif ele == ".":
                #if first condition is false, cannot be decimal and rest of if statement is passed
                if idx < len(raw_user_input) and raw_user_input[idx + 1].isnumeric():
                    braille_output += eng_to_braille_dict["decimal_next"]
            braille_output += eng_to_braille_dict[ele.lower()]
        #terminal_args[0] is translate.py and due to len() not accounting for 0th index, need to subtract 2
        if arg_idx == len(terminal_args) - 2:
            break
        braille_output += eng_to_braille_dict["space"]
    return braille_output
        
def convert_to_eng(raw_user_input):
    eng_output = ""
    char_start = 0
    char_end = 6
    is_num = 0
    is_capital = 0
    while len(raw_user_input) >= char_end:
        if braille_to_letter_dict[raw_user_input[char_start:char_end]] == " ":
            eng_output += braille_to_letter_dict[raw_user_input[char_start:char_end]]
            is_num = 0
        elif braille_to_letter_dict[raw_user_input[char_start:char_end]] == "number_next":
            is_num = 1
        elif is_num == 0:
            if raw_user_input[char_start:char_end] == ".....O":
                is_capital = 1
            elif is_capital:
                eng_output += braille_to_letter_dict[raw_user_input[char_start:char_end]].upper()
                is_capital = 0
            else:
                eng_output += braille_to_letter_dict[raw_user_input[char_start:char_end]]
        else:
            eng_output += braille_to_num_dict[raw_user_input[char_start:char_end]]
        char_start += 6
        char_end += 6
    return eng_output
      
def check_type():
    terminal_args = sys.argv
    raw_user_input = terminal_args[1]
    #test if the raw user input first 6 characters align with braille format
    if raw_user_input[0:6] in braille_to_letter_dict:
        print(convert_to_eng(raw_user_input))
    else:     
        print(convert_to_braille(terminal_args))

if __name__ == '__main__':
    check_type()


