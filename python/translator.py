import sys
from itertools import groupby
import time

def identify_lang(input):
    if len(input) > 1:
        return "En"
    for char in input[0]:
        if char not in [".", "O"]:
            return "En"
    return "Br"

def create_translation_dict(lang):
    transl_dict_En_to_Br_num = {
        0: '.OOO..',
        1: 'O.....',   
        2: 'O.O...', 
        3: 'OO....', 
        4: 'OO.O..', 
        5: 'O..O..', 
        6: 'OOO...', 
        7: 'OOOO..', 
        8: 'O.OO..', 
        9: '.O.O..'
    }
    transl_dict_En_to_Br_special_chars = {
        "." : "..OO.O",
        "," : "..O...",
        "?" : "..O.OO",
        "!" : "..OOO.",
        ":" : "..OO..",
        ";" : "..O.O.",
        "-" : "....OO",
        "/" : ".O..O.",
        "<" : ".OO..O" ,
        ">" : "O..OO.",
        "(" : "O.O..O",
        ")" : ".O.OO." 
    }
    transl_dict_En_to_Br_char = {}
    x_to_z_add_value = 0
    for i in range(1, 27):
        if i == 23:
            transl_dict_En_to_Br_char[119] = ".OOO.O" ## Special case "W"
            x_to_z_add_value = 1
            continue
        fifth_char = "." if i < 11 else "O"
        sixth_char = "." if i < 21 else "O"
        transl_dict_En_to_Br_char[i  + 96] = transl_dict_En_to_Br_num[i % 10 - x_to_z_add_value][:4] + fifth_char + sixth_char
    if lang == "En":
        return transl_dict_En_to_Br_num, transl_dict_En_to_Br_char, transl_dict_En_to_Br_special_chars
    return (
        {v: k for k, v in transl_dict_En_to_Br_num.items()},
        {v: k for k, v in transl_dict_En_to_Br_char.items()},
        {v: k for k, v in transl_dict_En_to_Br_special_chars.items()}
     ) ## Br_to_En

def translate_numbers(array_of_numbers, trans_dict, special_chars):
    return "".join([special_chars[digit_key] if digit_key in special_chars else str(trans_dict[digit_key]) 
                    for digit_key in array_of_numbers])

def translate_char(array_of_chars, index, trans_dict, special_chars):
    char = array_of_chars[index]
    if char in special_chars:
        return special_chars[char]
    if char == ".....O": ## Capital follow Char
        return ""
    unper_lower_case_add_value = -32 if index > 0 and array_of_chars[index - 1] == ".....O" else 0
    return chr(trans_dict[char] + unper_lower_case_add_value)

def translate_word(array_of_chars, trans_dict, special_chars):  
    return "".join([translate_char(array_of_chars, index, trans_dict, special_chars) for index in range(len(array_of_chars))])

def translate_Br_to_En(input):
    concatenated_str = ''.join(input)
    transl_dict_Br_to_En_num, transl_dict_Br_to_En_char, special_chars = create_translation_dict("Br")

    # Split the concatenated string into chunks of length 6
    chars = [concatenated_str[i:i + 6] for i in range(0, len(concatenated_str), 6)]

    words = [list(group) for k, group in groupby(chars, lambda x: x != "......") if k]

    for i in range(len(words)):
        if words[i][0] == ".O.OOO":
            words[i] = translate_numbers(words[i][1:], transl_dict_Br_to_En_num, special_chars)
        else:
            words[i] = translate_word(words[i], transl_dict_Br_to_En_char, special_chars)
    return " ".join(words)

def translate_word_En_to_Br(word, translate_dict_num, translate_dict_chars, translate_dict_special_chars):
    is_num = False
    braille_word = []
    for char in word:
        if char in translate_dict_special_chars:
            braille_word.append[translate_dict_special_chars]
        elif not is_num and char.isdigit():
            if len(braille_word) > 0  and braille_word[-1] == "..OO.O": ## decimal point
                braille_word.insert(-2, ".O.OOO") ## number follows
            else:
                braille_word.append(".O.OOO") ## number follows
            braille_word.append(translate_dict_num[int(char)])
            is_num = True
        elif is_num:
            braille_word.append(translate_dict_num[int(char)])
        else:
            char_num = ord(char)
            if char_num < 97: ## A
                braille_word.append(".....O") ## Capital follows
                char_num += 32 ## convert to lower case
            
            braille_word.append(translate_dict_chars[char_num])
    return "".join(braille_word)


def translate_En_to_Br(input):
    transl_dict_En_to_Br_num, transl_dict_En_to_Br_char, transl_dict_En_to_Br_special_chars = create_translation_dict("En")
    return "......".join([translate_word_En_to_Br(word, transl_dict_En_to_Br_num, transl_dict_En_to_Br_char, transl_dict_En_to_Br_special_chars) 
                          for word in input])
def main():
    if len(sys.argv) == 0:
        exit(0)
    input = sys.argv[1:]
    
    lang =  identify_lang(input)

    if lang == "En":
        output = translate_En_to_Br(input)
    else:
        output = translate_Br_to_En(input)
    print(output)
    return output





if __name__ == "__main__":
    main()

