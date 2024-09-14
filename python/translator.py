braille_dict = {
    'a': '0.....', 'b': '0.0...', 'c': '00....', 'd': '00.0..', 'e': '0..0..', 'f': '000...', 'g': '0000..',
    'h': '0.00..', 'i': '.00...', 'j': '.000..', 'k': '0...0.', 'l': '0.0.0.', 'm': '00..0.', 'n': '00.00.',
    'o': '0..00.', 'p': '000.0.', 'q': '00000.', 'r': '0.000.', 's': '.00.0.', 't': '.0000.', 'u': '0...00',
    'v': '0.0.00', 'w': '.000.0', 'x': '00..00', 'y': '00.000', 'z': '0..000', '0': '0.....', '2': '0.0...',
    '3': '00....', '4': '00.0..', '5': '0..0..', '6': '000...', '7': '0000..', '8': '0.00..', '9': '.00...',
    '.': '.0000.', ' ': '......'  
}
reverse_braille_dict = {x:y for y, x in braille_dict.items()}
uppercase_indicator = '.....0'
decimal_indicator = '.0...0'
number_indicator = '.0.000'

def text_to_braille(text):
    braille_result = []
    is_number_mode = False

    for char in text:
        if char == ' ':     #space, possible end of number
            braille_result.append('......')
            is_number_mode = False
        elif char.isupper():
            braille_result.append(uppercase_indicator)
            braille_result.append(braille_dict.get(char.lower()))
        elif char == '.':     #decimal
            braille_result.append(decimal_indicator)
            braille_result.append(braille_dict.get(char))
        elif char.isdigit():#number
            if not is_number_mode:#start of number insert num_indicator
                braille_result.append(number_indicator)
                is_number_mode = True
            braille_result.append(braille_dict.get(char))
        else: #no cap letter
            is_number_mode = False
            braille_result.append(braille_dict.get(char))

    return ''.join(braille_result)

def braille_to_text(braille_list):
    text_result = []
    is_number_mode = False
    i = 0
    while i < len(braille_list):
        braille = braille_list[i]
        if braille == uppercase_indicator: #uppercase the next letter
            i += 1
            braille = braille_list[i]
            text_result.append(reverse_braille_dict.get(braille).upper())
        elif braille == number_indicator:
            is_number_mode = True
        else: #normal letter
            text_result.append(reverse_braille_dict.get(braille))
        if braille == '......':  # Handle space in Braille
            is_number_mode = False
        i += 1

    return ''.join(text_result)

def main():
    import sys
    input_text = sys.argv[1]

    if all(char in '0.' for char in input_text):#braille
        braille_list = []
        for i in range(0, len(input_text), 6):
            braille_list.append(input_text[i:i+6]) #split into array consisting of 6 char each
        decoded_text = braille_to_text(braille_list)
        print(decoded_text)
    else:#text
        braille = text_to_braille(input_text)
        print (braille)

if __name__ == "__main__":
    main()
