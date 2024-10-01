import sys

english_to_braille_dict = {}
with open("braille_mappings.txt", "r") as file:
    for line in file:
        char, braille = line.strip().split(" : ")
        english_to_braille_dict[char] = braille
   
braille_to_english_dict = {v: k for k, v in english_to_braille_dict.items()}

def is_braille(input_text):
    return all(char in 'O.' for char in input_text)

def english_to_braille(english_text):
    result = []
    i = 0
    while i < len(english_text):
        char = english_text[i]
        if char.isupper():
            result.append(english_to_braille_dict['capital'])
            result.append(english_to_braille_dict[char.lower()])
        elif char.isdigit():
            number_sequence = ''
            while i < len(english_text) and english_text[i].isdigit():
                number_sequence += english_text[i]
                i += 1
            result.append(english_to_braille_dict['number'])  
            for digit in number_sequence:
                result.append(english_to_braille_dict[digit])
            continue  
        elif char == ' ':
            result.append(english_to_braille_dict['space'])
        else:
            result.append(english_to_braille_dict[char])
        i += 1  
    return ''.join(result)

def braille_to_english(braille_text):
    result = []
    capital_flag = False
    number_flag = False
    i = 0
    while i < len(braille_text):
        symbol = braille_text[i:i+6]
        if symbol == english_to_braille_dict['capital']:
           capital_flag = True
        elif symbol == english_to_braille_dict['number']:
            number_flag = True
        elif symbol == english_to_braille_dict['space']:
            result.append(' ')
        else:
            english_char = braille_to_english_dict[symbol]
            if capital_flag:
                result.append(english_char.upper())
                capital_flag = False
            elif number_flag:
                result.append(english_char)
                number_flag = False
            else:
                result.append(english_char)
        i += 6
    return ''.join(result)

if __name__ == '__main__':
    input_text = ' '.join(sys.argv[1:])
    if is_braille(input_text):
        output = braille_to_english(input_text)
    else:
        output = english_to_braille(input_text)
    print(output)  


