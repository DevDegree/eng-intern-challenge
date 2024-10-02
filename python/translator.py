import sys

eng_to_braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', 'capital': '.....O', 'decimal': '.O...O', 'number': '.O.OOO',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', 
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '(': 'O.O..O', 
    ')': '.O.OO.', ' ': '......'
    }

braille_to_eng_dict = {v: k for k, v in eng_to_braille_dict.items()}

number_to_braille_dict = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    ' ': '......', 'decimal': '.O...O', '.': '..OO.O'
}

braille_to_number_dict = {v: k for k, v in number_to_braille_dict.items()}

def eng_to_braille(input_string, eng_to_braille_dict, number_to_braille_dict):
    res = ""
    i = 0
    while i < len(input_string):
        c = input_string[i]
        if c.isdigit():
            temp_str = ""
            temp_str += eng_to_braille_dict['number']
            while i <= len(input_string) and input_string[i].isdigit():
                temp_str += number_to_braille_dict[input_string[i]]
                i += 1
                if i == len(input_string):
                    break
            res += temp_str
        
        elif c.isupper():
            temp_str = eng_to_braille_dict['capital'] + eng_to_braille_dict[c.lower()]
            res += temp_str
            i += 1
        
        else:
            if c in eng_to_braille_dict:
                res += eng_to_braille_dict[c] 
            i += 1
    return res

def braille_to_eng(input_string, braille_to_eng_dict,braille_to_number_dict):
    res = ""
    window_length = 6
    if len(input_string) % 6 != 0:
        return "error: invalid input string length"
    i = 0
    while i < len(input_string):
        segment = input_string[i:i+window_length]
        char = braille_to_eng_dict[segment]
        
        if char == 'capital':
            nextSeg = braille_to_eng_dict[input_string[i+window_length:i+(2*window_length)]]
            res += nextSeg.upper()
            i += (2 * window_length)

        elif char == 'number':
            i += window_length
            input_seg = input_string[i:i+(window_length)]
            nextSeg = braille_to_number_dict[input_seg]
            while nextSeg !=  ' ' and i < len(input_string):
                
                if nextSeg == 'decimal':
                    res += braille_to_number_dict[input_string[i+window_length:i+(2*window_length)]]
                    i+=window_length
                else:
                    res += nextSeg
                    i += window_length
                input_seg = input_string[i:i+(window_length)]
                if input_seg == '':
                    break
                nextSeg = braille_to_number_dict[input_seg]
        
        elif char == 'decimal':
            nextSeg = braille_to_eng_dict[input_string[i+window_length:i+(2*window_length)]]
            res += nextSeg
            i += (2 * window_length)
        
        else:
            res += char
            i += window_length

    return res

def translate_indtificiation(input_string):
    if all(c in 'O.' for c in input_string) and len(input_string) % 6 == 0:
        return 'Braille'
    else:
        return 'English'


def main():
    arguments = sys.argv[1:]
    input_string = ""
    
    if not arguments:
        return

    for argument in arguments:
        input_string += argument
        if argument != arguments[-1]:
            input_string += " "
            
    if translate_indtificiation(input_string) == "Braille":
        res = braille_to_eng(input_string, braille_to_eng_dict, braille_to_number_dict)
        print(res)
    else:
        res = eng_to_braille(input_string, eng_to_braille_dict, number_to_braille_dict)
        print(res)
if __name__ == '__main__':
    main()