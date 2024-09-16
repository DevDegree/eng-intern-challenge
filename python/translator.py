
eng_to_brl = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

capital_brl = '.....O'
number_brl = '.O.OOO'

brl_to_eng = {v: k for k, v in eng_to_brl.items()}

def detect_brl(input_str):
    return all(ch in "O." for ch in input_str)

def convert_brl_to_text(brl_input):
    output = ""
    idx = 0
    is_capital = False
    is_number = False

    while idx < len(brl_input):
        current_char = brl_input[idx:idx+6]
        
        if current_char == capital_brl:
            is_capital = True
            idx += 6
            continue
        elif current_char == number_brl:
            is_number = True
            idx += 6
            continue

        char = brl_to_eng.get(current_char, '?')
        
        if is_number and char.isdigit():
            output += char
        elif is_capital:
            output += char.upper()
            is_capital = False
        else:
            output += char
        
        idx += 6
        
        if char == ' ':
            is_number = False

    return output

def convert_text_to_brl(text):
    result = ""
    num_mode = False
    
    for ch in text:
        if ch.isdigit() and not num_mode:
            result += number_brl
            num_mode = True
        
        if ch.isalpha() and ch.isupper():
            result += capital_brl
            result += eng_to_brl[ch.lower()]
        elif ch.isdigit() or ch == ' ':
            result += eng_to_brl[ch]
        else:
            result += eng_to_brl[ch.lower()]
    
        if ch == ' ':
            num_mode = False

    return result

def process_translation():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python translator.py <text>")
        return
    
    input_val = sys.argv[1]
    
    if detect_brl(input_val):
        print(convert_brl_to_text(input_val))
    else:
        print(convert_text_to_brl(input_val))

if __name__ == "__main__":
    process_translation()
